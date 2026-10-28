"""
Second leg of the mass-fork test: along the PHYSICAL momentum (k'=0) and along mixed rays, the static Galois mass m(k,k')=sqrt|lam(k,k')lam(k',k)| (route56_massfork.py) against the dynamic energy E^(k,k').
Usage: py -3 -I -u route56_massfork_k.py
"""
import numpy as np, importlib.util, os, io, contextlib
here=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(here,'route56_massfork.py'),encoding='utf-8').read()
exec(compile(src[:src.index('print("m(0,0)')],'mf','exec'))
rng=np.random.default_rng(5)
print("physical ray, k'=0:  |k|, E^ , E^/|k|, m_static, m/12")
for t in range(3):
    d=rng.normal(size=4); d/=np.linalg.norm(d)
    for r in (0,0.1,0.3,0.6,1.0,1.5,2.0,2.5,3.0,3.5,4.0):
        k=r*d; z=np.zeros(4); print(f"  ray{t} |k|={r:4}: E^={Edyn(k,z):8.5f}  E^/|k|={(Edyn(k,z)/r if r else 1):8.5f}  m={mstat(k,z):9.5f}  m/12={mstat(k,z)/12:8.5f}")
print("\nmixed: k=0.3 d, k' = r d2:  r, E^, m")
for t in range(2):
    d=rng.normal(size=4); d/=np.linalg.norm(d); e=rng.normal(size=4); e/=np.linalg.norm(e)
    for r in (0,1,2,3,4,5):
        print(f"  r={r}: E^={Edyn(0.3*d,r*e):8.5f}  m={mstat(0.3*d,r*e):9.5f}   E^*m={Edyn(0.3*d,r*e)*mstat(0.3*d,r*e):8.4f}")
