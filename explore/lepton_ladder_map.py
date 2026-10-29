# Lepton-to-atom ladder: known masses and lengths on one axis, raw successive ratios, logs in several bases.
# New file; floor untouched. No fitting, no search: this tabulates ratios between known quantities and prints them.
# cycles = R E/(hbar c); one cycle = 12 radits = 30 ticks = 2 pi nats = 2 pi/ln2 bits.
from mpmath import mp, mpf, pi, log, sqrt, nstr, floor, nint
mp.dps = 30
# Inputs (CODATA 2018 unless noted; printed digits are the digits of the inputs, not of the arithmetic).
hbar = mpf('1.054571817e-34'); c = mpf('299792458'); G = mpf('6.67430e-11')
me = mpf('9.1093837015e-31'); mmu = mpf('1.883531627e-28'); mtau = mpf('3.16754e-27')   # tau: CODATA 2018, 3.16754(21)e-27 kg
mp_ = mpf('1.67262192369e-27'); mn = mpf('1.67492749804e-27')
al = mpf('7.2973525693e-3'); eV = mpf('1.602176634e-19')
phi = (1+sqrt(5))/2
lP = sqrt(hbar*G/c**3); mnu = mpf('0.05')*eV/c**2   # 0.05 eV neutrino anchor is rough (as in positronium_map.py)
l12 = lambda x: log(x)/log(12); l10 = lambda x: log(x, 10); lphi = lambda x: log(x)/log(phi); l2 = lambda x: log(x, 2)
cy = lambda R, E: R*E/(hbar*c)
ln2 = log(2)

print('INPUTS: hbar', hbar, ' c', c, ' G', G, ' alpha', al)
print('masses (kg): e', me, ' mu', mmu, ' tau', mtau, ' p', mp_, ' n', mn)
print('phi', phi, ' ln phi', log(phi), ' ln 12', log(12), ' ln 2', ln2)
print()

parts = [('e', me), ('mu', mmu), ('p', mp_), ('n', mn), ('tau', mtau)]

print('PART A  each particle at its own Compton cut (BC cycles = 1 by construction) and positions on the ladders')
print(f'  {"name":4s} {"mass kg":>16s} {"m/m_e":>20s} {"lambda_C m":>16s} {"cycles":>8s} {"mass dec":>10s} {"mass p12":>10s} {"len dec":>10s} {"len p12":>10s}')
for n, m in parts:
    lam = hbar/(m*c)
    print(f'  {n:4s} {nstr(m,10):>16s} {nstr(m/me,18):>20s} {nstr(lam,10):>16s} {nstr(cy(lam, m*c**2),6):>8s} {nstr(l10(m/mnu),6):>10s} {nstr(l12(m/mnu),6):>10s} {nstr(l10(lam/lP),6):>10s} {nstr(l12(lam/lP),6):>10s}')
print('  mass ladder anchor: 0.05 eV neutrino (rough); length ladder anchor: Planck length')
print()

print('PART B  successive mass steps in mass order (ratio, ln, log base 10, 12, phi, 2) and distance of log_phi / log_12 to the nearest integer')
def steps(label, a, b):
    r = b/a
    lp = lphi(r); l1 = l12(r)
    print(f'  {label:10s} ratio {nstr(r,18):>22s}  ln {nstr(log(r),12):>14s}  log10 {nstr(l10(r),10):>12s}  log12 {nstr(l1,10):>12s}  logphi {nstr(lp,10):>12s}  (logphi - nearest int) {nstr(lp-nint(lp),6):>10s}  (log12 - nearest int) {nstr(l1-nint(l1),6):>10s}  log2 {nstr(l2(r),10):>12s}')
order = parts
for i in range(len(order)-1):
    steps(f'{order[i][0]}->{order[i+1][0]}', order[i][1], order[i+1][1])
print('  lepton chain:')
steps('e->mu', me, mmu); steps('mu->tau', mmu, mtau); steps('e->tau', me, mtau)
print('  other:')
steps('e->p', me, mp_); steps('mu->p', mmu, mp_); steps('p->tau', mp_, mtau); steps('p->n', mp_, mn)
print()

print('PART C  the electromagnetic triple for each lepton: r_l = alpha lambda_l (inner), lambda_l, a_l = lambda_l/alpha (outer). Step between neighbours is 1/alpha by definition.')
print('   1/alpha =', 1/al, ' ln =', log(1/al), ' log12 =', l12(1/al), ' logphi =', lphi(1/al), ' log2 =', l2(1/al))
trip = []
for n, m in [('e', me), ('mu', mmu), ('tau', mtau)]:
    lam = hbar/(m*c)
    for tag, R in [('r', al*lam), ('lam', lam), ('a', lam/al)]:
        trip.append((f'{tag}_{n}', R))
        print(f'  {tag+"_"+n:8s} {nstr(R,12):>18s} m   len dec {nstr(l10(R/lP),8):>10s}  len p12 {nstr(l12(R/lP),8):>10s}  cycles of binding alpha/2 at this R: {nstr(al/2,12)}')
print()

print('PART D  all lepton lengths from Part C merged and sorted ascending, raw successive ratios (no pairing imposed)')
trip.sort(key=lambda t: t[1])
print(f'  {"item":8s} {"R m":>18s} {"step from previous":>22s} {"ln step":>14s} {"log12 step":>12s} {"logphi step":>12s}')
prev = None
for n, R in trip:
    if prev is None:
        print(f'  {n:8s} {nstr(R,12):>18s}')
    else:
        r = R/prev
        print(f'  {n:8s} {nstr(R,12):>18s} {nstr(r,18):>22s} {nstr(log(r),10):>14s} {nstr(l12(r),8):>12s} {nstr(lphi(r),8):>12s}')
    prev = R
print()

print('PART E  hadron step, atomic scale of hydrogen with real proton, raw')
a0 = hbar/(me*c*al)
mred = me*mp_/(me+mp_)
a0_red = a0*me/mred
lam_p = hbar/(mp_*c)
print('  a0 (infinite-mass) =', a0, ' a0 (reduced mass, hydrogen) =', a0_red, ' ratio', a0_red/a0)
print('  lambda_p =', lam_p, '  lambda_e/lambda_p =', (hbar/(me*c))/lam_p, ' (= m_p/m_e)')
print('  a0 / lambda_p =', a0/lam_p, ' = (m_p/m_e)/alpha =', (mp_/me)/al)
print('  m_p/m_e =', mp_/me, ' ln', log(mp_/me), ' log12', l12(mp_/me), ' logphi', lphi(mp_/me), ' log2', l2(mp_/me))
print('  muon-atom Bohr radius (mu-p, reduced mass) =', a0*me/(mmu*mp_/(mmu+mp_)), ' m')
print()

print('PART F  Koide quantity Q = (m_e+m_mu+m_tau)/(sqrt m_e + sqrt m_mu + sqrt m_tau)^2 with the inputs above (floor C2.2 touches Koide); 2/3 for comparison')
Q = (me+mmu+mtau)/(sqrt(me)+sqrt(mmu)+sqrt(mtau))**2
print('  Q =', Q, '  Q - 2/3 =', Q-mpf(2)/3, '  (tau mass uncertainty 0.21e-27/3.16754e-27 =', nstr(mpf('0.00021')/mpf('3.16754'),4), 'relative)')
print()

print('PART G  reference: powers of phi (Lucas-type) next to the mass ratios, to read the nearest-integer residuals above without a lookup')
for k in [5,8,10,11,12,13,14,15,16,17,18]:
    print(f'  phi^{k:<3d} = {nstr(phi**k,15):>20s}')
