# Stop Rules

These rules are meant to prevent silent drift, false certification, and accidental scope expansion.

## Hard stops

```text
Stop if source hash changes unexpectedly.
Stop if test count changes unexpectedly.
Stop if any mutation survives.
Stop if crash probe reports unsafe trust.
Stop if self-heal fails in a covered recovery path.
Stop if patcher anchor matching fails.
Stop if generated artifacts contradict the claimed state.
Stop if a generic template hardcodes project-specific paths outside examples/.
Stop if documentation claims production durability without evidence.
```

## Soft stops

```text
Pause if a branch objective changes mid-work.
Pause if local folder structure differs from the documented source-of-truth folder.
Pause if a tool returns stale or partial file contents.
Pause if a cleanup/rename changes file identity.
```

## Recovery behavior

When a stop rule triggers:

```text
1. Do not patch blindly.
2. Preserve the first failure block.
3. Identify whether the failure is source, test, probe, tool, or documentation drift.
4. Reconcile branch identity.
5. Only then patch or update documentation.
```
