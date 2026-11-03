# Provenance: the Maths 5 Lean proofs and derivation scripts for the floor nodes (copied 2026-11-03)

Imported at the human's direction (chat, 2026-11-03: "get what you need for floor nodes 03–67 … do not import rules, grading or walls to this project"). Source root: `C:\Users\Dad\OneDrive\Desktop\Optimus Prime\Maths 5`. The files are byte copies; `MANIFEST.sha256` lists the sha256 of every copied file, and each was compared with its source at copy time. Like the rest of `floor/`, they are inherited and not edited here; cite them by path and hash.

## What was copied
- `lean/` : `Container00` to `Container67` Lean sources (`*.lean`), plus `lakefile.lean`, `lean-toolchain` (`leanprover/lean4:v4.33.0-rc1`) and `lake-manifest.json` (the Mathlib pin). These are the machine-checked proofs behind floor nodes 00 to 67.
- `derivations/NN-name/` : `derivation.py` and `derivation.json` of each container 00 to 67 (the computations and their recorded output that the Lean models were built from).

## What was deliberately not copied
`PROTOCOL.md`, `FRONTIER.md`, `CONTACT.md`, `CORRECTIONS.md`, `HANDOFF.md`, `ROADMAP.md`, `INTERFACES.md`, `README.md`, `SPINE*.md`, the per-container `statement.md` files, `verify.py`, the `check/` and `model/` folders, the `.docx` files, `archive/`, and the Lean build products (`.lake`). No rules, protocols, grading scheme, warnings or prohibitions were imported. Any grade words, status tags or warnings that appear inside the copied Lean comments or JSON are the source's own text, carry no authority in Maths 8, and are not repeated in the documents written here. `explore/lean_M5_index.py` omits comments when it builds the declaration index.

## Using them
- Declaration index (signatures only, generated from the sources): `DECLARATION_INDEX.md`.
- Compile every module (read-only use of Maths 5's already-built Mathlib oleans; the toolchain executable is called directly so nothing is downloaded or resolved by elan): `py -3 -I -X utf8 -u explore/lean_M5_check.py --pkgs "<Maths 5>/lean/.lake/packages" > explore/lean_M5_check.out`. Result: `explore/lean_M5_check.out`.
- Rebuild the index: `py -3 -I -X utf8 -u explore/lean_M5_index.py > floor/lean_M5/DECLARATION_INDEX.md`.

## An incident to record
While looking at the Maths 5 folder, a `lean --version` run from inside it made elan start downloading Lean 4.35.0 (the toolchain it resolved there). I stopped the download within about two minutes and removed the partial file (244 MB, `~/.elan/tmp`) and the `.lock` it created; two older temporary files in the same folder (dated 2026-07-28) were not mine and were left. Nothing in Maths 5 was written to. After that, no Lean command was run inside Maths 5; everything runs from this repository with `LEAN_PATH` pointing read-only at the existing builds.
