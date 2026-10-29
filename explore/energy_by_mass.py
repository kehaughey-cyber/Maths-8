# Energies keyed by the binding mass, not by size. For a pair bound by a coupling g (reduced mass ~ the lighter mass m) the three lengths are g*lambda (classical),
# lambda = hbar/(m c) (Compton) and lambda/g (Bohr), and the energies are m c^2 {g, 1, g^2/2 (binding), g^4/32 (n=2 fine structure)}. So size is DERIVED from (m, g).
# Couplings: EM g = alpha; strong g = C_F alpha_g1(0) = 4 pi/3 (non-perturbative, nonrelativistic forms are invalid for g > 1; shown, flagged); weak g = alpha/sin^2 theta_W with the Yukawa range hbar/(m_W c);
# gravity g = G m^2/(hbar c) = (m/m_P)^2. New file; nothing fitted; no rule proposed.
# Run: py -3 -I -X utf8 -u explore/energy_by_mass.py   (writes maps/energy_by_mass.xlsx and .csv; formulas verified with an independent evaluator)
import csv, math, os, re
from math import sqrt, pi
from openpyxl import Workbook, load_workbook
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter as L
HERE = os.path.dirname(os.path.abspath(__file__)); MAPS = os.path.join(HERE, '..', 'maps'); OUT = os.path.join(MAPS, 'energy_by_mass.xlsx')
AR = 'Arial'; blue = Font(name=AR, color='0000FF'); blk = Font(name=AR); bold = Font(name=AR, bold=True); hdrfill = PatternFill('solid', fgColor='DDE6F0'); flagfill = PatternFill('solid', fgColor='FCE5CD')
wb = Workbook(); ws = wb.active; ws.title = 'By mass (eV, m)'; wh = wb.create_sheet('Log10 (heat)'); wk = wb.create_sheet('Constants'); wn = wb.create_sheet('Sources and notes')
consts = [('hbar c (eV m)', 1.973269804e-7, 'CODATA 2018'), ('alpha', 7.2973525693e-3, 'CODATA 2018'), ('sin^2 theta_W (MS-bar, M_Z)', 0.23122, 'PDG, recalled (not a saved file)'),
          ('m_W c^2 (eV)', 80.3692e9, 'PDG 2024 gauge/Higgs table (saved)'), ('C_F (SU(3))', 4/3, 'SU(3) quark Casimir'), ('alpha_g1(0) = pi', pi, 'Deur, Brodsky, de Teramond 2016 eq 4.4 (saved)'),
          ('Planck mass c^2 (eV)', 1.220890e28, 'CODATA 2018 (sqrt(hbar c/G) c^2)'), ('Planck length (m)', 1.616255e-35, 'CODATA 2018'), ('G (m^3 kg^-1 s^-2)', 6.67430e-11, 'CODATA 2018'),
          ('c (m/s)', 299792458.0, 'exact'), ('e (J per eV)', 1.602176634e-19, 'exact'), ('k_B (eV/K)', 8.617333262e-5, 'CODATA 2018'), ('T ambient (K)', 298.15, 'standard'), ('T CMB (K)', 2.7255, 'PDG 2024 cosmology (saved)'),
          ('Hubble radius (m)', 4.4e26, 'order of magnitude, c/H0 with H0 ~ 68 km/s/Mpc (recalled)')]
wk['A1'] = 'constant'; wk['B1'] = 'value'; wk['C1'] = 'source'
K = {}
for i, (a, b, s) in enumerate(consts, start=2):
    wk.cell(i, 1, a).font = blk; wk.cell(i, 2, b).font = blue; wk.cell(i, 3, s).font = blk; K[a] = 'Constants!$B$%d' % i
for c_ in 'ABC': wk[c_ + '1'].font = bold
wk.column_dimensions['A'].width = 34; wk.column_dimensions['B'].width = 20; wk.column_dimensions['C'].width = 60
hbarc, alpha, s2w, mW, CF, ag1, mP, lP, G, c, eVJ, kB, Tamb, Tcmb, RH = [K[a] for a, _, _ in consts]
# rows: binding mass (eV), source. The mass is the lighter of the bound pair (reduced mass ~ m); composites use the mass of the object doing the binding.
masses = [
 ('neutrino nu3 (oscillation minimum)', 0.0503021, 'M: oscillation lower bound (full_ladder.md); not a measured mass'),
 ('electron', 510998.95, 'M: CODATA; binds every atom, molecule and solid in the carbon study'),
 ('up quark (MS-bar 2 GeV)', 2.16e6, 'M: PDG 2024; scheme-dependent'),
 ('down quark (MS-bar 2 GeV)', 4.70e6, 'M: PDG 2024; scheme-dependent'),
 ('strange quark (MS-bar 2 GeV)', 93.5e6, 'M: PDG 2024; scheme-dependent'),
 ('muon', 105.6583755e6, 'M: PDG 2024'),
 ('proton', 938.27208816e6, 'M: CODATA; nucleon binding mass'),
 ('neutron', 939.56542052e6, 'M: CODATA'),
 ('charm quark (MS-bar m_c)', 1.2730e9, 'M: PDG 2024; scheme-dependent'),
 ('tau', 1776.93e6, 'M: PDG 2024'),
 ('bottom quark (MS-bar m_b)', 4.183e9, 'M: PDG 2024; scheme-dependent'),
 ('12C nucleus', 12*931494102.42 - 6*510998.95, 'C: (12 u - 6 m_e) c^2; the object whose mass enters the nuclear rest energy'),
 ('W boson', 80.3692e9, 'M: PDG 2024'),
 ('Z boson', 91.1880e9, 'M: PDG 2024'),
 ('Higgs boson', 125.20e9, 'M: PDG 2024'),
 ('top quark (direct)', 172.57e9, 'M: PDG 2024'),
 ('the gram of 12C', 1e-3*299792458.0**2/1.602176634e-19, 'C: M c^2 for M = 1 g'),
 ('Planck mass', 1.220890e28, 'C: sqrt(hbar c/G) c^2; here m/m_P = 1 by construction'),
]
cols = [('m', 'Binding mass m c^2 (eV)'), ('mme', 'm / m_e'), ('mmP', 'm / m_P'), ('lam', 'Compton length hbar/(m c) (m)'), ('p12', 'p12 of the Compton length'),
        ('gE', 'g EM = alpha'), ('gS', 'g strong = C_F alpha_g1'), ('gW', 'g weak = alpha/sin^2 theta_W'), ('gG', 'g gravity = (m/m_P)^2'),
        ('aE', 'Bohr size EM  lambda/g (m)'), ('aS', 'Bohr size strong (m) [g>1: invalid]'), ('aW', 'Bohr size weak (m)'), ('aG', 'Bohr size gravity (m)'), ('rs', 'Schwarzschild 2Gm/c^2 (m)'),
        ('rest', 'Rest energy m c^2 (eV)'),
        ('cE', 'Pair energy at Compton length: EM  g m c^2 (eV)'), ('cS', 'strong (eV)'), ('cW', 'weak (eV)'), ('cG', 'gravity (eV)'),
        ('bE', 'Binding  g^2 m c^2 / 2: EM (eV)'), ('bS', 'strong (eV)'), ('bW', 'weak (eV)'), ('bG', 'gravity (eV)'),
        ('fE', 'Fine structure  g^4 m c^2 / 32: EM (eV)'), ('fS', 'strong (eV)'), ('fW', 'weak (eV)'), ('fG', 'gravity (eV)'),
        ('wr', 'Weak Bohr size / weak range hbar/(m_W c)'), ('gr', 'Gravity Bohr size / Hubble radius'), ('kT', 'Ambient kT (eV)'), ('kTc', 'CMB kT (eV)')]
idx = {k: i + 2 for i, (k, _) in enumerate(cols)}; nc = len(cols) + 2
A = lambda k, r: '%s%d' % (L(idx[k]), r)
ws.cell(1, 1, 'Energies keyed by the binding mass; sizes are derived from (m, g). Twenty-two orders of mass separate the electron from the Planck mass; every column is m c^2 times a power of the coupling.').font = bold
hdr = 3; first = hdr + 1
ws.cell(hdr, 1, 'Binding mass').font = bold; ws.cell(hdr, 1).fill = hdrfill
for k, h in cols:
    x = ws.cell(hdr, idx[k], h); x.font = bold; x.fill = hdrfill; x.alignment = Alignment(wrap_text=True, vertical='top')
ws.cell(hdr, nc, 'Source of the mass').font = bold; ws.cell(hdr, nc).fill = hdrfill
for i, (nm, m, src) in enumerate(masses):
    r = first + i
    ws.cell(r, 1, nm).font = blk
    def put(k, v, inp=False, f='0.000E+00'):
        x = ws.cell(r, idx[k], v); x.font = blue if inp else blk; x.number_format = f; return x
    put('m', m, True)
    put('mme', '=%s/%s' % (A('m', r), '$%s$%d' % (L(idx['m']), first + 1)))     # row 2 is the electron
    put('mmP', '=%s/%s' % (A('m', r), mP))
    put('lam', '=%s/%s' % (hbarc, A('m', r))); put('p12', '=LOG(%s/%s)/LOG(12)' % (A('lam', r), lP), f='0.000')
    put('gE', '=%s' % alpha); put('gS', '=%s*%s' % (CF, ag1)); put('gW', '=%s/%s' % (alpha, s2w)); put('gG', '=%s^2' % A('mmP', r))
    for a, g in (('aE', 'gE'), ('aS', 'gS'), ('aW', 'gW'), ('aG', 'gG')): put(a, '=%s/%s' % (A('lam', r), A(g, r)))
    put('rs', '=2*%s*%s*%s/(%s^2*%s*%s)' % (G, A('m', r), eVJ, c, c, '1') if False else '=2*%s*(%s*%s/%s^2)/%s^2' % (G, A('m', r), eVJ, c, c))
    put('rest', '=%s' % A('m', r))
    for p, g in (('c', 'g'),):
        pass
    for k, g in (('cE', 'gE'), ('cS', 'gS'), ('cW', 'gW'), ('cG', 'gG')): put(k, '=%s*%s' % (A(g, r), A('m', r)))
    for k, g in (('bE', 'gE'), ('bS', 'gS'), ('bW', 'gW'), ('bG', 'gG')): put(k, '=%s^2*%s/2' % (A(g, r), A('m', r)))
    for k, g in (('fE', 'gE'), ('fS', 'gS'), ('fW', 'gW'), ('fG', 'gG')): put(k, '=%s^4*%s/32' % (A(g, r), A('m', r)))
    put('wr', '=%s*%s/%s/%s' % (A('aW', r), mW, hbarc, '1'), f='0.00E+00')
    put('gr', '=%s/%s' % (A('aG', r), RH), f='0.00E+00')
    put('kT', '=%s*%s' % (kB, Tamb)); put('kTc', '=%s*%s' % (kB, Tcmb))
    ws.cell(r, nc, src).font = blk
ws.freeze_panes = ws.cell(first, 2); ws.column_dimensions['A'].width = 38
for k, _ in cols: ws.column_dimensions[L(idx[k])].width = 17
ws.column_dimensions[L(nc)].width = 90; ws.row_dimensions[hdr].height = 76
# heat sheet: log10 of energies
wh.cell(1, 1, 'log10 of each energy (eV) and of each size (m); colour scale -12 to 11 on energies').font = bold
wh.cell(hdr, 1, 'Binding mass').font = bold; wh.cell(hdr, 1).fill = hdrfill
heatk = ['m', 'lam', 'aE', 'aS', 'aW', 'aG', 'rs', 'rest', 'cE', 'cS', 'cW', 'cG', 'bE', 'bS', 'bW', 'bG', 'fE', 'fS', 'fW', 'fG', 'wr', 'gr', 'kT', 'kTc']
hl = {k: h for k, h in cols}
for j, k in enumerate(heatk):
    x = wh.cell(hdr, j + 2, 'log10 ' + hl[k]); x.font = bold; x.fill = hdrfill; x.alignment = Alignment(wrap_text=True, vertical='top')
for i in range(len(masses)):
    r = first + i; wh.cell(r, 1, "='By mass (eV, m)'!A%d" % r).font = blk
    for j, k in enumerate(heatk):
        x = wh.cell(r, j + 2, "=LOG10('By mass (eV, m)'!%s)" % A(k, r)); x.font = blk; x.number_format = '0.00'
wh.freeze_panes = wh.cell(first, 2); wh.column_dimensions['A'].width = 38; wh.row_dimensions[hdr].height = 76
for j in range(len(heatk)): wh.column_dimensions[L(j + 2)].width = 14
en = [j + 2 for j, k in enumerate(heatk) if k in ('m', 'rest', 'cE', 'cS', 'cW', 'cG', 'bE', 'bS', 'bW', 'bG', 'fE', 'fS', 'fW', 'fG', 'kT', 'kTc')]
wh.conditional_formatting.add('%s%d:%s%d' % (L(min(en)), first, L(max(en)), first + len(masses) - 1), ColorScaleRule(start_type='num', start_value=-12, start_color='F7FBFF', mid_type='num', mid_value=0, mid_color='9ECAE1', end_type='num', end_value=11, end_color='08306B'))
notes = ['Energies keyed by the mass of the particle doing the binding, with sizes derived. For a pair of reduced mass ~ m bound by coupling g: classical size g*lambda, Compton lambda = hbar/(m c), Bohr size lambda/g; energies m c^2 times g (pair energy at lambda), 1 (rest), g^2/2 (binding), g^4/32 (n=2 fine structure). The Bohr-size rows and the binding rows are the virial/hydrogenic forms.',
 'Couplings: EM g = alpha. Strong g = C_F alpha_g1(0) = 4 pi/3 (4.19, the measured effective charge at Q = 0). A coupling above 1 makes the nonrelativistic Bohr forms invalid (the Bohr size comes out below the Compton length); the strong columns are shown for completeness and are formal. Weak g = alpha/sin^2 theta_W = 0.0316, with the Yukawa range hbar/(m_W c): the column "weak Bohr size / range" greater than 1 means the Coulomb-like weak form has no bound state at that mass (true for every row lighter than about 2.5 TeV).',
 'Gravity g = G m^2/(hbar c) = (m/m_P)^2: gravity is the only coupling that depends on the mass; its Bohr size exceeds the Hubble radius for every row lighter than about 40 MeV (the neutrino, electron, up and down rows), i.e. no gravitational atom fits in the universe for them. The gram and the Planck mass are the rows where the gravity columns are not astronomically small (the gram: g = 2.1e9; Planck mass: g = 1).',
 'Mass is the binding particle: composites enter with the mass doing the binding (the electron for atoms, molecules, solids and phonon-free cohesion; the nucleon for nuclei), not their total mass. The 12C nucleus and the gram rows are shown as objects of that total mass for completeness.',
 'Carbon analogs from the earlier maps (not repeated here): the electron row corresponds to every atomic, molecular and lattice row (hydrogen: alpha^2 m c^2/2 = 13.606 eV = Ry exactly); the muon and tau rows correspond to the hydrogenic lepton-on-12C rows (those use Z alpha and the reduced mass); the proton and neutron rows correspond to the nuclear rows, where the measured binding per nucleon is ~7.7 MeV against the formal strong binding in these columns of 8e9 eV, a mismatch of ~1000 that shows the non-perturbative coupling cannot be used in the Bohr form.',
 'Recalled, not in a saved file: sin^2 theta_W = 0.23122; Hubble radius. Neutrino mass is an oscillation lower bound, not a measurement. Quark masses are MS-bar and scheme-dependent. No LibreOffice here: formulas carry no cached values until Excel opens the file; an independent evaluator verifies them and the CSV carries the numbers. No rule is proposed.']
for i, t in enumerate(notes, start=1): wn.cell(i, 1, t).font = blk
wn.column_dimensions['A'].width = 200
wb.save(OUT)
# ---------------- independent evaluator -> CSV
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
    f2 = f2.replace('^', '**').replace('LOG(', 'log(')
    return eval(f2, {'__builtins__': {}}, dict(log=math.log))
vals = []
for i in range(len(masses)):
    r = first + i; rec = {'name': masses[i][0]}
    for k, _ in cols:
        v = wb2['By mass (eV, m)'].cell(r, idx[k]).value
        if isinstance(v, str) and v.startswith('='):
            try: v = evalf('By mass (eV, m)', v[1:])
            except Exception as ex: v = 'ERR:%s' % ex
        cache[('By mass (eV, m)', A(k, r))] = v; rec[k] = v
    vals.append(rec)
errs = [(x['name'], k) for x in vals for k, _ in cols if isinstance(x[k], str)]
print('formula errors in evaluator:', errs)
with open(os.path.join(MAPS, 'energy_by_mass.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['binding mass'] + [h for _, h in cols])
    for x in vals: w.writerow([x['name']] + [repr(x[k]) for k, _ in cols])
print('saved', os.path.abspath(OUT))
show = ['m', 'lam', 'aE', 'aS', 'aW', 'aG', 'rs', 'bE', 'bS', 'bW', 'bG', 'fE', 'wr', 'gr']
print('%-34s ' % 'mass' + ' '.join('%9s' % k for k in show))
for x in vals: print('%-34s ' % x['name'] + ' '.join('%9.2e' % x[k] for k in show))
