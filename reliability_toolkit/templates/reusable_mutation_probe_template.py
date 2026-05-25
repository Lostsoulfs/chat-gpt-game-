"""
Reusable mutation probe template.

Purpose:
    Apply small source mutations and verify that the test suite rejects each
    mutated version.

Expected interpretation:
    KILLED   = tests failed against mutated source; contract is covered.
    SURVIVED = tests passed against mutated source; coverage or contract gap.
    ERROR    = probe infrastructure failed; result is not evidence.

This is a template. Do not use it as proof until customized and tested.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import shutil
import subprocess
import sys


@dataclass(frozen=True)
class Mutation:
    name: str
    old: str
    new: str
    expected: str = "KILLED"


MUTATIONS = [
    # Mutation(
    #     name="remove_required_validation",
    #     old="raise ConfigError",
    #     new="# raise ConfigError",
    # ),
]


APP_FILE = Path("app_under_test.py")
TEST_COMMAND = [sys.executable, "-m", "unittest", "-q"]


def run_tests() -> int:
    return subprocess.run(TEST_COMMAND).returncode


def apply_mutation(source: str, mutation: Mutation) -> str:
    if mutation.old not in source:
        raise ValueError(f"anchor not found for mutation: {mutation.name}")
    return source.replace(mutation.old, mutation.new, 1)


def main() -> int:
    original = APP_FILE.read_text(encoding="utf-8")
    backup = APP_FILE.with_suffix(APP_FILE.suffix + ".mutation_backup")
    shutil.copy2(APP_FILE, backup)

    killed = survived = errors = 0

    try:
        for mutation in MUTATIONS:
            try:
                APP_FILE.write_text(apply_mutation(original, mutation), encoding="utf-8")
                returncode = run_tests()
                if returncode != 0:
                    killed += 1
                    print(f"KILLED   | {mutation.name}")
                else:
                    survived += 1
                    print(f"SURVIVED | {mutation.name}")
            except Exception as exc:
                errors += 1
                print(f"ERROR    | {mutation.name} | {exc}")
            finally:
                APP_FILE.write_text(original, encoding="utf-8")
    finally:
        if backup.exists():
            backup.unlink()
        APP_FILE.write_text(original, encoding="utf-8")

    print(f"killed={killed} survived={survived} errors={errors}")
    return 0 if survived == 0 and errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
