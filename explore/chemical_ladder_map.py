# Chemical-level ladder: atoms, diatomic molecules, atomization of all species with sourced 0 K enthalpies, solids' cohesion.
# Same dictionary: cycles = R E/(hbar c); alpha/2 = hydrogen binding rung. New file; floor untouched. No fitting, no search: tabulate and print.
# Inputs in explore/data/: PeriodicTableJSON.json (Bowserinator, Wikipedia-derived), cccbdb_diatomic_exp_bondlengths.html (NIST CCCBDB, Release 22),
# cccbdb_enthalpy_formation_0K.html (NIST CCCBDB: Hfg at 0 K, CODATA/JANAF/Gurvich/...). Parsed only, never executed.
import json, re, html, os, math
from statistics import median
HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.join(HERE, 'data')
al = 7.2973525693e-3; Ry = 13.605693123; a0 = 5.29177210903e-11; lam_e = 3.8615926768e-13; kJ = 96.485332
hbarc = 1.973269804e-7          # eV m
NA = 6.02214076e23; me_eV = 510998.95; lP = 1.616255e-35
l12 = lambda x: math.log(x)/math.log(12)
cyc = lambda R, E: R*E/hbarc
half = al/2

def txt(s):
    s = re.sub(r'<sub>(.*?)</sub>', r'\1', s, flags=re.I); s = re.sub(r'<sup>(.*?)</sup>', r'^\1', s, flags=re.I)
    return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()

# ---------------- elements
EL = json.load(open(os.path.join(DATA, 'PeriodicTableJSON.json'), encoding='utf-8'))['elements']
by = {e['symbol']: e for e in EL}

# ---------------- CCCBDB 0 K enthalpies of formation (kJ/mol) and diatomic bond lengths (angstrom)
raw = open(os.path.join(DATA, 'cccbdb_enthalpy_formation_0K.html'), encoding='utf-8', errors='replace').read()
Hf = []   # (formula, name, kJ/mol, source)
for row in re.findall(r'<TR>(.*?)</TR>', raw, flags=re.S | re.I):
    cells = re.findall(r'<TD[^>]*>(.*?)</TD>', row, flags=re.S | re.I)
    if len(cells) >= 4:
        f = txt(cells[0]); name = txt(cells[1]); v = txt(cells[2]); src = txt(cells[3])
        try: Hf.append((f, name, float(v), src))
        except ValueError: pass
atomH = {}
for f, n, v, s in Hf:
    if re.fullmatch(r'[A-Z][a-z]?', f): atomH[f] = (v, s, n)
def parse(f):
    if re.search(r'[\^()\-+]', f): return None
    toks = re.findall(r'([A-Z][a-z]?)(\d*)', f)
    if ''.join(a+b for a, b in toks) != f: return None
    d = {}
    for a, b in toks: d[a] = d.get(a, 0) + (int(b) if b else 1)
    return d
mol = []   # neutral molecules with all atoms in atomH
for f, n, v, s in Hf:
    d = parse(f)
    if not d or sum(d.values()) < 2 or any(a not in atomH for a in d): continue
    D0 = sum(c*atomH[a][0] for a, c in d.items()) - v      # kJ/mol, atomization energy at 0 K
    mol.append((f, n, d, D0/kJ, s))

bl = open(os.path.join(DATA, 'cccbdb_diatomic_exp_bondlengths.html'), encoding='utf-8', errors='replace').read()
tab = bl[bl.find('<table border="1">'):]
head = [txt(x) for x in re.findall(r'<th>(.*?)</th>', tab.split('</tr>')[0], flags=re.S) if txt(x) not in ('', '\xa0')]
re_len = {}
for row in tab.split('</tr>')[1:]:
    m = re.match(r'\s*<tr>\s*<th>(.*?)</th>', row, flags=re.S)
    if not m: continue
    rel = txt(m.group(1)); cells = re.findall(r'<td[^>]*>(.*?)</td>', row, flags=re.S)
    for j, c in enumerate(cells):
        t = txt(c)
        if t and j < len(head):
            try: re_len[(rel, head[j])] = float(t)
            except ValueError: pass

print('INPUT COUNTS: elements', len(EL), '; CCCBDB 0 K entries', len(Hf), ' (atoms', len(atomH), ', neutral molecules with all atoms tabulated', len(mol), '); diatomic bond-length cells', len(re_len), ' header elements', len(head))
print('constants: alpha', al, ' Ry', Ry, ' a0', a0, ' lam_e', lam_e, ' hbar c', hbarc, 'eV m ; alpha/2 =', half)
print()

# ================= PART A: atoms
print('PART A  atoms: valence rung from IE1 (shell-level assumption: electron removed from the outermost occupied shell n); Z_eff = n sqrt(IE1/Ry); R = n^2 a0/Z_eff; cycles = Z_eff alpha/2 (identity)')
print(f'  {"Z":>3s} {"sym":3s} {"n":>2s} {"IE1 eV":>9s} {"Zeff":>8s} {"R m":>12s} {"X=R/lam_e":>10s} {"log12 X":>8s} {"len p12":>8s}')
A = []
for e in EL:
    IE = e.get('ionization_energies')
    if not IE: continue
    n = len(e['shells']); E = IE[0]/kJ; Z = n*math.sqrt(E/Ry); R = n*n*a0/Z
    A.append((e['number'], e['symbol'], n, E, Z, R));
    print(f'  {e["number"]:3d} {e["symbol"]:3s} {n:2d} {E:9.4f} {Z:8.4f} {R:12.4e} {R/lam_e:10.2f} {l12(R/lam_e):8.4f} {l12(R/lP):8.4f}')
Zs = [a[4] for a in A]; Xs = [a[5]/lam_e for a in A]
print(f'  {len(A)} elements: Zeff1 {min(Zs):.4f}..{max(Zs):.4f}; X {min(Xs):.2f}..{max(Xs):.2f}; log12 X {l12(min(Xs)):.4f}..{l12(max(Xs)):.4f}; length position p12 {l12(min(a[5] for a in A)/lP):.4f}..{l12(max(a[5] for a in A)/lP):.4f}')
print()

# ================= PART B: diatomics with bond length (CCCBDB) and atomization energy at 0 K (from Hfg)
print('PART B  diatomic molecules: r_e (A, CCCBDB experimental) and D0 = Hfg(A)+Hfg(B)-Hfg(AB) at 0 K (eV); cycles = r_e D0/(hbar c); in units of alpha/2; X = r_e/lam_e')
print(f'  {"mol":6s} {"r_e A":>7s} {"D0 eV":>9s} {"cycles":>12s} {"cyc/(a/2)":>10s} {"X":>9s} {"log12 X":>8s} {"D0/Ry":>8s} {"D0/(m_e c^2)":>13s} {"src":>8s}')
dia = []
mols = {f: (d, D, s) for f, n, d, D, s in mol}
seen = set()
for (a, b), r in sorted(re_len.items()):
    cand = [a+b, b+a] if a != b else [a+'2']
    f = next((c for c in cand if c in mols), None)
    if f is None or f in seen: continue
    seen.add(f)
    d, D0, s = mols[f]
    R = r*1e-10; c_ = cyc(R, D0)
    dia.append((f, r, D0, c_, c_/half, R/lam_e, s))
    print(f'  {f:6s} {r:7.3f} {D0:9.4f} {c_:12.6e} {c_/half:10.4f} {R/lam_e:9.2f} {l12(R/lam_e):8.4f} {D0/Ry:8.4f} {D0*1.0/me_eV:13.4e} {s:>8s}')
cs = [x[4] for x in dia]
print(f'  {len(dia)} diatomics with both entries: cycles/(alpha/2) min {min(cs):.4f} max {max(cs):.4f} median {median(cs):.4f}; X min {min(x[5] for x in dia):.2f} max {max(x[5] for x in dia):.2f}')
print()

# ================= PART C: atomization energy of every neutral molecule with tabulated atoms
print('PART C  atomization energy at 0 K of every neutral molecule with atoms in the table (no sizes available from these data): D0 (eV), per atom, in Ry, atoms count. Duplicate formulas (different states) listed separately.')
print(f'  {"formula":10s} {"atoms":>5s} {"D0 eV":>10s} {"D0/atom eV":>11s} {"D0/Ry":>9s} {"D0/atom/Ry":>11s} {"src":>8s}')
for f, n, d, D0, s in sorted(mol, key=lambda t: sum(t[2].values())):
    k = sum(d.values())
    print(f'  {f:10s} {k:5d} {D0:10.4f} {D0/k:11.4f} {D0/Ry:9.4f} {D0/k/Ry:11.4f} {s:>8s}')
print()

# ================= PART D: solids, cohesion from reference-state atomization (Hfg of the gas atom at 0 K), Wigner-Seitz radius from density
print('PART D  solids: cohesive/atomization energy per atom Ec = Hfg(atom, 0 K) (from the reference state; H, N, O, F, Cl are molecular gases so Ec is half the bond energy), Wigner-Seitz radius from density and mass; cycles = r_ws Ec/(hbar c)')
print(f'  {"sym":3s} {"phase":6s} {"rho g/cc":>9s} {"r_ws m":>11s} {"Ec eV":>8s} {"cycles":>12s} {"cyc/(a/2)":>10s} {"Ec/IE1":>8s} {"r_ws/R_val":>10s} {"log12 r_ws/lam_e":>16s}')
sol = []
Ad = {a[1]: a for a in A}
for e in EL:
    s = e['symbol']; rho = e.get('density_g_cm3')
    if s not in atomH or not rho or rho < 0.5 or e.get('phase') != 'Solid' or s not in Ad: continue
    r = (3*e['atomic_mass']/(4*math.pi*rho*NA))**(1/3)*1e-2
    Ec = atomH[s][0]/kJ; c_ = cyc(r, Ec)
    sol.append((s, rho, r, Ec, c_, c_/half, Ec/Ad[s][3], r/Ad[s][5]))
    print(f'  {s:3s} {e["phase"]:6s} {rho:9.4f} {r:11.4e} {Ec:8.4f} {c_:12.6e} {c_/half:10.4f} {Ec/Ad[s][3]:8.4f} {r/Ad[s][5]:10.4f} {l12(r/lam_e):16.4f}')
sc = [x[5] for x in sol]
print(f'  {len(sol)} solids with Hfg(atom): cycles/(alpha/2) min {min(sc):.4f} max {max(sc):.4f} median {median(sc):.4f}; Ec/IE1 min {min(x[6] for x in sol):.4f} max {max(x[6] for x in sol):.4f}')
print()

# ================= PART E: one consolidated cross-level table (representatives)
print('PART E  cross-level view: size R, energy E, cycles = R E/(hbar c), cycles/(alpha/2), log12 of R/l_Planck, for hydrogen atom, representative atoms, molecules, solids')
rows = [('H atom Bohr, E=Ry', a0, Ry), ('r_e = alpha lam_e, E=m_e c^2 alpha ... (not used)', None, None)]
rows = [('H atom: R=a0, E=Ry', a0, Ry)]
for s in ['He', 'Li', 'C', 'Fe', 'Cs']:
    if s in Ad: rows.append((f'{s} atom: R_val, E=IE1', Ad[s][5], Ad[s][3]))
for f in ['H2', 'N2', 'O2', 'CO', 'HF', 'LiH', 'NaCl', 'Li2', 'F2']:
    x = next((d for d in dia if d[0] == f), None)
    if x: rows.append((f'{f} molecule: R=r_e, E=D0', x[1]*1e-10, x[2]))
for s in ['Li', 'Fe', 'C', 'Si']:
    x = next((d for d in sol if d[0] == s), None)
    if x: rows.append((f'{s} solid: R=r_ws, E=Ec', x[2], x[3]))
print(f'  {"level":34s} {"R m":>12s} {"E eV":>10s} {"cycles":>12s} {"cyc/(a/2)":>10s} {"log12 R/lP":>10s}')
for n, R, E in rows:
    print(f'  {n:34s} {R:12.4e} {E:10.4f} {cyc(R, E):12.6e} {cyc(R, E)/half:10.4f} {l12(R/lP):10.4f}')
print()

# ================= PART F: level-to-level ratios of the characteristic scales
print('PART F  ratios between levels (raw): lengths and energies for H atom -> H2 molecule -> Li solid, and the Fe peak; extents against lam_e')
def get(lst, name, idx): return next((d[idx] for d in lst if d[0] == name), None)
r_H2 = get(dia, 'H2', 1)*1e-10; D_H2 = get(dia, 'H2', 2)
r_Li = get(sol, 'Li', 2); E_Li = get(sol, 'Li', 3)
print(f'  H atom a0 = {a0:.6e} m, Ry = {Ry} eV;  H2 r_e = {r_H2:.6e} m, D0 = {D_H2:.6f} eV;  Li r_ws = {r_Li:.6e} m, Ec = {E_Li:.6f} eV')
print(f'  r_e(H2)/a0 = {r_H2/a0:.8f}   D0(H2)/Ry = {D_H2/Ry:.8f}   r_ws(Li)/a0 = {r_Li/a0:.6f}   Ec(Li)/Ry = {E_Li/Ry:.8f}')
print(f'  1/alpha = {1/al:.9f}; a0/lam_e = {a0/lam_e:.9f}; r_ws(Li)/lam_e = {r_Li/lam_e:.6f}; log12 of that = {l12(r_Li/lam_e):.6f}')
