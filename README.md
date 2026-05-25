# Dice Duel Reliability Lab

Dice Duel is a small Python game used as a controlled reliability-testing target. The game itself is intentionally narrow. The useful work is the surrounding lab: unit tests, mutation probes, crash-window probes, guarded source hashes, recovery checks, and reusable reliability patterns.

## Current Stable Version

Status: stable version declared for GitHub tracking on 2026-05-25 after local Drive cleanup/move mismatch.

Current source identity provided from the local `dice_duel_lab/` guard output:

```text
dice_duel.py: dbc0767716e7ddb7cb6350ceff61688e89a96ee703ec19b5cec6150b4a35eb2d
dice_duel_tests.py: 5fcc56dc5701aee1258841e48dc35f668a667d519833a4df0ee7729e025cc544
```

Previous full-sweep evidence preserved for the reliability-lab checkpoint:

```text
Unit suite: 124 tests passed
Mutation probes: 63/63 tracked mutations killed
Mutation survivors: 0
Mutation errors: 0
Crash probe unsafe_trust: 0
Crash probe self_heal_failed: 0
Full sweep failures: 0
Full sweep exit code: 0
```

## What This Repository Tracks

This repository is being set up for the Dice Duel reliability lab and the reusable reliability-toolkit extraction branch.

Current push scope:

```text
- stable-version identity documentation
- baseline certification notes
- branch plan
- stop rules
- certification ladder
- reusable toolkit scaffold
- generic template files
```

Not included yet:

```text
- raw local generated artifacts
- Google Drive local paths
- private machine paths
- raw sweep logs containing local account paths
```

## Next Branch

Recommended next branch: extract reusable reliability toolkit patterns from Dice Duel while preserving the current stable version identity.
