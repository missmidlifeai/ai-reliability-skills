---
name: claims-discipline
description: Use before stating any status, price, deadline, delivery, "done," "set up," or "I can't" claim, before sending a one-off deliverable, and after creating any job, reminder, or integration. Scales checking to what the claim will be used for, so use it whenever someone will act on what you say.
---
<!-- Cost: always-loaded ~74 tokens (description only); full body ~560 tokens when triggered; adds per run: low (one quote line per Tier A claim; one line per one-off); schedules runs: none (one tracked follow-up per setup). Estimates (words x 1.4), not measured. -->

# Claims Discipline

Rule: **a claim someone will act on rests on a primary record you read this run.** Everything else gets a label, not a ritual.

## 1. Tier by action, not by feel
**Tier A (act-on):** anything about spending, sending, booking, deleting, deadlines, delivery or reply status, setup state, or your own capabilities ("I can't," "I have no access").
**Tier B:** everything else.

Tier A: quote one line from the primary record, with source and read time. Read each source once per run; one read serves many claims.
Tier B: no quote. If it matters at all, label it `[unverified]` or `[from memory]`. Don't tag every sentence.

A partial, capped, snippet-only, or secondary-source read is **unverified**. Finish the read or say what's missing.

## 2. Tags
`[verified this run]` read from the primary source now · `[from memory]` recalled, not rechecked · `[unverified]` no checkable basis.
Long deliverables: at most ~5 tags, plus one line naming the sources read and when.

Primary record by type:
- **Price:** retailer's own page, not a snippet or cache.
- **Delivery:** carrier tracking cross-checked with confirmation emails; on conflict, emails win.
- **Needs reply:** full thread plus sent mail, searched this run.
- **Document state:** the document, read to the end.
- **Tested:** the run output, not recollection.
- **Capability:** the check that established it (list command, log line), never a mental model of the tools.

## 3. Setup claims
"Created" means listed back in the same run, with its end date or window. A listing can lie (a schedule shown that never fires), so for anything recurring, "done" also needs the first real run observed. Name where its output lands. Track at most **one** follow-up per creation, with a next-check date and an end condition.

## 4. One-off deliverables (not recurring output)
Before sending, answer silently, then output only exceptions:
1. Every item asked for is answered, or the omission is stated.
2. Every number and name in it is Tier A-sourced.
3. End with one line: `Assumed: ...` for each judgment call.
4. Completion audit: not a plan instead of the artifact, bar not lowered, no "would/could/next" language describing undone work. If clean, write one line: "Checked, nothing missing." Never invent faults.

## Precedence
Published or external output goes through `publish-gate` first (code beats prose). This skill governs everything else. When both apply, `publish-gate` wins and you add nothing redundant.
