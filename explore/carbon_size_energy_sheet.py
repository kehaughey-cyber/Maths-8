# Size versus energy for carbon, as a spreadsheet: rows are sizes, columns are the different energies that live at that size.
# New file; nothing fitted. Inputs are sourced numbers (blue); everything derivable is a live formula (black).
# Run: py -3 -I -X utf8 -u explore/carbon_size_energy_sheet.py ; then recalc with the xlsx skill's scripts/recalc.py
# Sources: explore/data/{ame2020_mass_1.mas20.txt, iaea_livechart_12C_levels.csv (ENSDF Kelley/Purcell/Sheu 2017), nist_asd_CI.txt, nist_asd_CII.txt,
#   PeriodicTableJSON.json (IE3-IE6), cccbdb_exp_diatomic_constants.html, cccbdb_diatomic_exp_bondlengths.html, cccbdb_enthalpy_formation_0K.html,
#   pdg2024_mesons_light.txt (pion), pdg2024_baryons.txt (N(1440)), nist_webbook_diamond_condensed.html, carbon_remaining_sourced_values.txt}
import csv, html, json, os, re
from math import sqrt, pi
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter as L
HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.join(HERE, 'data'); OUT = os.path.join(HERE, '..', 'maps', 'carbon_size_vs_energy.xlsx')
cm = 1.239841984e-4   # eV per cm^-1
# ---------------- inputs from files
ame = {}
for line in open(os.path.join(DATA, 'ame2020_mass_1.mas20.txt')).read().split('\n'):
    if len(line) > 100 and line[14:19].strip().isdigit():
        try: ame[(int(line[14:19]), line[20:23].strip())] = (float(line[28:42]), float(line[54:67]))
        except Exception: pass
mex = lambda A, s: ame[(A, s)][0]*1e3        # eV
Sn = mex(11, 'C') + mex(1, 'n') - mex(12, 'C'); Sp = mex(11, 'B') + mex(1, 'H') - mex(12, 'C'); Sa = mex(8, 'Be') + mex(4, 'He') - mex(12, 'C')
B12 = 12*ame[(12, 'C')][1]*1e3
lv = {}
for r in csv.DictReader(open(os.path.join(DATA, 'iaea_livechart_12C_levels.csv'))): lv[int(r['idx'])] = (float(r['energy'])*1e3, r['jp'])
EL = {e['symbol']: e for e in json.load(open(os.path.join(DATA, 'PeriodicTableJSON.json'), encoding='utf-8'))['elements']}
IE = [x/96.485332 for x in EL['C']['ionization_energies']]
IE[0] = 11.2602880; IE[1] = 24.383143       # NIST ASD series limits (C I, C II level files)
def asd(fn):
    d = {}
    for row in csv.reader(open(os.path.join(DATA, fn), encoding='utf-8'), delimiter='\t'):
        if len(row) > 4 and row[0] not in ('Configuration',):
            try: d.setdefault((row[1].strip('"'), row[2].strip('"')), float(row[4].strip('"')))
            except ValueError: pass
    return d
CI = asd('nist_asd_CI.txt'); CII = asd('nist_asd_CII.txt')
rawh = open(os.path.join(DATA, 'cccbdb_enthalpy_formation_0K.html'), encoding='utf-8', errors='replace').read()
def txt(s): return html.unescape(re.sub(r'<[^>]+>', '', re.sub(r'<sub>(.*?)</sub>', r'\1', s, flags=re.I))).strip()
Hf = {}
for row in re.findall(r'<TR>(.*?)</TR>', rawh, flags=re.S | re.I):
    c = re.findall(r'<TD[^>]*>(.*?)</TD>', row, flags=re.S | re.I)
    if len(c) >= 4:
        try: Hf[txt(c[0])] = float(txt(c[2]))
        except ValueError: pass
D0 = lambda atoms, f: (sum(n*Hf[a] for a, n in atoms.items()) - Hf[f])/96.485332
D_CO = D0({'C': 1, 'O': 1}, 'CO'); D_C2 = D0({'C': 2}, 'C2'); D_CH4 = D0({'C': 1, 'H': 4}, 'CH4'); D_C6H6 = D0({'C': 6, 'H': 6}, 'C6H6') if 'C6H6' in Hf else 56.617932
# ---------------- workbook
wb = Workbook(); ar = 'Arial'
blue = Font(name=ar, color='0000FF'); blk = Font(name=ar); bold = Font(name=ar, bold=True); hdrfill = PatternFill('solid', fgColor='DDE6F0')
ws = wb.active; ws.title = 'Energies (eV)'; wc = wb.create_sheet('Cycles'); wk = wb.create_sheet('Constants'); wn = wb.create_sheet('Sources and notes')
# constants
consts = [('hbar c (eV m)', 1.973269804e-7, 'CODATA 2018'), ('alpha', 7.2973525693e-3, 'CODATA 2018'), ('Rydberg energy (eV)', 13.605693123, 'CODATA 2018'), ('Bohr radius a0 (m)', 5.29177210903e-11, 'CODATA 2018'),
          ('Planck length (m)', 1.616255e-35, 'CODATA 2018'), ('k_B (eV/K)', 8.617333262e-5, 'CODATA 2018'), ('T (K)', 298.15, 'standard state'), ('atoms in the gram, N', 5.0184506350676e22, '1 g / (12 u)')]
wk['A1'] = 'constant'; wk['B1'] = 'value'; wk['C1'] = 'source'
for i, (a, b, c) in enumerate(consts, start=2):
    wk.cell(i, 1, a).font = blk; x = wk.cell(i, 2, b); x.font = blue; wk.cell(i, 3, c).font = blk
for c in 'ABC': wk[c+'1'].font = bold
wk.column_dimensions['A'].width = 26; wk.column_dimensions['B'].width = 18; wk.column_dimensions['C'].width = 22
hbarc, alpha, Ry, a0c, lP, kBc, Tc, Nc = ['Constants!$B$%d' % i for i in range(2, 10)]
# columns
cols = [('R', 'Size R (m)'), ('p12', 'Size in p12 above Planck length'), ('Q', 'Charge felt Q (e)'), ('n', 'Shell n'),
        ('hcR', 'hbar c / R (eV)'), ('coul', 'Coulomb alpha Q^2 hbar c / R (eV)'), ('rest', 'Rest energy m c^2 (eV)'), ('bind', 'Binding / dissociation / cohesion (eV)'),
        ('rem1', 'Removal 1: IE_k or S_alpha (eV)'), ('rem2', 'Removal 2: S_p (eV)'), ('rem3', 'Removal 3: S_n (eV)'),
        ('ex1', 'Excitation 1 (eV)'), ('ex2', 'Excitation 2 (eV)'), ('ex3', 'Excitation 3 (eV)'), ('fs1', 'Fine structure / splitting 1 (eV)'), ('fs2', 'Fine structure 2 (eV)'),
        ('vib', 'Vibrational hbar omega_e (eV)'), ('rot', 'Rotational 2 B_e (eV)'), ('deb', 'Debye phonon k Theta_D (eV)'), ('ram', 'Raman optical phonon (eV)'),
        ('zpe', 'Zero point (9/8) k Theta_D per atom (eV)'), ('kT', 'Thermal kT at 298.15 K (eV)'), ('heat', 'Debye heat content per atom at 298.15 K (eV)')]
idx = {k: i+2 for i, (k, _) in enumerate(cols)}       # column index; column 1 is the row label
Rp = 0.84075e-15; rch = 2.4702e-15; a_dia = 3.56683e-10; N = 5.0184506350676e22
V = N*a_dia**3/8; R_sph = (3*V/(4*pi))**(1/3)
mp = 938.27208816e6; mn = 939.56542052e6; me = 510998.95; u_eV = 931494102.42; Ec = 711.2/96.485332
kTh = 0.16037239   # eV, Debye from Cp (carbon_gram_remaining.out)
rows = [
 dict(name='nucleon (proton, r_p)', R=Rp, Q=1, rest=mp, ex1=139.57039e6, ex2=1440e6-mp, fs1=mn-mp,
      note='ex1 = pion mass (lightest hadron, PDG 2024); ex2 = N(1440) Breit-Wigner centre minus m_p (range 1410-1470); fs1 = m_n - m_p; r_p = CODATA 2022'),
 dict(name='12C nucleus (charge radius)', R=rch, Q=6, rest=(12-6*me/u_eV)*u_eV, bind=B12, rem1=Sa, rem2=Sp, rem3=Sn, ex1=lv[1][0], ex2=lv[2][0], ex3=lv[3][0],
      note='rest = (12 u - 6 m_e) c^2; bind = 12 x B/A (AME2020); S_alpha, S_p, S_n from AME2020 mass excesses; levels 2+, 0+ (Hoyle), 3- from ENSDF (IAEA livechart, 1-Jan-2017)'),
 dict(name='C5+ 1s (IE6)', n=1, rem1=IE[5], note='size from n a0/sqrt(IE/Ry); Q = Z_eff = n sqrt(IE/Ry); IE6 from PeriodicTableJSON (kJ/mol / 96.485332)'),
 dict(name='C4+ 1s2 (IE5)', n=1, rem1=IE[4], note='same construction; IE5 from PeriodicTableJSON'),
 dict(name='C3+ n=2 (IE4)', n=2, rem1=IE[3], note='same construction; IE4 from PeriodicTableJSON'),
 dict(name='C2+ n=2 (IE3)', n=2, rem1=IE[2], note='same construction; IE3 from PeriodicTableJSON'),
 dict(name='C+ n=2 (IE2)', n=2, rem1=IE[1], ex1=CII[('4P', '1/2')], ex2=CII[('2D', '5/2')], fs1=CII[('2P*', '3/2')],
      note='IE2 = C II series limit (NIST ASD); ex1 = 2s2p2 4P1/2, ex2 = 2s2p2 2D5/2, fs1 = 2P3/2 - 2P1/2 of the C+ ground term (NIST ASD C II)'),
 dict(name='C valence n=2 (IE1)', n=2, rem1=IE[0], rest=12*u_eV, ex1=CI[('1D', '2')], ex2=CI[('1S', '0')], ex3=CI[('5S*', '2')], fs1=CI[('3P', '1')], fs2=CI[('3P', '2')],
      note='IE1 = C I series limit (NIST ASD); rest = atom 12 u c^2; ex = 1D2, 1S0, 5S2 levels of C I; fs = 3P1, 3P2 above 3P0 (NIST ASD C I)'),
 dict(name='CO molecule (r_e 1.128 A)', R=1.128e-10, bind=D_CO, vib=2169.756*cm, rot=2*1.931602*cm, note='r_e CCCBDB exp. bond lengths; bind = D0 from 0 K enthalpies (CCCBDB); omega_e, B_e CCCBDB diatomic constants (2007Iri)'),
 dict(name='C2 molecule (r_e 1.243 A)', R=1.243e-10, bind=D_C2, vib=1855.066*cm, rot=2*1.820053*cm, note='same sources; D0 = 2 Hfg(C) - Hfg(C2) at 0 K'),
 dict(name='CH4, C-H edge (1.087 A)', R=1.087e-10, bind=D_CH4/4, note='bind = D0/4 (mean edge energy, not a measured bond energy); geometry CCCBDB exp.'),
 dict(name='benzene, mean edge (1.2405 A)', R=1.2405e-10, bind=D_C6H6/12, note='bind = D0/12 (mean edge energy); mean of 6 C-C 1.397 and 6 C-H 1.084 A'),
 dict(name='graphite in-plane C-C (1.42 A)', R=1.42e-10, bind=Ec/1.5, note='secondary geometry; bind = Ec/1.5 (3 neighbours, 1.5 bonds per atom)'),
 dict(name='diamond C-C bond (1.5445 A)', R=a_dia*sqrt(3)/4*1.0, bind=Ec/2, deb=kTh, ram=1332.7*cm, zpe=9/8*kTh, kT='f', heat=3*0.00180905,
      note='bind = Ec/2 (2 bonds per atom); Debye Theta from Cp(298.16 K) = 6.1149 J/mol K (NIST WebBook), k Theta = 0.16037 eV; Raman 1332.7 cm^-1 (secondary); heat = 3 x 0.00180905 eV per atom (Debye)'),
 dict(name='diamond lattice constant (3.5668 A)', R=a_dia, kT='f', note='kT at the lattice constant; cubic cell of 8 atoms'),
 dict(name='the gram (equal-volume sphere)', R=R_sph, rest=1e-3*299792458**2/1.602176634e-19, bind='N*B', note='rest = M c^2; bind = N x B (nuclear) as formula below; gram heat content 43.64 J not repeated per atom'),
]
rows.sort(key=lambda r: r['R'] if 'R' in r else r['n']*5.29177210903e-11/sqrt(r['rem1']/13.605693123))
# header
ws.cell(1, 1, 'Size (row) / energies at that size (columns); all energies in eV').font = bold
hdr = 3
ws.cell(hdr, 1, 'Size').font = bold; ws.cell(hdr, 1).fill = hdrfill
for k, h in cols:
    c = ws.cell(hdr, idx[k], h); c.font = bold; c.fill = hdrfill; c.alignment = Alignment(wrap_text=True, vertical='top')
nc = len(cols)+2
ws.cell(hdr, nc, 'What the numbers are / source').font = bold; ws.cell(hdr, nc).fill = hdrfill
fmt = '0.000E+00'
for i, r in enumerate(rows):
    rr = hdr+1+i
    ws.cell(rr, 1, r['name']).font = blk
    if 'n' in r: ws.cell(rr, idx['n'], r['n']).font = blue
    if 'R' in r: c = ws.cell(rr, idx['R'], r['R']); c.font = blue
    else:
        ie = '%s%d' % (L(idx['rem1']), rr); nn = '%s%d' % (L(idx['n']), rr)
        c = ws.cell(rr, idx['R'], '=%s*%s/SQRT(%s/%s)' % (nn, a0c, ie, Ry)); c.font = blk
        ws.cell(rr, idx['Q'], '=%s*SQRT(%s/%s)' % (nn, ie, Ry)).font = blk
    if 'Q' in r: ws.cell(rr, idx['Q'], r['Q']).font = blue
    Rc = '%s%d' % (L(idx['R']), rr)
    ws.cell(rr, idx['p12'], '=LOG(%s/%s)/LOG(12)' % (Rc, lP)).font = blk
    ws.cell(rr, idx['hcR'], '=%s/%s' % (hbarc, Rc)).font = blk
    if 'Q' in r or 'n' in r:
        ws.cell(rr, idx['coul'], '=%s*%s%d^2*%s%d' % (alpha, L(idx['Q']), rr, L(idx['hcR']), rr)).font = blk
    for k in ('rest', 'bind', 'rem1', 'rem2', 'rem3', 'ex1', 'ex2', 'ex3', 'fs1', 'fs2', 'vib', 'rot', 'deb', 'ram', 'zpe', 'heat'):
        if k in r and r[k] is not None and r[k] != 'f':
            if k == 'bind' and r[k] == 'N*B': ws.cell(rr, idx[k], '=%s*%s%d' % (Nc, L(idx[k]), 5)).font = blk   # N x B of the nucleus row (set below)
            else: ws.cell(rr, idx[k], r[k]).font = blue
    if r.get('kT') == 'f': ws.cell(rr, idx['kT'], '=%s*%s' % (kBc, Tc)).font = blk
    ws.cell(rr, nc, r['note']).font = blk
    for k in ('R',) + tuple(x for x, _ in cols if x not in ('R', 'Q', 'n', 'p12')):
        ws.cell(rr, idx[k]).number_format = fmt
    ws.cell(rr, idx['p12']).number_format = '0.000'; ws.cell(rr, idx['Q']).number_format = '0.000'
# fix the gram bind formula: reference the nucleus row's bind
nuc = next(i for i, r in enumerate(rows) if r['name'].startswith('12C nucleus')) + hdr + 1
gram = next(i for i, r in enumerate(rows) if r['name'].startswith('the gram')) + hdr + 1
ws.cell(gram, idx['bind'], '=%s*%s%d' % (Nc, L(idx['bind']), nuc)).font = blk
ws.cell(gram, nc, 'rest = M c^2; bind = N x (nuclear B of one 12C), a formula referencing the 12C row').font = blk
ws.freeze_panes = ws.cell(hdr+1, 2)
ws.column_dimensions['A'].width = 36
for k, _ in cols: ws.column_dimensions[L(idx[k])].width = 17
ws.column_dimensions[L(nc)].width = 90
ws.row_dimensions[hdr].height = 60
# cycles sheet
wc.cell(1, 1, 'Cycles = E / (hbar c / R) = R E / hbar c, for every energy in the Energies sheet (formulas; blank where the energy does not apply)').font = bold
wc.cell(hdr, 1, 'Size').font = bold; wc.cell(hdr, 1).fill = hdrfill
for k, h in cols:
    if k in ('R', 'p12', 'Q', 'n'): continue
    c = wc.cell(hdr, idx[k], h.replace('(eV)', '(cycles)')); c.font = bold; c.fill = hdrfill; c.alignment = Alignment(wrap_text=True, vertical='top')
wc.cell(hdr, idx['R'], 'Size R (m)').font = bold; wc.cell(hdr, idx['p12'], 'p12').font = bold
for i in range(len(rows)):
    rr = hdr+1+i
    wc.cell(rr, 1, "='Energies (eV)'!A%d" % rr).font = blk
    wc.cell(rr, idx['R'], "='Energies (eV)'!%s%d" % (L(idx['R']), rr)).number_format = fmt
    wc.cell(rr, idx['p12'], "='Energies (eV)'!%s%d" % (L(idx['p12']), rr)).number_format = '0.000'
    for k, _ in cols:
        if k in ('R', 'p12', 'Q', 'n', 'hcR'): continue
        src = "'Energies (eV)'!%s%d" % (L(idx[k]), rr); hc = "'Energies (eV)'!$%s%d" % (L(idx['hcR']), rr)
        c = wc.cell(rr, idx[k], '=IF(%s="","",%s/%s)' % (src, src, hc)); c.font = blk; c.number_format = '0.000E+00'
wc.freeze_panes = wc.cell(hdr+1, 2); wc.column_dimensions['A'].width = 36
for k, _ in cols: wc.column_dimensions[L(idx[k])].width = 17
wc.row_dimensions[hdr].height = 60
# notes sheet
notes = ['Carbon: size versus energy. Rows are sizes; columns are the different energies that live at that size. Energies in eV; the Cycles sheet divides each by hbar c / R.',
 'Blue = sourced or hardcoded input; black = formula. The size of the IE rows is n a0 / sqrt(IE/Ry) and the charge felt is Z_eff = n sqrt(IE/Ry): hydrogenic constructions, not measured radii.',
 'Sources (all in explore/data/): AME2020 (separation energies, binding); ENSDF 12C levels via IAEA livechart CSV (Kelley, Purcell, Sheu 2017); NIST ASD level files for C I and C II (energies, series limits IE1, IE2);',
 'PeriodicTableJSON (IE3-IE6; Wikipedia-derived, not NIST-checked); CCCBDB (bond lengths, 0 K enthalpies, omega_e, B_e); PDG 2024 (pion mass, N(1440)); CODATA 2022 (r_p) and 2018 (constants);',
 'NIST WebBook diamond Cp for the Debye temperature (Debye model, defined by Cp(298.16 K)); Raman 1332.7 cm^-1 and graphite geometry are secondary (search-result quotations).',
 'Not included (no sourced value or not applicable): hyperfine (12C has nuclear spin 0), nuclear giant resonances, N(1232) Delta, molecular electronic excited states, polyatomic vibrations, spin Zeeman (field dependent).',
 'Edge energies for CH4 and benzene are D0 divided by structural edges, not measured bond energies. Molecule rest energies are blank.',
 'No rule is proposed; the sheet is for examination.']
for i, t in enumerate(notes, start=1): wn.cell(i, 1, t).font = blk
wn.column_dimensions['A'].width = 180
wb.save(OUT)
print('saved', os.path.abspath(OUT), 'rows', len(rows), 'cols', len(cols))
print('check inputs: S_alpha %.1f S_p %.1f S_n %.1f B %.1f eV; D0 CO %.4f C2 %.4f CH4 %.4f C6H6 %.4f eV' % (Sa, Sp, Sn, B12, D_CO, D_C2, D_CH4, D_C6H6))

# ---------------- values-only copy (no LibreOffice on this machine, so the xlsx formulas have no cached values until Excel opens it)
import math
hc = 1.973269804e-7; al_ = 7.2973525693e-3; Ry_ = 13.605693123; a0_ = 5.29177210903e-11; lP_ = 1.616255e-35; kT_ = 8.617333262e-5*298.15
keys = [k for k, _ in cols]
vals = []
for r in rows:
    v = dict(r)
    if 'R' not in v:
        v['R'] = r['n']*a0_/math.sqrt(r['rem1']/Ry_); v['Q'] = r['n']*math.sqrt(r['rem1']/Ry_)
    v['p12'] = math.log(v['R']/lP_)/math.log(12); v['hcR'] = hc/v['R']
    if 'Q' in v: v['coul'] = al_*v['Q']**2*v['hcR']
    if v.get('kT') == 'f': v['kT'] = kT_
    vals.append(v)
nuc_b = next(v['bind'] for v in vals if v['name'].startswith('12C nucleus'))
for v in vals:
    if v.get('bind') == 'N*B': v['bind'] = N*nuc_b
with open(os.path.join(HERE, '..', 'maps', 'carbon_size_vs_energy_values.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['size'] + [h for _, h in cols] + ['cycles: ' + h for k, h in cols if k not in ('R', 'p12', 'Q', 'n', 'hcR')])
    for v in vals:
        w.writerow([v['name']] + [repr(v[k]) if k in v and v[k] != '' else '' for k in keys] +
                   [repr(v[k]/v['hcR']) if k in v else '' for k in keys if k not in ('R', 'p12', 'Q', 'n', 'hcR')])
print()
show = ['hcR', 'coul', 'rest', 'bind', 'rem1', 'ex1', 'fs1', 'vib', 'rot', 'deb', 'kT']
print('%-34s %10s %7s ' % ('size', 'R (m)', 'p12') + ' '.join('%10s' % k for k in show))
for v in vals:
    print('%-34s %10.3e %7.3f ' % (v['name'], v['R'], v['p12']) + ' '.join(('%10.3e' % v[k]) if isinstance(v.get(k), float) else '%10s' % '' for k in show))
