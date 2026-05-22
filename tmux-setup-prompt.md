---
date: 2026-05-18
updated: 2026-05-22
type: reference
project: internal_seminar
tags:
  - claude-code
  - tmux
  - seminar
  - hands-on
  - prompt
---

# tmux Setup Prompt (Seminar Hands-on)

## Purpose

A copy-pasteable prompt for seminar attendees to set up a tmux Alt-key environment in one shot from inside the Claude Code TUI. No sudo required. Alt+digit reserved for Claude Code TUI. Prefix-less shortcuts. OS detection auto-branches between macOS / Ubuntu / WSL2. Short enough to fit on a single slide.

## One-line slide tagline

`no sudo · no Alt+digit · home directory only`

## Hands-on flow (presenter cues)

1. Run `claude` in a terminal.
2. Paste the prompt block below in one chunk, hit Enter.
3. Review the dry-run diff, approve with `y`.
4. Demo `Alt+D`, `Alt+<arrow>`, `Alt+Z` for one or two minutes.

## Full prompt

```
Set up a tmux shortcut environment on my machine.

Constraints
- No sudo. No writes to system directories.
- Scope of changes is limited to ~/.tmux.conf and ~/.tmux/ only.

Pre-checks
- First check which shortcuts the Claude Code TUI reserves
  (claude --help, the `?` key, official docs).
- Exclude any conflicting keys from the tmux bindings and report them.
- Always exclude Alt+1 through Alt+0.

Requirements
- Keep the prefix as Ctrl+B, but all daily-use shortcuts must be
  prefix-less (`bind -n M-x`).
- Required bindings:
  split horizontal (Alt+D), split vertical (Alt+Shift+D),
  pane navigation (Alt+<arrow>), pane resize (Alt+Shift+<arrow>),
  zoom toggle (Alt+Z), close pane (Alt+W),
  new window (Alt+T), previous/next window (Alt+[ / Alt+]),
  reload config (Alt+R).
- Window-number jump uses the default tmux prefix flow (Ctrl+B -> digit).
  Do NOT bind Alt+digit.
- mouse on, history 50000 lines, 256-color + truecolor.
- Clipboard auto-branched per OS
  (macOS pbcopy / Linux xclip / WSL clip.exe).
- Window prev/next bindings must quote the bracket characters in the
  conf because brackets are special to the tmux parser:
    bind -n "M-[" previous-window
    bind -n "M-]" next-window
- If docs are unreachable during the TUI-conflict check, print the
  known conflicts (Alt+digit, Esc sequences, etc.), ask the audience
  if anything else conflicts, then continue.

Sequence
1. Detect OS (macOS / Ubuntu / WSL2).
2. Check installation with `command -v tmux`.
   If missing, prefer a no-sudo install path and pause:
     macOS:  brew install tmux
     Linux:  mamba install -c conda-forge tmux  (or conda)
     Last resort: sudo apt install -y tmux
   The user installs it themselves. Resume when notified.
3. If ~/.tmux.conf exists, back it up as ~/.tmux.conf.backup.<date>.
4. Write ~/.tmux.conf per the requirements above
   (excluding Alt+digit and any TUI-conflict keys).
5. If tmux is already running, apply immediately with
   `tmux source-file ~/.tmux.conf`.
6. On macOS, ask which terminal app is in use and explain how to
   enable Option=Meta.
7. Print a table of the five shortcuts to try first.

Show the dry-run diff and ask for approval before applying.
```

## Design decisions

| Decision | Reason |
|---|---|
| No sudo | Safe for audience environments (shared servers, laptops without admin rights). |
| No Alt+digit bindings | Conflicts with Claude Code TUI shortcuts (subagent picker, etc.). Window-number jump falls back to tmux default `Ctrl+B -> digit`. |
| Prefix-less (`bind -n M-x`) | Matches modern terminal UX. One-step input. Ctrl+B prefix is kept for compatibility. |
| OS auto-branch | macOS (brew + pbcopy), Ubuntu (mamba + xclip), WSL2 (clip.exe). No need to know the audience's setup in advance. |
| Dry-run approval gate | Diff is shown before overwriting ~/.tmux.conf. Existing config is preserved as `.backup.<date>`. |
| Short prompt (one screen) | Fits inside a single slide box. A self-contained long-form version was tried and the audience couldn't read it in one glance. |

## Five shortcuts to try first (demo order)

| Action | Key |
|---|---|
| Split horizontal | Alt+D |
| Pane navigation | Alt+<arrow> |
| Zoom toggle | Alt+Z |
| New window | Alt+T |
| Reload config | Alt+R |
