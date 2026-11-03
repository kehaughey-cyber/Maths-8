# Environment and how to reproduce (2026-11-02)

Written by Claude (Sonnet 5.5). The numbers in the results notes were produced on the machine below; the version list is what the reproduce check ran on, recorded so a later reader knows what "same output" was tested against.

## Software
- Windows 11 Pro 10.0.26200, Python 3.14.6 (CPython), NumPy 2.5.3, SymPy 1.14.0, mpmath 1.3.0. No SciPy (the scripts do not use it). Everything else is the standard library.
- Run with `py -3 -I -X utf8 -u <script>` from the repository root, as each results note says (`-I` isolates from user site-packages and the current directory; `-X utf8` fixes the output encoding).
- Scripts write only to stdout; the `.out` file beside each script is that stdout redirected (`> explore/<name>.out`).

## Check it yourself
```bash
py -3 -I -X utf8 -u explore/reproduce.py --workers 4 > explore/reproduce_run.out
```
This exports the committed tree (`git archive HEAD`, so a fresh clone's content) to a scratch directory, runs every `explore/<name>.py` that has a committed `<name>.out`, and compares the new output byte for byte with the committed file and with the sha256 recorded in the notes. It never touches repository files except to write `explore/REPRODUCE_REPORT_<date>.md`. It also checks the exec/import chain (below). Use `--only <substring>` for a subset and `--timeout` for the slow ones (the Dirac solver scripts take minutes).

## What reproducibility means here, and its limits
- Same Python, NumPy, SymPy, mpmath: expect identical bytes. Different versions or a different CPU/BLAS: floating-point output may differ in the last digits; a DIFFERS status in the report shows the first differing line so you can tell last-digit noise from a real change.
- The results of the E-series and hyperfine notes are deterministic (fixed seeds, e.g. `default_rng(20261103)`); nothing depends on the clock or the network.
- **Inputs that are not reproducible by code:** the measured values in `explore/data/*.txt` (CODATA 2022 and the hyperfine frequencies, heavy-ion Compton wavelengths and charge radii) were collected from search summaries and are secondary. Re-running the code reproduces the computation, not the sourcing. Primary-paper citations are an open thread in `HANDOFF_2026-11-02_hyperfine_arc.md`.
- No independent review has been done.

## The source-splitting chain (a known fragility, kept deliberately)
Several scripts build on earlier ones by executing the earlier file's text up to a marker string, for example
`exec(open('e_series_one_copy.py').read().split('# ---------------- structure checks')[0])`, or by loading a file with `importlib`. The chain as it stands:

- `e_series_one_copy.py` loads `route56_subdiv.py`
- `e_series_two_copy.py` and `e_series_readouts.py` exec `e_series_one_copy.py` up to the marker `# ---------------- structure checks`
- `e_series_ablation.py`, `e_series_response.py` exec `e_series_two_copy.py` (up to `rng = np.random.default_rng(20261103)`) and `e_series_readouts.py` (up to `print('== check: ring states`)
- `e_series_resonance.py`, `e_series_zeeman.py`, `e_series_chain.py` exec `e_series_readouts.py` (same marker)
- `e_series_chain_origin.py`, `e_series_chain_spectrum.py`, `dirac_series_vs_chain_weights.py`, `size_exponent_listening.py` exec `e_series_chain.py` up to `phi = (1+5**.5)/2`
- `nuclear_size_hfs_scan.py` imports `nuclear_size_hfs.py`

These files were **not rewritten into importable modules**, because the recorded sha256 of each script is part of the evidence (CLAUDE.md: never overwrite prior evidence). Instead `reproduce.py` guards the chain: for every dependency it checks that the marker string is still present (`MARKER_MISSING` otherwise) and that the dependency's current sha256 is one recorded in the notes (`DEP_DRIFT` otherwise), so an edit to an upstream file cannot silently change a downstream result. **Rule for edits:** never edit a file listed above in place; copy it to a new name (as the `_run1_` convention does) and record the new hash. If a clean rewrite as modules is wanted later, do it as new files with their own `.out` and a note showing the outputs match.
