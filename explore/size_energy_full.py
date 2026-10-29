# Size versus energy across scales, leptons to the gram: rows are sizes, columns are the kinds of energy present at every scale (size, mass, charge x3, bound-state, ambient).
# New file (the carbon-only sheet carbon_size_vs_energy.xlsx is left as committed). Nothing fitted; no rule proposed.
# Every cell is one of: a number (sourced input in blue, or a live formula in black); 0 (shaded) = the interaction or structure is absent at this size by construction;
# 'n/s' (shaded) = exists but no sourced value was obtained. Legend and counts are on the Sources and notes sheet.
# Run: py -3 -I -X utf8 -u explore/size_energy_full.py   (writes maps/size_vs_energy_full.xlsx and .csv; then verifies the formulas with an independent evaluator)
import csv, html, json, math, os, re
from math import sqrt, pi
from openpyxl import Workbook
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter as L
HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.join(HERE, 'data'); MAPS = os.path.join(HERE, '..', 'maps')
cm = 1.239841984e-4
# ---------------- sourced inputs from saved files
ame = {}
for line in open(os.path.join(DATA, 'ame2020_mass_1.mas20.txt')).read().split('\n'):
    if len(line) > 100 and line[14:19].strip().isdigit():
        try: ame[(int(line[14:19]), line[20:23].strip())] = (float(line[28:42]), float(line[54:67]))
        except Exception: pass
mex = lambda A, s: ame[(A, s)][0]*1e3
Sn = mex(11, 'C') + mex(1, 'n') - mex(12, 'C'); Sp = mex(11, 'B') + mex(1, 'H') - mex(12, 'C'); Sa = mex(8, 'Be') + mex(4, 'He') - mex(12, 'C')
B12 = 12*ame[(12, 'C')][1]*1e3
lv = {}
for r in csv.DictReader(open(os.path.join(DATA, 'iaea_livechart_12C_levels.csv'))): lv[int(r['idx'])] = float(r['energy'])*1e3
EL = {e['symbol']: e for e in json.load(open(os.path.join(DATA, 'PeriodicTableJSON.json'), encoding='utf-8'))['elements']}
IE = [x/96.485332 for x in EL['C']['ionization_energies']]
def asd(fn):
    out = []
    for row in csv.reader(open(os.path.join(DATA, fn), encoding='utf-8'), delimiter='	'):
        if len(row) > 4 and row[0] != 'Configuration':
            try: out.append(((row[0].strip('"'), row[1].strip('"')), row[2].strip('"'), float(row[4].strip('"'))))
            except ValueError: pass
    return out
def levels(fn):
    lev = [x for x in asd(fn) if x[1] != '---']                  # (config, term), J, energy; drop series limits
    ground = lev[0][0]
    ex1 = next(e for t, j, e in lev if t != ground)               # lowest level of the first (configuration, term) above the ground one
    split = None
    for t in dict.fromkeys(x[0] for x in lev):                    # in energy order of first appearance
        js = sorted(x[2] for x in lev if x[0] == t)
        if len(js) >= 2: split = js[1] - js[0]; break           # first J-splitting of the lowest multiplet
    return ex1, split, lev
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
    c = re.findall(r'<TD[^>]*>(.*?)</TD>', row, flags=re.S | re.I)
    if len(c) >= 4:
        try: Hf[txt(c[0])] = float(txt(c[2]))
        except ValueError: pass
D_CO = (Hf['C'] + Hf['O'] - Hf['CO'])/96.485332; D_C2 = (2*Hf['C'] - Hf['C2'])/96.485332
# ---------------- workbook scaffolding
wb = Workbook(); AR = 'Arial'
blue = Font(name=AR, color='0000FF'); blk = Font(name=AR); bold = Font(name=AR, bold=True); grey = PatternFill('solid', fgColor='E8E8E8'); hdrfill = PatternFill('solid', fgColor='DDE6F0')
ws = wb.active; ws.title = 'Energies (eV)'; wc = wb.create_sheet('Cycles'); wh = wb.create_sheet('Log10 eV (heat)'); wk = wb.create_sheet('Constants'); wn = wb.create_sheet('Sources and notes')
consts = [('hbar c (eV m)', 1.973269804e-7), ('alpha', 7.2973525693e-3), ('Rydberg (eV)', 13.605693123), ('Bohr radius a0 (m)', 5.29177210903e-11), ('Planck length (m)', 1.616255e-35),
          ('k_B (eV/K)', 8.617333262e-5), ('T ambient (K)', 298.15), ('T CMB (K)', 2.7255), ('G (m^3 kg^-1 s^-2)', 6.67430e-11), ('e (J per eV)', 1.602176634e-19), ('c (m/s)', 299792458.0),
          ('sin^2 theta_W (MS-bar, M_Z)', 0.23122), ('m_W c^2 (eV)', 80.3692e9), ('C_F (SU(3))', 4/3), ('alpha_g1(Q^2=0) = pi', pi), ('m_u (eV, MS-bar 2 GeV)', 2.16e6), ('m_d (eV, MS-bar 2 GeV)', 4.70e6),
          ('m_e (eV)', 510998.95), ('m_mu (eV)', 105.6583755e6), ('m_tau (eV)', 1776.93e6), ('m_p (eV)', 938.27208816e6), ('atom 12 u c^2 (eV)', 12*931494102.42), ('12C nucleus mass (eV)', 12*931494102.42 - 6*510998.95),
          ('N atoms in the gram', 5.0184506350676e22), ('Z of carbon', 6.0)]
srcs = {'sin^2 theta_W (MS-bar, M_Z)': 'PDG value, recalled (not from a saved file)', 'm_W c^2 (eV)': 'PDG 2024 gauge/Higgs table (saved)', 'alpha_g1(Q^2=0) = pi': 'Deur, Brodsky, de Teramond 2016 eq 4.4 (saved)',
        'm_u (eV, MS-bar 2 GeV)': 'PDG 2024 quarks (saved)', 'm_d (eV, MS-bar 2 GeV)': 'PDG 2024 quarks (saved)'}
wk['A1'] = 'constant'; wk['B1'] = 'value'; wk['C1'] = 'source'
K = {}
for i, (a, b) in enumerate(consts, start=2):
    wk.cell(i, 1, a).font = blk; wk.cell(i, 2, b).font = blue; wk.cell(i, 3, srcs.get(a, 'CODATA 2018 / PDG 2024 / standard')).font = blk; K[a] = 'Constants!$B$%d' % i
for c_ in 'ABC': wk[c_ + '1'].font = bold
wk.column_dimensions['A'].width = 32; wk.column_dimensions['B'].width = 20; wk.column_dimensions['C'].width = 48
hbarc, alpha, Ry, a0, lP, kB, Tamb, Tcmb, G, eVJ, c, s2w, mW, CF, ag1, mu_q, md_q, me, mmu, mtau, mp, mAtom, mNuc, Nat, Zc = [K[a] for a, _ in consts]
cols = [('R', 'Size R (m)'), ('p12', 'p12 above Planck length'), ('m', 'Mass of the object m (eV)'), ('m2', 'Partner mass (eV)'), ('QQ', 'Charge product Q1Q2 (e^2)'),
        ('hcR', 'hbar c / R (eV)'), ('kin', 'Confinement kinetic (hbar c/R)^2 / 2 m (eV)'),
        ('rest', 'Rest energy m c^2 (eV)'), ('grav', 'Gravity G m m2 / R (eV)'),
        ('em', 'EM  alpha Q1Q2 hbar c / R (eV)'), ('strong', 'Strong  C_F alpha_g1 hbar c / R (eV)'), ('weak', 'Weak  alpha_W hbar c exp(-R m_W c/hbar c)/R (eV)'),
        ('bind', 'Binding / dissociation / cohesion total (eV)'), ('exc', 'First excitation (eV)'), ('spin', 'Spin / fine / isospin splitting (eV)'), ('coll', 'Collective mode: vibration, phonon, octupole (eV)'), ('rot', 'Rotational (eV)'),
        ('kT', 'Ambient kT, 298.15 K (eV)'), ('kTc', 'CMB kT, 2.7255 K (eV)')]
idx = {k: i + 2 for i, (k, _) in enumerate(cols)}
nc = len(cols) + 2
A = lambda k, r: '%s%d' % (L(idx[k]), r)
# ---------------- rows. R: ('v', value) given | ('hyd', lepton mass const) hydrogenic lepton on 12C | ('ie', k, n) hydrogenic from the k-th ionization energy
S = 'n/s'
rows = [
 dict(name='tau, free (Compton length)', R=('v', 1.1105e-16), m=mtau, m2=mtau, QQ=1, bind=0, exc=0, spin=0, coll=0, rot=0,
      note='R = hbar/(m c). QQ = 1 (self). exc = 0: no heavier charged lepton is known. bound-state cells 0: pointlike, no internal structure.'),
 dict(name='nucleon (proton at r_p)', R=('v', 0.84075e-15), m=mp, m2=mp, QQ=1, strong='f', bind='=%s-(2*%s+%s)' % (mp, mu_q, md_q), exc=1440e6-938.27208816e6, spin=939.56542052e6-938.27208816e6, coll=139.57039e6, rot=1232e6-938.27208816e6,
      note='r_p CODATA 2022. bind = m_p c^2 minus bare 2u+d (MS-bar, scheme-dependent). exc = N(1440) BW centre - m_p (PDG). spin = m_n - m_p (isospin). coll = pion mass (PDG). rot = Delta(1232) - N, 1232 MeV RECALLED (not a saved source).'),
 dict(name='muon, free (Compton length)', R=('v', 1.8676e-15), m=mmu, m2=mmu, QQ=1, bind=0, exc='=%s-%s' % (mtau, mmu), spin=0, coll=0, rot=0,
      note='as tau. exc = m_tau - m_mu: the gap to the next heavier lepton, not an excitation of the muon.'),
 dict(name='12C nucleus (charge radius)', R=('v', 2.4702e-15), m=mNuc, m2=mNuc, QQ=36, bind=B12, exc=lv[1], spin=lv[10], coll=lv[3], rot=lv[1],
      note='bind = 12 x B/A (AME2020). exc = 2+ level; spin = first 1+ level (12.71 MeV, spin-flip); coll = 3- octupole level; rot = the 2+ level (same as exc); levels from ENSDF via IAEA livechart. QQ = Z^2 = 36 (nuclear Coulomb scale). strong = 0: nucleons are colour singlets, the residual is the binding.'),
 dict(name='tau on 12C, 1s (hydrogenic, point nucleus)', R=('hyd', 1776.93e6), m=mtau, m2=mNuc, QQ='=%s' % Zc, bind='hyd', exc='hyd_e', spin='hyd_f', coll=0, rot=0,
      note='Z alpha mu c^2 formulas, nonrelativistic, point nucleus: the orbit (1.19 r_ch) lies inside the nucleus so this is NOT a physical level; shown only to put the tau at its carbon scale.'),
 dict(name='muon on 12C, 1s (hydrogenic, point nucleus)', R=('hyd', 105.6583755e6), m=mmu, m2=mNuc, QQ='=%s' % Zc, bind='hyd', exc='hyd_e', spin='hyd_f', coll=0, rot=0,
      note='hydrogenic: E1s = (Z alpha)^2 mu c^2 / 2, 2p-1s = 3/4 E1s, n=2 fine structure (Z alpha)^4 mu c^2 / 32, reduced mass; finite-size effects ignored.'),
 dict(name='electron, free (Compton length)', R=('v', 3.8616e-13), m=me, m2=me, QQ=1, bind=0, exc='=%s-%s' % (mmu, me), spin=0, coll=0, rot=0,
      note='as tau. exc = m_mu - m_e: the gap to the next heavier lepton, not an excitation of the electron.'),
 dict(name='C5+ 1s (IE6)', R=('ie', 6, 1), m=me, m2=mAtom, bind='sumIE6', exc=ion['CVI'][0], spin=ion['CVI'][1], coll=0, rot=0, note='hydrogenic size 1 a0/sqrt(IE/Ry), charge felt Z_eff = n sqrt(IE/Ry). exc, spin: NIST ASD C VI (2p - 1s, 2p3/2 - 2p1/2).'),
 dict(name='C4+ 1s2 (IE5)', R=('ie', 5, 1), m=me, m2=mAtom, bind='sumIE5', exc=ion['CV'][0], spin=ion['CV'][1], coll=0, rot=0, note='exc, spin: NIST ASD C V (1s2s 3S1; 1s2p 3P splitting).'),
 dict(name='C3+ (IE4)', R=('ie', 4, 2), m=me, m2=mAtom, bind='sumIE4', exc=ion['CIV'][0], spin=ion['CIV'][1], coll=0, rot=0, note='exc, spin: NIST ASD C IV (2p; 2p3/2 - 2p1/2).'),
 dict(name='C2+ (IE3)', R=('ie', 3, 2), m=me, m2=mAtom, bind='sumIE3', exc=ion['CIII'][0], spin=ion['CIII'][1], coll=0, rot=0, note='exc, spin: NIST ASD C III (2s2p 3P0; 3P1 - 3P0).'),
 dict(name='C+ (IE2)', R=('ie', 2, 2), m=me, m2=mAtom, bind='sumIE2', exc=ion['CII'][0], spin=ion['CII'][1], coll=0, rot=0, note='IE2 = C II series limit (NIST ASD). exc: 2s2p2 4P1/2; spin: 2P3/2 - 2P1/2 (NIST ASD C II).'),
 dict(name='CO molecule (r_e)', R=('v', 1.128e-10), m=me, m2=mAtom, QQ=0, bind=D_CO, exc=48686.7*cm, spin=S, coll=2169.756*cm, rot=2*1.931602*cm,
      note='r_e, omega_e, B_e: CCCBDB. bind = D0 from 0 K enthalpies. exc = a3Pi Te 48686.7 cm^-1 (NIST WebBook). spin: A not listed on the page. QQ = 0: neutral, bond polarity not included.'),
 dict(name='C valence electron (IE1)', R=('ie', 1, 2), m=me, m2=mAtom, bind='sumIE1', exc=ion['CI'][0], spin=ion['CI'][1], coll=0, rot=0, note='IE1 = C I series limit (NIST ASD). exc: 1D2; spin: 3P1 - 3P0 (NIST ASD C I).'),
 dict(name='C2 molecule (r_e)', R=('v', 1.243e-10), m=me, m2=mAtom, QQ=0, bind=D_C2, exc=716.24*cm, spin=S, coll=1855.066*cm, rot=2*1.820053*cm,
      note='r_e CCCBDB; bind = 2 Hfg(C) - Hfg(C2) at 0 K; exc = a3Piu Te 716.24 cm^-1 (NIST WebBook); omega_e, B_e CCCBDB. spin not obtained.'),
 dict(name='diamond C-C bond', R=('v', 3.56683e-10*sqrt(3)/4), m=me, m2=mAtom, QQ=0, bind='=711.2/96.485332/2', exc=5.47, spin=0.006, coll=0.16037239, rot=0,
      note='bind = Ec/2. exc = indirect band gap 5.47 eV (Ioffe NSM lists 5.46-5.6; 5.47 recalled). spin = valence-band spin-orbit 6 meV (Ioffe; disputed, ~13 meV ab initio). coll = Debye k Theta_D from Cp(298.16 K) (Debye model).'),
 dict(name='diamond lattice constant', R=('v', 3.56683e-10), m=me, m2=mAtom, QQ=0, bind='=711.2/96.485332', exc=5.47, spin=0.006, coll=0.16037239, rot=0, note='bind = Ec (cohesion per atom); others as the C-C row.'),
 dict(name='the gram (equal-volume sphere)', R=('v', 4.0808074e-3), m='=1e-3*%s^2/%s' % (c, eVJ), m2='=1e-3*%s^2/%s' % (c, eVJ), QQ=0, bind='gram', exc=5.47, spin=0, coll='=43.636776/%s' % eVJ, rot=0,
      note='bind = N x (nuclear B + all six ionization energies + Ec). exc = band gap. spin 0: all electron spins paired, 12C nuclear spin 0. coll = Debye thermal energy of the gram at 298.15 K (43.64 J). QQ = 0: net neutral.'),
]
mNuc_ = 12*931494102.42 - 6*510998.95
def size_key(r):
    t = r['R']
    if t[0] == 'v': return t[1]
    if t[0] == 'hyd': return 1.973269804e-7/((t[1]*mNuc_/(t[1]+mNuc_)) * 6*7.2973525693e-3)
    return t[2]*5.29177210903e-11/sqrt(IE[t[1]-1]/13.605693123)
rows.sort(key=size_key)
# ---------------- header
ws.cell(1, 1, 'Size (row) and the energies present at that size (columns); eV. Grey = absent by construction (0) or not sourced (n/s).').font = bold
hdr = 3
ws.cell(hdr, 1, 'Size').font = bold; ws.cell(hdr, 1).fill = hdrfill
for k, h in cols:
    x = ws.cell(hdr, idx[k], h); x.font = bold; x.fill = hdrfill; x.alignment = Alignment(wrap_text=True, vertical='top')
ws.cell(hdr, nc, 'What the numbers are / source').font = bold; ws.cell(hdr, nc).fill = hdrfill
first = hdr + 1
rowof = {r['name']: first + i for i, r in enumerate(rows)}
ie_row = {}
for r in rows:
    if r['R'][0] == 'ie': ie_row[r['R'][1]] = rowof[r['name']]
for i, r in enumerate(rows):
    rr = first + i
    ws.cell(rr, 1, r['name']).font = blk
    kind = r['R'][0]
    def put(k, v, inp=False):
        x = ws.cell(rr, idx[k], v)
        x.font = blue if inp else blk
        if v == 0 or v == S: x.fill = grey; x.font = blk
        x.number_format = '0.000E+00'
        return x
    # inputs for m, m2, QQ may be constants refs / formulas
    for k in ('m', 'm2'):
        v = r[k]; put(k, ('=' + v) if isinstance(v, str) and v.startswith('Constants') else v, inp=not isinstance(v, str))
    # R
    if kind == 'v': put('R', r['R'][1], True)
    elif kind == 'hyd':
        put('R', '=%s/(%s*%s/(%s+%s)*%s*%s)' % (hbarc, A('m', rr), A('m2', rr), A('m', rr), A('m2', rr), Zc, alpha))
    else:
        k_, n_ = r['R'][1], r['R'][2]
        put('R', '=%d*%s/SQRT(%s/%s)' % (n_, a0, 'IEREF%d' % k_, Ry))
    # QQ
    if kind == 'ie': put('QQ', '=%d*SQRT(%s/%s)' % (r['R'][2], 'IEREF%d' % r['R'][1], Ry))
    else:
        v = r.get('QQ', 0); put('QQ', ('=' + v[1:] if False else v) if isinstance(v, str) else v, inp=not isinstance(v, str))
    put('p12', '=LOG(%s/%s)/LOG(12)' % (A('R', rr), lP)).number_format = '0.000'
    put('hcR', '=%s/%s' % (hbarc, A('R', rr)))
    put('kin', '=%s^2/(2*%s)' % (A('hcR', rr), A('m', rr)))
    put('rest', '=%s' % A('m', rr))
    put('grav', '=%s*%s*%s*%s/(%s*%s^4)' % (G, eVJ, A('m', rr), A('m2', rr), A('R', rr), c))
    put('em', '=%s*%s*%s' % (alpha, A('QQ', rr), A('hcR', rr)))
    put('strong', ('=%s*%s*%s' % (CF, ag1, A('hcR', rr))) if r.get('strong') == 'f' else 0)
    put('weak', '=%s/%s*%s*EXP(-%s*%s/%s)' % (alpha, s2w, A('hcR', rr), A('R', rr), mW, hbarc))
    # bound-state
    b = r['bind']
    if b == 'hyd': put('bind', '=(%s*%s)^2*%s*%s/(%s+%s)/2' % (Zc, alpha, A('m', rr), A('m2', rr), A('m', rr), A('m2', rr)))
    elif isinstance(b, str) and b.startswith('sumIE'):
        put('bind', 0)   # placeholder, rewritten below
    elif b == 'gram': put('bind', 0)
    else: put('bind', b, not (isinstance(b, str)))
    e = r['exc']
    if e == 'hyd_e': put('exc', '=0.75*%s' % A('bind', rr))
    else: put('exc', e, not isinstance(e, str))
    sp = r['spin']
    if sp == 'hyd_f': put('spin', '=(%s*%s)^4*%s*%s/(%s+%s)/32' % (Zc, alpha, A('m', rr), A('m2', rr), A('m', rr), A('m2', rr)))
    else: put('spin', sp, not isinstance(sp, str))
    put('coll', r['coll'], not isinstance(r['coll'], str)); put('rot', r['rot'], not isinstance(r['rot'], str))
    put('kT', '=%s*%s' % (kB, Tamb)); put('kTc', '=%s*%s' % (kB, Tcmb))
    ws.cell(rr, nc, r['note']).font = blk
# place the ionization energies as a small block on the Constants sheet and wire IEREFk
base = len(consts) + 4
wk.cell(base - 1, 1, 'ionization energies of carbon (eV)').font = bold
srcie = {1: 'NIST ASD C I series limit', 2: 'NIST ASD C II series limit'}
IEC = {}
for k in range(1, 7):
    wk.cell(base + k - 1, 1, 'IE%d' % k).font = blk; wk.cell(base + k - 1, 2, IE[k - 1]).font = blue; wk.cell(base + k - 1, 3, srcie.get(k, 'PeriodicTableJSON (Wikipedia-derived), kJ/mol / 96.485332')).font = blk
    IEC[k] = 'Constants!$B$%d' % (base + k - 1)
def fix(s): return re.sub(r'IEREF(\d)', lambda m_: IEC[int(m_.group(1))], s) if isinstance(s, str) else s
for row in ws.iter_rows(min_row=first, max_row=first + len(rows) - 1):
    for x in row:
        if isinstance(x.value, str) and 'IEREF' in x.value: x.value = fix(x.value)
# bind rewritten for the ionization rows (sum of remaining removal energies) and the gram
for r in rows:
    rr = rowof[r['name']]; b = r['bind']
    if isinstance(b, str) and b.startswith('sumIE'):
        k0 = int(b[5:]); ws.cell(rr, idx['bind'], '=' + '+'.join(IEC[k] for k in range(k0, 7))).font = blk; ws.cell(rr, idx['bind']).number_format = '0.000E+00'
    if b == 'gram':
        nuc = rowof['12C nucleus (charge radius)']; dia = rowof['diamond lattice constant']
        x = ws.cell(rr, idx['bind'], '=%s*(%s+%s+%s)' % (Nat, A('bind', nuc), '+'.join(IEC[k] for k in range(1, 7)), A('bind', dia))); x.font = blk; x.number_format = '0.000E+00'; x.fill = PatternFill(fill_type=None)
ws.freeze_panes = ws.cell(first, 2); ws.column_dimensions['A'].width = 44
for k, _ in cols: ws.column_dimensions[L(idx[k])].width = 17
ws.column_dimensions[L(nc)].width = 100; ws.row_dimensions[hdr].height = 62
# ---------------- cycles and heat sheets
wc.cell(1, 1, 'Cycles = E / (hbar c / R), for every energy column on the Energies sheet (text n/s passes through)').font = bold
wh.cell(1, 1, 'log10 of each energy in eV (colour scale per sheet; blank where the energy is 0 or n/s)').font = bold
skipc = ('R', 'p12', 'm', 'm2', 'QQ', 'hcR')
for sh, title in ((wc, 'cycles'), (wh, 'log10 eV')):
    sh.cell(hdr, 1, 'Size').font = bold; sh.cell(hdr, 1).fill = hdrfill
    for k, h in cols:
        if k in ('m', 'm2', 'QQ'): continue
        x = sh.cell(hdr, idx[k], h if k in ('R', 'p12') else h.replace('(eV)', '(%s)' % title)); x.font = bold; x.fill = hdrfill; x.alignment = Alignment(wrap_text=True, vertical='top')
    for i in range(len(rows)):
        rr = first + i
        sh.cell(rr, 1, "='Energies (eV)'!A%d" % rr).font = blk
        for k, _ in cols:
            if k in ('m', 'm2', 'QQ'): continue
            src = "'Energies (eV)'!%s" % A(k, rr)
            if k in ('R', 'p12'): f = '=' + src
            elif sh is wc: f = '=IF(ISNUMBER(%s),%s/\'Energies (eV)\'!%s,%s)' % (src, src, A('hcR', rr), src)
            else: f = '=IF(ISNUMBER(%s),IF(%s>0,LOG10(%s),""),"")' % (src, src, src)
            x = sh.cell(rr, idx[k], f); x.font = blk; x.number_format = '0.000' if k == 'p12' else ('0.000E+00' if sh is wc else '0.00')
    sh.freeze_panes = sh.cell(first, 2); sh.column_dimensions['A'].width = 44; sh.row_dimensions[hdr].height = 62
    for k, _ in cols: sh.column_dimensions[L(idx[k])].width = 15
heatcols = [k for k, _ in cols if k not in ('R', 'p12', 'm', 'm2', 'QQ')]
rng = '%s%d:%s%d' % (L(idx[heatcols[0]]), first, L(idx[heatcols[-1]]), first + len(rows) - 1)
wh.conditional_formatting.add(rng, ColorScaleRule(start_type='min', start_color='F7FBFF', mid_type='percentile', mid_value=50, mid_color='9ECAE1', end_type='max', end_color='08306B'))
# ---------------- notes
notes = ['Size versus energy, leptons to the gram. Rows are sizes (the object whose size it is); columns are kinds of energy present at every scale: size (hbar c/R, confinement kinetic), mass (rest, gravity), charge (EM, strong, weak), bound-state (binding, excitation, spin, collective, rotational) and ambient (kT, CMB kT).',
 'Blue = sourced input; black = formula. Grey 0 = absent by construction (pointlike, colourless, neutral, no solid, nuclear spin 0 ...); grey n/s = exists but no sourced value was obtained. Counts of each are in the CSV summary row.',
 'Universal columns (hbar c/R, confinement, rest, gravity, EM, strong, weak, kT) are formulas of (R, m, m2, Q1Q2) and are filled for every row. Weak uses alpha_W = alpha / sin^2 theta_W with Yukawa cutoff at lambda_W = hbar/(m_W c); strong uses C_F alpha_g1(0) = 4 pi/3 and is evaluated only at the nucleon row (colourless elsewhere; confinement beyond ~1 fm makes the Coulomb-like form invalid there).',
 'Free-lepton rows: R is the Compton length. Their bound-state cells are 0 (no internal structure) except the excitation cell, which holds the gap to the next heavier lepton (0 for the tau, none known) and is NOT an excitation of that lepton.',
 'tau/muon on 12C are point-nucleus hydrogenic formulas, not measured levels; the tau orbit is inside the nucleus. C5+ to C I rows use NIST ASD levels (first level of the first term above the ground term; first J-splitting of the lowest multiplet) and hydrogenic sizes n a0/sqrt(IE/Ry).',
 'Recalled, not in a saved file: sin^2 theta_W = 0.23122; Delta(1232) = 1232 MeV; diamond band gap 5.47 eV (Ioffe NSM lists 5.46-5.6); diamond valence-band spin-orbit 6 meV (disputed, ~13 meV). IE3-IE6 are Wikipedia-derived (PeriodicTableJSON).',
 'Sources saved in explore/data/: AME2020, ENSDF 12C (IAEA livechart CSV), NIST ASD C I-C VI, CCCBDB (bond lengths, 0 K enthalpies, omega_e, B_e), PDG 2024 (leptons, quarks, gauge/Higgs, mesons, baryons), Deur et al. 2016, CODATA 2022 r_p, NIST WebBook (CO, C2 states).',
 'No rule is proposed; the sheet is for examination. No LibreOffice on this machine: formulas carry no cached values until Excel opens the file; the CSV and the independent evaluator below carry the numbers.']
for i, t in enumerate(notes, start=1): wn.cell(i, 1, t).font = blk
wn.column_dimensions['A'].width = 200
OUT = os.path.join(MAPS, 'size_vs_energy_full.xlsx'); wb.save(OUT)
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
        sh = m_.group(1); cell = m_.group(2)
        shn = (sh.rstrip('!').strip("'") if sh else sheet)
        v = getv(shn, cell)
        return repr(v) if not isinstance(v, str) else repr(v)
    f2 = re.sub(r"((?:'[^']+'|[A-Za-z]+)!)?(\$?[A-Z]{1,2}\$?\d+)", ref, f)
    f2 = f2.replace('^', '**').replace('SQRT(', 'sqrt(').replace('EXP(', 'exp_(').replace('LOG10(', 'log10(').replace('LOG(', 'log(').replace('ISNUMBER(', 'isnum(')
    f2 = re.sub(r'IF\(', 'iff(', f2)
    env = dict(sqrt=sqrt, exp_=lambda x: math.exp(x) if x > -700 else 0.0, log=math.log, log10=math.log10, isnum=lambda x: isinstance(x, (int, float)), iff=lambda a, b, c_=None: b if a else c_)
    return eval(f2, {'__builtins__': {}}, env)
# iff evaluates both branches eagerly; guard division by zero / log domain via try in the callers
def safe(sheet, v):
    try: return evalf(sheet, v[1:]) if isinstance(v, str) and v.startswith('=') else v
    except Exception as ex: return 'ERR:%s' % ex
vals = []
for i in range(len(rows)):
    rr = first + i; rec = {'name': rows[i]['name']}
    for k, h in cols:
        v = wb2['Energies (eV)'].cell(rr, idx[k]).value
        key = ('Energies (eV)', '%s%d' % (L(idx[k]), rr));
        if isinstance(v, str) and v.startswith('='):
            try: v = evalf('Energies (eV)', v[1:])
            except Exception as ex: v = 'ERR:%s' % ex
            cache[key] = v
        else: cache[key] = v
        rec[k] = v
    vals.append(rec)
errs = [(r['name'], k) for r in vals for k, _ in cols if isinstance(r[k], str) and r[k].startswith('ERR')]
print('formula errors in evaluator:', errs)
with open(os.path.join(MAPS, 'size_vs_energy_full.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['size'] + [h for _, h in cols] + ['cycles: ' + h for k, h in cols if k not in ('R', 'p12', 'm', 'm2', 'QQ', 'hcR')])
    for r in vals:
        w.writerow([r['name']] + [repr(r[k]) if not isinstance(r[k], str) else r[k] for k, _ in cols] +
                   [(repr(r[k]/r['hcR']) if isinstance(r[k], (int, float)) else r[k]) for k, _ in cols if k not in ('R', 'p12', 'm', 'm2', 'QQ', 'hcR')])
    zero = sum(1 for r in vals for k in ('bind', 'exc', 'spin', 'coll', 'rot', 'strong') if r[k] == 0); ns = sum(1 for r in vals for k in ('bind', 'exc', 'spin', 'coll', 'rot', 'strong') if r[k] == 'n/s')
    w.writerow(['summary: zeros (absent by construction) among the 6 structure/strong columns', zero, 'n/s', ns, 'rows', len(vals), 'cells', len(vals)*len(cols)])
print('saved', os.path.abspath(OUT), '; zeros', zero, 'n/s', ns, 'of', len(vals)*6, 'structure/strong cells')
show = ['hcR', 'kin', 'grav', 'em', 'strong', 'weak', 'bind', 'exc', 'spin', 'coll', 'rot', 'kT']
print('%-46s %9s %7s ' % ('size', 'R (m)', 'p12') + ' '.join('%9s' % k for k in show))
for r in vals:
    print('%-46s %9.3e %7.3f ' % (r['name'], r['R'], r['p12']) + ' '.join(('%9.2e' % r[k]) if isinstance(r[k], (int, float)) else '%9s' % r[k] for k in show))
