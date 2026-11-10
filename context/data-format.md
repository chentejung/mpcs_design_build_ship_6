# Data formats

## data/calendar.json (read-only)
`{ timezone, events: [ { id, title, start, end, location, type, recurring? } ] }`
- `start`/`end` are local ISO times like `2026-11-10T17:30`.
- `type`: class | interview | office-hours | personal | ...
- Recurring events appear only for their listed dates. Infer later weeks from `recurring` if you need them.

## data/tasks.json (read-only)
`{ tasks: [ { id, title, course, due, estimate_hours, priority, status, notes? } ] }`
- `due` may be null (no deadline). `status`: not-started | in-progress | done.

## plans/YYYY-MM-DD.json (written only after I agree)
Also copy it to `plans/today.json`, which the UI reads.
```json
{
  "date": "2026-11-10",
  "saved_at": "2026-11-10T09:12",
  "blocks": [
    { "start": "12:00", "end": "15:00", "title": "DBS Assignment 6", "kind": "focus", "task_id": "t1",
      "steps": ["Finish hook + test", "Record demo video", "Post in #general + submit link"] }
  ],
  "due_soon": [ { "title": "AFT assignment", "due": "2026-11-11T17:29" } ],
  "carried_over": [ "Email TA" ],
  "warnings": [ "Dinner with Sam clashes with Web Dev (Fri)" ]
}
```
`kind`: fixed | focus | task | meal | swim | prep  (`task` = a small task I agreed to add; there are no break or free blocks)
`steps` (optional): the bulleted sub-steps inside one slot. Use it instead of splitting a task into back-to-back blocks. Shown as a bulleted list under the slot title.
Page layout: **Heads up** box (`warnings` + `carried_over`) → **Due soon** (`due_soon`, next 2 days shown, toggle for the rest) → **Schedule** (`blocks`).

## notes/notes.md
Append a dated entry after each saved plan: what was planned, what carried over, anything I told you that should change future plans.
