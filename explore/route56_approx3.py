"""
Optimised band top of the route56 operators on the periodic approximants of the icosahedral quasicrystal (continuation of route56_approx.py, which sampled 40 random K).
For tau = p/q: random starts (coarse), best 5 refined by pattern search on K (3D) maximising the top eigenvalue of H(K); operators B (consistent) and A (unit weight, /kappa).
Also: for A, the same maximum after dividing each site's row by its own degree-normalised scale is NOT used (no ad-hoc correction); instead the degree distribution and E_max*a for A
are reported per tau so the tau-dependence is visible.   Usage: py -3 -I -u route56_approx3.py p/q [nstart]
"""
import numpy as np, sys, importlib.util, os
from fractions import Fraction
here=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('route56_approx',os.path.join(here,'route56_approx.py')); ap=importlib.util.module_from_spec(sp); sp.loader.exec_module(ap)
def lan(H,m=90):                                       # top eigenvalue by Lanczos (full reorthogonalisation); checked against eigvalsh below
    d=H.shape[0]; r=np.random.default_rng(0); v=r.normal(size=d)+1j*r.normal(size=d); v/=np.linalg.norm(v); Vs=[v]; al=[];be=[]
    for k in range(m):
        w=H@Vs[-1]; a_=np.vdot(Vs[-1],w).real; al.append(a_); w=w-a_*Vs[-1]-(be[-1]*Vs[-2] if k>0 else 0)
        for u in Vs: w=w-np.vdot(u,w)*u
        b=np.linalg.norm(w)
        if b<1e-10: break
        be.append(b); Vs.append(w/b)
    T=np.diag(al)+np.diag(be[:len(al)-1],1)+np.diag(be[:len(al)-1],-1); return np.linalg.eigvalsh(T)[-1]
tau=Fraction(sys.argv[1]); nst=int(sys.argv[2]) if len(sys.argv)>2 else 24
rng=np.random.default_rng(7); gamma=np.array([0.0131,-0.0087,0.0049])
P,B,vol,idx,K=ap.cell_points(tau,gamma,7); N=len(P); nb=ap.build(P,B,0.78)
deg=np.array([len(x[1]) for x in nb]); kap=np.mean([np.linalg.norm(D,axis=1).sum()/3 for D,J in nb]); a=3*kap/deg.mean()
print(f"tau={tau}: N={N}, volume {vol:.3f}, degree mean {deg.mean():.2f} (min {deg.min()}, max {deg.max()}), kappa={kap:.4f}, a={a:.4f}, sqrt2/a={2**.5/a:.4f}",flush=True)
_k=np.array([1.2,-1.1,-0.7])
for _op in ("B","A"):
    Hc=ap.H_of_k(nb,N,_k,_op,kap); print(f"  Lanczos check {_op}: {lan(Hc):.10f} vs eigvalsh {np.linalg.eigvalsh(Hc)[-1]:.10f}",flush=True)
for op in ("B","A"):
    top=lambda k: lan(ap.H_of_k(nb,N,k,op,kap))
    starts=[]
    for _ in range(nst):
        kv=rng.normal(size=3); kv=kv/np.linalg.norm(kv)*rng.uniform(1.5,3.5); starts.append((top(kv),kv))
    starts.sort(key=lambda t:-t[0]); best=[]
    for v0,k in starts[:5]:
        k=k.copy(); v=v0; step=0.3
        while step>1e-3:
            imp=False
            for d in np.vstack([np.eye(3),-np.eye(3),(np.ones((1,3))*.577),-(np.ones((1,3))*.577)]):
                k2=k+step*d; v2=top(k2)
                if v2>v+1e-12: k,v,imp=k2,v2,True
            if not imp: step/=2
        best.append((v,k))
    best.sort(key=lambda t:-t[0]); v,k=best[0]
    print(f"  {op}: best top eigenvalue {v:.5f} at K={np.round(k,4)} (|K|={np.linalg.norm(k):.4f});  E_max*a = {v*a:.5f}  (coarse-start best {starts[0][0]*a:.5f}; five refined maxima E_max*a: {[round(b[0]*a,4) for b in best]})",flush=True)
