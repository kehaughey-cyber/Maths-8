# VERSION 2 of size_energy_full.py (v1 stays as committed). Every cell is filled: sourced values are kept; each blank is filled by a stated formula of only R, mass and charge,
# and every cell carries a provenance flag: M = measured or sourced, C = computed from constants or a closed form, F = formal estimate. No fitting.
# Formal fills (used only where no sourced or conventionally computed value exists; B = the row's binding, m = the object's mass, R = its size, kin = (hbar c/R)^2/(2 m)):
#   binding  = 1/2 x (EM energy alpha Q1Q2 hbar c / R)                  [virial for a 1/R potential; Q1Q2 = 1 if the row carries no charge]
#   first excitation = (x^2 - pi^2) kin, x = 4.493409 (l=1 root of tan x = x)   [gap 1s -> 1p of a particle of mass m in a spherical box of radius R]
#   spin / fine splitting = B^2 / (8 m)                                  [equals the hydrogenic n=2 fine structure (Z alpha)^4 m c^2 / 32 when B = (Z alpha)^2 m c^2 / 2]
#   collective mode = (hbar c / R) sqrt(2 B / m)                          [harmonic oscillator with depth B at displacement R]
#   rotational = 2 kin                                                    [J = 0 -> 1 of a mass m on a ring of radius R, I = m R^2]
#   absent forces: EM with Q1Q2 = 1, strong with C_F = 4/3 and alpha_s: alpha_g1(0) = pi at and above the nucleon size, one-loop running below it, at every row.
# Run: py -3 -I -X utf8 -u explore/size_energy_full_v2.py   (writes maps/size_vs_energy_filled.xlsx and .csv, then verifies the formulas with an independent evaluator)
import csv, html, json, math, os, re
from math import sqrt, pi
from openpyxl import Workbook
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter as L
HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.join(HERE, 'data'); MAPS = os.path.join(HERE, '..', 'maps')
cm = 1.239841984e-4
# ---------------- sourced inputs from saved files (same as v1)
ame = {}
for line in open(os.path.join(DATA, 'ame2020_mass_1.mas20.txt')).read().split('\n'):
    if len(line) > 100 and line[14:19].strip().isdigit():
        try: ame[(int(line[14:19]), line[20:23].strip())] = (float(line[28:42]), float(line[54:67]))
        except Exception: pass
B12 = 12*ame[(12, 'C')][1]*1e3
lv = {}
for r in csv.DictReader(open(os.path.join(DATA, 'iaea_livechart_12C_levels.csv'))): lv[int(r['idx'])] = float(r['energy'])*1e3
EL = {e['symbol']: e for e in json.load(open(os.path.join(DATA, 'PeriodicTableJSON.json'), encoding='utf-8'))['elements']}
IE = [x/96.485332 for x in EL['C']['ionization_energies']]
def asd(fn):
    out = []
    for row in csv.reader(open(os.path.join(DATA, fn), encoding='utf-8'), delimiter='\t'):
        if len(row) > 4 and row[0] != 'Configuration':
            try: out.append(((row[0].strip('"'), row[1].strip('"')), row[2].strip('"'), float(row[4].strip('"'))))
            except ValueError: pass
    return out
def levels(fn):
    lev = [x for x in asd(fn) if x[1] != '---']
    ground = lev[0][0]
    ex1 = next(e for t, j, e in lev if t != ground)
    split = None
    for t in dict.fromkeys(x[0] for x in lev):
        js = sorted(x[2] for x in lev if x[0] == t)
        if len(js) >= 2: split = js[1] - js[0]; break
    return ex1, split
lim = {}
for fn, key in [('nist_asd_CI.txt', 'CI'), ('nist_asd_CII.txt', 'CII')]:
    for row in csv.reader(open(os.path.join(DATA, fn), encoding='utf-8'), delimiter='\t'):
        if len(row) > 4 and row[1].strip('"') == 'Limit': lim.setdefault(key, float(row[4].strip('"')))
IE[0] = lim['CI']; IE[1] = lim['CII']
ion = {k: levels('nist_asd_%s.txt' % k) for k in ['CI', 'CII', 'CIII', 'CIV', 'CV', 'CVI']}
rawh = open(os.path.join(DATA, 'cccbdb_enthalpy_formation_0K.html'), encoding='utf-8', errors='replace').read()
def txt(s): return html.unescape(re.sub(r'<[^>]+>', '', re.sub(r'<sub>(.*?)</sub>', r'\1', s, flags=re.I))).strip()
Hf = {}
for row in re.findall(r'<TR>(.*?)</TR>', rawh, flags=re.S | re.I):
    c_ = re.findall(r'<TD[^>]*>(.*?)</TD>', row, flags=re.S | re.I)
    if len(c_) >= 4:
        try: Hf[txt(c_[0])] = float(txt(c_[2]))
        except ValueError: pass
D_CO = (Hf['C'] + Hf['O'] - Hf['CO'])/96.485332; D_C2 = (2*Hf['C'] - Hf['C2'])/96.485332
# one-loop alpha_s at the tau scale (formal): m_Z -> m_b with nf=5, m_b -> Q with nf=4
def alpha_run(Q, a_mz=0.1180, mz=91.1876, mb=4.18):
    inv = 1/a_mz + (11 - 2*5/3)/(2*pi)*math.log(mb/mz)
    inv += (11 - 2*4/3)/(2*pi)*math.log(Q/mb)
    return 1/inv
Q_tau = 1.973269804e-7/1.1105e-16/1e9     # GeV
a_tau = alpha_run(Q_tau)
# ---------------- workbook scaffolding
wb = Workbook(); AR = 'Arial'
blue = Font(name=AR, color='0000FF'); blk = Font(name=AR); bold = Font(name=AR, bold=True); hdrfill = PatternFill('solid', fgColor='DDE6F0')
FILL = {'M': PatternFill('solid', fgColor='D9EAD3'), 'C': PatternFill('solid', fgColor='DDE6F0'), 'F': PatternFill('solid', fgColor='FCE5CD')}
ws = wb.active; ws.title = 'Energies (eV)'; wp = wb.create_sheet('Provenance'); wc = wb.create_sheet('Cycles'); wh = wb.create_sheet('Log10 eV (heat)'); wk = wb.create_sheet('Constants'); wn = wb.create_sheet('Sources and notes')
consts = [('hbar c (eV m)', 1.973269804e-7), ('alpha', 7.2973525693e-3), ('Rydberg (eV)', 13.605693123), ('Bohr radius a0 (m)', 5.29177210903e-11), ('Planck length (m)', 1.616255e-35),
          ('k_B (eV/K)', 8.617333262e-5), ('T ambient (K)', 298.15), ('T CMB (K)', 2.7255), ('G (m^3 kg^-1 s^-2)', 6.67430e-11), ('e (J per eV)', 1.602176634e-19), ('c (m/s)', 299792458.0),
          ('sin^2 theta_W (MS-bar, M_Z)', 0.23122), ('m_W c^2 (eV)', 80.3692e9), ('C_F (SU(3))', 4/3), ('alpha_g1(Q^2=0) = pi', pi), ('alpha_s one-loop at the tau scale (formal)', a_tau),
          ('m_u (eV, MS-bar 2 GeV)', 2.16e6), ('m_d (eV, MS-bar 2 GeV)', 4.70e6),
          ('m_e (eV)', 510998.95), ('m_mu (eV)', 105.6583755e6), ('m_tau (eV)', 1776.93e6), ('m_p (eV)', 938.27208816e6), ('atom 12 u c^2 (eV)', 12*931494102.42), ('12C nucleus mass (eV)', 12*931494102.42 - 6*510998.95),
          ('N atoms in the gram', 5.0184506350676e22), ('Z of carbon', 6.0), ('x(1p) root of tan x = x', 4.493409457909064)]
srcs = {'sin^2 theta_W (MS-bar, M_Z)': 'PDG value, recalled (not from a saved file)', 'm_W c^2 (eV)': 'PDG 2024 gauge/Higgs table (saved)', 'alpha_g1(Q^2=0) = pi': 'Deur, Brodsky, de Teramond 2016 eq 4.4 (saved)',
        'alpha_s one-loop at the tau scale (formal)': 'one-loop from alpha_s(m_Z) = 0.1180 (PDG 2024 QCD review, saved), nf=5 to 4.18 GeV then nf=4; approximation', 'm_u (eV, MS-bar 2 GeV)': 'PDG 2024 quarks (saved)', 'm_d (eV, MS-bar 2 GeV)': 'PDG 2024 quarks (saved)',
        'x(1p) root of tan x = x': 'first nontrivial root, l=1 spherical Bessel zero'}
wk['A1'] = 'constant'; wk['B1'] = 'value'; wk['C1'] = 'source'
K = {}
for i, (a, b) in enumerate(consts, start=2):
    wk.cell(i, 1, a).font = blk; wk.cell(i, 2, b).font = blue; wk.cell(i, 3, srcs.get(a, 'CODATA 2018 / PDG 2024 / standard')).font = blk; K[a] = 'Constants!$B$%d' % i
for c_ in 'ABC': wk[c_ + '1'].font = bold
wk.column_dimensions['A'].width = 40; wk.column_dimensions['B'].width = 20; wk.column_dimensions['C'].width = 70
(hbarc, alpha, Ry, a0, lP, kB, Tamb, Tcmb, G, eVJ, c, s2w, mW, CF, ag1, atau, mu_q, md_q, me, mmu, mtau, mp, mAtom, mNuc, Nat, Zc, x1p) = [K[a] for a, _ in consts]
cols = [('R', 'Size R (m)'), ('p12', 'p12 above Planck length'), ('m', 'Mass of the object m (eV)'), ('m2', 'Partner mass (eV)'), ('QQ', 'Charge product Q1Q2 (e^2); 0 = neutral'),
        ('hcR', 'hbar c / R (eV)'), ('kin', 'Confinement kinetic (hbar c/R)^2 / 2 m (eV)'),
        ('rest', 'Rest energy m c^2 (eV)'), ('grav', 'Gravity G m m2 / R (eV)'),
        ('em', 'EM  alpha Q1Q2 hbar c / R (eV); Q1Q2 = 1 if neutral'), ('strong', 'Strong  C_F alpha_s hbar c / R (eV)'), ('weak', 'Weak  alpha_W hbar c exp(-R m_W c/hbar c)/R (eV)'), ('weakL', 'Weak, log10 eV (no underflow)'),
        ('Bf', 'Binding used by formal fills B (eV)'),
        ('bind', 'Binding / dissociation / cohesion total (eV)'), ('exc', 'First excitation (eV)'), ('spin', 'Spin / fine / isospin splitting (eV)'), ('coll', 'Collective mode: vibration, phonon, octupole (eV)'), ('rot', 'Rotational (eV)'),
        ('kT', 'Ambient kT, 298.15 K (eV)'), ('kTc', 'CMB kT, 2.7255 K (eV)')]
idx = {k: i + 2 for i, (k, _) in enumerate(cols)}
nc = len(cols) + 2
A = lambda k, r: '%s%d' % (L(idx[k]), r)
F = 'F'
rows = [
 dict(name='tau, free (Compton length)', R=('v', 1.1105e-16), m=mtau, m2=mtau, QQ=1, bind=F, exc=F, spin=F, coll=F, rot=F, strongR='tau',
      note='R = hbar/(m c). Structure cells are formal (pointlike). For reference the mass gap to the next heavier lepton is: none known.'),
 dict(name='nucleon (proton at r_p)', R=('v', 0.84075e-15), m=mp, m2=mp, QQ=1, bind='=%s-(2*%s+%s)' % (mp, mu_q, md_q), exc=1440e6-938.27208816e6, spin=939.56542052e6-938.27208816e6, coll=139.57039e6, rot=1232e6-938.27208816e6,
      note='r_p CODATA 2022. bind = m_p c^2 minus bare 2u+d (MS-bar, scheme-dependent). exc = N(1440) BW centre - m_p (PDG). spin = m_n - m_p (isospin). coll = pion mass (PDG). rot = Delta(1232) - N, 1232 MeV RECALLED. strong: alpha_g1 = pi (measured effective charge).'),
 dict(name='muon, free (Compton length)', R=('v', 1.8676e-15), m=mmu, m2=mmu, QQ=1, bind=F, exc=F, spin=F, coll=F, rot=F,
      note='as tau. For reference the gap to the next heavier lepton is m_tau - m_mu = 1.6713 GeV.'),
 dict(name='12C nucleus (charge radius)', R=('v', 2.4702e-15), m=mNuc, m2=mNuc, QQ=36, bind=B12, exc=lv[1], spin=lv[10], coll=lv[3], rot=lv[1],
      note='bind = 12 x B/A (AME2020). exc = 2+ level; spin = first 1+ level (12.71 MeV); coll = 3- level; rot = the 2+ level (same as exc); levels from ENSDF via IAEA livechart. QQ = Z^2 = 36. strong is formal here (nucleons are colour singlets; confinement makes the Coulomb form invalid beyond ~1 fm).'),
 dict(name='tau on 12C, 1s (hydrogenic, point nucleus)', R=('hyd', 1776.93e6), m=mtau, m2=mNuc, QQ='=%s' % Zc, bind='hyd', exc='hyd_e', spin='hyd_f', coll=F, rot=F,
      note='Z alpha mu c^2 formulas, nonrelativistic, point nucleus: the orbit (1.19 r_ch) lies inside the nucleus so this is NOT a physical level.'),
 dict(name='muon on 12C, 1s (hydrogenic, point nucleus)', R=('hyd', 105.6583755e6), m=mmu, m2=mNuc, QQ='=%s' % Zc, bind='hyd', exc='hyd_e', spin='hyd_f', coll=F, rot=F,
      note='hydrogenic: E1s = (Z alpha)^2 mu c^2 / 2, 2p-1s = 3/4 E1s, n=2 fine structure (Z alpha)^4 mu c^2 / 32, reduced mass; finite-size effects ignored.'),
 dict(name='electron, free (Compton length)', R=('v', 3.8616e-13), m=me, m2=me, QQ=1, bind=F, exc=F, spin=F, coll=F, rot=F,
      note='as tau. For reference the gap to the next heavier lepton is m_mu - m_e = 105.15 MeV.'),
 dict(name='C5+ 1s (IE6)', R=('ie', 6, 1), m=me, m2=mAtom, bind='sumIE6', exc=ion['CVI'][0], spin=ion['CVI'][1], coll=F, rot=F, note='hydrogenic size 1 a0/sqrt(IE/Ry), charge felt Z_eff = n sqrt(IE/Ry). exc, spin: NIST ASD C VI (2p - 1s, 2p3/2 - 2p1/2).'),
 dict(name='C4+ 1s2 (IE5)', R=('ie', 5, 1), m=me, m2=mAtom, bind='sumIE5', exc=ion['CV'][0], spin=ion['CV'][1], coll=F, rot=F, note='exc, spin: NIST ASD C V (1s2s 3S1; 1s2p 3P splitting).'),
 dict(name='C3+ (IE4)', R=('ie', 4, 2), m=me, m2=mAtom, bind='sumIE4', exc=ion['CIV'][0], spin=ion['CIV'][1], coll=F, rot=F, note='exc, spin: NIST ASD C IV (2p; 2p3/2 - 2p1/2).'),
 dict(name='C2+ (IE3)', R=('ie', 3, 2), m=me, m2=mAtom, bind='sumIE3', exc=ion['CIII'][0], spin=ion['CIII'][1], coll=F, rot=F, note='exc, spin: NIST ASD C III (2s2p 3P0; 3P1 - 3P0).'),
 dict(name='C+ (IE2)', R=('ie', 2, 2), m=me, m2=mAtom, bind='sumIE2', exc=ion['CII'][0], spin=ion['CII'][1], coll=F, rot=F, note='IE2 = C II series limit (NIST ASD). exc: 2s2p2 4P1/2; spin: 2P3/2 - 2P1/2 (NIST ASD C II).'),
 dict(name='CO molecule (r_e)', R=('v', 1.128e-10), m=me, m2=mAtom, QQ=0, bind=D_CO, exc=48686.7*cm, spin=F, coll=2169.756*cm, rot=2*1.931602*cm,
      note='r_e, omega_e, B_e: CCCBDB. bind = D0 from 0 K enthalpies. exc = a3Pi Te 48686.7 cm^-1 (NIST WebBook). spin: A not listed on the page, formal fill. QQ = 0: neutral.'),
 dict(name='C valence electron (IE1)', R=('ie', 1, 2), m=me, m2=mAtom, bind='sumIE1', exc=ion['CI'][0], spin=ion['CI'][1], coll=F, rot=F, note='IE1 = C I series limit (NIST ASD). exc: 1D2; spin: 3P1 - 3P0 (NIST ASD C I).'),
 dict(name='C2 molecule (r_e)', R=('v', 1.243e-10), m=me, m2=mAtom, QQ=0, bind=D_C2, exc=716.24*cm, spin=F, coll=1855.066*cm, rot=2*1.820053*cm,
      note='r_e CCCBDB; bind = 2 Hfg(C) - Hfg(C2) at 0 K; exc = a3Piu Te 716.24 cm^-1 (NIST WebBook); omega_e, B_e CCCBDB. spin formal.'),
 dict(name='diamond C-C bond', R=('v', 3.56683e-10*sqrt(3)/4), m=me, m2=mAtom, QQ=0, bind='=711.2/96.485332/2', exc=5.47, spin=0.006, coll=0.16037239, rot=F,
      note='bind = Ec/2. exc = indirect band gap 5.47 eV (Ioffe NSM lists 5.46-5.6; 5.47 recalled). spin = valence-band spin-orbit 6 meV (Ioffe; disputed, ~13 meV ab initio). coll = Debye k Theta_D from Cp(298.16 K).'),
 dict(name='diamond lattice constant', R=('v', 3.56683e-10), m=me, m2=mAtom, QQ=0, bind='=711.2/96.485332', exc=5.47, spin=0.006, coll=0.16037239, rot=F, note='bind = Ec (cohesion per atom); others as the C-C row.'),
 dict(name='the gram (equal-volume sphere)', R=('v', 4.0808074e-3), m='=1e-3*%s^2/%s' % (c, eVJ), m2='=1e-3*%s^2/%s' % (c, eVJ), QQ=0, bind='gram', exc=5.47, spin=F, coll='=43.636776/%s' % eVJ, rot=F,
      note='bind = N x (nuclear B + all six ionization energies + Ec). exc = band gap. coll = Debye thermal energy of the gram at 298.15 K (43.64 J). QQ = 0: net neutral. spin, rot formal with m = M.'),
]
mNuc_ = 12*931494102.42 - 6*510998.95
def size_key(r):
    t = r['R']
    if t[0] == 'v': return t[1]
    if t[0] == 'hyd': return 1.973269804e-7/((t[1]*mNuc_/(t[1]+mNuc_)) * 6*7.2973525693e-3)
    return t[2]*5.29177210903e-11/sqrt(IE[t[1]-1]/13.605693123)
rows.sort(key=size_key)
hdr = 3; first = hdr + 1
rowof = {r['name']: first + i for i, r in enumerate(rows)}
ws.cell(1, 1, 'Size (row) and the energies at that size (columns); eV. Cell colour = provenance: green measured/sourced, blue computed, orange formal estimate (see Sources and notes).').font = bold
ws.cell(hdr, 1, 'Size').font = bold; ws.cell(hdr, 1).fill = hdrfill
for k, h in cols:
    x = ws.cell(hdr, idx[k], h); x.font = bold; x.fill = hdrfill; x.alignment = Alignment(wrap_text=True, vertical='top')
ws.cell(hdr, nc, 'What the numbers are / source').font = bold; ws.cell(hdr, nc).fill = hdrfill
# ionization-energy block on Constants
base = len(consts) + 4
wk.cell(base - 1, 1, 'ionization energies of carbon (eV)').font = bold
srcie = {1: 'NIST ASD C I series limit', 2: 'NIST ASD C II series limit'}
IEC = {}
for k in range(1, 7):
    wk.cell(base + k - 1, 1, 'IE%d' % k).font = blk; wk.cell(base + k - 1, 2, IE[k - 1]).font = blue; wk.cell(base + k - 1, 3, srcie.get(k, 'PeriodicTableJSON (Wikipedia-derived), kJ/mol / 96.485332')).font = blk
    IEC[k] = 'Constants!$B$%d' % (base + k - 1)
prov = {}
for i, r in enumerate(rows):
    rr = first + i
    ws.cell(rr, 1, r['name']).font = blk
    kind = r['R'][0]
    def put(k, v, pv, inp=False):
        x = ws.cell(rr, idx[k], v)
        x.font = blue if inp else blk
        x.fill = FILL[pv]; x.number_format = '0.000E+00'; prov[(rr, k)] = pv
        return x
    for k in ('m', 'm2'):
        v = r[k]
        if isinstance(v, str) and v.startswith('Constants'): put(k, '=' + v, 'C')
        elif isinstance(v, str): put(k, v, 'C')
        else: put(k, v, 'M', True)
    if kind == 'v': put('R', r['R'][1], 'M', True)
    elif kind == 'hyd': put('R', '=%s/(%s*%s/(%s+%s)*%s*%s)' % (hbarc, A('m', rr), A('m2', rr), A('m', rr), A('m2', rr), Zc, alpha), 'C')
    else: put('R', '=%d*%s/SQRT(%s/%s)' % (r['R'][2], a0, IEC[r['R'][1]], Ry), 'C')
    if kind == 'ie': put('QQ', '=%d*SQRT(%s/%s)' % (r['R'][2], IEC[r['R'][1]], Ry), 'C')
    else:
        v = r.get('QQ', 0)
        put('QQ', v, 'C' if isinstance(v, str) else 'M', not isinstance(v, str))
    put('p12', '=LOG(%s/%s)/LOG(12)' % (A('R', rr), lP), 'C').number_format = '0.000'
    put('hcR', '=%s/%s' % (hbarc, A('R', rr)), 'C')
    put('kin', '=%s^2/(2*%s)' % (A('hcR', rr), A('m', rr)), 'C')
    put('rest', '=%s' % A('m', rr), 'C')
    put('grav', '=%s*%s*%s*%s/(%s*%s^4)' % (G, eVJ, A('m', rr), A('m2', rr), A('R', rr), c), 'C')
    neutral = (r.get('QQ', 0) == 0) and kind != 'ie'
    put('em', '=%s*IF(%s=0,1,%s)*%s' % (alpha, A('QQ', rr), A('QQ', rr), A('hcR', rr)), 'F' if neutral else 'C')
    if r.get('strongR') == 'tau': put('strong', '=%s*%s*%s' % (CF, atau, A('hcR', rr)), 'F')
    else: put('strong', '=%s*%s*%s' % (CF, ag1, A('hcR', rr)), 'C' if r['name'].startswith('nucleon') else 'F')
    put('weak', '=IF(%s>-300,10^%s,"see log10")' % (A('weakL', rr), A('weakL', rr)), 'C')
    put('weakL', '=LN(%s/%s*%s)/LN(10)-%s*%s/%s/LN(10)' % (alpha, s2w, A('hcR', rr), A('R', rr), mW, hbarc), 'C').number_format = '0.00'
    # Bf: binding used for formal fills
    b = r['bind']
    if kind == 'ie': put('Bf', '=' + IEC[r['R'][1]], 'C')
    else: put('Bf', '=%s' % A('bind', rr), 'C')
    # bound-state columns
    if b == 'hyd': put('bind', '=(%s*%s)^2*%s*%s/(%s+%s)/2' % (Zc, alpha, A('m', rr), A('m2', rr), A('m', rr), A('m2', rr)), 'C')
    elif isinstance(b, str) and b.startswith('sumIE'): put('bind', '=' + '+'.join(IEC[k] for k in range(int(b[5:]), 7)), 'C')
    elif b == 'gram': put('bind', 0, 'C')                                  # rewritten below
    elif b == F: put('bind', '=0.5*%s' % A('em', rr), 'F')
    else: put('bind', b, 'C' if isinstance(b, str) else 'M', not isinstance(b, str))
    e = r['exc']
    if e == F: put('exc', '=(%s^2-3.141592653589793^2)*%s' % (x1p, A('kin', rr)), 'F')
    elif e == 'hyd_e': put('exc', '=0.75*%s' % A('bind', rr), 'C')
    else: put('exc', e, 'M', True)
    sp = r['spin']
    if sp == F: put('spin', '=%s^2/(8*%s)' % (A('Bf', rr), A('m', rr)), 'F')
    elif sp == 'hyd_f': put('spin', '=(%s*%s)^4*%s*%s/(%s+%s)/32' % (Zc, alpha, A('m', rr), A('m2', rr), A('m', rr), A('m2', rr)), 'C')
    else: put('spin', sp, 'M', True)
    cl = r['coll']
    if cl == F: put('coll', '=%s*SQRT(2*%s/%s)' % (A('hcR', rr), A('Bf', rr), A('m', rr)), 'F')
    else: put('coll', cl, 'C' if isinstance(cl, str) else 'M', not isinstance(cl, str))
    rt = r['rot']
    if rt == F: put('rot', '=2*%s' % A('kin', rr), 'F')
    else: put('rot', rt, 'M', True)
    put('kT', '=%s*%s' % (kB, Tamb), 'C'); put('kTc', '=%s*%s' % (kB, Tcmb), 'C')
    ws.cell(rr, nc, r['note']).font = blk
# gram binding (references the nucleus and diamond rows)
gram = rowof['the gram (equal-volume sphere)']; nuc = rowof['12C nucleus (charge radius)']; dia = rowof['diamond lattice constant']
x = ws.cell(gram, idx['bind'], '=%s*(%s+%s+%s)' % (Nat, A('bind', nuc), '+'.join(IEC[k] for k in range(1, 7)), A('bind', dia))); x.font = blk; x.number_format = '0.000E+00'
ws.freeze_panes = ws.cell(first, 2); ws.column_dimensions['A'].width = 44
for k, _ in cols: ws.column_dimensions[L(idx[k])].width = 17
ws.column_dimensions[L(nc)].width = 100; ws.row_dimensions[hdr].height = 62
# provenance sheet
wp.cell(1, 1, 'Provenance of each cell on the Energies sheet: M measured/sourced, C computed (constants or a closed form), F formal estimate (formula of R, mass, charge only)').font = bold
wp.cell(hdr, 1, 'Size').font = bold
for k, h in cols:
    wp.cell(hdr, idx[k], h).font = bold; wp.cell(hdr, idx[k]).alignment = Alignment(wrap_text=True, vertical='top')
for i in range(len(rows)):
    rr = first + i; wp.cell(rr, 1, "='Energies (eV)'!A%d" % rr).font = blk
    for k, _ in cols:
        x = wp.cell(rr, idx[k], prov[(rr, k)]); x.fill = FILL[prov[(rr, k)]]; x.alignment = Alignment(horizontal='center'); x.font = blk
wp.column_dimensions['A'].width = 44
for k, _ in cols: wp.column_dimensions[L(idx[k])].width = 12
wp.row_dimensions[hdr].height = 62
# cycles and heat
skip = ('m', 'm2', 'QQ', 'Bf')
wc.cell(1, 1, 'Cycles = E / (hbar c / R) for every energy column; the weak column uses its log10 (cycles shown as log10 cycles = weak log10 eV - log10 hbar c / R)').font = bold
wh.cell(1, 1, 'log10 of each energy in eV (weak column from its analytic log10; colour scale per sheet)').font = bold
for sh, title in ((wc, 'cycles'), (wh, 'log10 eV')):
    sh.cell(hdr, 1, 'Size').font = bold; sh.cell(hdr, 1).fill = hdrfill
    for k, h in cols:
        if k in skip or k == 'weak': continue
        x = sh.cell(hdr, idx[k], h if k in ('R', 'p12', 'weakL') else h.replace('(eV)', '(%s)' % title)); x.font = bold; x.fill = hdrfill; x.alignment = Alignment(wrap_text=True, vertical='top')
    for i in range(len(rows)):
        rr = first + i
        sh.cell(rr, 1, "='Energies (eV)'!A%d" % rr).font = blk
        for k, _ in cols:
            if k in skip or k == 'weak': continue
            src = "'Energies (eV)'!%s" % A(k, rr)
            if k in ('R', 'p12', 'weakL'): f = '=' + src
            elif sh is wc: f = '=%s/%s' % (src, "'Energies (eV)'!%s" % A('hcR', rr))
            else: f = '=LOG10(%s)' % src
            x = sh.cell(rr, idx[k], f); x.font = blk; x.number_format = '0.000' if k == 'p12' else ('0.000E+00' if sh is wc else '0.00')
    sh.freeze_panes = sh.cell(first, 2); sh.column_dimensions['A'].width = 44; sh.row_dimensions[hdr].height = 62
    for k, _ in cols: sh.column_dimensions[L(idx[k])].width = 15
heatcols = [k for k, _ in cols if k not in ('R', 'p12', 'm', 'm2', 'QQ', 'Bf', 'weak')]
rng = '%s%d:%s%d' % (L(idx[heatcols[0]]), first, L(idx[heatcols[-1]]), first + len(rows) - 1)
wh.conditional_formatting.add(rng, ColorScaleRule(start_type='num', start_value=-12, start_color='F7FBFF', mid_type='num', mid_value=0, mid_color='9ECAE1', end_type='num', end_value=11, end_color='08306B'))
notes = ['Size versus energy, leptons to the gram, every cell filled. Rows are sizes (the object whose size it is); columns are kinds of energy present at every scale: size (hbar c/R, confinement), mass (rest, gravity), charge (EM, strong, weak), bound-state (binding, excitation, spin, collective, rotational) and ambient (kT, CMB kT).',
 'Provenance: green M = measured/sourced; blue C = computed from constants or a closed form (hydrogenic formulas, sums of ionization energies, hbar c/R and the like); orange F = formal estimate. See the Provenance sheet cell by cell.',
 'Formal fills use only R, the object mass m, the charge product and the row binding B: binding = 1/2 EM energy (virial for a 1/R potential); first excitation = (x^2 - pi^2) kin with x = 4.4934 (1s to 1p of a mass m in a spherical box of radius R); spin/fine = B^2/(8 m) (equals the hydrogenic n=2 fine structure when B = (Z alpha)^2 m c^2/2); collective = (hbar c/R) sqrt(2 B/m); rotational = 2 kin (J=0 to 1, I = m R^2).',
 'Absent forces are evaluated formally at every size: EM with Q1Q2 = 1 where the row is neutral; strong with C_F = 4/3 and alpha_g1(0) = pi at and above the nucleon size (measured effective charge, near-flat), one-loop running only for the tau row (Q = 1.78 GeV, an approximation); weak with alpha_W = alpha/sin^2 theta_W and the Yukawa cutoff at hbar/(m_W c).',
 'Limits of the formal fills: they are non-relativistic. Where hbar c/R is comparable to or above m c^2 (the free-lepton rows at their Compton length) the box gap, rotational and collective fills exceed the rest energy; they are shown as stated by the formulas, not as physical energies.',
 'The weak energy falls below the double-precision floor (1e-308) from the muon scale upward: the Energies cell then reads see log10, and the analytic log10 column and the heat sheet carry the value.',
 'These are estimates by construction, not data: a lepton has no colour, an atom has no strong pair energy at its radius, a free lepton has no spin splitting. The formal entries put every column on every row so the ratios across scales can be read; they are not claims about the physics at those sizes.',
 'Recalled, not in a saved file: sin^2 theta_W = 0.23122; Delta(1232) = 1232 MeV; diamond band gap 5.47 eV (Ioffe NSM lists 5.46-5.6); diamond valence-band spin-orbit 6 meV (disputed, ~13 meV). IE3-IE6 are Wikipedia-derived (PeriodicTableJSON).',
 'tau/muon on 12C are point-nucleus hydrogenic formulas, not measured levels; the tau orbit is inside the nucleus. C5+ to C I rows use NIST ASD levels (first level of the first term above the ground term; first J-splitting of the lowest multiplet).',
 'Sources saved in explore/data/: AME2020, ENSDF 12C (IAEA livechart CSV), NIST ASD C I-C VI, CCCBDB, PDG 2024 (leptons, quarks, gauge/Higgs, mesons, baryons, QCD review), Deur et al. 2016, CODATA 2022 r_p, NIST WebBook (CO, C2 states).',
 'No LibreOffice on this machine: formulas carry no cached values until Excel opens the file; the CSV and the independent evaluator in the builder carry the numbers. No rule is proposed; the sheet is for examination.']
for i, t in enumerate(notes, start=1): wn.cell(i, 1, t).font = blk
wn.column_dimensions['A'].width = 200
OUT = os.path.join(MAPS, 'size_vs_energy_filled.xlsx'); wb.save(OUT)
# ---------------- independent evaluator of the saved formulas -> CSV
from openpyxl import load_workbook
wb2 = load_workbook(OUT); cache = {}
def getv(sheet, ref):
    key = (sheet, ref.replace('$', ''))
    if key in cache: return cache[key]
    v = wb2[sheet][key[1]].value
    if isinstance(v, str) and v.startswith('='): v = evalf(sheet, v[1:])
    cache[key] = v; return v
def evalf(sheet, f):
    def ref(m_):
        shn = (m_.group(1).rstrip('!').strip("'") if m_.group(1) else sheet)
        return repr(getv(shn, m_.group(2)))
    f2 = re.sub(r"((?:'[^']+'|[A-Za-z]+)!)?(\$?[A-Z]{1,2}\$?\d+)", ref, f)
    f2 = f2.replace('^', '**').replace('SQRT(', 'sqrt(').replace('LN(', 'ln(').replace('LOG(', 'log(')
    f2 = f2.replace('IF(', 'iff(')
    f2 = re.sub(r'(?<![<>=!])=(?!=)', '==', f2)
    env = dict(sqrt=sqrt, ln=math.log, log=math.log, iff=lambda a, b, c_=None: b if a else c_)
    return eval(f2, {'__builtins__': {}}, env)
vals = []
for i in range(len(rows)):
    rr = first + i; rec = {'name': rows[i]['name']}
    for k, h in cols:
        v = wb2['Energies (eV)'].cell(rr, idx[k]).value
        if isinstance(v, str) and v.startswith('='):
            try: v = evalf('Energies (eV)', v[1:])
            except Exception as ex: v = 'ERR:%s' % ex
        cache[('Energies (eV)', '%s%d' % (L(idx[k]), rr))] = v
        rec[k] = v
    vals.append(rec)
errs = [(r['name'], k) for r in vals for k, _ in cols if isinstance(r[k], str) and r[k].startswith('ERR')]
print('formula errors in evaluator:', errs)
numcols = [k for k, _ in cols]
with open(os.path.join(MAPS, 'size_vs_energy_filled.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['size'] + [h for _, h in cols] + ['prov: ' + h for _, h in cols])
    for i, r in enumerate(vals):
        rr = first + i
        w.writerow([r['name']] + [repr(r[k]) if not isinstance(r[k], str) else r[k] for k in numcols] + [prov[(rr, k)] for k in numcols])
nb = 6
print('saved', os.path.abspath(OUT))
cnt = {'M': 0, 'C': 0, 'F': 0}
for (rr, k), p in prov.items(): cnt[p] += 1
print('provenance counts over all cells:', cnt, '; empty cells:', sum(1 for r in vals for k in numcols if r[k] in (None, '')))
show = ['hcR', 'kin', 'grav', 'em', 'strong', 'weakL', 'bind', 'exc', 'spin', 'coll', 'rot']
print('%-46s %9s %7s ' % ('size', 'R (m)', 'p12') + ' '.join('%9s' % k for k in show))
for i, r in enumerate(vals):
    rr = first + i
    print('%-46s %9.3e %7.3f ' % (r['name'], r['R'], r['p12']) + ' '.join(('%9.2e' % r[k] if k != 'weakL' else '%9.1f' % r[k]) + prov[(rr, k)] if isinstance(r[k], (int, float)) else '%9s' % r[k] for k in show))
