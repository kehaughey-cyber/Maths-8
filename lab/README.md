# SPINE LAB

A visual reference and small simulator built from the spine (`floor/M5_SPINE_10-9-26.md`, with the M6 D2 transit), inspired by `lattice(1).html`. Open `lab/spine_lab.html` in a browser (single file, no network).

Rebuild after changing the data or the source: `py -3 -I -X utf8 -u explore/build_lab.py` (reads `lab/spine_lab_src.html`, `maps/size_vs_energy_filled.csv`, `floor/M5_SPINE_10-9-26.md`; writes `lab/spine_lab.html`).

## What it shows
- **Zoom over 64 decades** (view radius 10⁻³⁶ m to 10²⁸ m; mouse wheel, shift-wheel ×5, `+`/`−`, the ruler along the bottom, or the jump buttons). Concentric rings mark decades, powers of 12 above ℓP, or the φ tower; the ruler shows every φ-tower step and every rung.
- **Rung circles at true relative size** (concentric): the 18 rows of `maps/size_vs_energy_filled.csv` (leptons, nucleon, ¹²C, ionization stages, CO, C₂, diamond bond and lattice, the gram) plus the Planck length, the proton Compton length and the Hubble radius. Click a ring or a name in the Rungs tab for its energy columns with provenance (M measured, C computed, F formal estimate).
- **The lattice** (120 vertices, 720 edges; w-shells; four 30-clocks of the tick q → g₅·q·g₆ with the fold at t = 15; the native continuation T on 1440 directed edges, 144 ten-cycles, T⁵ antipode, T¹⁰ identity), drawn as the nested copies of the φ tower nearest the view (S³ radius φ^(k+1)·ℓP). The page verifies the counts on load (status bar).
- **Physical readouts** for the lattice copy in view: edge = ℓP φ^k, tick = edge/c, the 30-tick cycle and the fold in seconds; inject (as in the original lattice(1).html) sends a breadth-first wave from the picked vertex over the five copies drawn around the view: one hop is an edge inside a copy or, with radial hops on, the same vertex one copy up or down. It reports hops, nodes lit and the copies reached; the time readout takes one hop as one tick of the starting copy (the radial-hop cost is the original's choice, not derived).
- **Spine tab:** the M5 nodes as written (grade included); gold rows are what the lab draws or computes. Click a gold row to jump to its view.

## What it assumes (declared)
- The Planck anchor (edge at tower copy k = 0 is ℓP, tick = edge/c, wave speed c by construction) is the spine's nodes 17/18/33, a declared non-discriminating bridge. The φ step per copy is the original visualizer's choice, not a derived scale (the spine keeps several meanings of scale apart, D6).
- Rung circles are sizes from the maps; their positions relative to the lattice copies carry no claim (see `maps/lattice_physical_map.md`: no common offset in the tower).
- The Hubble radius rung is c/H₀ with H₀ = 67.4 km/s/Mpc (recalled); the observable-universe radius (46.5 Gly, recalled) is its own rung. An earlier build used 4.4e26 m and called it the Hubble radius; see `maps/hubble_radius_correction.md`. Formal (F) energy cells are non-relativistic estimates, not data.

## Amplitude tab (amplitudes only, no link phases yet)
- **Histories on one copy:** real amplitude on the 1440 directed edges. Each tick is (1−m)·T (coherent, history kept) + m·K (random exit to the 12 neighbours of the endpoint, marginal P = A/12, history erased; spine D4). Orange halos on the lattice show where the amplitude sits. With m = 1 the first moment of the vertex marginal shrinks by exactly φ/2 per tick (the page shows the measured ratio). With m = 0 amplitude returns after ten ticks.
- **Reinjection (D5):** optional, size selectable, at every 30-tick return. The measured slowest-mode amplitude over the injected size is 1/(1−(φ/2)^30) = 1.0017357, as D5 states, for injection into that mode.
- **Sag:** shown as ε Σ(φ/2)^(30 i)/(864φ²) after n returns, ε = 2π − 5 arccos(1/3), against ς = 5.6858×10⁻⁵ rad; it is computed from the survival cascade, not from the wave amplitude.
- **Injection between orders:** a chain of tower copies from k = −10 to 300. A hop inside a copy costs one tick of that copy (speed c). A radial hop costs the tick of the larger copy: a declared, c-preserving choice (D6 does not fix the cost of causal lag). Planck-to-atom then arrives in 2.62 atom-order ticks; an injection at the c/H₀ order reaches any smaller order only after about a Hubble time. If a radial hop cost the starting copy's tick, Planck-to-atom would be faster than light by about 10²². Elapsed-time presets (1 s, 1 yr, 200 yr, 13.8 Gyr, or seconds) show the orders reached and the slowest-mode contrast left at the observer.

## Not yet in the lab (to add)
- The E-series: charged histories and the joint action (link phases on the amplitude layer; the amplitude layer above is the first step, with real amplitudes only).
- The 12-cone orbifold sphere.
- E8.
- The cosmological scale N.
- The periodic-table work (`maps/known_ratios_elements.md`, `maps/size_vs_energy_filled.csv` for other elements).

## Not verified
- Not run on a phone or in any browser other than the Claude desktop built-in browser pane; touch input (pinch zoom, tap to pick a vertex) has not been tried and the layout has not been checked at phone width.
- The Spine tab parses `floor/M5_SPINE_10-9-26.md` by its table rows and picked up 49 nodes (builder output: `rungs 21 spine nodes 49`). That count has not been checked against the M5 table by hand, so a node could be missing, merged or split by the parser.
