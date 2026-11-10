#!/usr/bin/env python3
"""PreToolUse hook: Claude may READ data/ but never change it.

Also protects the harness's own guardrails (this hook and .claude/settings.json),
so Claude can't switch the hook off. Exit code 2 = block, and stderr goes back to Claude.
"""
import json
import os
import re
import sys

PROJECT = os.path.realpath(os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd())
PROTECTED = [
    os.path.join(PROJECT, "data"),
    os.path.join(PROJECT, ".claude", "settings.json"),
    os.path.join(PROJECT, ".claude", "hooks"),
]
PROTECTED_NAMES = r"(data/|data\b|calendar\.json|tasks\.json|settings\.json|protect-data\.py|\.claude/hooks)"

# Shell patterns that write, move, delete, or change permissions.
WRITE_OPS = re.compile(
    r"(>>?|\btee\b|\bsed\s+(-\w*\s+)*-i|\bperl\s+-\w*i|\brm\b|\bmv\b|\bcp\b|\brsync\b|\btruncate\b|"
    r"\btouch\b|\bchmod\b|\bchown\b|\bln\b|\bdd\b|\binstall\b|\bunlink\b|\bpatch\b|\bgit\s+(checkout|restore|reset|stash|clean|apply)\b|"
    r"open\([^)]*['\"][wax+]|\.write|json\.dump|writeFile|appendFile|\bjq\b.*-i|\bsponge\b)"
)


def is_protected(path):
    if not path:
        return False
    full = os.path.realpath(path if os.path.isabs(path) else os.path.join(PROJECT, path))
    return any(full == p or full.startswith(p + os.sep) for p in PROTECTED)


def block(reason):
    print(
        f"BLOCKED by protect-data hook: {reason}\n"
        "data/ is read-only for the harness. Tell the user exactly what to change "
        "(file, event/task id, new value) so they can make the edit themselves.",
        file=sys.stderr,
    )
    sys.exit(2)


def main():
    event = json.load(sys.stdin)
    tool = event.get("tool_name", "")
    args = event.get("tool_input", {}) or {}

    if tool in ("Edit", "Write", "MultiEdit", "NotebookEdit"):
        path = args.get("file_path") or args.get("notebook_path")
        if is_protected(path):
            block(f"{tool} on {path}")

    elif tool == "Bash":
        cmd = args.get("command", "")
        # Drop redirects that only send output to /dev/null or merge streams (2>&1).
        scrubbed = re.sub(r"\d?>>?\s*(/dev/null|&\d)", "", cmd)
        if re.search(PROTECTED_NAMES, scrubbed) and WRITE_OPS.search(scrubbed):
            block(f"shell command that may modify protected files: {cmd!r}")

    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # fail closed: if the hook can't decide, it blocks
        print(f"BLOCKED by protect-data hook: could not check this call ({e}).", file=sys.stderr)
        sys.exit(2)
