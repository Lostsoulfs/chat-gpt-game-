# Certification Ladder

Do not call a patch certified because it merely applies.

## Standard order

```text
1. Confirm source identity.
2. Apply patch or create extracted artifact.
3. Run unit tests.
4. Run relevant mutation probe.
5. Run crash/integration probe if persistence or recovery is affected.
6. Confirm guarded source has no unexpected drift.
7. Save console output.
8. Update checkpoint documentation.
9. Only then select the next branch.
```

## Reduced documentation-only path

If a change only adds documentation or generic templates and does not touch app/test/probe/sweep files:

```text
1. Confirm source identity.
2. Confirm docs do not claim unproven behavior.
3. Run guard locally when practical.
4. Run unit suite locally when practical.
5. Skip full sweep unless source/test/probe files changed.
```

## Failure classification

```text
Unit failure: app behavior or test expectation changed.
Mutation survivor: tests do not prove the intended contract, or source behavior is wrong.
Crash unsafe trust: verifier trusted a bad state.
Self-heal failure: recovery path failed for a covered scenario.
Guard failure: source drift or wrong branch.
Documentation conflict: written claim exceeds evidence.
```
