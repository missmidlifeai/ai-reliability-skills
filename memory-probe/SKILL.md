# Memory Probe

## Purpose
Verify that an agent's long-term memory can be *read*, not just written. Every memory system is write-tested — notes get saved, logs get appended. Almost none are read-tested: can the agent actually retrieve what it stored, resolve a superseded claim to its current state, and reject a plausible-but-false statement? Pairs with `memory-budget`: that skill governs what gets written; this one checks what comes back out.

## When to run it
- After building or changing a memory system, before trusting it.
- As a periodic spot-check — but only on a standing schedule after a run catches something real (see Scoring).

## The method

### 1. Commit the questions first
Write 8–12 questions to a file *before* answering any of them. Mix five kinds:
- **Stable facts** — things that should be in the always-loaded summary.
- **Deep retrievals** — things living only in dated logs or secondary notes, requiring search.
- **Conflict updates** — claims that were true and later superseded. The correct answer is the *current* state, with the history named.
- **Distractors** — plausible-but-false statements, including the agent's own past errors. These must be actively rejected, not just left unanswered.
- **Why-questions** — "why did we decide not to do X?" The canonical test: conclusion + reason + source, in the original framing.

### 2. Answer from working memory first
Answer each question from the always-loaded layer only. Where that layer is insufficient, run the agent's normal retrieval mechanism — the retrieval pipeline itself is what's under test, so record what it actually returned, not what you hoped it would.

### 3. Verify every answer against the primary record
Read the real file lines behind each answer and quote them. An answer without a quoted source is unverified, not passed.

### 4. Score honestly — including the probe itself
Pass/fail per question, with the verification trail. Then grade the probe:
- **Too easy?** If most questions were answerable from the always-loaded summary, it tested working memory, not deep retrieval.
- **Blinded?** A self-authored probe grades its own homework. Ideally a third party writes the questions from the logs, unseen by the answerer.
- **Untested categories?** Name what the probe didn't cover — especially superseded claims where the outdated answer sounds plausible.

### 5. The backtest rule
A probe that catches nothing real does not earn a standing schedule. Promote to recurring only after a run surfaces a genuine retrieval failure. A 10/10 on an easy probe is a baseline, not a victory.

## Worked example
First run: 10 questions, 10/10. Real signals: both distractors rejected — including refusing to repeat the agent's own earlier model-number error when baited with it — and a conflict-update (access granted, later revoked) resolved to the current state. Honest limitations: 8 of 10 were answerable from the always-loaded summary, no blinding, and the superseded-claim category went untested. Verdict: no standing schedule; the bar for promotion was set as a blind second round with third-party-authored questions.
