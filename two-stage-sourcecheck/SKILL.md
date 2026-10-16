# Two-Stage Sourcecheck

## Purpose
Stop hallucinations in anything published: briefs, reports, summaries, posts. A deterministic gate that every quoted claim must pass before delivery.

## The method
Two stages, both must pass:

**Stage 1 — Verbatim existence.** Every quoted claim must appear word-for-word in its cited source. Implement with a simple string-match over the source text. Threshold: exact match. No fuzzy credit.

**Stage 2 — Support.** Every quote must actually *support* the claim it's attached to — not merely share vocabulary. Implement with an offline lexical verifier: check that the claim's key nouns, numbers, and relations are present in the quoted passage, not just scattered across the document.

## The worker rule
If a stage flags a claim: reword closer to the source's own words and re-run. If it still fails, drop the claim. Never override the gate. It fails closed by design — occasional true-but-loosely-worded claims get dropped, which beats the old failure mode of publishing confident falsehoods.

## Known limits (say these out loud)
- Paraphrase can pass a claim whose key noun is absent if filler words overlap.
- Wrong numbers pass if they reuse the source's own words around them.
These remain for a future judge stage or human review. A gate with known blind spots, stated plainly, beats a gate that pretends to be complete.

## Rollback
Ship every enforced check with a rollback note: how to disable it in one action, and what breaks if you do. A gate you can't turn off is a liability the first time it misfires.
