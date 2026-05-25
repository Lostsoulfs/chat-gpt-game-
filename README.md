# Dice Duel Reliability Lab

Dice Duel is a small Python game used as a controlled reliability-testing target. The game itself is intentionally narrow. The useful work is the surrounding lab: unit tests, mutation probes, crash-window probes, guarded source hashes, recovery checks, and reusable reliability patterns.

## Current Certified Baseline

Status: freeze-worthy cleaned baseline.

```text
Guard: no source drift
Unit suite: 124 tests passed
Mutation probes: 63/63 tracked mutations killed
Mutation survivors: 0
Mutation errors: 0
Crash probe unsafe_trust: 0
Crash probe self_heal_failed: 0
Full sweep failures: 0
Full sweep exit code: 0
```

Certified source hashes from the cleaned local lab folder:

```text
dice_duel.py: cc176c272b989ddd6cb391f8d7641c670e6757b507527853992246f15dc8bf33
dice_duel_tests.py: 5fcc56dc5701aee1258841e48dc35f668a667d519833a4df0ee7729e025cc544
```

## What This Repository Tracks

This repository is being set up for the Dice Duel reliability lab and the reusable reliability-toolkit extraction branch.

Current push scope:

```text
- baseline certification documentation
- branch plan
- stop rules
- certification ladder
- reusable toolkit scaffold
- generic template files
```

Not included in this first GitHub push:

```text
- local generated artifacts
- Google Drive paths
- private machine paths
- raw sweep logs containing local account paths
- unverified source-code copies
```

## Next Branch

Recommended next branch: extract reusable reliability toolkit patterns from Dice Duel without modifying the certified app-under-test.

Do not patch `dice_duel.py` by default. App changes should happen only on an explicit hardening/gameplay branch after the certified baseline is preserved.
