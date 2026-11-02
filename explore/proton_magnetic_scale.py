# What length and mass the proton's magnetic moment implies (the 0.358 of the moment-ratio comparison, read as a scale). New file (2026-11-02); nothing fitted.
# The instrument's ring moment is current x area; a charge e circling at c on radius R has mu = e c R / 2.  So a measured moment mu defines R_mag = 2 mu / (e c) and, with R = hbar/(m c), a mass m_eff = hbar/(c R_mag).
# Sourced inputs: explore/data/moment_benchmark_sourced_values.txt (CODATA 2022), saved IAEA table (neutron, proton r_p from carbon maps).  The quark relations are textbook (from memory).
# Run: py -3 -I -X utf8 -u explore/proton_magnetic_scale.py > explore/proton_magnetic_scale.out
import math
e = 1.602176634e-19; h = 6.62607015e-34; hbar = h/(2*math.pi); c = 299792458.0
muB = 9.2740100657e-24; mup = 1.41060679545e-26; MPME = 1836.152673426; rp = 0.84075e-15; lP = 1.616255e-35; phi = (1+5**0.5)/2
me = e*hbar/(2*muB); mp = me*MPME; muN = e*hbar/(2*mp); lam_p = hbar/(mp*c); mpMeV = mp*c**2/e/1e6
Rm = 2*mup/(e*c)
print('proton reduced Compton length', lam_p, 'm ; charge radius r_p', rp, 'm =', rp/lam_p, 'lambda_p')
print('R_mag = 2 mu_p/(e c) =', Rm, 'm =', Rm/lam_p, 'lambda_p = ', Rm/rp, 'r_p ; 1/(R_mag/lambda_p) =', lam_p/Rm, '(the 0.358)')
print('m_eff = hbar/(c R_mag) = m_p/(mu_p/mu_N) =', mpMeV/(mup/muN), 'MeV ;', 'm_p/3 =', mpMeV/3, 'MeV')
mun = 1.9130427
print('neutron, quark relation mu_n = -(2/3)(m_p/m_q) mu_N (textbook): m_q =', (2/3)*mpMeV/mun, 'MeV ; proton, mu_p = (m_p/m_q) mu_N: m_q =', mpMeV/2.792847351, 'MeV ; they differ by', ((2/3)*mpMeV/mun)/(mpMeV/2.792847351)-1)
print('hbar c / m_eff =', 197.3269804/(mpMeV/(mup/muN)), 'fm')
print('position on the phi tower, k = log_phi(L / l_P):')
for name, L in (('proton Compton lambda_p', lam_p), ('R_mag', Rm), ('proton charge radius r_p', rp)): print(f'   {name:26s} {L:.5e} m  k = {math.log(L/lP)/math.log(phi):.4f}')
print('R_mag / r_p =', Rm/rp, ' (compare 1/sqrt 2 =', 2**-0.5, ': noticed, not claimed)')
print('lambda_p / R_mag =', lam_p/Rm, ' = ', 1/(mup/muN), '= 1/(mu_p in nuclear magnetons)')
