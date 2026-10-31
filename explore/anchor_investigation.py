# Which tower copy sits at the Planck length: the choice tested, not assumed. New file; nothing fitted.
# Question: if the 600-cell copy at order k=0 is tied to l_P through different lattice lengths (edge chord, edge arc, S^3 radius, antipode distance, S^3 circumference),
# where do the measured rungs fall, and how much nested structure does each order contain?
# Tower: copy k has edge chord e_k = e_0 phi^k (recursive, both directions, no smallest copy). Rung R is read as the same lattice length at its own order.
# Run: py -3 -I -X utf8 -u explore/anchor_investigation.py > explore/anchor_investigation.out
import math
from math import sqrt, pi, log
PHI = (1 + sqrt(5))/2
c = 299792458.0; hbar = 1.054571817e-34; G = 6.67430e-11; lP = sqrt(hbar*G/c**3)
hc = 1.973269804e-7
rungs = [('tau Compton', hc/1776.93e6), ('proton Compton', hc/938.27208816e6), ('nucleon r_p', 0.84075e-15), ('muon Compton', hc/105.6583755e6), ('12C charge radius', 2.4702e-15),
         ('electron Compton', hc/0.51099895e6), ('C5+ 1s radius', 5.29177210903e-11/6), ('Bohr radius', 5.29177210903e-11), ('diamond C-C', 3.56683e-10*sqrt(3)/4), ('diamond a', 3.56683e-10),
         ('1 g radius', 4.0808074e-3), ('Hubble c/H0 (recalled, ~8%)', 4.4e26)]
# lattice lengths of one copy in units of the edge chord (unit S^3: chord 1/phi, arc pi/5, radius 1, antipode pi, circumference 2 pi)
chord = 1/PHI
L = [('edge chord', 1.0), ('edge arc (36 deg)', (pi/5)/chord), ('S3 radius', 1/chord), ('antipode distance (pi R)', pi/chord), ('S3 great circle (2 pi R)', 2*pi/chord)]
print('Lattice lengths in units of the edge chord (unit S^3): ' + '; '.join('%s = %.6f' % (n, v) for n, v in L))
print('Anchor: that length at order k=0 equals l_P = %.6e m. Rung R read as the same length at order k: k = log_phi(R / l_P) + log_phi(length factor)... shown below as k = log_phi(R/l_P) - log_phi(factor).' % lP)
print()
print('k of each rung under each anchor (fractional offset to nearest integer in brackets)')
hdr = '%-30s' % 'rung' + ''.join('%-28s' % n for n, _ in L)
print(hdr)
rows = {}
for nm, R in rungs:
    out = '%-30s' % nm
    for an, f in L:
        k = log(R/lP)/log(PHI) - log(f)/log(PHI)
        out += '%-28s' % ('%.4f [%+.4f]' % (k, k - round(k)))
    print(out)
print()
print('How many rungs sit within +-0.02 of an integer, per anchor (the 11 rungs without the Hubble radius; expected by chance 11 x 0.04 = 0.44):')
for an, f in L:
    n = 0; hits = []
    for nm, R in rungs[:-1]:
        k = log(R/lP)/log(PHI) - log(f)/log(PHI)
        if abs(k - round(k)) <= 0.02: n += 1; hits.append('%s %+.4f' % (nm, k - round(k)))
    print('  %-28s %d  %s' % (an, n, '; '.join(hits)))
print('  Changing the anchor adds the same constant to every k, so it cannot change how the rungs are spread relative to each other; it only changes which rung, if any, lands on an integer.')
print()
print('Nested structure per order, anchor = edge chord at k=0 (each copy: 120 vertices, 720 edges, 600 cells; diameter 5 edges; 30-tick clock; fold at 15 ticks):')
print('%-30s %-12s %-14s %-16s %-16s %-16s' % ('rung', 'order k', 'copies 0..k', 'vertices 0..k', 'order-0 ticks per', 'order-0 edges per'))
print('%-30s %-12s %-14s %-16s %-16s %-16s' % ('', '', '', '(120 each)', 'tick of order k', 'edge of order k'))
for nm, R in rungs:
    k = log(R/lP)/log(PHI); kn = round(k)
    print('%-30s %-12.4f %-14d %-16d %-16.6e %-16.6e' % (nm, k, kn + 1, 120*(kn + 1), R/lP, R/lP))
print('  (order-0 ticks per tick of order k = R/l_P because tick = edge/c at every order; it is the same number as order-0 edges per edge of order k.)')
print()
print('Raw counts at the largest rung, edge anchor: k = %.4f; (R/l_P)^2 = %.6e; (R/l_P)^3 = %.6e; phi^(2k) = %.6e.' % (log(4.4e26/lP)/log(PHI), (4.4e26/lP)**2, (4.4e26/lP)**3, PHI**(2*log(4.4e26/lP)/log(PHI))))
print('  Orders from the Planck copy to the gram radius: %.4f; to the Hubble radius: %.4f.' % (log(4.0808074e-3/lP)/log(PHI), log(4.4e26/lP)/log(PHI)))
print()
print('Ticks of one copy per tick of a larger one (the same clock count at both orders, 30-tick cycle): ratio of tick durations between orders j and k is phi^(k-j); between adjacent orders %.6f.' % PHI)
