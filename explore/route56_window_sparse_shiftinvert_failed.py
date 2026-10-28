"""
SPARSE window-restricted 4D icosian lattice Dirac operator (SciPy). Same lattice, edges, Q(u) and bulk prediction as route56_window.py (which is dense and limited to A=B~4).
H^2 = W^dag W (s=30*E^) is diagonalised near 0 by Lanczos (scipy eigsh, which='LA') on the filter T=(I-H2/lmax)^m, m=argv[4] (default 30; shift-invert was tried at A=B=4 and did not finish in 10 min: fill-in of an 8D graph);
the eigenvalues are then re-evaluated as Rayleigh quotients of H2 on the returned vectors, with the residual norms reported. K lowest eigenpairs.
Reports N, degree fractions, count(E^<eps) against the bulk 8-torus prediction 2N P(eps) (the count is only complete for eps below the K-th eigenvalue; flagged), and polynomial shares (internal/physical) of the lowest 20 and 100 modes.
Usage: py -3 -I -u route56_window_sparse.py A B K [m]
"""
import numpy as np, importlib.util, os, io, contextlib, sys, itertools
here=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('h',os.path.join(here,'route56_hecke.py')); h=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(h)
sd=h.sd; U=h.U; PHI=h.PHI; PSI=h.PSI
A=float(sys.argv[1]); B=float(sys.argv[2]); K=int(sys.argv[3])
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
import scipy.sparse as sps, scipy.sparse.linalg as spl, time
Uf=U.reshape(120,8); Qu=np.array([sd.Qmat(p) for p in h.phys(U)])
t0=time.time(); rows=[];cols=[];vals=[]; deg=np.zeros(N,int)
for i,r in enumerate(X):
    for a in range(120):
        j=index.get(tuple(r+Uf[a]))
        if j is not None:
            deg[i]+=1
            for s in range(2):
                for t in range(2): rows.append(2*i+s); cols.append(2*j+t); vals.append(Qu[a][s,t])
W=sps.csr_matrix((vals,(rows,cols)),shape=(2*N,2*N),dtype=complex); del rows,cols,vals
print(f"   degrees: min {deg.min()}, mean {deg.mean():.1f}, max {deg.max()};  full-degree fraction {np.mean(deg==120):.3f};  nnz {W.nnz};  build {time.time()-t0:.0f}s",flush=True)
H2=(W.conj().T@W).tocsc()
t0=time.time(); lmax=float(spl.eigsh(H2,k=1,which='LA',return_eigenvectors=False)[0])*1.02; MM=int(sys.argv[4]) if len(sys.argv)>4 else 30
def _T(v):
    for _ in range(MM): v=v-H2@v/lmax
    return v
Top=spl.LinearOperator(H2.shape,matvec=_T,dtype=complex)
_,Vv=spl.eigsh(Top,k=K,which='LA',tol=1e-6,maxiter=2000); Vv,_=np.linalg.qr(Vv)
HV=H2@Vv; Rm=Vv.conj().T@HV; w2,Z=np.linalg.eigh((Rm+Rm.conj().T)/2); Vv=Vv@Z; res=np.linalg.norm(H2@Vv-Vv*w2,axis=0)
Eh=np.sqrt(np.abs(w2))/30
print(f"   lmax(s^2)={lmax:.1f}; eigsh k={K} done in {time.time()-t0:.0f}s;  E^ of the K lowest: {Eh[0]:.3e} .. {Eh[-1]:.4f};  max residual |H2v-lv|/l_max: {res.max()/lmax:.2e}",flush=True)
rng=np.random.default_rng(0); first=[i for i in range(120) if next(x for x in h.phys(U)[i] if abs(x)>1e-9)>0]
Pu=h.phys(U)[first]; th=rng.uniform(0,2*np.pi,size=(300000,8)); ph=th@Uf[first].astype(float).T
Ek=2*np.linalg.norm(np.einsum('mj,ja->ma',np.sin(ph),Pu),axis=1)/30
print("   eps    count(E^<eps)   bulk 2N P(eps)   ratio    [complete iff eps <= %.4f]"%Eh[-1])
for e in (0.001,0.003,0.01,0.02,0.05,0.1,0.2,0.5):
    c=int(np.sum(Eh<e)); pr=2*N*np.mean(Ek<e); print(f"   {e:6.3f}  {c:8d}   {pr:12.1f}   {c/max(pr,1e-9):8.2f}   {'complete' if e<=Eh[-1] else 'TRUNCATED'}")
import itertools
def polyspace(coords,d):
    mons=[m for deg_ in range(d+1) for m in itertools.combinations_with_replacement(range(4),deg_)]
    F=np.stack([np.prod(coords[:,list(m)],axis=1) if m else np.ones(len(coords)) for m in mons],1)
    cols=[]
    for k in range(F.shape[1]):
        for s in range(2):
            v=np.zeros(2*N,complex); v[s::2]=F[:,k]; cols.append(v)
    Bm=np.array(cols).T; Q,R=np.linalg.qr(Bm); keepc=np.abs(np.diag(R))>1e-8*np.abs(R).max(); return Q[:,keepc]
print("   share of lowest-M modes inside polynomials deg<=d of sigma(x) [int] vs x [phys]  (random baseline = dim/(2N))")
for d in (2,4,6):
    Pi=polyspace(xs,d); Pp=polyspace(xp,d); row=[]
    for Mn in (20,100):
        Vl=Vv[:,:Mn]; row.append(f"M={Mn}: int {np.linalg.norm(Pi.conj().T@Vl)**2/Mn:.3f} phys {np.linalg.norm(Pp.conj().T@Vl)**2/Mn:.3f}")
    print(f"      d={d} dim {Pi.shape[1]} base {Pi.shape[1]/(2*N):.4f}: "+";  ".join(row),flush=True)
