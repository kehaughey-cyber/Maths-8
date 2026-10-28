"""
Kernel-polynomial (Chebyshev) count of near-zero modes of the window-restricted 4D icosian lattice Dirac operator, SciPy sparse.
Same lattice and operator as route56_window.py. Count(E^<eps) = Tr theta(eps^2*900 - W^dag W) estimated by stochastic trace (R random +-1/ i-phase vectors) of a Jackson-damped
Chebyshev expansion of degree D of the step function on H2 = W^dag W, spectrum in [0,lmax] (lmax from Lanczos x1.02). Only mat-vecs; no eigenvectors, no factorisation.
Output next to the bulk-torus prediction 2N P(eps) (as route56_window.py). Validate at A=B=3 against the dense counts in LIVE_WEB_RESULTS.md section 23 (94 / 566 / 1282 at 0.01 / 0.05 / 0.1).
Usage: py -3 -I -u route56_window_kpm.py A B R D
"""
import numpy as np, importlib.util, os, io, contextlib, sys, itertools
here=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('h',os.path.join(here,'route56_hecke.py')); h=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(h)
sd=h.sd; U=h.U; PHI=h.PHI; PSI=h.PSI
A=float(sys.argv[1]); B=float(sys.argv[2]); R=int(sys.argv[3]); D=int(sys.argv[4])
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
X=X[keep]; N=len(X)
print(f"A={A}, B={B}: N={N}",flush=True)
import scipy.sparse as sps, scipy.sparse.linalg as spl, time
Uf=U.reshape(120,8).astype(np.int64); Qu=np.array([sd.Qmat(p) for p in h.phys(U)])
lo=X.min(0)-Uf.max(0)-1; rng_=X.max(0)+Uf.max(0)+1-lo+1; mult=np.concatenate([[1],np.cumprod(rng_[:-1])]).astype(np.int64)
key=lambda Y:((Y-lo)*mult).sum(-1)
kx=key(X); o=np.argsort(kx); ks=kx[o]
t0=time.time(); I_=[];J_=[];A_=[]; deg=np.zeros(N,int)
for a in range(120):
    k2=key(X+Uf[a]); pos=np.searchsorted(ks,k2); pos[pos>=N]=N-1; ok=ks[pos]==k2; i=np.nonzero(ok)[0]; j=o[pos[ok]]
    deg[i]+=1; I_.append(i); J_.append(j); A_.append(np.full(len(i),a))
I_=np.concatenate(I_); J_=np.concatenate(J_); A_=np.concatenate(A_)
rows=np.concatenate([2*I_+s for s in range(2) for t in range(2)]); cols=np.concatenate([2*J_+t for s in range(2) for t in range(2)])
vals=np.concatenate([Qu[A_,s,t] for s in range(2) for t in range(2)])
W=sps.csr_matrix((vals,(rows,cols)),shape=(2*N,2*N),dtype=complex); W.sum_duplicates()
print(f"   degrees: min {deg.min()}, mean {deg.mean():.1f}, full-degree fraction {np.mean(deg==120):.3f}; nnz {W.nnz}; build {time.time()-t0:.0f}s",flush=True)
Wd=W.conj().T.tocsr()
H2=lambda V:Wd@(W@V)
lmax=float(spl.eigsh(spl.LinearOperator((2*N,2*N),matvec=lambda v:H2(v),dtype=complex),k=1,which='LA',return_eigenvectors=False)[0])*1.02
print(f"   lmax(s^2)={lmax:.2f}  (Ehat_max ~ {np.sqrt(lmax/1.02)/30:.4f})",flush=True)
g=np.random.default_rng(7); V0=np.exp(2j*np.pi*g.random((2*N,R)))
mu=np.zeros(D); Tm=V0.copy(); Tn=(2*H2(V0)/lmax-V0)
t0=time.time(); mu[0]=np.vdot(V0,V0).real/R; mu[1]=np.vdot(V0,Tn).real/R
for n in range(2,D):
    Tp=2*(2*H2(Tn)/lmax-Tn)-Tm; Tm,Tn=Tn,Tp; mu[n]=np.vdot(V0,Tn).real/R
print(f"   {D} Chebyshev moments x {R} vectors in {time.time()-t0:.0f}s",flush=True)
jk=((D-np.arange(D)+1)*np.cos(np.pi*np.arange(D)/(D+1))+np.sin(np.pi*np.arange(D)/(D+1))/np.tan(np.pi/(D+1)))/(D+1)
def count(eps):
    t=(30*eps)**2; a=2*t/lmax-1; th=np.arccos(a); n=np.arange(1,D)
    c=np.concatenate([[1-th/np.pi],-2*np.sin(n*th)/(n*np.pi)])
    return float((jk*c*mu).sum())     # mu has been normalised per-vector (Tr/R); times 1 => estimated count of eigenvalues of H2 below t
rng=np.random.default_rng(0); first=[i for i in range(120) if next(x for x in h.phys(U)[i] if abs(x)>1e-9)>0]
Pu=h.phys(U)[first]; th_=rng.uniform(0,2*np.pi,size=(300000,8)); ph=th_@Uf[first].astype(float).T
Ek=2*np.linalg.norm(np.einsum('mj,ja->ma',np.sin(ph),Pu),axis=1)/30
print("   eps     KPM count(E^<eps) [of 2N=%d]   bulk 2N P(eps)   ratio"%(2*N))
for e in (0.005,0.01,0.02,0.05,0.1,0.2,0.5):
    c=count(e); pr=2*N*np.mean(Ek<e); print(f"   {e:6.3f}  {c:12.1f}   {pr:12.1f}   {c/max(pr,1e-9):8.2f}",flush=True)
