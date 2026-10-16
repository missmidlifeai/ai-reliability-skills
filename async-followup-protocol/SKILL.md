# Async Follow-Up Protocol

## Purpose
Reliable check-backs on delegated async work — emails to collaborators, subagent tasks, anything where you asked and are waiting.

## The cadence
- **Check at 30 minutes.** If there's a reply, report it.
- **Check again at 60 minutes.** If still nothing, assume an outage and switch to **hourly**.
- **Stop after 24 hours** of silence: send one short note naming the thread and the silence, then stop checking.

## The critical detail
Always schedule BOTH the 30-minute and the 60-minute checks up front. Scheduling only the first is how replies sit unread: the first check runs, finds nothing, and there's nothing scheduled to catch the reply that lands five minutes later. The second check stays silent if the first already reported.

## Delivery rule
Report a reply the moment you find one — who replied, the decision or deliverable, what it unblocks. Silence between checks is not news; don't surface "still nothing" until the cadence says to escalate.
