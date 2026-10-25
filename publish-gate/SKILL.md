---
name: publish-gate
description: Use before any externally visible or published output (briefs, reports, posts, summaries sent to third parties) that contains quoted or sourced claims. Runs a deterministic check that each claim's quote exists in its source and matches the claim's numbers and names. Skip for internal messages.
---
<!-- Cost: always-loaded ~68 tokens (description only); full body ~341 tokens when triggered; adds per run: low-moderate (script is free; reword/retry is the cost); schedules runs: none. Estimates (words x 1.4), not measured. -->

# Publish Gate

A **paraphrase-and-consistency gate**, not an anti-hallucination guarantee. It catches invented quotes, wrong numbers, and unsupported names. It does not judge meaning.

## Run
1. Collect every sourced claim as `{claim, quote, source}`; batch them all in one pass.
2. `python scripts/sourcecheck.py items.json`
3. Stage 1: the quote must appear in the source after normalizing case, whitespace, thousands separators, "percent"/"%", "$", and minute/min.
   Stage 2: every number in the claim must appear in the quote; every capitalized name (after the first word) must appear in the quote; at least 60% of the claim's content words must appear in the quote.
4. On failure: reword closer to the source and rerun **once**. If it still fails, drop the claim. Never override.

Numbers and names are always checked. For long prose, check a sample plus every claim you'd be embarrassed to get wrong.

## Known limits (say them when you report)
- Meaning isn't checked: a negation or reversed relation can pass if the words overlap.
- A name that is the first word of a claim isn't checked as a name.
- Unit or currency swaps pass (`$5` vs `5 euros`); check these by eye.
- Sources paraphrased by a secondary site pass if the quote is in that site.
Remaining risk goes to human review for anything consequential.

## Rollback
Disable by skipping step 2 and noting "gate skipped" in the output. Without it, nothing blocks a fabricated quote. Don't disable silently.
