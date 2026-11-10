# Life Harness: Demo Script (3–5 min)

**Setup before recording**
- Left: browser at http://localhost:8000/ui/ (run `./serve.sh` if it isn't up).
- Right: a **fresh** Claude Code session in `week6/`.
- To show a clean live update, delete `plans/today.json` and `plans/2026-11-10.json` first, or plan for a different day.
- Have the file tree ready to show: `AGENTS.md`, `context/`, `data/`, `notes/`, `.claude/`.

---

## 1. Intro + harness overview (~45 s)

> "This is my Life Harness, a morning check-in built on Claude Code. Every morning I open it, say good morning, and it plans my day as time blocks. The page on the left updates when I agree to a plan."

> "It has six parts:
> - **Two data sources**: `calendar.json` and `tasks.json` in `data/`. I had Claude make up a realistic week from my real schedule: my three classes, my PLUG interviews, and my assignment deadlines.
> - **`AGENTS.md`**: a short context file that loads every session.
> - **Context files** in `context/`: my detailed planning rules and the file formats.
> - **A skill**, `morning-checkin`, in `.claude/skills/`: the check-in itself.
> - **Notes**, `notes/notes.md`: the harness's memory between days.
> - **A hook** in `.claude/settings.json` that blocks any change to my data."

> "I built it by talking it through with Claude, not in one shot. It asked me questions one at a time: how I plan, what's fixed, when I focus. Then I kept refining. For example, I asked for 3-hour assignment blocks instead of short sessions, no break blocks, no filler tasks in my mornings, and a cleaner page."

---

## 2. Live check-in (~1 min 45 s)

**Type:** `good morning`

While it reads, say:
> "I didn't name the skill. Claude picked it because its description says 'plan my day, good morning, check in, what's due.' Only that description is in context until it matches. Then the full skill loads."

When it shows the brief and questions, say:
> "It recapped yesterday from its notes, listed what's due, and is asking me about [the Friday dinner clash / where to fit a swim]. One of my rules is: if anything clashes, it asks me. It never decides on its own."

**Answer its question** (e.g. `cancel dinner with Sam, swim Saturday at 11:30`).

When it proposes the plan, point out:
> "Assignments get one 3-hour block, with the parts as bullets underneath. No breaks, nothing it made up to fill my morning. It suggests things for free time and only adds them if I say yes. Classes and interviews never move, and nothing goes past 11:30 PM."

**Type:** `yes`

Point at the page:
> "Plan saved, and the page updated by itself. Heads up at the top in red is what needs my attention. Due soon shows the next two days and expands to show the rest. Below that is my schedule."

---

## 3. What loads when (~45 s)

**Type:** `/context` (point at `AGENTS.md` in the memory files)

> "**Every session:** `AGENTS.md`, about 25 lines: where my data lives, my hard rules, and my planning style in two lines. I kept it short because it costs context in every conversation, even ones that aren't about planning.
>
> **Only when needed:** the skill's full instructions load only when I ask to plan. `planning-rules.md` (pool hours for swimming, dinner after class, the 3-hour block rule, interview prep) and `data-format.md` are read only while it builds and saves a plan. Notes are read at check-in and appended after I approve a plan."

---

## 4. Decides vs. enforces + hook test (~1 min)

> "Some things Claude **decides**, and some things Claude Code **enforces**."

> "**Claude decides:** how to rank my tasks, where the blocks go, what to suggest for free time, what goes in Heads up. Those are instructions in `AGENTS.md` and my rules. It follows them, but they're guidance."

**Type:** `move my Web Development class on Friday to 6 PM`

> "**Claude Code enforces:** my data is read-only. I asked it to edit my calendar, and the `PreToolUse` hook blocked the edit before it happened. Instead it tells me what to change myself."

(If it tries a workaround like `sed` and gets blocked again, point that out: "Even the shell route is blocked.")

> "The hook is a Python script that runs before every Edit, Write and Bash call. It checks the real file path, so path tricks don't work. It also protects itself and `settings.json`, so Claude can't turn off its own guardrail. If the hook ever errors, it blocks rather than allows. An instruction can be ignored. A hook can't."

---

## 5. Wrap-up (~15 s)

> "So that's my harness: a short context file, rules it reads only when needed, a skill it picks up from how I talk, memory that carries over day to day, and a hook that makes 'read, plan, suggest, but I make the changes' an actual rule. Thanks!"

---

### Backup lines if something goes off
- **It plans before asking:** "The skill tells it to ask one or two questions first. Here it had nothing to ask because nothing clashed."
- **The page doesn't update:** it checks `plans/today.json` every 2 seconds. Refresh, and check `./serve.sh` is running.
- **Running long?** Skip the `/context` view and just say the "What loads when" lines.
