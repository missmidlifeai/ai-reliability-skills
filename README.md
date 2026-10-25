# AI Reliability Skills, v2 (consolidated)

Twelve skills became eight, plus a short always-loaded core. Premise unchanged: the model supplies judgment, the harness supplies discipline.

## Layering (what wins when several apply)
1. `untrusted-content`: security; always first.
2. `publish-gate`: code gate for external/published output; beats prose rules.
3. `claims-discipline`: everything else someone will act on.
4. `build-and-decide`, `followup-cadence`, `independent-evaluation`: task disciplines.
5. `learning-ledger`, `memory-probe`: improvement and memory; they measure the others.

## Old → new
| Old | New |
|---|---|
| verify-before-you-speak, evidence-tags, pre-send-gate, read-back-verification | claims-discipline |
| two-stage-sourcecheck | publish-gate (renamed to what it does; script added) |
| async-followup-protocol | followup-cadence (machine vs human; capped) |
| correction-loop, memory-budget | learning-ledger (duplicated ledger rules merged) |
| memory-probe | memory-probe (trimmed) |
| recusal-and-evaluation | independent-evaluation (full card only when consequential) |
| build-discipline, discussion-vs-decision | build-and-decide |
| (new) | untrusted-content (injection, private-info release, tool failure) |

Old folder names are retired on purpose: no stub folders are kept, so the always-loaded cost stays at the estimate below. Use the table above to find a skill's new home.

## Loading and cost
Install `core.md` as standing instructions (~160 tokens). Install each folder as a skill so only its description (~50-75 tokens) is always loaded and the body loads on trigger. Estimated always-loaded total: ~650 tokens. Full bodies total ~2,700 tokens, loaded only as triggered. All figures are word-count estimates, not measurements. Trigger reliability depends on your harness: where the model is the only trigger, add harness triggers (before send, after job creation).

## Adoption order
1. core.md + untrusted-content. 2. claims-discipline. 3. learning-ledger (it produces the failure evidence everything else needs). 4. The rest as the ledger shows need.

## Not yet done (be honest)
- Every number here is an untested default: follow-up cadence, the 60% overlap threshold, the ~5 tag cap, every-fifth sampling, the memory budget (blank on purpose). Tune from ledger data.
- No failure replays are shipped. The README's own bar says a rule needs them; build them from your own corrections log.
- Measure token spend by source for a week before and after adopting, to confirm the savings.
