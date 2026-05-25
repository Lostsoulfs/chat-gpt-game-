"""
Reusable crash-window probe template.

Purpose:
    Simulate interruption windows in persistence or recovery code and verify
    that the loader does not trust unsafe states.

This is not real OS process-kill testing. It is deterministic interruption
simulation. Real durability requires separate process/fsync testing.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import tempfile


@dataclass(frozen=True)
class CrashScenario:
    name: str
    crash_point: str | None
    expected_raw_state: str
    expected_recovery_state: str


SCENARIOS = [
    # CrashScenario(
    #     name="crash_before_main_replace",
    #     crash_point="before_main_replace",
    #     expected_raw_state="BACKUP_ONLY_OK",
    #     expected_recovery_state="SELF_HEAL_BACKUP",
    # ),
]


def run_scenario(root: Path, scenario: CrashScenario) -> tuple[str, str]:
    """Replace with project-specific persistence and recovery calls."""
    raise NotImplementedError("customize this probe for the target project")


def main() -> int:
    unsafe_trust = 0
    self_heal_failed = 0

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for scenario in SCENARIOS:
            try:
                raw_state, recovery_state = run_scenario(root, scenario)
            except NotImplementedError:
                print("TEMPLATE ONLY | customize run_scenario()")
                return 2

            if raw_state != scenario.expected_raw_state:
                unsafe_trust += 1
                print(f"UNSAFE_TRUST | {scenario.name} | got={raw_state}")

            if recovery_state != scenario.expected_recovery_state:
                self_heal_failed += 1
                print(f"SELF_HEAL_FAILED | {scenario.name} | got={recovery_state}")

    print(f"unsafe_trust={unsafe_trust} self_heal_failed={self_heal_failed}")
    return 0 if unsafe_trust == 0 and self_heal_failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
