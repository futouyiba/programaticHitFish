"""Durable append-only journal for Opportunity and Settlement identities.

The journal is intentionally small: production schedulers can put it behind a
database or replicated log, while this implementation provides the same
idempotency contract for local replay and crash testing.
"""

from copy import deepcopy
import json
import os
import threading
import sqlite3
import time
from typing import Any, Dict, List, Optional, Protocol

try:
    import fcntl
except ImportError:  # pragma: no cover - Windows uses msvcrt byte-range locks below
    fcntl = None
try:
    import msvcrt
except ImportError:  # pragma: no cover - POSIX uses fcntl.flock above
    msvcrt = None


class JournalConflict(ValueError):
    pass


class JournalAdapter(Protocol):
    """Storage contract required by FCFEngine for durable replay semantics."""

    def append_once(self, event_id: str, event_type: str, payload: Dict[str, Any]) -> bool: ...
    def get(self, event_id: str) -> Optional[Dict[str, Any]]: ...
    def records(self) -> List[Dict[str, Any]]: ...


class DurableJournal:
    def __init__(self, path: str):
        self.path = path
        self._lock = threading.RLock()
        self._records: Dict[str, Dict[str, Any]] = {}
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as stream:
                for line_number, line in enumerate(stream, 1):
                    if not line.strip():
                        continue
                    try:
                        record = json.loads(line)
                    except json.JSONDecodeError as exc:
                        raise ValueError(f"corrupt journal line {line_number}") from exc
                    self._ingest(record)

    def _ingest(self, record: Dict[str, Any]) -> None:
        if not isinstance(record, dict):
            raise ValueError("invalid journal record")
        required = {"event_id", "event_type", "payload"}
        if set(record) != required or not isinstance(record["event_id"], str):
            raise ValueError("invalid journal record")
        previous = self._records.get(record["event_id"])
        if previous is not None and previous != record:
            raise JournalConflict("event_id reused with different payload")
        self._records[record["event_id"]] = deepcopy(record)

    def _acquire_os_lock(self, stream) -> Optional[int]:
        """Serialize cross-process appenders; no silent unlocked fallback."""
        if fcntl is not None:
            fcntl.flock(stream.fileno(), fcntl.LOCK_EX)
            return None
        if msvcrt is not None:
            # Windows byte-range locks are mandatory: locking the journal file
            # itself would block this process's own "a+" reads. Guard with a
            # sidecar lock file instead; the journal stays freely readable.
            lock_fd = os.open(self.path + ".lock", os.O_RDWR | os.O_CREAT)
            os.lseek(lock_fd, 0, os.SEEK_SET)
            msvcrt.locking(lock_fd, msvcrt.LK_LOCK, 1)
            return lock_fd
        raise OSError("no inter-process file locking available on this platform")

    def _release_os_lock(self, stream, lock_fd: Optional[int]) -> None:
        if fcntl is not None:
            fcntl.flock(stream.fileno(), fcntl.LOCK_UN)
        elif lock_fd is not None:
            os.lseek(lock_fd, 0, os.SEEK_SET)
            msvcrt.locking(lock_fd, msvcrt.LK_UNLCK, 1)
            os.close(lock_fd)

    def append_once(self, event_id: str, event_type: str, payload: Dict[str, Any]) -> bool:
        """Append exactly once; return False for an identical replay."""
        record = {"event_id": event_id, "event_type": event_type, "payload": deepcopy(payload)}
        with self._lock:
            parent = os.path.dirname(os.path.abspath(self.path))
            os.makedirs(parent, exist_ok=True)
            # The process-local index is stale under multiprocess writers.
            # Re-index the file while holding the OS lock, then decide exactly
            # once whether this event ID is new, identical, or conflicting.
            with open(self.path, "a+", encoding="utf-8") as stream:
                lock_fd = self._acquire_os_lock(stream)
                try:
                    disk_records: Dict[str, Dict[str, Any]] = {}
                    stream.seek(0)
                    for line_number, line_text in enumerate(stream, 1):
                        if not line_text.strip():
                            continue
                        try:
                            parsed = json.loads(line_text)
                        except json.JSONDecodeError as exc:
                            raise ValueError(f"corrupt journal line {line_number}") from exc
                        if not isinstance(parsed, dict):
                            raise ValueError("invalid journal record")
                        required = {"event_id", "event_type", "payload"}
                        if (set(parsed) != required or not isinstance(parsed["event_id"], str)):
                            raise ValueError("invalid journal record")
                        prior = disk_records.get(parsed["event_id"])
                        if prior is not None and prior != parsed:
                            raise JournalConflict("event_id reused with different payload")
                        disk_records[parsed["event_id"]] = deepcopy(parsed)
                    previous = disk_records.get(event_id)
                    if previous is not None:
                        if previous != record:
                            raise JournalConflict("event_id reused with different payload")
                        self._records = disk_records
                        return False
                    line = json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n"
                    stream.seek(0, os.SEEK_END)
                    # One complete line under O_APPEND + an inter-process lock.
                    stream.write(line)
                    stream.flush()
                    os.fsync(stream.fileno())
                    disk_records[event_id] = deepcopy(record)
                finally:
                    self._release_os_lock(stream, lock_fd)
            self._records = disk_records
            return True

    def get(self, event_id: str) -> Optional[Dict[str, Any]]:
        with self._lock:
            value = self._records.get(event_id)
            return deepcopy(value) if value is not None else None

    def records(self) -> List[Dict[str, Any]]:
        with self._lock:
            return [deepcopy(self._records[key]) for key in sorted(self._records)]


class SQLiteJournal:
    """Transactional reference adapter for a shared production-local database.

    A unique event ID plus an immediate transaction gives the same exact-once
    contract as DurableJournal without relying on process-local indexes.
    """

    def __init__(self, path: str):
        self.path = path
        self._lock = threading.RLock()
        self._db = sqlite3.connect(path, timeout=30, isolation_level=None,
                                    check_same_thread=False)
        self._db.execute("PRAGMA busy_timeout=30000")
        for attempt in range(20):
            try:
                self._db.execute("PRAGMA journal_mode=WAL")
                break
            except sqlite3.OperationalError:
                if attempt == 19:
                    raise
                time.sleep(0.05 * (attempt + 1))
        self._db.execute("PRAGMA synchronous=FULL")
        self._db.execute(
            "CREATE TABLE IF NOT EXISTS fcf_events ("
            "event_id TEXT PRIMARY KEY, event_type TEXT NOT NULL, payload TEXT NOT NULL)"
        )

    @staticmethod
    def _record(row: tuple) -> Dict[str, Any]:
        return {"event_id": row[0], "event_type": row[1], "payload": json.loads(row[2])}

    def append_once(self, event_id: str, event_type: str, payload: Dict[str, Any]) -> bool:
        record = {"event_id": event_id, "event_type": event_type, "payload": deepcopy(payload)}
        payload_json = json.dumps(record["payload"], sort_keys=True, separators=(",", ":"))
        with self._lock:
            self._db.execute("BEGIN IMMEDIATE")
            try:
                row = self._db.execute(
                    "SELECT event_type, payload FROM fcf_events WHERE event_id = ?", (event_id,)
                ).fetchone()
                if row is not None:
                    existing = {"event_id": event_id, "event_type": row[0], "payload": json.loads(row[1])}
                    if existing != record:
                        raise JournalConflict("event_id reused with different payload")
                    self._db.execute("COMMIT")
                    return False
                self._db.execute(
                    "INSERT INTO fcf_events(event_id,event_type,payload) VALUES (?,?,?)",
                    (event_id, event_type, payload_json),
                )
                self._db.execute("COMMIT")
                return True
            except Exception:
                self._db.execute("ROLLBACK")
                raise

    def get(self, event_id: str) -> Optional[Dict[str, Any]]:
        with self._lock:
            row = self._db.execute(
                "SELECT event_id,event_type,payload FROM fcf_events WHERE event_id = ?", (event_id,)
            ).fetchone()
            return deepcopy(self._record(row)) if row is not None else None

    def records(self) -> List[Dict[str, Any]]:
        with self._lock:
            rows = self._db.execute(
                "SELECT event_id,event_type,payload FROM fcf_events ORDER BY event_id"
            ).fetchall()
            return [self._record(row) for row in rows]

    def close(self) -> None:
        with self._lock:
            self._db.close()

    def __enter__(self) -> "SQLiteJournal":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()
