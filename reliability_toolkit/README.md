# Reliability Toolkit

This folder is the extraction target for reusable reliability patterns proven against the Dice Duel reliability lab.

Dice Duel proved the workflow. This toolkit extracts the workflow.

## Status

Initial scaffold only. These files are not yet a production package and should not be treated as a drop-in framework.

## Design boundary

The toolkit should contain reusable methods, templates, and documentation. Dice Duel-specific assumptions belong only in `examples/`.

## Pattern classes

```text
- guarded source baselines
- patcher safety
- unit-test orchestration
- mutation probes
- crash-window probes
- previous-good recovery
- run-budget validation
- checkpoint reports
- stop rules
```

## Evidence source

Current case study: Dice Duel Reliability Lab.

Certified result:

```text
124 unit tests passed
63/63 tracked mutations killed
unsafe_trust=0
self_heal_failed=0
```

## Non-goals for first extraction

```text
- package publishing
- CLI framework
- real power-loss durability
- universal test registry
- replacing project-specific tests
```
