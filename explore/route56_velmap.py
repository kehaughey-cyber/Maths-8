"""
Exact velocity matrix of the 4D icosian lattice Weyl block (route56_lattice4d.py):
 E^(k,k') = 2|V|/30, V = sum_pairs P sin(k.P + k'.S),  P = physical 4-vector of a unit, S = its Galois conjugate.
 To first order in k:  V = M(k') k,  M(k') = sum_pairs P P^T cos(k'.S);  v-matrix = 2M/30 = (1/15) sum_pairs P P^T cos(k'.S).
 Reports: M(0)=I; eigenvalues of v-matrix vs |k'|; minimum over k' of the spectral norm and of |det|; whether any k' gives v=0.
Usage: py -3 -I -u route56_velmap.py
"""
import numpy as np, importlib.util, os, io, contextlib
from scipy.optimize import minimize
here=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('h',os.path.join(here,'route56_hecke.py')); h=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(h)
U=h.U; phi=(1+5**.5)/2; psi=1-phi
first=[i for i in range(120) if next(x for x in h.phys(U)[i] if abs(x)>1e-9)>0]
P=np.array([[(int(U[i,c,0])+int(U[i,c,1])*phi)/2 for c in range(4)] for i in first])
S=np.array([[(int(U[i,c,0])+int(U[i,c,1])*psi)/2 for c in range(4)] for i in first])
PP=np.einsum('ia,ib->iab',P,P)
def vm(kp): return np.einsum('i,iab->ab',np.cos(S@kp),PP)/15
print("v(0) - I max abs:",abs(vm(np.zeros(4))-np.eye(4)).max(),"  (pairs",len(first),")")
rng=np.random.default_rng(1)
print("\n|k'|   eigenvalues of v(k') for 3 random directions (sorted)")
for r in (0.5,1,2,3,4,6):
    for t in range(3):
        d=rng.normal(size=4); d/=np.linalg.norm(d)
        print(f"{r:4}  ",np.round(np.linalg.eigvalsh(vm(r*d)),6))
# is v isotropic (multiple of identity) ?  spread of eigenvalues relative to trace/4 over random k'
sp_=[]
for _ in range(2000):
    k=rng.normal(size=4)*rng.uniform(0,4); w=np.linalg.eigvalsh(vm(k)); sp_.append(w.max()-w.min())
print("\nmax eigenvalue spread over 2000 random k' (|k'|<~4*N(0,1)):",max(sp_)," median:",np.median(sp_))
# minima
def nrm(k): return np.linalg.norm(vm(k),2)
def dtm(k): return abs(np.linalg.det(vm(k)))
best=[]
for _ in range(300):
    k0=rng.normal(size=4)*rng.uniform(0.5,8)
    r=minimize(nrm,k0,method='Nelder-Mead',options=dict(xatol=1e-12,fatol=1e-14,maxiter=4000))
    best.append((r.fun,np.linalg.norm(r.x),r.x))
best.sort(key=lambda t:t[0])
print("\nminimum of spectral norm ||v(k')|| over 300 starts (lowest 8): value, |k'|")
for f,n,x in best[:8]: print(f"  {f:.10f}  {n:.5f}")
mx=[]
for _ in range(300):
    k0=rng.normal(size=4)*rng.uniform(0.5,8)
    r=minimize(lambda k:-np.linalg.eigvalsh(vm(k)).min(),k0,method='Nelder-Mead',options=dict(xatol=1e-12,fatol=1e-14,maxiter=4000))
    mx.append(-r.fun)
print("most negative eigenvalue of v(k') found:",-max(mx))
mn=[]
for _ in range(300):
    k0=rng.normal(size=4)*rng.uniform(0.5,8)
    r=minimize(dtm,k0,method='Nelder-Mead',options=dict(xatol=1e-12,fatol=1e-16,maxiter=4000))
    mn.append((r.fun,np.linalg.norm(r.x)))
mn.sort(); print("min |det v(k')| (lowest 5):",mn[:5])
# smallest |k'| where the *largest* eigenvalue first hits 0 along random rays
print("\nalong rays: first |k'| where max eigenvalue of v(k') changes sign / min |eig|")
for t in range(6):
    d=rng.normal(size=4); d/=np.linalg.norm(d)
    rs=np.linspace(0,12,12001); ev=np.array([np.linalg.eigvalsh(vm(r*d)) for r in rs])
    cr=[(rs[i]) for i in range(1,len(rs)) if ev[i,-1]*ev[i-1,-1]<0]
    print(f"  ray {t}: first zero of top eig {cr[:1]}, min |top eig| on [0,12] = {abs(ev[:,-1]).min():.4g}, mean eig at r=12: {ev[-1].mean():.4g}")
