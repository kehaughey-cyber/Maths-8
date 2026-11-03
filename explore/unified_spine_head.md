# SPINE with proofs, Maths 8: from the 00 floor to the current frontier (2026-11-03)

Authored by Claude (Sonnet 5.5). Not independently reviewed. This is one file: the spine of `SPINE_M8_2026-11-03.md` with, under each part, the equations and proofs of that part's claims (copied from `SPINE_M8_PROOFS_2026-11-03.md`; assembled by `explore/build_unified_spine.py` from that file, the spine, and three small hand-written pieces in `explore/unified_spine_*.md`, so the files cannot drift apart silently). Nothing here replaces the files it cites. Where a claim is the floor's it keeps the floor's grade; where it is Maths 8's it is graded by what was actually run. Older words ("archic", "archon") are written "registration" (`notes/terminology.md`); floor files keep the old words.

## How a claim is carried here, and what "proved" means
Each claim sits next to one of four things, and the label says which:
- **LEAN**: the floor's formal statements for nodes 00 to 67, as Lean 4 proofs imported from Maths 5 and compiled in this repository (71 of 71 modules, no `sorry`, no axiom declarations). The kernel accepts each theorem *as stated*; whether the stated theorem is the whole of the node's prose claim is not assessed.
- **PROVED / CHECKED**: a derivation written out in the entry, and its identities verified independently by a script (`explore/spine_proofs_check.py`, 71 PASS; `explore/spine_route56_check.py`, PASS).
- **COMPUTED**: a number from a named script with a committed `.out` and a sha256; reproduces by `explore/reproduce.py`. Computed is a result, not a proof.
- **NOT CARRIED**: the proof is not in this repository; the entry says where the evidence lives. These are listed in one place at the end (Part IX).

**To verify everything that can be verified from this repository** (from the repository root; NumPy, SymPy, mpmath only, Lean 4.33.0-rc1 for the first line):
```bash
py -3 -I -X utf8 -u explore/lean_M5_check.py --pkgs "<Maths 5>/lean/.lake/packages" > explore/lean_M5_check.out
py -3 -I -X utf8 -u explore/spine_proofs_check.py > explore/spine_proofs_check.out
py -3 -I -X utf8 -u explore/spine_route56_check.py > explore/spine_route56_check.out
py -3 -I -X utf8 -u explore/reproduce.py
```
The last line re-runs every explore script that has a committed `.out`, against a fresh export of HEAD.

---
