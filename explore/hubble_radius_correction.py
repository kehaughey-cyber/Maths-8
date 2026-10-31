# Correction (2026-10-31): the 'Hubble radius c/H0' rung used in lattice_physical_map, anchor_investigation, ratios_128_137, energy_by_mass and the lab was 4.4e26 m.
# 4.4e26 m is the comoving radius of the observable universe (about 46.5 Gly), not c/H0. The repo's own value (explore/positronium_map.py) is c/H0 with H0 = 67.4 km/s/Mpc.
# This replays the affected numbers with c/H0. New file; the earlier files are not edited.
# Run: py -3 -I -X utf8 -u explore/hubble_radius_correction.py > explore/hubble_radius_correction.out
from math import sqrt, log, log10
PHI = (1 + sqrt(5))/2
c = 299792458.0; hbar = 1.054571817e-34; G = 6.67430e-11; lP = sqrt(hbar*G/c**3)
Mpc = 3.0856775814913673e22
print('l_P = %.6e m' % lP)
for H0kms in (67.4, 70.0, 73.0):
    RH = c/(H0kms*1e3/Mpc)
    k = log(RH/lP)/log(PHI)
    print('H0 = %.1f km/s/Mpc: c/H0 = %.6e m = %.3f Gly; k = log_phi(R/l_P) = %.4f (offset from nearest integer %+.4f); (R/l_P)^2 = %.4e; tick at that order = %.4e s' % (H0kms, RH, RH/9.4607304725808e15/1e9, k, k - round(k), (RH/lP)**2, RH/c))
R46 = 4.4e26
print('the value used before: 4.4e26 m = %.2f Gly; k = %.4f; (R/l_P)^2 = %.4e' % (R46/9.4607304725808e15/1e9, log(R46/lP)/log(PHI), (R46/lP)**2))
print('ratio 4.4e26 / c/H0(67.4) = %.4f ; in tower steps %.4f' % (R46/(c/(67.4e3/Mpc)), log(R46/(c/(67.4e3/Mpc)))/log(PHI)))
print('Spread of k over H0 = 67.4 to 73 : %.4f (so the tower position of c/H0 is uncertain by about +-%.2f)' % (log((73/67.4))/log(PHI), log((73/67.4))/log(PHI)/2))
print('Age scales: 1/H0 = %.4e s (H0 = 67.4); age of universe used in the lab: 13.8 Gyr = %.4e s' % (1/(67.4e3/Mpc), 13.8e9*3.15576e7))
