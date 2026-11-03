"""
Combines the computed corrections to the heavy-ion 1s hyperfine splittings and shows what is left of the measured r/A (new file, 2026-11-03; nothing fitted).
Reads the raw outputs of nuclear_size_hfs.py (finite charge delta_BR and the two Bohr-Weisskopf bounds), bw_single_particle.py (single-particle delta_BW) and vp_hfs.py (vacuum polarization),
and multiplies:  predicted r/A = (1 + BR)(1 + BW)(1 + VP);  left = (measured r/A) / predicted - 1.  Left is what is not computed: the bound-state self-energy beyond the free-electron anomalous moment already in E_nr,
higher-order terms, the nuclear-model uncertainty, deformation (Ho, Re), and the secondary measured values.
Measured r/A (hydrogenlike_series.out): Ho 0.93344, Re 0.90557, Pb 0.85539, Bi 0.87360; relative uncertainties of the splittings 2.6e-4, 4.4e-4, 2.0e-4, 1.6e-4.
Usage: py -3 -I -X utf8 -u explore/combine_hfs.py > explore/combine_hfs.out
"""
import os, re
here = os.path.dirname(os.path.abspath(__file__))
rd = lambda n: open(os.path.join(here, n), encoding='utf-8').read()
meas = {'165Ho66+': (0.93344, 2.6e-4), '187Re74+': (0.90557, 4.4e-4), '207Pb81+': (0.85539, 2.0e-4), '209Bi82+': (0.87360, 1.6e-4)}
BR = {}; BWu = {}; BWs = {}
for l in rd('nuclear_size_hfs.out').splitlines():
    t = l.split()
    if len(t) >= 9 and t[0] in meas and t[1].isdigit(): BR[t[0]] = float(t[4]); BWu[t[0]] = float(t[5]); BWs[t[0]] = float(t[6])
VP = {}
for l in rd('vp_hfs.out').splitlines():
    t = l.split()
    if len(t) >= 6 and t[0] in meas and t[1].isdigit(): VP[t[0]] = float(t[4])
SP = {}; cur = None
for l in rd('bw_single_particle.out').splitlines():
    m = re.match(r'(187Re74\+|207Pb81\+|209Bi82\+):', l)
    if m: cur = m.group(1); SP[cur] = {}; continue
    if cur and l.strip().startswith('r0=1.25 a=0.65'):
        d = re.findall(r'delta_BW = ([+-]\d\.\d+)', l); SP[cur] = dict(schmidt_free=float(d[0]), schmidt_q06=float(d[1]), match_mu=float(d[2]))
print('computed pieces (relative corrections to the point-dipole, point-nucleus Dirac value):')
print(f'{"ion":9s} {"BR":>9s} {"BW unif":>9s} {"BW shell":>9s} {"BW sp: Schmidt":>15s} {"g_s x 0.6":>10s} {"match mu":>9s} {"VP":>9s}   measured r/A')
for n in meas:
    sp = SP.get(n, {}); print(f'{n:9s} {BR[n]:+9.5f} {BWu[n]:+9.5f} {BWs[n]:+9.5f} {sp.get("schmidt_free", float("nan")):+15.5f} {sp.get("schmidt_q06", float("nan")):+10.5f} {sp.get("match_mu", float("nan")):+9.5f} {VP[n]:+9.5f}   {meas[n][0]}')
print('\nleft = measured / [(1 + BR)(1 + BW)(1 + VP)] - 1 (measured uncertainty in brackets)')
print(f'{"ion":9s} {"BW model":28s} {"predicted r/A":>14s} {"left":>10s}')
for n, (m, u) in meas.items():
    rows = [('uniform sphere (old bound)', BWu[n]), ('thin shell (old bound)', BWs[n])]
    if n in SP: rows += [('single particle, Schmidt g_s', SP[n]['schmidt_free']), ('single particle, g_s x 0.6', SP[n]['schmidt_q06']), ('single particle, spin scaled to mu', SP[n]['match_mu'])]
    for lab, bw in rows:
        pred = (1+BR[n])*(1+bw)*(1+VP[n]); print(f'{n:9s} {lab:28s} {pred:14.6f} {m/pred-1:+10.5f}  (+-{u:.1e})')
    pred0 = (1+BR[n])*(1+BWu[n]); print(f'{n:9s} {"(for comparison: BR + uniform BW, no VP)":28s} {pred0:14.6f} {m/pred0-1:+10.5f}')
