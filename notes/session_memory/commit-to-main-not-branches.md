---
name: commit-to-main-not-branches
description: "In the Maths 8 repo, commit directly to main — no claude/* feature branches or PRs unless asked"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 3d3f0acb-af57-4a14-b997-81e884ef82a9
  modified: 2026-10-25T20:56:03.838Z
---

The human wants commits made **directly on `main`** in the Maths 8 repo — not on `claude/<thread>` feature branches. Verbatim (2026-10-25): "there shouldn't be a branch at this point only the main." This **overrides** CLAUDE.md's "Branch `claude/<thread>` for your own work."

**Why:** it's a solo research repo; the branch/PR dance is unwanted overhead, and the human tracks the work on main.

**How to apply:** commit straight to main; do not create feature branches or open PRs unless the human explicitly asks. Pushes to the remote remain the human's call (CLAUDE.md: "the human decides commits, pushes and assignments") — commit locally, offer to push, don't push unprompted.
