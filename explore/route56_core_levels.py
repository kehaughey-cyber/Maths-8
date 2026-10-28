"""
Lowest eigenvalue clusters of D_A/kappa on the refined 600-cell with their (left-2I, right-2I) irreps (uses the characters of route56_core.py), n = 1, 2, 3.
Shows what the Galois-conjugate blocks (right irreps 2', 3', 4g) do: exactly zero (n=1, 2) or lifted to a finite level (n=3), and how far.
Usage: py -3 -I -u route56_core_levels.py [n ...]
"""
import numpy as np, importlib.util, os, sys, io, contextlib
here=os.path.dirname(os.path.abspath(__file__))
def load(name):
    sp=importlib.util.spec_from_file_location(name,os.path.join(here,name+'.py')); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
with contextlib.redirect_stdout(io.StringIO()): core=load('route56_core')
sd=core.sd; V=core.V; CH=core.CH
def run(n,ncl=14):
    P,E=sd.subdivide(V,n); N=len(P); Q=np.array([sd.Qmat(p) for p in P]); key={tuple(np.round(p,6)+0.0):i for i,p in enumerate(P)}
    D=np.zeros((2*N,2*N),complex); ths=[]; nbr=[[] for _ in range(N)]
    for a,b in E: nbr[a].append(b); nbr[b].append(a)
    for i in range(N):
        s_=0
        for j in nbr[i]:
            c=float(np.clip(P[i]@P[j],-1,1)); s=np.sqrt(1-c*c); D[2*i:2*i+2,2*j:2*j+2]=(Q[j]@Q[i].conj().T-c*sd.I2)/s; s_+=np.arccos(c)
        ths.append(s_/3)
    kap=np.mean(ths); w,U=np.linalg.eigh(D); w=w/kap
    # clusters of |w| (tol 1e-7), nonnegative side of the spectrum sorted by |w|
    order=np.argsort(np.abs(w)); cl=[]; cur=[order[0]]
    for t in order[1:]:
        if abs(abs(w[t])-abs(w[cur[0]]))<2e-6: cur.append(t)
        else: cl.append(cur); cur=[t]
    cl.append(cur)
    perms=[]
    for g in V:
        Qg=sd.Qmat(g); iL=np.empty(N,int); iR=np.empty(N,int)
        for i,p in enumerate(P):
            for M,idx in ((Qg@Q[i],iL),(Q[i]@Qg,iR)):
                v=np.array([(1j*np.trace(s@M)/2).real for s in core.sig]); q=np.array([(np.trace(M)/2).real,*v]); idx[i]=key[tuple(np.round(q,6)+0.0)]
        perms.append((Qg,iL,iR))
    print(f"\n==== n={n}: N={N}, kappa={kap:.5f}; lowest eigenvalue clusters (|lambda|/kappa-scaled): value, multiplicity, left-2I content, right-2I content")
    for c in cl[:ncl]:
        Vs=U[:,c]; m=len(c); X=Vs.reshape(N,2,m); chl=np.zeros(120); chr_=np.zeros(120)
        for k,(Qg,iL,iR) in enumerate(perms):
            out=np.zeros_like(X); out[iL]=np.einsum('ab,nbm->nam',Qg,X); chl[k]=np.vdot(Vs,out.reshape(2*N,m)).real
            out=np.zeros_like(X); out[iR]=X; chr_[k]=np.vdot(Vs,out.reshape(2*N,m)).real
        f=lambda ch:{k:round(float(np.sum(ch*CH[k])/120),2) for k in CH if abs(np.sum(ch*CH[k])/120)>0.05}
        print(f"   |lam|={abs(w[c[0]]):.6f}  x{m:3d}  L {f(chl)}   R {f(chr_)}",flush=True)
if __name__=="__main__":
    for n in [int(a) for a in sys.argv[1:]] or [1,2,3]: run(n)
