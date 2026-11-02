"""
Two parts, new file (2026-11-02), nothing fitted.
 A. The tick ratio between adjacent orders as nature shows it: sizes of the rungs of one gram of carbon (maps/carbon_complete_stack.md, master table), sorted, adjacent ratios.
    A rung's tick is taken as proportional to its size (the lab's declared anchor edge = c x tick), so a size ratio is a tick ratio rho.  Then the two-copy instrument is run at those measured ratios.
 B. An ablation record: one scenario (a neutral pair of current-carrying rings in copy A, Gauss-prepared with A's links, copy B empty) evolved with each switch turned off in turn,
    the expressed / manifest readouts (e_series_readouts.py) and the exchange with B recorded as time means over T = 20.  The base setting is declared: rho = the median measured adjacent ratio,
    kappa_r = 1, mu_r = M6 value, transport q.  Switches are listed in the output; nothing is predicted before the run.
Usage:  py -3 -I -X utf8 -u e_series_ablation.py > e_series_ablation.out
"""
import numpy as np, os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(here, 'e_series_two_copy.py'), encoding='utf-8').read().split("rng = np.random.default_rng(20261103)")[0])
exec(open(os.path.join(here, 'e_series_readouts.py'), encoding='utf-8').read().split("print('== check: ring states")[0])
# ---------------- A: adjacent ratios ----------------
rows = []
for line in open(os.path.join(here, '..', 'maps', 'carbon_complete_stack.md'), encoding='utf-8'):
    if line.startswith('| ') and not line.startswith('| rung') and not line.startswith('|---'):
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        try: rows.append((c[0], c[1], float(c[2])))
        except: pass
rows.sort(key=lambda r: r[2])
print('== A. rungs of one gram of carbon by size (maps/carbon_complete_stack.md §1), and the ratio to the next size up')
for i, (n, cl, R) in enumerate(rows):
    print(f'{R:11.4e} m  {cl:8s} {n[:52]:52s}' + (f'  next/this = {rows[i+1][2]/R:12.5g}' if i+1 < len(rows) else ''))
# distinct sizes: merge rungs whose sizes differ by less than 3 percent (same object read two ways)
dist = []
for n, cl, R in rows:
    if not dist or R/dist[-1] > 1.03: dist.append(R)
ratios = np.array([dist[i+1]/dist[i] for i in range(len(dist)-1)])
print('\ndistinct sizes (merged within 3%):', len(dist), '| adjacent ratios:', ' '.join('%.4g' % r for r in ratios))
body = ratios[ratios < 1e4]
print('excluding the jump to the gram: min %.4g  median %.4g  max %.4g  | log_phi of them:' % (body.min(), np.median(body), body.max()), ' '.join('%.2f' % (np.log(r)/np.log(phi)) for r in body))
RHO_MED = float(np.median(body)); print('declared base rho = median measured adjacent ratio =', repr(RHO_MED))
# ---------------- exchange at the measured ratios ----------------
far = int(np.argmin(V @ V[0])); KEY = 'q'
def pair_state(P, jx, key):
    ps, vs, _, _ = ring(0, 1, key, -1); pj, vj, _, _ = ring(jx, 1, key, +1); psi = ps+pj; vel = vs+vj
    r = rho_v(psi, vel, 1.0); Lm = 12*np.eye(N) - (adj*1.0); rhs = -P['kk']*r/P['I'][0]; rhs = rhs - rhs.mean()
    phv = np.linalg.lstsq(Lm, rhs, rcond=1e-10)[0]
    Z = np.zeros((H, 2), complex)
    return ([psi, Z.copy()], [vel, Z.copy()], [np.zeros(NE), np.zeros(NE)], [phv[HEAD]-phv[TAIL], np.zeros(NE)], np.zeros(N), np.zeros(N))
# a partner cycle in a generic position (manifest/expressed current about 1/sqrt(2) against cycle 0)
JX = None
for jx in range(1, len(cyc)):
    if jx == reverse_cycle(0): continue
    pj, vj, _, _ = ring(jx, 1, KEY, +1); ps, vs, _, _ = ring(0, 1, KEY, -1); d = readouts(ps+pj, vs+vj, np.zeros(NE), KEY)
    if abs(d['j_man']/d['j_exp'] - 2**-0.5) < 1e-6: JX = jx; break
print('\nscenario partner cycle', JX, '(second ring, opposite charge, generic position)')
print('\n== A (cont.). two-copy exchange at the measured adjacent ratios, kappa_r = 1, mu_r = 0 and mu_r = M6, links live, T = 40')
print('rho | mu_r = 0: t_arrive(>1e-3), max fraction in B | mu_r = M6: t_arrive, max fraction')
for rho in sorted(set(round(float(r), 6) for r in body)):
    cells = []
    for mur in (0.0, MU_N):
        P = mkP(rho=rho, kr=1.0, mur=mur, key=KEY); o = run(pair_state(P, JX, KEY), P, 2000, 0.02)
        cells.append(f'{("%.2f" % o["tarr"]) if o["tarr"] is not None else "none":>6}, {max(o["fracB"]):.4f}  (gauss {o["gd"]:.0e})')
    print(f'{rho:10.5g} | {cells[0]} | {cells[1]}')
# ---------------- B: ablation record ----------------
print('\n== B. ablation record: base rho = %.5g, kappa_r = 1, mu_r = M6, transport q; time means over T = 20 (snapshots every 0.5)' % RHO_MED)
cols = ['charge exp A', 'dipole A', 'current exp A', 'moment man A', 'flux exp A', 'flux man A', 'moment man B', 'frac energy B', 'gauss drift', 'dE max']
def scenario(name, rho=RHO_MED, kr=1.0, mur=MU_N, key='q', mu=MU_N, kk=1.0, live=True):
    P = mkP(rho=rho, kr=kr, mur=mur, key=key, mu=mu); P['kk'] = kk
    jx = JX if key == 'q' else None
    if jx is None:
        for j2 in range(1, len(cyc)):
            if j2 == reverse_cycle(0): continue
            pj, vj, _, _ = ring(j2, 1, key, +1); ps, vs, _, _ = ring(0, 1, key, -1); d = readouts(ps+pj, vs+vj, np.zeros(NE), key)
            if abs(d['j_man']/d['j_exp'] - 2**-0.5) < 1e-6: jx = j2; break
    S0 = pair_state(P, jx, key); o = run(S0, P, 1000, 0.02, live=live, snap=25)
    acc = []
    for t, e, S in o['snaps']:
        dA = readouts(S[0][0], S[1][0], S[2][0], key, m=1.0); dB = readouts(S[0][1], S[1][1], S[2][1], key, m=P['m'][1])
        acc.append([dA['abs_rho'], dA['dip'], dA['j_exp'], dA['j_man'], dA['F_exp'], dA['F_man'], dB['j_man'], (e['matter1']+e['link1'])/o['e0']['total']])
    m = np.mean(acc, axis=0); return [name] + list(m) + [o['gd'], o['dEmax']]
runs = [scenario('base'),
        scenario('links frozen (a, b not updated)', live=False),
        scenario('charge coupling off (k = 0)', kk=0.0),
        scenario('face flux energy off in both copies (mu = 0)', mu=0.0),
        scenario('plaquette flux between copies off (mu_r = 0)', mur=0.0),
        scenario('matter coupling between copies off (kappa_r = 0)', kr=0.0),
        scenario('copies decoupled (kappa_r = mu_r = 0)', kr=0.0, mur=0.0),
        scenario('transport gamma instead of q', key='gamma'),
        scenario('equal ticks (rho = 1)', rho=1.0),
        scenario('rho = 1836.152673426 (proton/electron mass ratio)', rho=1836.152673426)]
print(f'{"switch":54s}' + ''.join(f'{c:>15s}' for c in cols))
for r in runs: print(f'{r[0]:54s}' + ''.join(f'{x:15.5g}' for x in r[1:]))
print('\nchange relative to base (ratio of the column to the base value; 1 = unchanged, 0 = vanishes):')
b = runs[0]
print(f'{"switch":54s}' + ''.join(f'{c:>15s}' for c in cols[:8]))
for r in runs[1:]: print(f'{r[0]:54s}' + ''.join(f'{(r[i]/b[i] if abs(b[i]) > 1e-12 else float("nan")):15.4g}' for i in range(1, 9)))
