# Dice Duel Case Study

Dice Duel is a compact Python app used to test reliability methods without the noise of a large game codebase.

## Certified checkpoint

```text
Unit tests: 124
Mutation targets: 63
Mutation survivors: 0
Mutation errors: 0
Crash unsafe trust: 0
Self-heal failures: 0
Sweep failures: 0
```

## What made it useful

```text
- small enough to reason about
- large enough to contain real persistence/recovery risks
- deterministic enough for repeatable tests
- simple enough for mutation probes to expose contract gaps
- file-based enough to test manifests, backups, and previous-good recovery
```

## Reusable patterns extracted

```text
- guard source hashes before branch work
- separate raw verifier state from self-heal state
- use mutation probes to test whether unit tests catch broken contracts
- treat patchers as one-shot migration tools, not permanent app code
- require explicit stop rules before continuing after failures
- record both proof and limits in checkpoint docs
```

## Known limits

```text
- no real OS power-loss testing yet
- no fsync/directory-sync durability yet
- no package layout yet
- no claim that templates are a generic framework yet
- legacy globals remain in the app-under-test
```
