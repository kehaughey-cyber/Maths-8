# Correction: the "Hubble radius" used in this session was the wrong number (2026-10-31)

**What was wrong.** Several files this session used R = 4.4×10²⁶ m and called it "Hubble radius c/H₀ (recalled)". 4.4×10²⁶ m is the comoving radius of the observable universe (about 46.5 Gly). c/H₀ with H₀ = 67.4 km/s/Mpc (the value this repo's own `explore/positronium_map.py` uses) is 1.372497×10²⁶ m (14.507 Gly). The two differ by a factor 3.2058, which is 2.42 tower steps.

**Replay:** `py -3 -I -X utf8 -u explore/hubble_radius_correction.py > explore/hubble_radius_correction.out` (raw output there).
sha256: *hubble_radius_correction.py 0964147b9321500d41f62b1d289920d21e81c04f831ef3e550b09e639339acb8; *hubble_radius_correction.out 8d451b9a604160f928d40e30b030539d3be175a919e47cf1c6f3c4f9887d38b4.

## Corrected values (edge anchor, ℓP = 1.616255×10⁻³⁵ m)
| quantity | wrong (4.4e26 m) | c/H₀ at H₀ = 67.4 | at 70 | at 73 |
|---|---|---|---|---|
| tower order k = log_φ(R/ℓP) | 293.9645 | 291.5436 | 291.4649 | 291.3777 |
| offset from nearest integer | −0.0355 | −0.4564 | +0.4649 | +0.3777 |
| (R/ℓP)² | 7.4111×10¹²² | 7.2111×10¹²¹ | 6.6854×10¹²¹ | 6.1472×10¹²¹ |
| edge/c at that order (s) | 1.468×10¹⁸ | 4.5782×10¹⁷ | 4.4081×10¹⁷ | 4.2270×10¹⁷ |

## What this changes
- **The Hubble radius is not near a tower integer.** `maps/lattice_physical_map.md` said the Hubble radius sits at k = 293.96, near an integer, and was only uncertain by about 8%. With c/H₀ it sits at k = 291.54, about half a step from an integer, and H₀ = 67.4 to 73 alone moves k by 0.166. The statement in "The ends" of that map is retracted.
- **The area count was 10× too large.** `explore/anchor_investigation.out` gave (R/ℓP)² = 7.4×10¹²². With c/H₀ it is 7.2×10¹²¹ (H₀ = 67.4). Neither was claimed as a match, but the earlier figure should not be quoted.
- **The orders from the Planck copy to the Hubble radius** are 291.54, not 293.96.
- **One tick at the c/H₀ order is the Hubble time** (edge/c = 1/H₀ = 4.5782×10¹⁷ s). The age used in the lab (13.8 Gyr = 4.3549×10¹⁷ s) is 0.951 of that tick, which replaces the "0.29 of a tick" stated in chat for the k = 294 order.
- **The 4.4×10²⁶ m value is kept as its own rung** in the lab (observable-universe radius, comoving, recalled). The jump button "Hubble" now goes to c/H₀.

## Not changed by this (checked)
The epoch table (orders above about k = 284 have not completed one 30-tick cycle in 13.8 Gyr, above about k = 247 in 200 years) depends on the age and not on the Hubble radius. The ratio search `ratios_128_137` was re-run inline (not saved as a file) with c/H₀ = 1.372497×10²⁶ m: the pairwise size ratios in 128–137.5 are still only Bohr/electron Compton = 137.035999 (the α identity). The tower-step differences in that window change: the previous run found none, and the corrected run finds one pair, the radius of 1 g of diamond to c/H₀ at 136.4998 steps (k = 155.0438 and 291.5436). That is 0.0002 from 136.5, but the gram's radius depends on the crystal phase (±0.06) and c/H₀ moves by 0.166 over H₀ = 67.4 to 73, so it is a coincidence of two uncertain positions among 66 pairs, noted and not claimed.

## Files that still contain the wrong value (left as they are, listed here)
`explore/lattice_physical_map.py/.out` and `maps/lattice_physical_map.md`; `explore/anchor_investigation.py/.out`; `explore/ratios_128_137.py/.out`; `explore/energy_by_mass.py` with `maps/energy_by_mass.csv/.xlsx` (the gravity-Bohr-size / Hubble-radius column is high by 3.2058); `explore/build_lab.py` before this fix. Earlier maps (`positronium_map`, `lithium`) used c/H₀ = 1.37×10²⁶ m (60.93 decades) and are not affected.

I was wrong about this in the chat reply that said "8% gets us in the decade": the 8% was applied to the wrong radius.
