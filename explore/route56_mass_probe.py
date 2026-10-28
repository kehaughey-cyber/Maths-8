"""
Does the internal momentum act as a mass for the physical Weyl cone?  In the 4D icosian lattice Dirac operator (route56_lattice4d.py) E^(k,k') = 2|sum_pairs u sin(k.u + k'.sigma u)|/30.
Test E^^2 - |k|^2 at small physical k and fixed internal k' = r d, in 60-digit arithmetic (the effect is ~1e-12..1e-5):
  at k = 0 it is m(r)^2 with m = E^(0,k') ~ c r^7 (c ~ 1.6e-6, route56_lattice4d_prec.py);  if E^^2 = |k|^2 + m^2 the combination (E^^2 - |k|^2) is k-independent.
Also reports d(E^^2)/d|k|^2 - 1 (a change of the physical velocity induced by k') and any dependence on the direction of k.   Usage: py -3 -I -u route56_mass_probe.py
"""
import numpy as np, importlib.util, os, io, contextlib
from mpmath import mp, mpf, sqrt, sin
mp.dps=50
here=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('h',os.path.join(here,'route56_hecke.py')); h=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(h)
U=h.U; phi=(1+sqrt(5))/2; psi=1-phi
first=[i for i in range(120) if next(x for x in h.phys(U)[i] if abs(x)>1e-9)>0]
Pm=[[(int(U[i,c,0])+int(U[i,c,1])*phi)/2 for c in range(4)] for i in first]; Sm=[[(int(U[i,c,0])+int(U[i,c,1])*psi)/2 for c in range(4)] for i in first]
def E2(k,kp):
    V=[mpf(0)]*4
    for P,S in zip(Pm,Sm):
        a=sin(sum(k[c]*P[c] for c in range(4))+sum(kp[c]*S[c] for c in range(4)))
        for c in range(4): V[c]+=P[c]*a
    return (2*sum(v*v for v in V)**mpf('0.5')/30)**2
rng=np.random.default_rng(4)
def unit(): d=rng.normal(size=4); return [mpf(float(x)) for x in d/np.linalg.norm(d)]
print("r      direction of k   |k|     E^2-|k|^2        (E^2-|k|^2)/E^2(k=0)")
for r in (1,2,3):
    kp=[r*x for x in unit()]; m2=E2([mpf(0)]*4,kp)
    for t in range(2):
        e=unit()
        for kk in (mpf('0.01'),mpf('0.03'),mpf('0.1')):
            v=E2([kk*x for x in e],kp)-kk**2
            print(f"{r}   k-dir {t}        {mp.nstr(kk,3)}   {mp.nstr(v,8):>14}   {mp.nstr(v/m2,6)}")
    print(f"   (k = 0: m^2 = {mp.nstr(m2,6)}, m = {mp.nstr(sqrt(m2),6)})")
