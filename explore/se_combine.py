"""
Adds the SOURCED all-order self-energy to the computed finite-charge, Bohr-Weisskopf and vacuum-polarization corrections and shows what is left (new file, 2026-11-03; nothing fitted).
The self-energy is NOT computed here: values are from explore/data/qed_hfs_sourced_values.txt (secondary, read from web page text; the papers were not read directly).
Convention: the tabulated self-energy is additive relative to the Fermi energy E_nr:  E_SE = x_SE * E_nr.  With r = E/E_nr measured and A the point-nucleus Dirac factor,
    r/A (predicted) = (1 + BR)(1 + BW)(1 + VP) + x_SE / A ,    left = (r/A measured) / (r/A predicted) - 1.
The tabulated x_SE tends to the free-electron anomalous-moment term alpha/(2 pi) at low Z (inferred; not checked against the PDFs), and this repository's E_nr already contains that term (it uses the measured electron moment),
so two versions are printed: (a) x_SE as tabulated; (b) x_SE - alpha/(2 pi), which removes the possible double count.
Inputs: BR, BW bounds from nuclear_size_hfs.out; single-particle BW from bw_single_particle.out; VP from vp_hfs.out (this repository's computation); A and r/A measured from hydrogenlike_series.out.
Usage: py -3 -I -X utf8 -u explore/se_combine.py > explore/se_combine.out
"""
import os, re, math
here = os.path.dirname(os.path.abspath(__file__)); rd = lambda n: open(os.path.join(here, n), encoding='utf-8').read()
ALPHA = 7.2973525643e-3
meas = {'165Ho66+': (0.93344, 1.53945), '187Re74+': (0.90557, 1.77309), '207Pb81+': (0.85539, 2.07183), '209Bi82+': (0.87360, 2.12497)}   # r/A measured, A (point Dirac), hydrogenlike_series.out
x_se = {'165Ho66+': -1.803*ALPHA, '187Re74+': -2.344*ALPHA, '209Bi82+': -3.090*ALPHA, '207Pb81+': -0.0218}                       # Table 1 (alpha X) of 9705029 via ar5iv; Pb: Table 2 of 9706031
x_se_cross = {'165Ho66+': -0.0132, '187Re74+': -0.0171, '207Pb81+': -0.0218, '209Bi82+': -0.0226}                              # self-energy column of Table 2 of 9706031
x_vp_lit = {'165Ho66+': 0.0044+0.0020, '187Re74+': 0.0064+0.0026, '207Pb81+': 0.0089+0.0033, '209Bi82+': 0.0094+0.0034}        # Uehling electric + magnetic, Table 2 of 9706031 (excluding Wichmann-Kroll)
BR = {}; BWu = {}; BWs = {}; VP = {}
for l in rd('nuclear_size_hfs.out').splitlines():
    t = l.split()
    if len(t) >= 9 and t[0] in meas and t[1].isdigit(): BR[t[0]] = float(t[4]); BWu[t[0]] = float(t[5]); BWs[t[0]] = float(t[6])
for l in rd('vp_hfs.out').splitlines():
    t = l.split()
    if len(t) >= 6 and t[0] in meas and t[1].isdigit(): VP[t[0]] = float(t[4])
SP = {}; cur = None
for l in rd('bw_single_particle.out').splitlines():
    m = re.match(r'(187Re74\+|207Pb81\+|209Bi82\+):', l)
    if m: cur = m.group(1); continue
    if cur and l.strip().startswith('r0=1.25 a=0.65'):
        d = re.findall(r'delta_BW = ([+-]\d\.\d+)', l); SP[cur] = [('single particle, Schmidt g_s', float(d[0])), ('single particle, g_s x 0.6', float(d[1])), ('single particle, spin scaled to mu', float(d[2]))]
print('self-energy as sourced, relative to the Fermi energy E_nr (x_SE), and in units of the point Dirac factor (x_SE / A):')
print(f'{"ion":9s} {"x_SE (alpha X)":>15s} {"x_SE (9706031)":>15s} {"x_SE/A":>10s} {"x_SE - a/2pi":>13s} {"(x_SE - a/2pi)/A":>17s}')
for n, (r, A) in meas.items(): print(f'{n:9s} {x_se[n]:+15.6f} {x_se_cross[n]:+15.4f} {x_se[n]/A:+10.6f} {x_se[n]-ALPHA/(2*math.pi):+13.6f} {(x_se[n]-ALPHA/(2*math.pi))/A:+17.6f}')
print(f'(alpha / 2 pi = {ALPHA/(2*math.pi):.6e})')
print('\ncomparison of the vacuum polarization: this repository (first order, relative) converted with the factor A (1 + BR)(1 + BW_uniform) to the literature convention (relative to E_nr):')
for n, (r, A) in meas.items():
    conv = VP[n]*A*(1+BR[n])*(1+BWu[n]); print(f'  {n:9s} computed {VP[n]:+.6f} -> x_VP {conv:+.5f}; literature Uehling electric + magnetic {x_vp_lit[n]:+.4f}; ratio computed / literature {conv/x_vp_lit[n]:.4f}')
print('\nleft = measured r/A / predicted r/A - 1:')
print(f'{"ion":9s} {"BW model":34s} {"(a) x_SE as tabulated":>22s} {"(b) x_SE - a/2pi":>18s}   (no SE)')
for n, (r, A) in meas.items():
    rows = [('uniform sphere (old bound)', BWu[n]), ('thin shell (old bound)', BWs[n])] + SP.get(n, [])
    for lab, bw in rows:
        base = (1+BR[n])*(1+bw)*(1+VP[n]); la = r/(base + x_se[n]/A) - 1; lb = r/(base + (x_se[n]-ALPHA/(2*math.pi))/A) - 1; l0 = r/base - 1
        print(f'{n:9s} {lab:34s} {la:+22.5f} {lb:+18.5f}   {l0:+.5f}')
