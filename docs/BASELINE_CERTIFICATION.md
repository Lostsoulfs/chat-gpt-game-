# Baseline Certification

Date: 2026-05-25
Project: Dice Duel Reliability Lab
Repository target: `Lostsoulfs/chat-gpt-game-`

## Certified local lab state

The cleaned local `dice_duel_lab/` folder passed the full lab sweep before this GitHub documentation push.

```text
Unit suite: 124/124 passed
Mutation probe 1: 13 killed, 0 survived, 0 errors
Mutation probe 2: 14 killed, 0 survived, 0 errors
Mutation probe 3: 14 killed, 0 survived, 0 errors
Mutation probe 4 previous-good: 8 killed, 0 survived, 0 errors
Mutation probe 5 contracts/summary: 14 killed, 0 survived, 0 errors
Total tracked mutations: 63/63 killed
Crash probe unsafe_trust: 0
Crash probe self_heal_failed: 0
Sweep commands: 7
Sweep failures: 0
Sweep exit code: 0
Visible stage runtime total: 281.27 seconds
```

## Guarded hashes

```text
dice_duel.py: cc176c272b989ddd6cb391f8d7641c670e6757b507527853992246f15dc8bf33
dice_duel_tests.py: 5fcc56dc5701aee1258841e48dc35f668a667d519833a4df0ee7729e025cc544
```

## Interpretation

This is a freeze-worthy cleaned baseline for the Dice Duel reliability lab.

The baseline proves the covered contracts, mutation targets, and crash-probe classifications represented by the current test/probe suite. It does not prove production durability.

## Not proven

```text
- true OS power-loss durability
- real process-kill crash testing
- fsync/directory-sync durability
- production packaging
- removal of legacy global config bridge
- general-purpose framework status
```

## Standing rule

Do not patch `dice_duel.py` by default. The next push should extract reusable reliability-toolkit patterns unless an explicit new Dice Duel branch is selected.
