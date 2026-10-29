# Solid-state rungs for the sample, same dictionary. Data file path in argv[1] (parsed only). New file; nothing fitted.
# Wigner-Seitz radius r_ws = (3 A/(4 pi rho N_A))^(1/3) from density and mass; thermal energies kT at the melting and boiling points as proxies for the
# cohesive scale; cycles = r_ws * E/(hbar c), reported in units of alpha/2 (the hydrogen binding rung). Only entries with density >= 0.5 g/cm^3.
import json, sys, math
D = json.load(open(sys.argv[1], encoding='utf-8'))['elements']; by = {e['symbol']: e for e in D}
al = 7.2973525693e-3; Ry = 13.605693123; a0 = 5.29177210903e-11; kJ = 96.485332; kB = 8.617333262e-5; hc = 197.3269804e-9; NA = 6.02214076e23
sample = ['Li', 'Na', 'K', 'Cs', 'Be', 'Mg', 'Ca', 'Ba', 'Fe', 'Cu', 'Ag', 'W', 'Au', 'Al', 'Sn', 'Pb', 'Bi', 'B', 'Si', 'Ge', 'C', 'S', 'Br', 'I', 'La', 'Ce', 'Gd', 'Lu', 'U']
print('%-3s %-22s %11s %9s %9s %10s %10s %9s %11s %10s' % ('sym', 'class', 'r_ws (m)', 'kTm eV', 'kTb eV', 'cyc_m/(a/2)', 'cyc_b/(a/2)', 'IE1 eV', 'r_ws/R_val', 'kTb/IE1'))
rows = []
for s in sample:
    e = by[s]; rho = e.get('density_g_cm3'); Tm = e.get('melt'); Tb = e.get('boil'); IE = (e.get('ionization_energies') or [None])[0]
    if not rho or rho < 0.5 or not Tm or not Tb or not IE: continue
    r = (3*e['atomic_mass']/(4*math.pi*rho*NA))**(1/3)*1e-2
    n = len(e['shells']); E1 = IE/kJ; Z = n*math.sqrt(E1/Ry); Rv = n*n*a0/Z
    cm = r*kB*Tm/hc/(al/2); cb = r*kB*Tb/hc/(al/2)
    rows.append((s, e['category'], r, kB*Tm, kB*Tb, cm, cb, E1, r/Rv, kB*Tb/E1))
    print('%-3s %-22s %11.4e %9.4f %9.4f %10.5f %10.5f %9.4f %11.4f %10.4f' % rows[-1])
print('\nclass means of kTb/IE1 and r_ws/R_val:')
cl = {}
for r in rows: cl.setdefault(r[1], []).append(r)
for c, v in cl.items():
    print('  %-22s n=%d  kTb/IE1 %.4f..%.4f   r_ws/R_val %.3f..%.3f   cyc_b/(a/2) %.4f..%.4f' % (c, len(v), min(x[9] for x in v), max(x[9] for x in v), min(x[8] for x in v), max(x[8] for x in v), min(x[6] for x in v), max(x[6] for x in v)))
print('\nall rows: r_ws/R_val range %.3f..%.3f ; cyc_b/(a/2) range %.4f..%.4f ; kTb/IE1 range %.4f..%.4f' % (min(x[8] for x in rows), max(x[8] for x in rows), min(x[6] for x in rows), max(x[6] for x in rows), min(x[9] for x in rows), max(x[9] for x in rows)))
