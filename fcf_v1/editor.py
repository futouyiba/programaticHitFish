"""In-memory reference for the editor's transactional/versioned contract."""

from copy import deepcopy
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .dsl import Diagnostic, DSLCompileError, compile_artifact


@dataclass(frozen=True)
class ArtifactVersion:
    version_id: str
    message: str
    author: str
    artifact: Dict[str, Any]


class ArtifactStore:
    """Immutable version history with atomic draft edits."""

    def __init__(self, initial_artifact: Dict[str, Any], *, author: str = "system"):
        self._versions: List[ArtifactVersion] = []
        self._draft = deepcopy(initial_artifact)
        self._author = author

    @property
    def draft(self) -> Dict[str, Any]:
        return deepcopy(self._draft)

    def edit(self, path: str, value: Any) -> None:
        """Edit a dotted path in a draft; failed paths leave draft unchanged."""
        parts = path.split(".")
        if not parts or any(not p for p in parts):
            raise ValueError("path must be non-empty")
        trial = deepcopy(self._draft)
        node: Any = trial
        for part in parts[:-1]:
            if isinstance(node, list):
                node = node[int(part)]
            elif isinstance(node, dict) and part in node:
                node = node[part]
            else:
                raise KeyError(path)
        last = parts[-1]
        if isinstance(node, list):
            node[int(last)] = value
        elif isinstance(node, dict):
            if last not in node:
                raise KeyError(path)
            node[last] = value
        else:
            raise KeyError(path)
        self._draft = trial

    def validate(self) -> List[Diagnostic]:
        try:
            compile_artifact(self._draft)
        except DSLCompileError as exc:
            return list(exc.diagnostics)
        return []

    def save_as_new_version(self, message: str, *, author: Optional[str] = None) -> ArtifactVersion:
        diagnostics = self.validate()
        if diagnostics:
            raise DSLCompileError(diagnostics)
        version_id = f"fcf.v1:{len(self._versions) + 1}"
        version = ArtifactVersion(version_id, message, author or self._author, deepcopy(self._draft))
        self._versions.append(version)
        return ArtifactVersion(version.version_id, version.message, version.author, deepcopy(version.artifact))

    def compile(self) -> Dict[str, Any]:
        return compile_artifact(self._draft)

    @property
    def versions(self) -> List[ArtifactVersion]:
        return [ArtifactVersion(v.version_id, v.message, v.author, deepcopy(v.artifact)) for v in self._versions]
