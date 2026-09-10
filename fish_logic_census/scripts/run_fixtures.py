"""Standalone fixture runner: prints the Acceptance Gate block (F-total/pass/fail)."""
import subprocess, sys
from pathlib import Path
if __name__ == "__main__":
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", str(Path(__file__).parent / "test_fixtures.py")],
        capture_output=True, text=True)
    tail = result.stdout.strip().splitlines()[-1] if result.stdout.strip() else "?"
    print(f"fixture_pass_line = {tail}")
    print("fixture_total = 12 (F01-F07,F10,F11,F13,F14,F15 as automated; F08/F09/F12/F16/F17 asserted via validator tests)")
    sys.exit(result.returncode)
