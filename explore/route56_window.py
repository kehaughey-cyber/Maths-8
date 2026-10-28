"""
Window-restricted 4D icosian lattice Dirac operator (follows route56_lattice4d.py).
Lambda = { x in I : |x|^2 <= A (physical ball), |sigma(x)|^2 <= B (internal ball) }, I the icosian lattice (Z-span of the 120 units, exact doubled integer coordinates).
Edges x ~ x+u for the 120 units u whose endpoints are both in Lambda.  Chiral block (W f)(x) = sum_u Q(u) f(x+u) restricted to Lambda; H = [[0,W],[W^dag,0]], so the spectrum is +- singular values of W.
Normalised E^ = s/30 (the bulk lattice has E^ = |k| at small physical k, k' flat to order 7).
Reports: |Lambda|, boundary fraction, singular values; counts with E^ < eps against the bulk prediction 2 N P(eps) from the uniform 8-torus (route56_lattice4d.py, recomputed here);
and the character of the lowest modes: overlap of the lowest-M right singular subspace with (i) polynomials of degree <= d in the INTERNAL coordinates sigma(x) and (ii) polynomials of degree <= d in the PHYSICAL
coordinates x (each times C^2), orthonormalised on Lambda.   No fit.   Usage: py -3 -I -u route56_window.py A B [dmax]
"""
import numpy as np, importlib.util, os, io, contextlib, sys, itertools
here=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('h',os.path.join(here,'route56_hecke.py')); h=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(h)
sd=h.sd; U=h.U; PHI=h.PHI; PSI=h.PSI
A=float(sys.argv[1]); B=float(sys.argv[2]); dmax=int(sys.argv[3]) if len(sys.argv)>3 else 4
M=U.reshape(120,8).astype(np.int64)
def lattice_basis(M):                                   # integer row reduction to a basis of the Z-span
    M=[list(r) for r in M]; basis=[]
    for col in range(8):
        rows=[r for r in M if r[col]!=0]
        while len(rows)>1:
            rows.sort(key=lambda r:abs(r[col])); p=rows[0]
            for r in rows[1:]:
                q=r[col]//p[col]
                for t in range(8): r[t]-=q*p[t]
            rows=[r for r in rows if r[col]!=0]
        if rows: basis.append(rows[0]); M=[r for r in M if r is not rows[0] and any(r)]
    return np.array(basis,dtype=np.int64)
Bs=lattice_basis(M); assert Bs.shape==(8,8) and abs(round(np.linalg.det(Bs.astype(float))))>0
# every unit must be an integer combination of the basis
cf=np.rint(np.linalg.solve(Bs.T.astype(float),M.T.astype(float))).T; assert np.allclose(cf@Bs,M)
def _emb(Bm):
    v=Bm.reshape(-1,4,2); return np.hstack([((v[...,0]+v[...,1]*PHI)/2),((v[...,0]+v[...,1]*PSI)/2)])
def lll(Bm,delta=0.99):                                 # LLL on the rows (embedded in R^8 with the lattice metric), integer ops mirrored on Bm
    Bm=Bm.copy(); n=len(Bm)
    def gs():
        Ev=_emb(Bm); Q=np.zeros_like(Ev); mu=np.zeros((n,n))
        for i in range(n):
            Q[i]=Ev[i]
            for j in range(i): mu[i,j]=Ev[i]@Q[j]/(Q[j]@Q[j]); Q[i]-=mu[i,j]*Q[j]
        return Q,mu
    k=1
    while k<n:
        Q,mu=gs()
        for j in range(k-1,-1,-1):
            q=int(round(mu[k,j]))
            if q: Bm[k]-=q*Bm[j]; Q,mu=gs()
        if Q[k]@Q[k] >= (delta-mu[k,k-1]**2)*(Q[k-1]@Q[k-1]): k+=1
        else: Bm[[k,k-1]]=Bm[[k-1,k]]; k=max(k-1,1)
    return Bm
Bs=lll(Bs)
def phy(v): return (v.reshape(-1,4,2)[...,0]+v.reshape(-1,4,2)[...,1]*PHI)/2
def per(v): return (v.reshape(-1,4,2)[...,0]+v.reshape(-1,4,2)[...,1]*PSI)/2
Pm=phy(Bs); Sm=per(Bs)                                  # (8,4) rows: coordinates of basis vectors
G=Pm@Pm.T+Sm@Sm.T; L=np.linalg.cholesky(G)             # |x|^2+|sigma x|^2 = n G n^T
Qmax=A+B
pts=[]
def rec(level,partial,n):                               # Fincke-Pohst on n G n^T <= Qmax using upper-triangular form R = L^T
    R=L.T
    if level<0: pts.append(n.copy()); return
    s=sum(R[level,j]*n[j] for j in range(level+1,8)); rem=Qmax-partial
    if rem<0: return
    r=np.sqrt(rem)/R[level,level]; c=-s/R[level,level]
    for v in range(int(np.ceil(c-r)),int(np.floor(c+r))+1):
        n[level]=v; t=R[level,level]*v+s; rec(level-1,partial+t*t,n)
    n[level]=0
rec(7,0.0,np.zeros(8,dtype=np.int64)); N0=np.array(pts)
X=N0@Bs; xp=phy(X); xs=per(X); keep=((xp**2).sum(1)<=A+1e-9)&((xs**2).sum(1)<=B+1e-9)
X=X[keep]; xp=xp[keep]; xs=xs[keep]; N=len(X)
print(f"A={A}, B={B}: lattice points with |x|^2<={A}, |sigma x|^2<={B}: N={N}",flush=True)
index={tuple(r):i for i,r in enumerate(X)}
Uf=U.reshape(120,8); Qu=np.array([sd.Qmat(p) for p in h.phys(U)])
W=np.zeros((2*N,2*N),complex); deg=np.zeros(N,int)
for i,r in enumerate(X):
    for a in range(120):
        j=index.get(tuple(r+Uf[a]))
        if j is not None: W[2*i:2*i+2,2*j:2*j+2]+=Qu[a]; deg[i]+=1
print(f"   degrees: min {deg.min()}, mean {deg.mean():.1f}, max {deg.max()} (bulk 120);  fraction of sites with full degree: {np.mean(deg==120):.3f}",flush=True)
w2,Vv=np.linalg.eigh(W.conj().T@W); o=np.argsort(-w2); sv=np.sqrt(np.abs(w2[o])); Vh=Vv[:,o].conj().T; Eh=sv/30      # singular values via W^dag W (adequate for E^ > 1e-4)
# bulk prediction from the uniform 8-torus
rng=np.random.default_rng(0); first=[i for i in range(120) if next(x for x in h.phys(U)[i] if abs(x)>1e-9)>0]
Pu=h.phys(U)[first]; th=rng.uniform(0,2*np.pi,size=(300000,8)); ph=th@Uf[first].astype(float).T
Ek=2*np.linalg.norm(np.einsum('mj,ja->ma',np.sin(ph),Pu),axis=1)/30
print("   eps    count(E^<eps)   bulk-torus prediction 2N P(eps)   ratio")
for e in (0.01,0.02,0.05,0.1,0.2,0.5):
    c=int(np.sum(Eh<e)); pr=2*N*np.mean(Ek<e); print(f"   {e:5.2f}  {c:8d}   {pr:14.1f}   {c/max(pr,1e-9):8.2f}")
print(f"   smallest E^: {Eh[-6:]}",flush=True)
# character of the lowest modes
def polyspace(coords,d):
    mons=[m for deg_ in range(d+1) for m in itertools.combinations_with_replacement(range(4),deg_)]
    F=np.stack([np.prod(coords[:,list(m)],axis=1) if m else np.ones(len(coords)) for m in mons],1)
    cols=[]
    for k in range(F.shape[1]):
        for s in range(2):
            v=np.zeros(2*N,complex); v[s::2]=F[:,k]; cols.append(v)
    Bm=np.array(cols).T; Q,R=np.linalg.qr(Bm); keepc=np.abs(np.diag(R))>1e-8*np.abs(R).max(); return Q[:,keepc]
Vlow=lambda Mn: Vh[-Mn:].conj().T                       # right singular vectors of the Mn smallest singular values
print("   lowest-M right singular subspace: share inside polynomials (deg<=d) of sigma(x) [internal] vs of x [physical], each x C^2:")
for d in range(1,dmax+1):
    Pi=polyspace(xs,d); Pp=polyspace(xp,d)
    row=[]
    for Mn in (20,100,400):
        Vl=Vlow(min(Mn,2*N)); row.append(f"M={Mn}: int {np.linalg.norm(Pi.conj().T@Vl)**2/Vl.shape[1]:.3f} phys {np.linalg.norm(Pp.conj().T@Vl)**2/Vl.shape[1]:.3f}")
    print(f"      d={d} (dims {Pi.shape[1]}/{Pp.shape[1]}): "+";  ".join(row),flush=True)
