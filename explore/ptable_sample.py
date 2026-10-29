# Periodic-table sample through the BC dictionary. Data: PeriodicTableJSON.json (Bowserinator/Periodic-Table-JSON, github raw), path given as argv[1]
# (the file is untrusted data: parsed only, never executed). New file; nothing fitted.
# For ionization stage k of an element: E_k (eV) = kJ/mol / 96.485332; the removed electron is taken from the outermost occupied SHELL (shell-level
# assumption; subshell order is ignored), n_k = that shell; hydrogenic effective charge Z_eff,k = n_k sqrt(E_k/Ry); radius R_k = n_k^2 a0 / Z_eff,k;
# cycles_k = R_k E_k/(hbar c) = Z_eff,k * alpha/2 (so Z_eff,k IS the stage in units of alpha/2); extent in electron-Compton cycles X_k = R_k/lambda_e.
import json, sys, hashlib, math
path = sys.argv[1]
raw = open(path, 'rb').read(); print('data file sha256', hashlib.sha256(raw).hexdigest(), len(raw), 'bytes')
D = json.loads(raw.decode('utf-8'))['elements']
al = 7.2973525693e-3; Ry = 13.605693123; a0 = 5.29177210903e-11; lam_e = 3.8615926772e-13; kJ = 96.485332
l12 = lambda x: math.log(x)/math.log(12)
by = {e['symbol']: e for e in D}
li = by['Li']; print('atomic_radii field for Li:', li.get('atomic_radii'), '| keys:', [k for k in li if 'radi' in k])

def stages(e, kmax=4):
    sh = list(e['shells']); IE = e.get('ionization_energies') or []; out = []
    occ = sh[:]
    for k in range(min(kmax, len(IE))):
        n = max(i for i, c in enumerate(occ, 1) if c > 0)
        occ[n-1] -= 1
        E = IE[k]/kJ; Z = n*math.sqrt(E/Ry); R = n*n*a0/Z
        out.append((k+1, n, E, Z, R, R/lam_e))
    return out

sample = {'alkali metal': ['H', 'Li', 'Na', 'K', 'Cs'], 'alkaline earth metal': ['Be', 'Mg', 'Ca', 'Ba'], 'transition metal': ['Fe', 'Cu', 'Ag', 'W', 'Au'],
          'post-transition metal': ['Al', 'Sn', 'Pb', 'Bi'], 'metalloid': ['B', 'Si', 'Ge'], 'nonmetal': ['C', 'N', 'O', 'S'],
          'halogen': ['F', 'Cl', 'Br', 'I'], 'noble gas': ['He', 'Ne', 'Ar', 'Kr', 'Xe'], 'lanthanide': ['La', 'Ce', 'Gd', 'Lu'], 'actinide': ['U']}
print('\nPART A  raw data vector per sampled element (as in the file)')
print(f'{"cls":22s}{"Z":>4s} {"sym":3s} {"mass":>9s} {"dens g/cm3":>11s} {"melt K":>8s} {"boil K":>8s} {"EN":>5s} {"EA kJ/mol":>10s} {"IE1":>9s} {"IE2":>9s} {"IE3":>9s} shells')
f = lambda x, w, p=4: (f'{x:{w}.{p}g}' if isinstance(x, (int, float)) else f'{"-":>{w}s}')
for cls, syms in sample.items():
    for s in syms:
        e = by[s]; IE = (e.get('ionization_energies') or []) + [None]*3
        print(f'{cls:22s}{e["number"]:4d} {s:3s} {f(e["atomic_mass"],9)} {f(e.get("density_g_cm3"),11)} {f(e.get("melt"),8)} {f(e.get("boil"),8)} {f(e.get("electronegativity_pauling"),5)} {f(e.get("electron_affinity"),10)} {f(IE[0],9)} {f(IE[1],9)} {f(IE[2],9)} {e["shells"]}')

print('\nPART B  BC translation per ionization stage: n (shell removed from), Z_eff = n sqrt(E/Ry) (= cycles in units of alpha/2), R (m), extent X = R/lambda_e (Compton cycles), log12 X')
print(f'{"cls":22s}{"sym":4s}{"k":>2s}{"n":>3s}{"E eV":>10s}{"Zeff":>9s}{"R (m)":>12s}{"X":>10s}{"log12 X":>9s}')
for cls, syms in sample.items():
    for s in syms:
        for (k, n, E, Z, R, X) in stages(by[s]):
            print(f'{cls:22s}{s:4s}{k:2d}{n:3d}{E:10.4f}{Z:9.4f}{R:12.4e}{X:10.2f}{l12(X):9.4f}')

print('\nPART C  valence rung over the WHOLE table (all elements with IE1): Zeff1, extent X1')
allv = []
for e in D:
    st = stages(e, 1)
    if st: allv.append((e['number'], e['symbol'], e['category'], st[0]))
Zs = [v[3][3] for v in allv]; Xs = [v[3][5] for v in allv]
print(f'  {len(allv)} elements: Zeff1 min {min(Zs):.4f} ({allv[Zs.index(min(Zs))][1]}) max {max(Zs):.4f} ({allv[Zs.index(max(Zs))][1]});  X1 min {min(Xs):.2f} ({allv[Xs.index(min(Xs))][1]}) max {max(Xs):.2f} ({allv[Xs.index(max(Xs))][1]})')
print(f'  valence extent spans log12 X from {l12(min(Xs)):.4f} to {l12(max(Xs)):.4f}  (= {math.log10(max(Xs)/min(Xs)):.3f} decades); hydrogen X = 1/alpha = {1/al:.4f}')
print('\n  class summary of the SAMPLE valence rung (Zeff1, log12 X1):')
for cls, syms in sample.items():
    zs = [stages(by[s], 1)[0][3] for s in syms]; xs = [stages(by[s], 1)[0][5] for s in syms]
    print(f'   {cls:22s} Zeff1 {min(zs):.4f}..{max(zs):.4f}   log12 X1 {l12(min(xs)):.4f}..{l12(max(xs)):.4f}   Zeff1 monotone with Z within class: {all(zs[i] <= zs[i+1] for i in range(len(zs)-1))}')

print('\nPART D  stage-to-stage jumps in Zeff (first stage after a closed shell vs within-shell stages)')
for s in ['Li', 'Na', 'K', 'Cs', 'Be', 'Mg', 'Ca', 'Ba', 'Al', 'C', 'F', 'Ne']:
    st = stages(by[s], 4); print(f'   {s:3s}', ' '.join(f'Z{k}={Z:.3f}(n{n})' for (k, n, E, Z, R, X) in st), ' ratios:', ' '.join(f'{st[i+1][3]/st[i][3]:.3f}' for i in range(len(st)-1)))
print('\nPART E  cross-checks against the earlier hand-built lithium run: IE (eV) from file', [round(x/kJ, 6) for x in by['Li']['ionization_energies'][:3]], ' vs lithium_map.py 5.391493 75.639476 122.453846')
