# Verify Before You Speak

## Purpose
Kill the most common failure mode in AI assistants: stating statuses — done, delivered, tested, current, still broken — from summaries, stale memory, or vibes instead of the primary record.

## The rule
Before stating any status claim, quote the primary record it rests on:
- **Needs-reply / still undone:** the full thread plus sent mail, searched this run.
- **Delivered / shipped:** the delivery record plus confirmation, cross-checked this run.
- **Document state:** the document itself, read to its end.
- **Tested / verified:** the test output or run log, not your recollection of running it.
- **Self-capability claims** ("I can't," "I don't have access," "I didn't do X"): the check that established it — the connector's account/list command, the doc section, the log line. Never a mental model of the tools.

## What counts as unverified
A partial, capped, or single-secondary-source read makes the claim unverified. Either finish the read, or label the claim and say exactly what's missing. "I checked the first page" is not verification.

## Why it works
Fluency is the enemy here: the model will happily produce a confident status from a vague memory because confident statuses are what training rewarded. Forcing a quoted primary record turns every status into a checkable fact. It also makes scheduled-worker handoffs safe — re-check decisive claims against the source before relaying them, even when the handoff sounds certain.
