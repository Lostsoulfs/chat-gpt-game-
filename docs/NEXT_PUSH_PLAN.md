# Next Push Plan

## Objective

Extract a reusable reliability toolkit from the Dice Duel reliability lab while preserving the certified Dice Duel baseline.

## Branch target

```text
reliability_toolkit/
```

## Push 1 scope

Create a toolkit scaffold and documentation only. Do not modify the app-under-test.

Planned structure:

```text
reliability_toolkit/
  README.md
  TOOLKIT_INVENTORY.md
  CERTIFICATION_LADDER.md
  STOP_RULES.md

  templates/
    reusable_patcher_template.py
    reusable_mutation_probe_template.py
    reusable_crash_probe_template.py
    reliability_checkpoint_report_template.py
    guarded_baseline_template.py

  examples/
    dice_duel_case_study.md

  docs/
    mutation_testing_notes.md
    crash_window_testing_notes.md
    previous_good_recovery_notes.md
    run_budget_notes.md
```

## In scope

```text
- documentation extraction
- generic template skeletons
- Dice Duel case-study summary
- stop rules
- certification ladder
- inventory of reusable patterns
```

## Out of scope

```text
- patching dice_duel.py
- modifying dice_duel_tests.py
- gameplay expansion
- CLI expansion
- fsync/directory-sync durability
- universal harness registry
- claiming production durability
```

## Acceptance criteria

```text
- Dice Duel source remains unchanged
- Dice Duel guard still passes locally
- Dice Duel unit suite still passes locally
- toolkit folder exists
- docs distinguish proven behavior from reusable pattern
- generic templates avoid hardcoded Dice Duel paths
- Dice Duel-specific content stays under examples/
```

## Verification rule

If no Dice Duel source/test/probe files change, local verification can be limited to:

```bash
python3 dice_duel_guard.py --check
python3 -m unittest -q dice_duel_tests.py
```

If any app, test, probe, or sweep file changes, full lab sweep is mandatory.
