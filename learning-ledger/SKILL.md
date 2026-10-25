---
name: learning-ledger
description: Use when you are corrected, when a mistake recurs, when deciding whether to add or change a durable rule or memory, or when reviewing which checks are worth their cost. Logs corrections, promotes patterns to enforced checks only when worth it, and keeps long-term memory within budget.
---
<!-- Cost: always-loaded ~71 tokens (description only); full body ~565 tokens when triggered; adds per run: low per correction; weekly review; schedules runs: none (weekly batch review). Estimates (words x 1.4), not measured. -->

# Learning Ledger

## Log every correction the same day (one short entry)
Date and task type · what happened vs what was right · **root cause** (skipped read, wrong assumption, stale memory, guessed instead of asking, procedure gap, rule not updated everywhere) · **level** (repair = local fix, redesign = mechanism change, reset = approach contradicts evidence) · **where else** the same class of miss could live · **what else used it** (patch the same day) · rule created, if any · tokens spent on the miss and its fix.
An unlogged correction is an unlearned one.

## Classify, then fix
- **Harm** (the rule caused damage): rewrite or remove it.
- **Non-compliance** (sound rule ignored): restructure or enforce it; never delete.
- **Irrelevant:** retire it.
- **Orchestration** (tooling fault): report only; no memory rule.

## Graduation: written rule → enforced check
If a pattern recurs 14+ days after its rule was written, the text failed. Propose an enforced check (gate, checklist item, harness step) instead of rewording.
Cost test before promoting: projected failures prevented per month (from the ledger) must exceed tokens spent per month, and fit the check's share of the agent's token budget. Failing the test keeps it a written rule.
Rank root causes by frequency × damage and buy enforced checks only from the top of that list.
Once stable, **sample prose checks** (e.g. every fifth). Never sample gates that block irreversible actions.

## Candidate learnings
One ledger line per sighting with a **verbatim quote**; no quote, no entry. Promote to durable memory only with sightings on 2+ distinct days from independent channels where possible, or on direct user request. A contradicting record keeps it provisional. One bad day never rewrites a rule. Review the ledger weekly in a batch, not per sighting.

## Memory budget
Set a numeric token budget for durable memory before adopting this skill (write your number here: ____). A blank budget means unset, not unlimited — do not claim budget compliance until a number is set. Additions at the limit must be paid for by **compaction** (merge, summarize, move to searchable logs) before deletion; never delete a true, unrelated fact just to make room.
A new rule ships with a replay of 2-3 past failures it targets (caught / not caught). Live only if the replay changes the outcome. A job with repeated corrections gets its instructions rewritten, not another rule appended.
Persona or identity changes are proposals to the user, never silent edits. Remember rejections; don't re-propose without strictly more evidence, and say what's new.
