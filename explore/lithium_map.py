# Lithium through the positronium/hydrogen dictionary. Sourced inputs only (Wikipedia 'Lithium' infobox; CRC work function via Wikipedia 'Work function';
# cohesive energy from arXiv 2602.16679 (experimental, ZPE-corrected); Fermi energy Ashcroft-Mermin via HyperPhysics). New file; nothing fitted.
# cycles = R E/(hbar c); 1 cycle = 12 radits = 30 ticks = 2 pi nats. Radii of the ionic/valence rungs come from the measured ionization energy via
# a hydrogenic effective charge (Z_eff = n sqrt(IE/Ry)), not from a fit to any other quantity.
import math
al = 7.2973525693e-3; Ry = 13.605693123; hc = 197.3269804e-9   # eV*m
a0 = 5.29177210903e-11; lP = 1.616255e-35; kJ = 96.485332
IE = [520.2/kJ, 7298.1/kJ, 11815.0/kJ]
l10 = lambda x: math.log10(x); l12 = lambda x: math.log(x)/math.log(12)
print('INPUTS (eV): IE1 %.6f  IE2 %.6f  IE3 %.6f   (Wikipedia kJ/mol 520.2, 7298.1, 11815.0 / %.6f)' % (IE[0], IE[1], IE[2], kJ))
print('IE3/(9 Ry) = %.6f  (hydrogenic Li2+)' % (IE[2]/(9*Ry)))
rows = []
def add(name, R, E): rows.append((name, R, E, R*E/hc))
Z1 = 2*math.sqrt(IE[0]/Ry); Z2 = math.sqrt(IE[1]/Ry); Z3 = 3.0
add('Li2+ 1s  (IE3, R=a0/3)', a0/3, IE[2])
add('Li+  1s  (IE2, R=a0/Zeff, Zeff=%.4f)' % Z2, a0/Z2, IE[1])
add('Li   2s  (IE1, R=4a0/Zeff, Zeff=%.4f)' % Z1, 4*a0/Z1, IE[0])
a = 350.93e-12; nn = a*math.sqrt(3)/2
solid = [('cohesive energy 1.66 eV', 1.66), ('work function 2.9 eV (CRC)', 2.9), ('Fermi energy 4.74 eV (free-electron)', 4.74),
         ('heat of vaporization 136 kJ/mol', 136/kJ), ('heat of fusion 3.00 kJ/mol', 3.00/kJ),
         ('kT at melting point 453.65 K', 8.617333262e-5*453.65), ('kT at 300 K', 8.617333262e-5*300)]
for n, E in solid: add('solid @ nn: ' + n, nn, E)
print('\nbcc a = 350.93 pm (Arblaster 2018), nearest-neighbour distance nn = a sqrt3/2 = %.6e m' % nn)
print('\n%-58s %14s %14s %12s %10s %10s' % ('row', 'R (m)', 'cycles', 'cycles/(a/2)', 'R dec>lP', 'R p12>lP'))
for n, R, E, c in rows:
    print('%-58s %14.6e %14.8e %12.6f %10.4f %10.4f' % (n, R, c, c/(al/2), l10(R/lP), l12(R/lP)))
print('\nZ_eff*alpha/2 check for the three ionic/valence rungs:', [round(z*al/2, 10) for z in (Z3, Z2, Z1)])
print('nn / R(2s) = %.6f ;  nn / a0 = %.6f ;  nn/lambda_e = %.4f' % (nn/(4*a0/Z1), nn/a0, nn/3.8615926772e-13))
print('Li-core capacities: shell n holds 2n^2 states; Li = 1s^2 2s^1: 2 + 1 of 8; spin-1/2 doublet = 2 states')
print('IE ratios: IE2/IE1 = %.6f  IE3/IE1 = %.6f  IE3/IE2 = %.6f' % (IE[1]/IE[0], IE[2]/IE[0], IE[2]/IE[1]))
