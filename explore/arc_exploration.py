# Exploring the arc: the plateau, the adjacency reading, and which quantities march with mass. New file (2026-11-02); nothing fitted. Exploratory; coincidences are flagged, not claimed.
# 1. Plateau: the ratio of nuclear cycles (R_N B / hbar c) to atomic cycles (tan(theta/2), sin theta = Z alpha) over all nuclides in the saved IAEA table with a radius and a binding energy and either stable or
#    half-life above 1e9 years (so Th and U are included); the local log-slopes d ln(nuclear)/d ln Z and d ln(atomic)/d ln Z in windows of Z; where the two slopes are equal the ratio is flat.
# 2. Adjacency: the exponent excess p - 3 of the hyperfine energy against the size ratio s = 1/(Z alpha) to the electron Compton rung, with its leading term 3/s^2; the nearest measured rungs of the carbon stack to each ion's atomic order.
# 3. Which quantities march with Z along the arc: theta, atomic and nuclear cycles, cycles per nucleon, equivalent-sphere nuclear density, gravitational registration (M/m_P)^2 = G M^2 / (hbar c).
# Run: py -3 -I -X utf8 -u explore/arc_exploration.py > explore/arc_exploration.out
import csv, os, math
here = os.path.dirname(os.path.abspath(__file__))
e = 1.602176634e-19; h = 6.62607015e-34; hbar = h/(2*math.pi); c = 299792458.0; hbarc = hbar*c/e; ALPHA = 7.2973525643e-3; G = 6.67430e-11; meu = 5.485799090e-4
muB = 9.2740100657e-24; me = e*hbar/(2*muB); mec2 = me*c**2/e; uc2 = mec2/meu; mP_c2 = math.sqrt(hbar*c**5/G)/e
rows = list(csv.DictReader(open(os.path.join(here, 'data', 'iaea_livechart_ground_states.csv'), encoding='utf-8')))
def cyc_atomic(Z): g = math.sqrt(1-(Z*ALPHA)**2); return (1-g)/(Z*ALPHA)
data = {}
for r in rows:
    try:
        Z = int(r['z']); N = int(r['n']); A = Z+N
        if Z < 3 or Z > 100 or not r['radius'] or not r['binding'] or not r['atomic_mass']: continue
        hl = r['half_life']; ok = (hl == 'STABLE')
        if not ok:
            try: ok = float(r['half_life_sec']) > 3.15e16
            except ValueError: ok = False
        if not ok: continue
        Rn = float(r['radius'])*1e-15; B = float(r['binding'])*1e-3*A*1e6; M = float(r['atomic_mass'])*1e-6*uc2 - Z*mec2
        Req = math.sqrt(5/3)*Rn*1e15
        d = dict(Z=Z, A=A, nuc=Rn*B/hbarc, atm=cyc_atomic(Z), dens=A/(4/3*math.pi*Req**3), M=M, B=B, Rn=Rn)
        d['ratio'] = d['nuc']/d['atm']; d['gr'] = (M/mP_c2)**2
        data.setdefault(Z, []).append(d)
    except ValueError: continue
Zs = sorted(data)
def avg(Z, k): v = [d[k] for d in data[Z]]; return sum(v)/len(v)
print(f'nuclides used: {sum(len(v) for v in data.values())} (stable or half-life > 1e9 y, with radius and binding), elements Z = {Zs[0]}..{Zs[-1]} ({len(Zs)} elements); 1/alpha = {1/ALPHA:.3f}')
print('\n== 1. the plateau: ratio of nuclear to atomic cycles, mean over the nuclides of each element')
print(f'{"Z":>4s} {"n":>3s} {"A (first)":>9s} {"nuclear cycles":>14s} {"atomic cycles":>14s} {"ratio":>8s} {"ratio x alpha":>13s}')
for Z in (3, 6, 8, 14, 20, 26, 30, 40, 50, 56, 60, 64, 67, 70, 75, 79, 82, 83, 90, 92):
    if Z in data: print(f'{Z:4d} {len(data[Z]):3d} {data[Z][0]["A"]:9d} {avg(Z, "nuc"):14.4f} {avg(Z, "atm"):14.5f} {avg(Z, "ratio"):8.2f} {avg(Z, "ratio")*ALPHA:13.4f}')
print('\nlocal log-slopes between element means (nuclear: d ln N/d ln Z; atomic: d ln a/d ln Z; their difference is the slope of the ratio):')
print(f'{"Z window":>12s} {"nuclear":>9s} {"atomic":>8s} {"ratio slope":>12s}   components of the nuclear slope: R_N, B')
wins = [(20, 30), (30, 40), (40, 50), (50, 60), (60, 70), (70, 83), (83, 92)]
for z1, z2 in wins:
    za = [z for z in Zs if z >= z1][0]; zb = [z for z in Zs if z <= z2][-1]
    if za == zb: continue
    L = math.log(zb/za); sn = math.log(avg(zb, 'nuc')/avg(za, 'nuc'))/L; sa = math.log(avg(zb, 'atm')/avg(za, 'atm'))/L
    sR = math.log(avg(zb, 'Rn')/avg(za, 'Rn'))/L; sB = math.log(avg(zb, 'B')/avg(za, 'B'))/L
    print(f'{za:4d}->{zb:<4d}  {sn:9.3f} {sa:8.3f} {sn-sa:12.3f}   {sR:.3f}, {sB:.3f}')
print('(the ratio is flat where the two slopes are equal; the window slopes show whether the equality is a crossing or a stay)')
print('\n== 2. adjacency: exponent excess p - 3 against the size ratio s = 1/(Z alpha) to the electron Compton rung')
def pexc(s):
    gg = math.sqrt(1-1/s**2); return (1/s**2)/gg*(1/gg + 2/(2*gg-1))
print(f'{"s":>9s} {"p - 3 (Dirac)":>14s} {"3/s^2":>9s} {"ratio":>7s} {"local slope d ln(p-3)/d ln s":>30s}')
prev = None
for s in (137.0, 68.5, 27.4, 13.7, 6.85, 4.57, 3.43, 2.74, 2.28, 2.05, 1.83, 1.67, 1.65, 1.40, 1.20):
    pe = pexc(s); sl = ''
    if prev: sl = f'{math.log(pe/prev[1])/math.log(s/prev[0]):.3f}'
    print(f'{s:9.2f} {pe:14.5f} {3/s**2:9.5f} {pe/(3/s**2):7.3f} {sl:>30s}'); prev = (s, pe)
print('so the influence of the electron rung on the exponent falls as s^-2 (an inverse-square in the size ratio) at large s and steepens into the pole as s -> 1.155 (the point-nucleus Dirac form).')
lP = 1.616255e-35; Rcomp = 3.8615926743e-13
rungs = [('proton Compton', 2.1031e-16), ('nucleon r_p', 8.4075e-16), ('muon Compton', 1.8676e-15), ('12C charge radius', 2.4702e-15), ('electron Compton', Rcomp), ('C5+ 1s (a0/6)', 8.82e-12), ('a0 (H atom)', 5.2918e-11)]
print('\nnearest carbon-stack rungs to each heavy ion\'s atomic order (size a0/Z) and nuclear order (charge radius), as ratios:')
a0 = Rcomp/ALPHA
for name, Z, Rn in (('H', 1, 0.84075e-15), ('3He+', 2, 1.9661e-15), ('165Ho66+', 67, 5.2022e-15), ('187Re74+', 75, 5.3698e-15), ('207Pb81+', 82, 5.4943e-15), ('209Bi82+', 83, 5.5211e-15)):
    Re = a0/Z; below = max((R for n, R in rungs if R <= Re), default=None); above = min((R for n, R in rungs if R > Re), default=None)
    nb = [n for n, R in rungs if R == below][0] if below else '-'; na = [n for n, R in rungs if R == above][0] if above else '-'
    print(f'  {name:9s} atomic order {Re:.4e} m: nearest below {nb} (x{Re/below:.3f}), above {na} (x{above/Re if above else float("nan"):.3f}); nuclear order {Rn:.4e} m')
print('\n== 3. what marches with Z along the arc (one nuclide per element shown; equivalent-sphere density n = A / (4 pi/3 (sqrt(5/3) R_ch)^3))')
print(f'{"element Z":>9s} {"A":>4s} {"theta deg":>9s} {"atomic cyc":>10s} {"nuclear cyc":>11s} {"cycles/A":>9s} {"n (fm^-3)":>9s} {"(M/m_P)^2":>10s} {"p - 3":>8s}')
for Z in (3, 6, 8, 14, 20, 26, 40, 50, 60, 67, 75, 82, 83, 90, 92):
    if Z not in data: continue
    d = data[Z][len(data[Z])//2]; th = math.degrees(math.asin(Z*ALPHA)); print(f'{Z:9d} {d["A"]:4d} {th:9.2f} {d["atm"]:10.5f} {d["nuc"]:11.3f} {d["nuc"]/d["A"]:9.4f} {d["dens"]:9.4f} {d["gr"]:10.3e} {pexc(1/(Z*ALPHA)):8.4f}')
Ds = [data[Z][len(data[Z])//2] for Z in Zs if Z >= 20]
def corr(xs, ys):
    n = len(xs); mx = sum(xs)/n; my = sum(ys)/n; sxy = sum((a-mx)*(b-my) for a, b in zip(xs, ys)); return sxy/math.sqrt(sum((a-mx)**2 for a in xs)*sum((b-my)**2 for b in ys))
th = [math.asin(d['Z']*ALPHA) for d in Ds]
print('\ncorrelation with theta over Z >= 20 (one nuclide per element): ln A %.4f, nuclear cycles %.4f, cycles per nucleon %.4f, ln(M/m_P)^2 %.4f, equivalent density %.4f' % (
    corr(th, [math.log(d['A']) for d in Ds]), corr(th, [d['nuc'] for d in Ds]), corr(th, [d['nuc']/d['A'] for d in Ds]), corr(th, [math.log(d['gr']) for d in Ds]), corr(th, [d['dens'] for d in Ds])))
dd = [d['dens'] for d in Ds]; print('equivalent nuclear density over Z >= 20: min %.4f max %.4f mean %.4f fm^-3 (saturation: nearly constant), spread %.1f%%' % (min(dd), max(dd), sum(dd)/len(dd), 100*(max(dd)-min(dd))/(sum(dd)/len(dd))))
print('nuclear cycles per nucleon rise as A^(1/3) (cycles ~ A^(4/3) at saturation): from %.4f (Z=20) to %.4f (Z=83)' % (data[20][len(data[20])//2]['nuc']/data[20][len(data[20])//2]['A'], data[83][0]['nuc']/data[83][0]['A']))
