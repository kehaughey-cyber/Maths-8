"""
Periodic approximants of the icosahedral quasicrystal (phi -> tau = p/q in the 6D->3D cut-and-project of route56_quasi.py) and exact Bloch bands of the
route56 operators on them: an unbiased dispersion and the bulk band top, replacing the wave-packet estimator and the finite-ball spectra of route56_band.py.

  construction: Ppar, Pperp as route56_quasi with phi->tau (psi = 1-tau), same triacontahedron window; a generic perpendicular shift gamma keeps the set periodic
  but off the window boundary.  Periods L = Ppar(ker Pperp ∩ Z^6) (integer kernel by sympy; index of the lattice they generate reported).
  cell content: points with frac coordinates in [0,1) of L.  Neighbours: all points within `cutoff` including the 27 neighbouring cells.
  Bloch operator, position gauge:  H(k)_{ij} = sum_images block_ij exp(i k.(r_j' - r_i)),  Hermitised (D + D^dag)/2.
    A: -i n.sigma unit weight, divided by kappa = mean over points of (sum_j r_ij)/3.   B: LS-consistent gradient (diagonal -blk).
  UNBIASED DISPERSION: the plane wave psi_i = u_+(K) (helicity eigenvector of sigma.K) in the position gauge is the exact extended-momentum state; E(K) =
  <psi|H(K)|psi>/<psi|psi>, spread sqrt(<H^2> - <H>^2).  BAND TOP: max over sampled K of the top eigenvalue of H(K).
No fit.  Usage: py -3 -I -u route56_approx.py [p/q ...]
"""
import numpy as np, sys, itertools, time
from fractions import Fraction
import sympy as sp
SIG=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
PHI=(1+5**0.5)/2

def setup(tau):
    t=float(tau); ps=1-t
    V6=np.array([[0,1,t],[0,1,-t],[1,t,0],[-1,t,0],[t,0,1],[t,0,-1]],float)
    V6s=np.array([[0,1,ps],[0,1,-ps],[1,ps,0],[-1,ps,0],[ps,0,1],[ps,0,-1]],float)
    Ppar=(V6/np.sqrt(2*(1+t*t))).T; Pperp=(V6s/np.sqrt(2*(1+ps*ps))).T
    Gg=Pperp.T; pairs=[(i,j) for i in range(6) for j in range(i+1,6)]
    Nrm=np.array([np.cross(Gg[i],Gg[j]) for i,j in pairs]); Nrm/=np.linalg.norm(Nrm,axis=1,keepdims=True)
    supp=0.5*np.sum(np.abs(Nrm@Gg.T),axis=1)
    # integer kernel of the perpendicular projection:  rows of V6s are (0,1,1-tau) ... ; use exact rationals
    tq=sp.Rational(tau.numerator,tau.denominator); pq=1-tq
    Mp=sp.Matrix([[0,1,pq],[0,1,-pq],[1,pq,0],[-1,pq,0],[pq,0,1],[pq,0,-1]]).T      # 3 x 6
    ker=Mp.nullspace(); K=[]
    for v in ker:
        den=sp.ilcm(*[sp.Rational(x).q for x in v]); w=[int(x*den) for x in v]; g=np.gcd.reduce(np.abs(w)); K.append([x//g for x in w])
    K=np.array(K,dtype=np.int64)
    def index(K):
        minors=[abs(int(round(np.linalg.det(K[:,list(c)].astype(float))))) for c in itertools.combinations(range(6),3)]
        return int(np.gcd.reduce([m for m in minors if m>0]))
    idx0=index(K)
    while index(K)>1:                                      # saturate: add (c.K)/p whenever it is an integer vector
        p=int(sp.factorint(index(K)).popitem()[0]); done=False
        for c in itertools.product(range(p),repeat=3):
            if not any(c): continue
            v=np.array(c)@K
            if np.all(v%p==0):
                i=[t for t in range(3) if c[t]%p!=0][0]; K[i]=v//p; done=True; break
        assert done
    return Ppar,Pperp,Nrm,supp,K,idx0

def cell_points(tau,gamma,Kbox):
    Ppar,Pperp,Nrm,supp,K,idx=setup(tau)
    Lc=(Ppar@K.T)                                        # 3 x 3, columns = physical period vectors
    # reduce the period basis (simple size reduction by integer combos) to improve the cell shape
    B=Lc.copy()
    for _ in range(4):
        for i in range(3):
            for j in range(3):
                if i!=j:
                    m=np.round(B[:,i]@B[:,j]/(B[:,j]@B[:,j]))
                    if m!=0: B[:,i]-=m*B[:,j]
    Linv=np.linalg.inv(B); vol=abs(np.linalg.det(B))
    ax=np.arange(-Kbox,Kbox+1); pts=[]
    g6=np.stack(np.meshgrid(*([ax]*5),indexing="ij"),axis=-1).reshape(-1,5).astype(np.int16)
    for z6 in ax:
        z=np.hstack([g6,np.full((len(g6),1),z6,dtype=np.int16)]); perp=z.astype(float)@Pperp.T+gamma
        ok=np.all(np.abs(perp@Nrm.T)<=supp+1e-12,axis=1)
        if ok.any(): pts.append(z[ok].astype(float)@Ppar.T)
    pts=np.vstack(pts); fr=(pts@Linv.T); fr=fr-np.floor(fr+1e-9)
    key=np.round(fr,6)%1.0; _,u=np.unique(np.round(key*1e5).astype(np.int64)%100000,axis=0,return_index=True)
    P=(fr[u]@B.T)
    return P,B,vol,idx,K

def build(P,B,cutoff):
    N=len(P); sh=np.array([n for n in itertools.product((-1,0,1),repeat=3)])@B.T
    nb=[]                                                 # per point: (displacement vectors)
    for i in range(N):
        vv=[]
        for s in sh:
            d=P+s-P[i]; r=np.linalg.norm(d,axis=1); m=(r<=cutoff)&(r>1e-9); vv.append((d[m],np.where(m)[0]))
        D=np.vstack([x[0] for x in vv]); J=np.concatenate([x[1] for x in vv]); nb.append((D,J))
    return nb

def H_of_k(nb,N,k,op,kap):
    H=np.zeros((2*N,2*N),complex)
    for i,(D,J) in enumerate(nb):
        r=np.linalg.norm(D,axis=1); n=D/r[:,None]
        if op=='A': C=n
        else: C=D@np.linalg.pinv(D.T@D)
        ph=np.exp(1j*(D@k))
        for c,j,p in zip(C,J,ph):
            blk=-1j*(c[0]*SIG[0]+c[1]*SIG[1]+c[2]*SIG[2])
            H[2*i:2*i+2,2*j:2*j+2]+=blk*p
            if op=='B': H[2*i:2*i+2,2*i:2*i+2]-=blk
    H=(H+H.conj().T)/2
    return H/(kap if op=='A' else 1.0)

if __name__=="__main__":
    taus=[Fraction(a) for a in sys.argv[1:]] or [Fraction(3,2),Fraction(5,3),Fraction(8,5)]
    rng=np.random.default_rng(3); gamma=np.array([0.0131,-0.0087,0.0049])
    for tau in taus:
        t0=time.time(); Kb=7
        P,B,vol,idx,K=cell_points(tau,gamma,Kb); N=len(P)
        print(f"\n==== tau={tau}={float(tau):.4f}: period basis |a_i| = {np.linalg.norm(B,axis=0).round(3)}, volume {vol:.3f}, kernel-lattice index {idx}, points per cell N={N}, density {N/vol:.4f} (true quasicrystal ~0.46?)  [{time.time()-t0:.0f}s]",flush=True)
        if N>2500: print("   too large, skipped"); continue
        nb=build(P,B,0.78); deg=np.array([len(x[1]) for x in nb]); kap=np.mean([np.linalg.norm(D,axis=1).sum()/3 for D,J in nb]); a=3*kap/deg.mean()
        print(f"   degrees: min {deg.min()} mean {deg.mean():.2f} max {deg.max()};  kappa={kap:.4f}; a=3kappa/<deg>={a:.4f}",flush=True)
        dirs={"5-fold":np.array([0,1,PHI]),"3-fold":np.array([1,1,1.]),"2-fold":np.array([1,0,0.]),"rand":rng.normal(size=3)}
        for op in ("B","A"):
            scale=kap if op=='A' else 1.0
            print(f"   operator {op}:  unbiased E(K) = <u_+|H(K)|u_+> (spread), and exact top eigenvalue of H(K):")
            for nm,d in dirs.items():
                d=d/np.linalg.norm(d); row=[]
                for kk in (0.3,0.6,1.0,1.5,2.0,3.0):
                    H=H_of_k(nb,N,kk*d,op,kap); sk=sum(kk*d[c]*SIG[c] for c in range(3)); w_,U=np.linalg.eigh(sk); u=U[:,1]
                    psi=np.tile(u,N); Hp=H@psi; E=np.vdot(psi,Hp).real/np.vdot(psi,psi).real; sd=np.sqrt(max(np.vdot(Hp,Hp).real/np.vdot(psi,psi).real-E*E,0))
                    row.append(f"k={kk}: {E:.4f}(±{sd:.3f})")
                print(f"     {nm:7s} "+"  ".join(row),flush=True)
            tops=[]
            for _ in range(40):
                kv=rng.normal(size=3); kv=kv/np.linalg.norm(kv)*rng.uniform(0.5,4.5); ev=np.linalg.eigvalsh(H_of_k(nb,N,kv,op,kap)); tops.append((ev.max(),-ev.min()))
            tops=np.array(tops); print(f"     sampled K (40 random, |K|<4.5): top eigenvalue max {tops[:,0].max():.4f}, bottom max |.| {tops[:,1].max():.4f};  E_max*a = {max(tops.max(),0)*a:.4f}",flush=True)
