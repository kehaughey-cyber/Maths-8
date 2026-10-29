# Carbon, everything stacked: one master table of every rung studied, sorted by size, with energy, cycles, information, mass and charge columns,
# plus the per-aspect tables (energy budget, information counts, couplings, through-the-gram rates, uncertainties). New file; nothing fitted; no rule proposed.
# Every number is recomputed here from the sourced inputs used in the earlier scripts, or copied from a named earlier .out (marked 'copied').
# Run: py -3 -I -u explore/carbon_stack.py > maps/carbon_complete_stack.md
import json, os
from mpmath import mp, mpf, pi, sqrt, log, nstr, exp, quad, findroot
mp.dps = 25
HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.join(HERE, 'data')
hbar = mpf('1.054571817e-34'); c = mpf('299792458'); G = mpf('6.67430e-11'); eV = mpf('1.602176634e-19'); kB = mpf('1.380649e-23'); u = mpf('1.66053906660e-27')
hbarc = mpf('1.973269804e-7'); al = mpf('7.2973525693e-3'); Ry = mpf('13.605693123'); a0 = mpf('5.29177210903e-11'); Rg = mpf('8.314462618')
me = mpf('510998.95'); mmu = mpf('105.6583755e6'); mtau = mpf('1776.93e6'); mp_ = mpf('938.27208816e6')
lP = sqrt(hbar*G/c**3); mP = sqrt(hbar*c/G)*c**2/eV
l12 = lambda x: log(x)/log(12); l10 = lambda x: log(x, 10)
cyc = lambda R, E: R*E/hbarc
bits = lambda cy: 2*pi*cy/log(2)
M = mpf('1e-3'); N = M/(12*u); Erest = M*c**2/eV; T = mpf('298.15')
a_dia = mpf('3.56683e-10'); V = N*a_dia**3/8; R_sph = (3*V/(4*pi))**(mpf(1)/3); r_bond = a_dia*sqrt(3)/4; r_ws = (3*V/(4*pi*N))**(mpf(1)/3)
r_ch = mpf('2.4702e-15'); B12 = mpf('92161735.2'); Mnuc = (12*u - 6*mpf('9.1093837015e-31'))*c**2/eV; Matom = 12*u*c**2/eV
r_pt = sqrt(mpf('5.4771029'))*mpf('1e-15'); r_p = mpf('0.84075e-15')
EL = {e['symbol']: e for e in json.load(open(os.path.join(DATA, 'PeriodicTableJSON.json'), encoding='utf-8'))['elements']}
IE = [mpf(x)/mpf('96.485332') for x in EL['C']['ionization_energies']]
Ec = mpf('711.2')/mpf('96.485332'); Zeff = 2*sqrt(IE[0]/Ry); R_val = 4*a0/Zeff
# Debye
D3 = lambda x: 3/x**3*quad(lambda t: t**3/(exp(t)-1), [0, x]); CvD = lambda x: 3/x**3*quad(lambda t: t**4*exp(t)/(exp(t)-1)**2, [0, x])
Th = findroot(lambda x: 3*Rg*CvD(x) - mpf('6.1149'), 7)*mpf('298.16'); kTh = kB*Th/eV
Eram = mpf('1332.7')*mpf('1.239841984e-4')
# rho graphite
R_gr = (3*(M/mpf('2267'))/(4*pi))**(mpf(1)/3)

# name, class, R m, E eV, mass eV or None, Q or None, count in gram or None, source
rows = [
 ('gram Compton wavelength hbar/(Mc)', 'bulk',   hbar/(M*c), Erest, Erest, None, 1, 'carbon_one_gram'),
 ('tau Compton',                     'lepton',  hbarc/mtau, mtau, mtau, 1, None, 'lepton_ladder'),
 ('proton Compton',                  'hadron',  hbarc/mp_,  mp_,  mp_,  1, 6*N, 'full_ladder'),
 ('12C nucleus, matter radius (point)', 'nuclear', r_pt, B12, Mnuc, 6, N, 'carbon_gram_remaining (isospin, no spin-orbit)'),
 ('12C nucleus, charge radius',      'nuclear', r_ch, B12, Mnuc, 6, N, 'carbon_one_gram'),
 ('muon Compton',                    'lepton',  hbarc/mmu, mmu, mmu, 1, None, 'lepton_ladder'),
 ('nucleon at r_p, E = m_p c^2',     'hadron',  r_p, mp_, mp_, 1, 12*N, 'nucleon_row (CODATA 2022 r_p)'),
 ('electron Compton',                'lepton',  hbarc/me, me, me, 1, 6*N, 'lepton_ladder'),
 ('C5+ 1s electron, a0/6, E = IE6',  'atomic',  a0/6, IE[5], None, 6, N, 'carbon_one_gram'),
 ('C valence, n=2, E = IE1',         'atomic',  R_val, IE[0], Matom, Zeff, N, 'carbon_one_gram'),
 ('H atom, a0, Ry',                  'atomic',  a0, Ry, mp_+me, 1, None, 'chemical_ladder'),
 ('CO2, mean C=O edge, D0/2',        'molecule', mpf('1.162e-10'), mpf('16.561067')/2, None, None, None, 'carbon_gram_remaining'),
 ('CH4, mean C-H edge, D0/4',        'molecule', mpf('1.087e-10'), mpf('17.016058')/4, None, None, None, 'carbon_gram_remaining'),
 ('CO, r_e, D0',                     'molecule', mpf('1.128e-10'), mpf('11.108424'), None, None, None, 'chemical_ladder'),
 ('C2H6, mean edge, D0/7',           'molecule', mpf('1.1545714e-10'), mpf('28.883147')/7, None, None, None, 'carbon_gram_remaining'),
 ('C6H6, mean edge, D0/12',          'molecule', mpf('1.2405e-10'), mpf('56.617932')/12, None, None, None, 'carbon_gram_remaining'),
 ('graphite in-plane C-C, Ec/1.5',   'lattice', mpf('1.42e-10'), Ec/mpf('1.5'), None, None, N*mpf('1.5'), 'carbon_gram_remaining (secondary geometry)'),
 ('diamond C-C, Ec/2',               'lattice', r_bond, Ec/2, None, None, 2*N, 'carbon_one_gram'),
 ('diamond Wigner-Seitz, Ec',        'lattice', r_ws, Ec, None, None, N, 'carbon_one_gram'),
 ('Debye quantum k Theta_D at C-C',  'phonon',  r_bond, kTh, None, None, 3*N, 'carbon_gram_remaining (Debye from Cp)'),
 ('Raman optical phonon at C-C',     'phonon',  r_bond, Eram, None, None, N, 'carbon_gram_remaining (secondary Raman)'),
 ('thermal kT (298.15 K) at lattice a', 'thermal', a_dia, kB*T/eV, None, None, N, 'carbon_one_gram'),
 ('graphite gram, equal-volume sphere, E = Mc^2', 'bulk', R_gr, Erest, Erest, None, 1, 'carbon_gram_remaining'),
 ('diamond gram, equal-volume sphere, E = Mc^2', 'bulk', R_sph, Erest, Erest, None, 1, 'carbon_one_gram'),
]
rows.sort(key=lambda r: r[2])
print('# Carbon, everything stacked (2026-10-29)')
print()
print('Generated by `explore/carbon_stack.py` (`py -3 -I -u explore/carbon_stack.py > maps/carbon_complete_stack.md`). One gram of carbon-12 as diamond unless a row says otherwise. Same dictionary throughout: cycles = R·E/ħc; bits = 2π·cycles/ln 2. Nothing fitted; no rule proposed. Sources are the earlier maps named in the last column; secondary or recalled inputs are named in `maps/carbon_gram_together.md`, `maps/carbon_gram_remaining.md` and `explore/data/*sourced_values.txt`.')
print()
print('## 1. Master table: every rung, by size')
print()
print('| rung | class | R (m) | p12 | E (eV) | cycles | cycles/(α/2) | bits/object | (m/m_P)² | αQ² | count in gram | source |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|')
for n, cl, R, E, m, Q, k, src in rows:
    cy = cyc(R, E)
    g = nstr((m/mP)**2, 4) if m is not None else '–'
    q = nstr(al*Q**2, 4) if Q is not None else '–'
    cnt = nstr(k, 4) if k is not None else '–'
    print(f'| {n} | {cl} | {nstr(R, 4)} | {nstr(l12(R/lP), 5)} | {nstr(E, 5)} | {nstr(cy, 5)} | {nstr(cy/(al/2), 4)} | {nstr(bits(cy), 4)} | {g} | {q} | {cnt} | {src} |')
print()
print('Reading the table: cycles = 1 on every Compton row by the definition; the bulk rows are 10^37 cycles; the chemical, lattice, phonon and thermal rows sit between 4.6e-5 and 6.6e-3 cycles (0.013 to 1.8 × α/2) = %s. Class "bulk" is the only place (m/m_P)² exceeds 1. Charge: the gram is neutral (6N positive, 6N negative).' % nstr(al/2, 5))
print()

print('## 2. Energy budget of one atom and of the gram')
print()
print('| item | eV per atom | J per gram | fraction of Mc² |')
print('|---|---|---|---|')
q_ud = 18*(mpf('2.16e6')+mpf('4.70e6'))
items = [('atom rest energy 12 u c²', Matom), ('nuclear rest energy', Mnuc), ('free nucleons 6p + 6n', 6*(mp_ + mpf('939.56542052e6'))), ('nuclear binding B', B12),
         ('18u + 18d bare masses (MS-bar 2 GeV)', q_ud), ('6 electrons rest', 6*me), ('sum of six ionization energies', sum(IE)), ('cohesion Ec', Ec), ('phonon zero point (9/8) k Θ_D', mpf(9)/8*kTh),
         ('Debye heat content at 298.15 K (per atom)', mpf('43.636776')/(N*eV)), ('thermal kT at 298.15 K', kB*T/eV)]
for n, e in items:
    print(f'| {n} | {nstr(e, 8)} | {nstr(e*eV*N, 6)} | {nstr(e*eV*N/(M*c**2), 5)} |')
print()
print('Quark masses are scheme-dependent: ±2% statistical (PDG ±0.07 MeV each), ±20% with the scale (copied, carbon_gram_refinements). About 99% of the atom is nucleon mass, not bare quark mass.')
print()

print('## 3. Information: three counts of the same gram')
print()
S_d = mpf('2.3782')/12/kB/log(2)
print('| count | bits | source |')
print('|---|---|---|')
print(f'| Bekenstein–Compton, diamond | {nstr(bits(cyc(R_sph, Erest)), 8)} | carbon_one_gram |')
print(f'| Bekenstein–Compton, graphite | {nstr(bits(cyc(R_gr, Erest)), 8)} | carbon_gram_remaining |')
print(f'| thermodynamic entropy, diamond 298.15 K | {nstr(S_d, 8)} | NIST WebBook (DeSorbo 1953) |')
print(f'| thermodynamic entropy, graphite-like (S 5.833–6.201) | {nstr(mpf("5.833")/12/kB/log(2), 6)} – {nstr(mpf("6.201")/12/kB/log(2), 6)} | NIST page, amorphous-labelled for the lower |')
print(f'| atoms | {nstr(N, 8)} (log2 = {nstr(log(N, 2), 6)} bits to label one) | AME/CODATA |')
print(f'| gap Bekenstein–Compton / thermodynamic (diamond) | {nstr(l10(bits(cyc(R_sph, Erest))/S_d), 6)} decades; graphite {nstr(l10(bits(cyc(R_gr, Erest))/(mpf("5.833")/12/kB/log(2))), 6)} – {nstr(l10(bits(cyc(R_gr, Erest))/(mpf("6.201")/12/kB/log(2))), 6)} | |')
print()

print('## 4. Couplings: the same quantity, "cycles of one pair\'s binding at any R"')
print()
print('| force | coupling | value | note |')
print('|---|---|---|---|')
print(f'| EM | αQ² (Q = 1) | {nstr(al, 8)} | virial: hydrogen is α/2; E/E_C = ½ |')
print(f'| gravity | (m/m_P)² | e {nstr((me/mP)**2, 4)}; p {nstr((mp_/mP)**2, 4)}; ¹²C {nstr((Mnuc/mP)**2, 4)}; gram {nstr((Erest/mP)**2, 4)} | passes 1 at the Planck mass |')
print(f'| strong, g1 scheme | C_F·α_g1(0) = 4π/3 | {nstr(mpf(4)/3*pi, 8)} | α_g1(0) = π (Deur–Brodsky–de Téramond 2016); ¹²C/that = {nstr(cyc(r_ch, B12)/(mpf(4)/3*pi), 6)}; nucleon/that = {nstr(cyc(r_p, mp_)/(mpf(4)/3*pi), 6)} |')
print(f'| strong, V scheme | C_F·α_V(0) | 0.56 (0.52–0.60) | ¹²C/that = {nstr(cyc(r_ch, B12)/mpf("0.56"), 5)} |')
print('| weak | – | not expressed | solar-neutrino crossings below |')
print()
print('Both sides of every colour comparison are standards; the scheme ambiguity (factor 7.5) exceeds the gaps, so those comparisons are undetermined, not matches or misses.')
print()

print('## 5. Charge content of the gram')
print()
print(f'Positive charge 6N e = {nstr(6*N*eV, 10)} C; all charges 12N e = {nstr(12*N*eV, 10)} C (= Faraday constant, since 12N = 1 mol); net 0. Unscreened Coulomb energy of the positive charge alone at the gram radius = {nstr(al*(6*N)**2*hbarc/R_sph/Erest, 5)} × Mc².')
print()

print('## 6. Through the gram (rates; copied from the named .out files)')
print()
print('| what | rate through / in the gram | source |')
print('|---|---|---|')
print('| solar pp + ⁷Be + pep neutrinos | 3.459e10 crossings s⁻¹ (pp 3.19e10, ⁷Be 2.61e9, pep 6.6e7) | carbon_gram_refinements |')
print('| solar ⁸B, hep | 2.75e6, 4.2e3 s⁻¹ | carbon_gram_remaining |')
print('| geo ν̄ (U + Th as listed) | 2.77e6 s⁻¹ | carbon_gram_remaining |')
print('| relic ν, all species at 0.0503 / 0.0087 eV | 5.5e10 / 3.2e11 s⁻¹ (isotropic, unclustered) | carbon_gram_remaining |')
print('| solar ν–e elastic interactions (order of magnitude) | ≈ 3e-11 s⁻¹ (2.6e-6 per day) | carbon_gram_refinements |')
print('| ¹⁴C decays (natural carbon, 0.226 Bq/g) | 0.226 β and 0.226 ν̄ s⁻¹ | carbon_one_gram |')
print('| cosmic muons, cube face 0.4327 cm² | 0.243–0.433 per minute (threshold-dependent) | carbon_gram_refinements |')
print('| atmospheric ν | not obtained as a number | – |')
print()

print('## 7. How much the inputs move it (copied)')
print()
print('| input | spread | effect |')
print('|---|---|---|')
print('| ¹²C charge radius 2.4702(22) fm; Mainz 2.464 | 0.1–0.6% | nuclear cycles 1.1508–1.1573 |')
print('| matter vs charge radius | 5.3% | nuclear cycles 1.0930 vs 1.1537 |')
print('| diamond lattice constant | 3e-5 | volume 1e-4 |')
print('| diamond → graphite | radius ×1.157 | +0.059 p12, bits ×1.157, gap 15.71 → ≈15.35–15.38 decades |')
print('| quark masses | ±2% stat, ±20% scale | share of atom 1.0–1.35% |')
print('| Debye Θ from Cp vs S | 0.2% | model-defined |')
print('| muon rate threshold | factor 1.78 | 0.24–0.43 per minute |')
print('| ¹⁴C ratio convention (5700 vs 5730 y) | 0.53% | derived ratio; not fixed |')
print()

print('## 8. What is identity, observed, open')
print()
print('- Identity: cycles = 1 at Compton; E/E_C = 1/α at Compton; ½ for hydrogen; bits = 2π·cycles/ln 2; the valence-rung rows.')
print('- Observed, not derived: nucleon radius = 3.9977 ± 0.0030 Compton lengths; ¹²C at 1.15 cycles (A^(4/3) growth); 15.7-decade information gap; neutrino-to-electron step; quark mass share ~1%; chemical shelf 22.6–23.75 p12; phonon quantum 0.034 × α/2.')
print('- Open: derivation of any ratio from the floor (none); which language places the levels; which count a level realises; weak column; atmospheric flux; ¹²C spin-orbit in the matter radius; secondary inputs (¹²C radius, diamond a, graphite structure, Raman frequency, geo table headings).')
