---
name: morning-checkin
description: Daily planning check-in. Use when I want to plan my day or week, say good morning, check in, ask what to work on today or what's due, or want my schedule time-blocked. Reads my calendar, tasks, and your notes, proposes a time-blocked plan, and saves it (updating my day page) only after I agree.
---

# Morning check-in

## 1. Gather (read only)
- Today's date and time: run `date`.
- Read `data/calendar.json`, `data/tasks.json`, `notes/notes.md`.
- Read `context/planning-rules.md` and follow it exactly.
- If `plans/` has yesterday's plan, read it to recap.

## 2. Open with a short brief (5–8 lines)
- **Yesterday:** what was planned and what carried over (from notes and yesterday's plan).
- **Today's fixed events.**
- **Due in the next 3 days**, ranked, with hours needed vs. hours open.
- **Clashes or warnings.**

## 3. Ask one or two questions, and suggest
Only ask what changes the plan. For example: "Did you finish X yesterday?" or "Swim at 11:30 today or Thursday evening?"
If there's a clash, you **must** ask how to handle it here. Don't decide it yourself.
For open slots (especially mornings), **suggest** a task or two that would fit, like "9–12 is free. Book flights?" Add them only if I say yes.

## 4. Propose the plan
A time-blocked list from wake (~8:30) to the 23:30 hard stop, with assignments in full 3-hour blocks, no breaks, and no filler. One task = one slot, with its parts as bullets:
```
12:00–15:00  focus  DBS Assignment 6
                    • Finish hook + test  • Record demo  • Post + submit
17:30–19:30  fixed  Design, Build, Ship
19:30–20:15  meal   Dinner
20:15–23:15  focus  AFT assignment
                    • Problems 1–3  • Problems 4–5
```
Then ask: "Save this plan?"

## 5. On "yes" (and only then)
1. Write `plans/YYYY-MM-DD.json` in the schema from `context/data-format.md`, and copy it to `plans/today.json`. The page at http://localhost:8000/ui/ updates within a few seconds.
2. Append a dated entry to `notes/notes.md`: plan summary, carry-overs, any new preference I mentioned. Update "Standing observations" if something changed.
3. Reply in one line: "Plan saved. Your page is updated."

If I want changes, revise and ask again. Don't save drafts.

## Never
- Edit `data/` (a hook blocks it anyway). If I ask to move an event or finish a task, tell me what to change in the file myself.
- Schedule past 23:30, move classes or interviews, or settle a clash without asking.
