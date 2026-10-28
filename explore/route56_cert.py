"""
Grid-and-curvature check of the band-top maximum of operator B on the periodic approximants (replaces 'five pattern searches agree').
Lambda(K) = top eigenvalue of H(K), K in the Brillouin zone (parallelepiped of the reciprocal basis, f in [0,1)^3; H(K+G) is unitarily equivalent to H(K)).
Evaluate Lambda on an n^3 grid of f (sparse matvec + Lanczos m=80, accuracy ~1e-5 against dense eigvalsh, reported).  Every point K of the zone is within r = |sum_i b_i/n|/2 of a grid point.
At the maximiser K* of Lambda (interior; Lambda is a max of smooth branches, so an active branch is stationary at K*), Lambda(K*) <= Lambda(grid) + (1/2) M r^2, where M bounds the second
derivative of H: M = sqrt(max row sum x max column sum) of  R_ij = ||blk_ij||_2 |d_ij|^2  (sum over images).  This holds under that stationarity assumption; it is not a floating-point-proof certificate.
Reports: grid maximum, M, r, upper bound, and E_max*a bounds, plus how the maximum compares with sqrt(2)/a.   Usage: py -3 -I -u route56_cert.py p/q n
"""
import numpy as np, sys, importlib.util, os, itertools
from fractions import Fraction
here=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('route56_approx',os.path.join(here,'route56_approx.py')); ap=importlib.util.module_from_spec(sp); sp.loader.exec_module(ap)
SIG=ap.SIG
tau=Fraction(sys.argv[1]); ng=int(sys.argv[2]); gamma=np.array([0.0131,-0.0087,0.0049])
P,Bm,vol,idx,K=ap.cell_points(tau,gamma,7); N=len(P); nb=ap.build(P,Bm,0.78)
I=[];J=[];Dv=[];BL=[];diag=np.zeros((N,2,2),complex)
for i,(D,Jj) in enumerate(nb):
    C=D@np.linalg.pinv(D.T@D)
    for c,j,d in zip(C,Jj,D):
        blk=-1j*(c[0]*SIG[0]+c[1]*SIG[1]+c[2]*SIG[2]); I.append(i);J.append(j);Dv.append(d);BL.append(blk); diag[i]-=blk
I=np.array(I);J=np.array(J);Dv=np.array(Dv);BL=np.array(BL)
kap=np.mean([np.linalg.norm(D,axis=1).sum()/3 for D,_ in nb]); deg=np.array([len(x[1]) for x in nb]); a=3*kap/deg.mean()
def matvec(x,ph):
    X=x.reshape(N,2); blk=BL*ph[:,None,None]
    t=np.einsum('eab,eb->ea',blk,X[J]); u=np.einsum('eba,eb->ea',blk.conj(),X[I])
    y=np.zeros((N,2),complex); z=np.zeros((N,2),complex)
    for c in (0,1):
        y[:,c]=np.bincount(I,weights=t[:,c].real,minlength=N)+1j*np.bincount(I,weights=t[:,c].imag,minlength=N)
        z[:,c]=np.bincount(J,weights=u[:,c].real,minlength=N)+1j*np.bincount(J,weights=u[:,c].imag,minlength=N)
    y+=np.einsum('nab,nb->na',diag,X); z+=np.einsum('nba,nb->na',diag.conj(),X)
    return ((y+z)/2).reshape(-1)
rng=np.random.default_rng(0); v0=rng.normal(size=2*N)+1j*rng.normal(size=2*N); v0/=np.linalg.norm(v0)
def lam(k,m=80):
    ph=np.exp(1j*(Dv@k)); Vs=[v0]; al=[];be=[]
    for t in range(m):
        w=matvec(Vs[-1],ph); a_=np.vdot(Vs[-1],w).real; al.append(a_); w=w-a_*Vs[-1]-(be[-1]*Vs[-2] if t>0 else 0)
        for u in Vs: w=w-np.vdot(u,w)*u
        b=np.linalg.norm(w)
        if b<1e-10: break
        be.append(b); Vs.append(w/b)
    T=np.diag(al)+np.diag(be[:len(al)-1],1)+np.diag(be[:len(al)-1],-1); return np.linalg.eigvalsh(T)[-1]
bvec=2*np.pi*np.linalg.inv(Bm).T                      # columns? rows of inv(B)^T are reciprocal vectors: b_i . B_j = 2 pi delta
bv=[2*np.pi*np.linalg.inv(Bm)[i] for i in range(3)]
r=0.5*np.linalg.norm(sum(b/ng for b in bv))
R=np.zeros((N,N))
for e in range(len(I)): R[I[e],J[e]]+=np.linalg.norm(BL[e],2)*Dv[e]@Dv[e]
M=np.sqrt(R.sum(1).max()*R.sum(0).max())
kk=np.array([0.7,-0.4,1.1]); Hd=ap.H_of_k(nb,N,kk,'B',kap); print(f"tau={tau}: N={N}, a={a:.4f}, sqrt2/a={2**.5/a:.4f}; BZ basis lengths {np.round([np.linalg.norm(b) for b in bv],4)}; Lanczos check {lam(kk):.8f} vs dense {np.linalg.eigvalsh(Hd)[-1]:.8f}",flush=True)
best=-1;bk=None
for f in itertools.product(range(ng),repeat=3):
    k=sum((f[i]/ng)*bv[i] for i in range(3)); v=lam(k)
    if v>best: best,bk=v,k
print(f"  grid {ng}^3: max Lambda = {best:.6f} at K={np.round(bk,4)};  M={M:.3f}, covering radius r={r:.4f}, curvature margin (1/2)M r^2 = {0.5*M*r*r:.6f}",flush=True)
print(f"  => E_max*a in [{best*a:.5f}, {(best+0.5*M*r*r)*a:.5f}];  sqrt2 = {2**.5:.5f}: the upper bound {'is below' if (best+0.5*M*r*r)*a<2**.5 else 'is NOT below'} sqrt2",flush=True)
