# SPINE LAB

A visual reference and small simulator built from the spine (`floor/M5_SPINE_10-9-26.md`, with the M6 D2 transit), inspired by `lattice(1).html`. Open `lab/spine_lab.html` in a browser (single file, no network).

Rebuild after changing the data or the source: `py -3 -I -X utf8 -u explore/build_lab.py` (reads `lab/spine_lab_src.html`, `maps/size_vs_energy_filled.csv`, `floor/M5_SPINE_10-9-26.md`; writes `lab/spine_lab.html`).

## What it shows
- **Zoom over 64 decades** (view radius 10⁻³⁶ m to 10²⁸ m; mouse wheel, shift-wheel ×5, `+`/`−`, the ruler along the bottom, or the jump buttons). Concentric rings mark decades, powers of 12 above ℓP, or the φ tower; the ruler shows every φ-tower step and every rung.
- **Rung circles at true relative size** (concentric): the 18 rows of `maps/size_vs_energy_filled.csv` (leptons, nucleon, ¹²C, ionization stages, CO, C₂, diamond bond and lattice, the gram) plus the Planck length, the proton Compton length and the Hubble radius. Click a ring or a name in the Rungs tab for its energy columns with provenance (M measured, C computed, F formal estimate).
- **The lattice** (120 vertices, 720 edges; w-shells; four 30-clocks of the tick q → g₅·q·g₆ with the fold at t = 15; the native continuation T on 1440 directed edges, 144 ten-cycles, T⁵ antipode, T¹⁰ identity), drawn as the nested copies of the φ tower nearest the view (S³ radius φ^(k+1)·ℓP). The page verifies the counts on load (status bar).
- **Physical readouts** for the lattice copy in view: edge = ℓP φ^k, tick = edge/c, the 30-tick cycle and the fold in seconds; a wave injected at a vertex reports its front in seconds through that tick.
- **Spine tab:** the M5 nodes as written (grade included); gold rows are what the lab draws or computes. Click a gold row to jump to its view.

## What it assumes (declared)
- The Planck anchor (edge at tower copy k = 0 is ℓP, tick = edge/c, wave speed c by construction) is the spine's nodes 17/18/33, a declared non-discriminating bridge. The φ step per copy is the original visualizer's choice, not a derived scale (the spine keeps several meanings of scale apart, D6).
- Rung circles are sizes from the maps; their positions relative to the lattice copies carry no claim (see `maps/lattice_physical_map.md`: no common offset in the tower).
- The Hubble radius is a recalled order of magnitude; formal (F) energy cells are non-relativistic estimates, not data.

## Not yet in the lab
The E-series (charged histories, the joint action), the 12-cone orbifold sphere, E8, the cosmological scale N, and the periodic-table work are not drawn.
