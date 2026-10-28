"""High-precision check (mpmath, 60 digits) of the order at which the internal sector k=0, k'!=0 of the 4D icosian lattice Dirac operator acquires energy:
E^(0,k') = 2|sum_pairs u sin(k'.sigma u)|/30 for k' = r*d (fixed random unit d), r = 0.02, 0.04, 0.08: ratios give the exponent p in E ~ r^p.   Usage: py -3 -I -u route56_lattice4d_prec.py"""
import numpy as np, importlib.util, os, io, contextlib
from mpmath import mp, mpf, sqrt, sin
mp.dps=60
here=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('h',os.path.join(here,'route56_hecke.py')); h=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(h)
U=h.U; phi=(1+sqrt(5))/2; psi=1-phi
first=[i for i in range(120) if next(x for x in h.phys(U)[i] if abs(x)>1e-9)>0]
Pm=[[ (int(U[i,c,0])+int(U[i,c,1])*phi)/2 for c in range(4)] for i in first]; Sm=[[ (int(U[i,c,0])+int(U[i,c,1])*psi)/2 for c in range(4)] for i in first]
rng=np.random.default_rng(1); 
for trial in range(3):
    d=rng.normal(size=4); d/=np.linalg.norm(d); d=[mpf(float(x)) for x in d]; out=[]
    for r in (mpf('0.02'),mpf('0.04'),mpf('0.08')):
        V=[mpf(0)]*4
        for P,S in zip(Pm,Sm):
            a=sin(r*sum(d[c]*S[c] for c in range(4)))
            for c in range(4): V[c]+=P[c]*a
        out.append(2*sqrt(sum(v*v for v in V))/30)
    print(f"direction {trial}: E^ = {[mp.nstr(x,6) for x in out]}; exponents log2 ratios: {mp.nstr(mp.log(out[1]/out[0],2),5)}, {mp.nstr(mp.log(out[2]/out[1],2),5)}")
