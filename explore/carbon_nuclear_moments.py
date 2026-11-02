# Expressed versus manifest magnetic moment in nuclei, from the saved IAEA ground-state table. New file (2026-11-02); nothing fitted.
# Expressed = what the constituents carry: the sum of the free-nucleon moments, taken in magnitude and with sign.
# Manifest  = the measured moment of the nucleus (0 when the ground state has spin 0).
# Free-nucleon moments are the table's own rows for the neutron and the hydrogen-1 nucleus.  Units: nuclear magnetons.
# Run: py -3 -I -X utf8 -u explore/carbon_nuclear_moments.py > explore/carbon_nuclear_moments.out
import csv, os
here = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(here, 'data', 'iaea_livechart_ground_states.csv'), encoding='utf-8')))
def get(z, n):
    for r in rows:
        if r['z'] == str(z) and r['n'] == str(n): return r
    return None
def f(x):
    try: return float(x)
    except: return None
mp = f(get(1, 0)['magnetic_dipole']); mn = f(get(0, 1)['magnetic_dipole'])
print('free proton (1H row)', repr(mp), 'unc', get(1, 0)['unc_md'], '| free neutron', repr(mn), 'unc', get(0, 1)['unc_md'], '(nuclear magnetons)')
print(f"{'nuclide':8s} {'Z':>2s} {'N':>2s} {'Jpi':>6s} {'half-life':>10s} | {'sum|mu_i|':>10s} {'signed sum':>11s} | {'measured mu':>13s} {'unc':>10s} | {'|mu|/sum|mu_i|':>14s}")
for (z, n) in [(1, 0), (1, 1), (2, 1), (2, 2), (3, 3), (4, 5), (5, 5), (5, 6), (6, 5), (6, 6), (6, 7), (6, 8), (7, 7), (7, 8), (8, 8), (9, 10), (14, 14), (26, 30)]:
    r = get(z, n)
    if r is None: print(z, n, 'not in table'); continue
    a = z*abs(mp) + n*abs(mn); s = z*mp + n*mn; m = f(r['magnetic_dipole'])
    sym = r['symbol']+str(z+n)
    meas = ('%.7f' % m) if m is not None else ('none (Jpi %s)' % r['jp'])
    ratio = ('%.6f' % (abs(m)/a)) if m is not None else ('0 (spin 0)' if r['jp'].startswith('0') else 'n/a')
    print(f"{sym:8s} {z:2d} {n:2d} {r['jp']:>6s} {r['half_life']+(' '+r['unit_hl'] if r['unit_hl'] else ''):>10s} | {a:10.4f} {s:11.4f} | {meas:>13s} {r['unc_md']:>10s} | {ratio:>14s}")
