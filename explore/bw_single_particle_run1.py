"""
Single-particle Bohr-Weisskopf correction to the 1s hyperfine splitting of Re-187, Pb-207 and Bi-209 (hydrogen-like).  New file (2026-11-03).  Nothing fitted.
Replaces the two bounds of nuclear_size_hfs.py (uniform sphere / thin shell of magnetization) by the magnetization of the valence nucleon: orbital current + spin magnetization of a
Woods-Saxon single-particle state |l, j, m = j>, with the depth set by the measured separation energy (AME2020, explore/data/ame2020_mass_1.mas20.txt).
Units: electron hbar = c = m_e = 1 (nuclear radii in fm are converted with lambda_e).  Dirac 1s electron in the finite (uniform-sphere) nuclear charge, from nuclear_size_hfs.solve.

Derivation (all in this file's comments, nothing assumed).  The electron's transition current is toroidal and L = 1: J_e = c(r) sin(theta) phi-hat, c = G F / r^2 (G = r g, F = r f, normalised int (G^2+F^2) dr = 1).  Its vector potential
A_e = a(r) sin(theta) phi-hat with a = (4 pi/3) a~, a~(r) = (1/r^2) int_0^r c r'^3 dr' + r int_r^inf c dr'   (the L = 1 kernel r_< / r_>^2).  The point-dipole radial integral is I = int_0^inf c dr, a~ -> r I for a point nucleus.
Energy shift = -int j_nuc . A_e dV (orbital current j) and -int M . B_e dV (spin magnetization M, B_e = curl A_e), B_e = (2 a cos(th)/r) r-hat - (sin(th)/r)(a + r a') th-hat.
Ratios to the point dipole of the same total moment:  W_orb = < a~(r)/(r I) >_R   (R the nucleon radial density),  W_spin = N_spin/(2 I g_s <s_z>),
N_spin = int r dr int sin(th) dth R^2 [ M_z (2 a~ cos^2 + (a~ + r a~') sin^2) + M_rho sin cos (a~ - r a~') ],   M_z = (c1^2 T1^2 - c2^2 T2^2)/2 , M_rho = c1 c2 T1 T2   (per unit g_s),
|j, m> = c1 Y_{l, m-1/2} up + c2 Y_{l, m+1/2} down.   a~ + r a~' = 2 r T - C3/r^2,  a~ - r a~' = 2 C3/r^2,  T = int_r^inf c dr', C3 = int_0^r c r'^3 dr'.
Checks printed: (1) the same code with an s-wave, spin-only, uniform density of radius R must reproduce delta_BW(uniform) of nuclear_size_hfs.py; (2) the point limit gives W = 1; (3) the Clebsch-Gordan sign is checked against a numerical diagonalisation of J^2.
delta_BW = [g_l <l_z> W_orb + g_s <s_z> W_spin] / [g_l <l_z> + g_s <s_z>] - 1   (Schmidt fractions, free g_s; also with g_s quenched to 0.6 of free).
Usage:  py -3 -I -X utf8 -u explore/bw_single_particle.py > explore/bw_single_particle.out
"""
import math, os, re, sys, importlib.util
import numpy as np
here = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location('nsh', os.path.join(here, 'nuclear_size_hfs.py')); nsh = importlib.util.module_from_spec(sp); sp.loader.exec_module(nsh)
ALPHA, LAM = nsh.ALPHA, nsh.LAMBDA_E_FM
HBARC = 197.3269804; MN = 938.918754                      # MeV fm ; nucleon mass (MeV), mean of n and p
HB2M = HBARC**2/(2*MN)                                   # hbar^2 / 2m in MeV fm^2

# ---------- angular functions (Condon-Shortley), Gauss-Legendre in cos(theta)
XG, WG = np.polynomial.legendre.leggauss(80)
def Theta(l, m, x):
    """normalised theta part with int Theta^2 sin(th) dth = 1; Y_lm = Theta e^{i m phi}/sqrt(2 pi), CS phase (-1)^m for m >= 0; m < 0 by Y_{l,-m} = (-1)^m conj(Y_lm)"""
    if abs(m) > l: return np.zeros_like(x)
    am = abs(m); P = np.polynomial.legendre.Legendre.basis(l).deriv(am)(x) if am > 0 else np.polynomial.legendre.Legendre.basis(l)(x)
    t = math.sqrt((2*l+1)/2*math.factorial(l-am)/math.factorial(l+am))*(-1)**am*(1-x*x)**(am/2)*P
    return t if m >= 0 else (-1)**am*t
def spinor_coeffs(l, j2):
    """j = l +- 1/2, m = j.  returns (c1, c2, m_l_up, m_l_down) with |j,j> = c1 Y_{l,mu} up + c2 Y_{l,md} down"""
    m = j2/2.0
    if j2 == 2*l+1: return 1.0, 0.0, int(round(m-0.5)), int(round(m+0.5))
    return -math.sqrt((l-m+0.5)/(2*l+1)), math.sqrt((l+m+0.5)/(2*l+1)), int(round(m-0.5)), int(round(m+0.5))

def check_cg(l, j2):
    """diagonalise J^2 in the (m_l, m_s) space for m_j = j and compare the relative sign with the closed form"""
    mj = j2/2.0; basis = []
    for ms in (0.5, -0.5):
        ml = mj-ms
        if abs(ml) <= l+1e-9: basis.append((int(round(ml)), ms))
    n = len(basis); J2 = np.zeros((n, n))
    for a, (ml, ms) in enumerate(basis): J2[a, a] = l*(l+1)+0.75+2*ml*ms
    # L+ S- + L- S+ terms:  <ml+1, ms-1| L+ S- |ml, ms> with ms = +1/2 -> -1/2 ; coefficient sqrt((l-ml)(l+ml+1)) * 1
    for a, (ml, ms) in enumerate(basis):
        for b, (ml2, ms2) in enumerate(basis):
            if ms == 0.5 and ms2 == -0.5 and ml2 == ml+1: J2[b, a] += math.sqrt((l-ml)*(l+ml+1)); J2[a, b] += math.sqrt((l-ml)*(l+ml+1))
    w, v = np.linalg.eigh(J2); jj = j2/2.0; k = int(np.argmin(abs(w-jj*(jj+1)))); vec = v[:, k]
    c1, c2, mu, md = spinor_coeffs(l, j2)
    if n == 1: return True, w[k]
    # basis order: ms = +1/2 first, then -1/2
    sgn = np.sign(vec[0]*vec[1]); return (sgn == np.sign(c1*c2)), (w[k], vec)

# ---------- nucleon radial wave function in a Woods-Saxon well
def ws_state(A, Zc, proton, l, j2, nodes, S_mev, r0=1.25, a=0.65, lam_so=2.0, vso_frac=0.44, rc=1.2, nsteps=6000, rmax_extra=14.0):
    Rw = r0*A**(1/3); rmax = Rw+rmax_extra; h = rmax/nsteps; r = np.linspace(h, rmax, nsteps)
    ls = 0.5*(j2/2.0*(j2/2.0+1) - l*(l+1) - 0.75); f = 1/(1+np.exp((r-Rw)/a)); dfdr = -f*(1-f)/a
    Rc = rc*A**(1/3); VC = np.where(r < Rc, Zc*ALPHA*HBARC*(3-(r/Rc)**2)/(2*Rc), Zc*ALPHA*HBARC/r) if proton else 0*r
    E = -S_mev; hh = h*h
    def shoot(V0):
        # Numerov for y'' = k2 y:  (1 - hh k2_{i+1}/12) y_{i+1} = 2 (1 + 5 hh k2_i/12) y_i - (1 - hh k2_{i-1}/12) y_{i-1}
        V = -V0*f + vso_frac*V0*lam_so/r*dfdr*ls + VC; k2 = l*(l+1)/r**2 + (V-E)/HB2M
        y = np.zeros(nsteps); y[0] = r[0]**(l+1); y[1] = r[1]**(l+1); nn = 0
        for i in range(1, nsteps-1):
            y[i+1] = (2*(1+5*hh*k2[i]/12)*y[i] - (1-hh*k2[i-1]/12)*y[i-1])/(1-hh*k2[i+1]/12)
            if y[i+1]*y[i] < 0: nn += 1
        return y, nn
    lo, hi = 15.0, 140.0
    assert shoot(lo)[1] <= nodes and shoot(hi)[1] > nodes, 'depth bracket does not contain the eigenvalue'
    for _ in range(70):
        mid = 0.5*(lo+hi)
        if shoot(mid)[1] > nodes: hi = mid
        else: lo = mid
    V0 = 0.5*(lo+hi); y, nn = shoot(V0)
    ia = int(np.sum(r <= Rw+2.0)); cut = nsteps-1
    for i in range(ia, nsteps-1):
        if abs(y[i+1]) > abs(y[i]): cut = i; break
    y = y.copy(); y[cut:] = 0.0
    u = y/math.sqrt(np.sum(y**2)*h); Rr = u/r
    return r, Rr, V0, Rw, float(np.sqrt(np.sum(u**2*r**2)*h)), nn

# ---------- electron side: a~(r), r a~'(r) on the electron solution
def electron_functions(Z, Rn_fm):
    R = Rn_fm/LAM
    E, sol = nsh.solve(Z, R); xs = np.array([s[0] for s in sol]); G = np.array([s[1] for s in sol]); F = np.array([s[2] for s in sol]); r = np.exp(xs)
    norm = np.trapezoid((G**2+F**2)*r, xs); c = G*F/r**2/norm                      # c = G F / r^2 with int(G^2+F^2) dr = 1
    ci = c*r                                                                       # integrand per dx
    I = np.trapezoid(ci, xs)
    cum = lambda f: np.concatenate(([0.0], np.cumsum(0.5*(f[1:]+f[:-1])*np.diff(xs))))
    C3 = cum(c*r**3*r); T = I - cum(ci)
    at = C3/r**2 + r*T; rat_p = 2*r*T - C3/r**2; rat_m = 2*C3/r**2                 # a~, a~ + r a~', a~ - r a~'
    return dict(E=E, r=r, xs=xs, c=c, I=I, at=at, atp=rat_p, atm=rat_m, C3=C3, T=T, R=R)

def interp_e(ef, r_e, key):
    r = ef['r']; f = ef[key]; out = np.interp(r_e, r, f)
    lo = r_e < r[0]
    if np.any(lo): out[lo] = f[0]*(r_e[lo]/r[0])                                    # linear in r below the grid (a~ ~ r I)
    return out

def weights(ef, r_fm, Rr, l, j2):
    """W_orb, W_spin, <l_z>, <s_z> for the stretched state |l, j, m = j> with radial function Rr (int Rr^2 r^2 dr = 1, r in fm)"""
    h = r_fm[1]-r_fm[0]; w = Rr**2*r_fm**2*h; r_e = r_fm/LAM; I = ef['I']
    a1 = interp_e(ef, r_e, 'at'); a2 = interp_e(ef, r_e, 'atp'); a3 = interp_e(ef, r_e, 'atm')
    c1, c2, mu, md = spinor_coeffs(l, j2); x = XG; sw = WG
    T1 = Theta(l, mu, x); T2 = Theta(l, md, x)
    lz = c1**2*mu + c2**2*md; sz = 0.5*(c1**2-c2**2)
    Wo = np.sum(w*a1/(r_e*I))
    Mz = 0.5*(c1**2*T1**2 - c2**2*T2**2); Mr = c1*c2*T1*T2; cos2 = x*x; sin2 = 1-cos2; sc = x*np.sqrt(1-x*x)
    # int sin(th) dth = int dx
    ang_z = np.array([np.sum(sw*Mz*(2*a1[k]*cos2 + a2[k]*sin2)) for k in range(len(r_e))])
    ang_r = np.array([np.sum(sw*Mr*sc*a3[k]) for k in range(len(r_e))])
    Ns = np.sum(Rr**2*r_fm**2*h*(ang_z+ang_r)/r_e)                              # int r dr R^2 (...) with r dr in electron units: r_fm^2 dr_fm/r_e ; r_e-scaled below
    # a~ carries electron length units: (a~ r_e^-1) is dimensionless-per-I; w includes r_fm^2 dr_fm, the 1/r factor is 1/r_e
    Ws = Ns/(2*I*sz) if abs(sz) > 0 else float('nan')
    return Wo, Ws, lz, sz

def schmidt_delta(Wo, Ws, lz, sz, proton, gs_scale=1.0):
    gl = 1.0 if proton else 0.0; gs = (5.5856946893 if proton else -3.8260854)*gs_scale
    mo = gl*lz; ms = gs*sz; mu = mo+ms
    return (Wo*mo + Ws*ms)/mu - 1, mo, ms

# ---------- AME separation energies
def ame():
    d = {}
    for line in open(os.path.join(here, 'data', 'ame2020_mass_1.mas20.txt'), encoding='utf-8', errors='replace'):
        t = line.split()
        if len(t) < 7 or not t[0].lstrip('-').isdigit(): continue
        try: N, Z, A = int(t[1]), int(t[2]), int(t[3])
        except ValueError: continue
        for tok in t[5:]:
            if re.fullmatch(r'-?\d+\.\d+#?', tok): d[(Z, A)] = float(tok.rstrip('#')); break
    return d
D = ame(); DN = 8071.31806; DH = 7288.971064
def Sp(Z, A): return (D[(Z-1, A-1)] + DH - D[(Z, A)])/1000.0
def Sn(Z, A): return (D[(Z, A-1)] + DN - D[(Z, A)])/1000.0

if __name__ == '__main__':
    print('== check 3: Clebsch-Gordan relative sign against numerical diagonalisation of J^2 (True = same relative sign)')
    for l, j2 in [(2, 5), (1, 1), (5, 9), (4, 7)]:
        ok, info = check_cg(l, j2); print(f'  l = {l}, j = {j2}/2: {ok}')
    print('\n== check 1 and 2: s-wave, spin only, uniform density in radius R_N versus the old uniform-sphere magnetization (same electron wave function)')
    for name, Z, Rch in [('209Bi82+', 83, 5.5211), ('207Pb81+', 82, 5.4943), ('187Re74+', 75, 5.3698)]:
        Rn = math.sqrt(5/3)*Rch; ef = electron_functions(Z, Rn)
        r_fm = np.linspace(Rn/4000, 2.0*Rn, 4000)      # uniform s-wave density, zero beyond R_N
        Rr = np.where(r_fm < Rn, math.sqrt(3/Rn**3), 0.0)
        nrm = np.sum(Rr**2*r_fm**2*(r_fm[1]-r_fm[0])); Rr = Rr/math.sqrt(nrm)
        Wo, Ws, lz, sz = weights(ef, r_fm, Rr, 0, 1)
        r = ef['r']; c = ef['c']; M = np.where(r < ef['R'], (r/ef['R'])**3, 1.0); old = np.trapezoid(c*r*M, ef['xs'])/ef['I']
        print(f'  {name}: new code W_spin = {Ws:.8f} (delta = {Ws-1:+.6f}); old uniform-sphere integral {old:.8f} (delta = {old-1:+.6f}); <s_z> = {sz}')
        # point limit: all density at tiny radius
        r2 = np.linspace(1e-5, 1e-3, 400); R2 = np.where(True, 1.0, 0.0)*r2**0; R2 = R2/math.sqrt(np.sum(R2**2*r2**2*(r2[1]-r2[0])))
        Wo2, Ws2, _, _ = weights(ef, r2, R2, 0, 1); print(f'    point limit: W_orb = {Wo2:.8f}, W_spin = {Ws2:.8f}')
    print('\n== single-particle states.  Woods-Saxon r0 = 1.25 fm, a = 0.65 fm, spin-orbit 0.44 V0 (hbar/m_pi c)^2, depth set by the separation energy (AME2020).  Free Schmidt g factors.')
    cases = [  # name, Z, A, Rch (fm, hydrogenlike_series ion table), proton?, l, j2, nodes, separation energy from AME
        ('187Re74+', 75, 187, 5.3698, True, 2, 5, 0, Sp(75, 187)),
        ('207Pb81+', 82, 207, 5.4943, False, 1, 1, 1, Sn(82, 208)),
        ('209Bi82+', 83, 209, 5.5211, True, 5, 9, 0, Sp(83, 209))]
    results = {}
    for name, Z, A, Rch, prot, l, j2, nodes, S in cases:
        Rn = math.sqrt(5/3)*Rch; ef = electron_functions(Z, Rn)
        print(f'\n{name}: valence {"proton" if prot else "neutron (hole)"} l = {l}, j = {j2}/2, nodes {nodes}, separation energy {S:.4f} MeV, electron-side E = {ef["E"]:.10f}, I = {ef["I"]:.8e}')
        for tag, kw in [('r0=1.25 a=0.65', {}), ('r0=1.20 a=0.60', dict(r0=1.20, a=0.60)), ('r0=1.30 a=0.70', dict(r0=1.30, a=0.70)), ('S-2 MeV', dict(S_shift=-2.0)), ('S+2 MeV', dict(S_shift=2.0))]:
            S_use = S + kw.pop('S_shift', 0.0)
            try: r_fm, Rr, V0, Rw, rrms, nn_ = ws_state(A, Z-1, prot, l, j2, nodes, S_use, **kw)
            except Exception as e: print(f'  {tag}: failed: {e}'); continue
            Wo, Ws, lz, sz = weights(ef, r_fm, Rr, l, j2)
            line = f'  {tag:16s} V0 = {V0:7.3f} MeV, rms radius of the orbital {rrms:.3f} fm, <l_z> = {lz:+.4f}, <s_z> = {sz:+.4f}, W_orb = {Wo:.6f}, W_spin = {Ws:.6f};'
            for gsc in (1.0, 0.6):
                dl, mo, ms = schmidt_delta(Wo, Ws, lz, sz, prot, gsc); line += f'  g_s x {gsc}: delta_BW = {dl:+.6f} (mu_orb {mo:+.3f}, mu_spin {ms:+.3f})'
            print(line)
            if tag == 'r0=1.25 a=0.65': results[name] = (Wo, Ws, lz, sz, prot)
    print('\n(165Ho66+ is not modelled: its ground state 7/2- is a deformed Nilsson state with no spherical |l, j = 7/2> partner in the proton shell below Z = 82 of the right parity; Re-187 is also deformed, so its number is a spherical estimate.)')
