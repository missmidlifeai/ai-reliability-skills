# Correction Loop

## Purpose
Turn corrections into compounding reliability instead of repeated apologies.

## The log
Log every correction the same day, with fixed fields:
- **Date, task type**
- **What happened / what was right**
- **Root cause** — named honestly: skipped read, wrong assumption, stale memory, guessed instead of asking, procedure gap, rule not updated everywhere.
- **Where-else**: the *class* of miss, not just this instance. A wrong detail in one place means checking every place with the same shape.
- **What-else-used-it**: every artifact and job that carried the wrong fact — patched the same day.
- **Rule created** (if any), **status**.

An unlogged correction is an unlearned one.

## Two-week graduation
If a logged pattern recurs 14+ days after its rule was created, the written rule failed. Don't rewrite the rule — propose an *enforced check* instead (a gate, a checklist item, a verification step). Rules that only exist as text decay; checks that run don't.

## Classification decides the fix
- **Harm**: the rule itself caused damage → rewrite or remove it.
- **Non-compliance**: you ignored a sound rule → reinforce or restructure it, never delete it.
- **Irrelevant**: retire it.
- **Orchestration**: the tooling caused it → report-only, never a memory rule.

## Ledger discipline
Candidate learnings go to a ledger with a verbatim quote per sighting — no quote, no entry. A learning promotes into durable memory only with sightings from 2+ distinct days. One bad day never rewrites the rules.
