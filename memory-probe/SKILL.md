---
name: memory-probe
description: Use after building or changing a long-term memory system, or when a specific decision depends on whether stored memory can actually be retrieved. Tests reads, not writes. Do not run on a schedule it hasn't earned.
---
<!-- Cost: always-loaded ~56 tokens (description only); full body ~277 tokens when triggered; adds per run: moderate per run; rare; schedules runs: none; never on an unearned schedule. Estimates (words x 1.4), not measured. -->

# Memory Probe

Memory systems get write-tested constantly and read-tested almost never.

**Before running:** state the decision the result would change. If none, don't run.

## Method
1. **Commit 8-12 questions to a file before answering any.** Mix: stable facts; deep retrievals (only in dated logs); conflict updates (true once, since superseded; answer is the current state plus the history); distractors (plausible-but-false, including your own past errors, which must be actively rejected); why-questions (conclusion + reason + source). Tag each by tier: always-loaded summary, log retrieval, or superseded-claim resolution. Require all three tiers.
2. Answer from the always-loaded layer; where it's insufficient, run the normal retrieval and record what it actually returned.
3. Quote the real file lines behind each answer. No quote, not passed.
4. Score per question, then grade the probe: too easy (mostly summary-answerable)? unblinded (self-authored)? what categories untested?
5. **Backtest rule:** a probe earns a standing schedule only after a run surfaces a real retrieval failure. A 10/10 on an easy probe is a baseline.

Worked example: 10/10, but 8 of 10 answerable from the summary, no blinding, superseded claims untested. Verdict: no standing schedule; next bar is a blind round with third-party-written questions.
