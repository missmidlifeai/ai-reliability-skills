---
name: independent-evaluation
description: Use before scoring, grading, ranking, or reviewing anything: tests, agents' work, your own deliverables, options being compared. Checks independence first; runs the full evaluation card only for consequential judgments.
---
<!-- Cost: always-loaded ~46 tokens (description only); full body ~225 tokens when triggered; adds per run: low (2 questions); moderate on consequential judgments; schedules runs: none. Estimates (words x 1.4), not measured. -->

# Independent Evaluation

## Always: recusal check (two questions)
1. Am I an author or subject of any part of this?
2. Have I seen its keys, scores, or expected results?
Either yes: disclose it and don't take the evaluator seat (or label the result "not independent").

## Consequential judgments only (rankings you act on, hires, published scores, go/no-go)
Run all six, and report answers alongside the verdict:
1. What is the claim, what result would count against it, and what's the strongest alternative reading?
2. Independent: no stake, no keys or scores seen?
3. Criteria fixed before results arrived?
4. Grading state and traces, not a summary or self-report?
5. Judge from a different model family than the subject? Verify it from configuration or provider, not by assumption; if you can't verify it, say so.
6. Worst run reported; what I didn't check, stated.

Self-grading fails because the model finds its own work reasonable. Independence is the mechanism, not courtesy.
