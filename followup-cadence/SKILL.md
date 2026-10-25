---
name: followup-cadence
description: Use when delegating work or sending a message that needs a reply (emails, subagent tasks, async jobs) and you must check back later. Sets capped, low-cost check-backs for machines and humans separately.
---
<!-- Cost: always-loaded ~50 tokens (description only); full body ~224 tokens when triggered; adds per run: low per check; minimal-context reads; schedules runs: yes: capped at 4 checks (machine) or 2 (human). Estimates (words x 1.4), not measured. -->

# Follow-up Cadence

Every check is a full run. Cap them.

## Schedule all checks up front, in one step
Scheduling only the first is how a reply landing at minute 31 gets missed.

**Machine work** (subagent, job, API): checks at 30 min, 60 min, 4 h, then one 24 h report. Stop.
**Humans:** one check next business day, one follow-up message after that, then one short note naming the thread and the silence. Stop. Polling does not change human latency.

Defaults are untested guesses. Log each real reply latency in the ledger and adjust after 10 samples.

## Each check is minimal
Read only the thread or status line being watched, not the skill library or history. If a check finds nothing, say nothing. If an earlier check already reported the reply, later checks stay silent.

## Reporting
Report the moment there is news: who replied, the decision or deliverable, what it unblocks. Silence between checks is not news.
