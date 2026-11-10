# Planning rules (read before building a plan)

## Order of operations
1. List the **fixed events** for the day from `data/calendar.json`.
2. List **what's due** today and over the next 3 days from `data/tasks.json`.
3. Rank the tasks (see Ranking).
4. Find the **open blocks** between fixed events, meals, and the day's limits.
5. Fill the blocks with the top-ranked tasks, using their `estimate_hours` (see Assignment blocks).
6. Check `notes/notes.md` for carry-overs from yesterday and fold them in.

## Day limits
- Wake about 8:30. **Don't fill mornings (8:30–12:00) yourself.** Leave them open unless a fixed event, interview prep, or a swim goes there.
- **Focus time is 12:00 until night.** Put deep work (assignments) here.

## Free time slots
- **Never put light tasks or filler into open time on your own.**
- Instead, in the check-in, **suggest** a few things that would fit the open slots (e.g. "You have 9:00–12:00 free. Want to book flights or update your resume?"). Add them to the plan only if I say yes.
- Open time appears in the plan as nothing at all: no "free" blocks.

## Assignment blocks
- Book assignment work in **one 3-hour block** whenever there's that much open time before it's due.
- Don't split assignments into short sessions. If a full 3 hours won't fit, use the biggest open block available, and say so.
- If a task needs more than 3 hours, add another block (preferably on another day, or after a meal).
- Hard stop: **nothing after 11:30 PM.**

## Can't move / can move
| Can't move | Can move |
|---|---|
| Classes, interviews, office hours | Swimming, errands, personal tasks |

When two things clash, **classes and interviews win**. Still **ask me** before booking anything around a clash.

## Ranking
1. Class assignments and exams come first.
2. Among those, the nearest due date ranks highest.
3. Then interview prep, then career tasks, then personal tasks.
4. If a task can't finish before its due date in the open time, say so plainly.

## Interview prep
- Block **45 min right before** each interview.

## Meals
- Lunch around **12:30** (30–45 min). Dinner around **18:30** (45 min).
- On class days (classes start at 17:30), have dinner **right after class** (e.g. ~19:30 after DBS, ~20:30 after AFT or Web Dev).

## Swimming
- At least **once a week**. 1 hr swim + 1 hr to get back and shower = a **2 hr block**.
- Only during pool hours: **11:30–13:30** or **17:00–21:00**. Never before 10:30.
- The swim itself must fit in pool hours. The shower hour can run after them.
- Prefer days with lighter deadlines. If the week is packed, suggest the best slot and let me decide.

## Breaks
- **Don't schedule breaks.** They clutter the plan. I take my own.

## Plan style
- Propose the plan as a short time-blocked list with **as few blocks as possible**, then ask **one or two questions** at most.
- **One task = one slot.** Never split a task into "part 1 / part 2 / wrap-up" blocks back to back. Merge them into one block and list the parts as **bullets** (`steps`).
  - Put meals before or after a task's slot, not in the middle of it, when you can.
  - A task gets a second slot only when something fixed (a class, an interview) or the day's end splits it. That slot gets its own bullets.
- **Heads up** (the box at the top of the page) = `warnings` + `carried_over`. It's the first thing I read, so only what needs my attention goes there.
  - `warnings`: the most important problems (clashes, risk of missing a deadline, nothing booked), 3 at most, each under 10 words, most important first.
  - Don't repeat plain deadlines here. They show in **Due soon** (from `due_soon`), which lists the next 2 days and can expand to show the rest. Include every deadline in the next 7 days in `due_soon`.
- Keep it honest: if the day is overloaded, say what to drop or push.
