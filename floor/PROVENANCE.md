# Floor provenance — inherited, immutable

These files are the load-bearing map and deepest anchors of the Maths 5/6 floor, copied in byte-for-byte so Maths 8 is self-contained on the floor's core. They are **immutable**: cite them, never edit them. The one exception is the 2026-11-02 edit recorded under "Edits at the human's direction" below. The complete Maths 5/6/7 trees remain at their original locations on this machine for deep reference; this folder carries only the spine-level map plus the first containers and the field equations.

Imported 2026-10-25. Source root: `C:\Users\Dad\OneDrive\Desktop\Optimus Prime`.

| file (in `floor/`) | source path | sha256 |
|---|---|---|
| `M5_SPINE_10-9-26.md` | `Maths 5/SPINE10-9-26.md.txt` | `a8b148ecab2fef8b112e51953dc164e1a0349d662ea0c78f72837a5a9dec3d18` |
| `M6_SPINE_2026-10-19.md` | `Maths 6/SPINE.md` | `3ca3e918fe5f994df416c1caa1718afb4b483acddf2f601d67a3057796b967ca` |
| `field_equations_v3.txt` | `Maths 6/explore/law_sources/field_equations.txt` | `383b8ce9cc07911253249619b9ccfa3b94f775a69feeadd88970370a45046883` |
| `container_00_distinction.md` | `Maths 5/containers/00-distinction/statement.md` | `1c92b2e7a3b14f9866894064463d2993c8db0a497c2c0ebc53b9f0a2c14bff33` |
| `container_01_recursive_registration.md` | `Maths 5/containers/01-recursive-registration/statement.md` | `7ea882e6a8f6c0915650f3ae51dd54122f50ff8d918060198f7d52e6bd7919f4` |
| `container_02_registration_event.md` | `Maths 5/containers/02-registration-event/statement.md` | `3555b1f766badf2f21c2b6c42540e5fffa3b89c34f4235697c8d7efae1b2872d` |

Cross-check: `container_01` sha256 `7ea882e6…` equals the hash recorded in the Maths 7 provenance (`provenance/setup_verification.json`, `claim_ledger_anchors`), confirming the inherited copy is the same byte stream.

Grades inside these files are the source's own (DERIVED / POSTULATE / REDUCTION / HELD / OPEN).

## Edits at the human's direction (2026-11-02)
Three files were edited at the human's direction; the table above carries their hashes after the edit. The as-imported files are kept unchanged in `floor/as_imported/` and still hash to the values in the Imported column.

| file | as-imported sha256 (also in `floor/as_imported/`) | edit |
|---|---|---|
| `M6_SPINE_2026-10-19.md` | `4b7385ce14d4ed87eb2f295fb4d3924eb1cd5a28b67d7a98be323560438e87e7` | Removed from "Evidence, grades and notation" the grade-notation sentence and "A source grade is not a new certification of its physical interpretation." The sentence that earlier warnings are scoped and prohibit nothing is kept. Second edit: removed "do not reset to 65's old debt", "Do not reset to old blocked status." and "Counts do not substitute for coupling." |
| `field_equations_v3.txt` | `8f879260c05764054782d8834573d6de4b413e6db63f69c8f55bcb7ad62cdf7d` | Removed §3 (the contamination audit, lines 0288-0345); the sentence in 0003 pointing to it and saying measured masses appear only as checks; the clause in F14 saying Gell-Mann-Nishijima is "NOT used". Change-log line 0360 added. Second edit: removed "never a derivation" in F9 (0244) and "Masses enter only as checks." in F17 (0276); change-log line 0361 added. |
| `M5_SPINE_10-9-26.md` | `8e4cb51fa3c16953312c2d8074cb16e0a9aa2b6fe26b708096ee78c9f10c2320` | Removed the pointers to PROTOCOL.md, FRONTIER.md and CONTACT.md, the "quarantined (no DERIVED rests on it)" clause in the POSTULATE grade definition, and "under the five gates". Other grade definitions kept. |
