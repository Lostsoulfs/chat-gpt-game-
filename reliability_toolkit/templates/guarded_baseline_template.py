"""
Guarded baseline template.

Purpose:
    Record expected hashes for critical files and fail loudly when the local
    working tree differs from the certified baseline.

This is a template. Replace TARGETS with project-specific files and hashes.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


TARGETS = {
    # "app.py": "expected_sha256_here",
    # "tests.py": "expected_sha256_here",
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def check_baseline(root: Path = Path(".")) -> bool:
    ok = True
    for relative_path, expected_hash in TARGETS.items():
        path = root / relative_path
        if not path.exists():
            print(f"MISSING | {relative_path}")
            ok = False
            continue

        actual_hash = sha256_file(path)
        if actual_hash != expected_hash:
            print(f"DRIFT   | {relative_path}")
            print(f"expected: {expected_hash}")
            print(f"actual:   {actual_hash}")
            ok = False
        else:
            print(f"OK      | {relative_path}")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if check_baseline() else 1)
