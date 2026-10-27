"""
The route56 connection on the icosahedral cut-and-project quasicrystal (the corpus's other refinement; Maths 6 explore/scale.py).

Construction inherited from Maths 6 explore/scale.py (6D->3D icosahedral cut-and-project, triacontahedron window, first shell
cutoff 0.78 -> mean coordination ~13, the kissing-12 carrier motif extended to a quasilattice).  Re-implemented here, not edited.

Why the connection transfers: on S^3 the per-edge object is gamma_ij = (Q_j Q_i^dag - c)/s = -i n_ij.sigma, with n_ij the unit tangent
direction (route56_subdiv.py).  In R^3 the same expression, n_ij = unit vector from i to j in the (flat, translation-invariant) frame,
is the small-angle limit; the continuum operator is the Weyl operator sigma.p with levels +/-|k| (no 3/2 shift, no curvature).
Operator A: D_ij = -i n_ij.sigma, unit weight.  Operator B: least-squares consistent gradient, D_B = sym(-i sigma_a X_a), scale 1.
Tests (no fit):
  (i)  integrated state count N(|lambda|<L) against the Weyl law  V L^3/(3 pi^2)  (2 spinor components, +/-|k|), V = ball volume;
  (ii) kernel dimension and the count of modes below the first continuum scale (doublers);
  (iii) POSITIVE/DOUBLER CONTROL: the identical pipeline on a simple-cubic lattice ball, where the central-difference Dirac operator is
       known to carry 2^3 = 8 species (so count/Weyl -> 8 at low L);
  (iv) the scalar phi^2 dilation seam of the Skull Candy web_engine_scale: chain with hops phi^2 / phi^-2 vs the plain path graph.
Usage: py -3 -I -u route56_quasi.py
"""
import numpy as np, sys
np.set_printoptions(suppress=True, linewidth=170)
PHI=(1+5**0.5)/2; PSI=1-PHI
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex); SIG=[sx,sy,sz]

# ---- inherited cut-and-project (Maths 6 scale.py) ----
V6=np.array([[0,1,PHI],[0,1,-PHI],[1,PHI,0],[-1,PHI,0],[PHI,0,1],[PHI,0,-1]],float)
V6s=np.array([[0,1,PSI],[0,1,-PSI],[1,PSI,0],[-1,PSI,0],[PSI,0,1],[PSI,0,-1]],float)
Ppar=(V6/np.sqrt(2*(2+PHI))).T; Pperp=(V6s/np.sqrt(2*(2+PSI))).T
Gg=Pperp.T; pairs=[(i,j) for i in range(6) for j in range(i+1,6)]
Nrm=np.array([np.cross(Gg[i],Gg[j]) for i,j in pairs]); Nrm/=np.linalg.norm(Nrm,axis=1,keepdims=True)
supp=0.5*np.sum(np.abs(Nrm@Gg.T),axis=1)
def quasilattice(K):
    ax=np.arange(-K,K+1); grid=np.stack(np.meshgrid(*([ax]*6),indexing="ij"),axis=-1).reshape(-1,6).astype(np.int16)
    grid=grid[np.any(grid!=0,axis=1)]; perp=grid.astype(float)@Pperp.T
    inside=np.all(np.abs(perp@Nrm.T)<=supp+1e-9,axis=1); return grid[inside].astype(float)@Ppar.T
def crop_ball(pts,n):
    r2=np.sum(pts**2,axis=1); idx=np.argsort(r2)[:n]; return pts[idx]

def build(pts,cutoff):
    N=len(pts); d2=np.sum((pts[:,None,:]-pts[None,:,:])**2,axis=2); np.fill_diagonal(d2,np.inf)
    nbr=[np.where(d2[i]<=cutoff**2)[0] for i in range(N)]
    DA=np.zeros((2*N,2*N),complex); DB=np.zeros((2*N,2*N),complex); ani=[]; bal=[]; kap=[]
    for i in range(N):
        v=pts[nbr[i]]-pts[i]; r=np.linalg.norm(v,axis=1); n=v/r[:,None]
        if len(v)<3: ani.append(np.inf); bal.append(np.inf); kap.append(0); continue
        M=v.T@v; ev=np.linalg.eigvalsh(M); ani.append(ev[-1]/max(ev[0],1e-12)); bal.append(np.linalg.norm(n.sum(0))); kap.append(r.sum()/3)
        W=v@np.linalg.pinv(M)
        for jj,j in enumerate(nbr[i]):
            DA[2*i:2*i+2,2*j:2*j+2]=-1j*sum(n[jj,a]*SIG[a] for a in range(3))
            blk=-1j*sum(W[jj,a]*SIG[a] for a in range(3)); DB[2*i:2*i+2,2*j:2*j+2]+=blk; DB[2*i:2*i+2,2*i:2*i+2]-=blk
    return DA,(DB+DB.conj().T)/2,np.array(ani),np.array(bal),np.array(kap),np.array([len(x) for x in nbr])

def weyl(L,Vol): return Vol*L**3/(3*np.pi**2)
def report(tag,pts,cutoff):
    N=len(pts); R=np.max(np.linalg.norm(pts,axis=1)); Vol=4*np.pi*R**3/3
    DA,DB,ani,bal,kap,deg=build(pts,cutoff)
    interior=np.linalg.norm(pts,axis=1)<0.6*R
    print(f"\n-- {tag}: N={N}, ball radius {R:.3f}, mean degree {deg.mean():.2f} (interior {deg[interior].mean():.2f}), density {N/Vol:.4f};"
          f" interior anisotropy max {ani[interior].max():.3f}, interior imbalance max {bal[interior].max():.3f}")
    ka=kap[interior].mean()
    print(f"   hermiticity A {np.abs(DA-DA.conj().T).max():.0e};  geometric scale kappa (mean sum r_ij/3, interior) = {ka:.4f}")
    for name,D,sc in (("A/kappa",DA,ka),("B",DB,1.0)):
        ev=np.sort(np.abs(np.linalg.eigvalsh(D)/sc))
        # first continuum scale: lowest Weyl level ~ (pi/R)-ish; report raw counts at fixed L
        Ls=[0.15,0.3,0.5,0.8,1.2]
        row="  ".join(f"L={L:.2f}: {int(np.sum(ev<L))}/{weyl(L,Vol):.1f}" for L in Ls)
        ker=int(np.sum(ev<1e-6))
        # log-log slope of the cumulative count between counts 30 and 20% of N
        cnt=np.arange(1,len(ev)+1); lo=np.searchsorted(cnt,30); hi=int(0.15*len(ev))
        sl=np.polyfit(np.log(ev[lo:hi]+1e-12),np.log(cnt[lo:hi]),1)[0] if hi>lo+5 else float('nan')
        print(f"   {name:8s} kernel {ker};  count/Weyl:  {row};  log-log slope of N(|lambda|) between counts 30 and 15%: {sl:.2f} (Weyl: 3)")
    return

if __name__=="__main__":
    print("(iv) scalar phi^2 dilation seam: chain of S scales, hops phi^2 (outward) / phi^-2 (inward)")
    for S in (6,):
        M=np.zeros((S,S));
        for s in range(S-1): M[s+1,s]=PHI**2; M[s,s+1]=PHI**-2
        ev=np.sort(np.linalg.eigvals(M).real); ref=np.sort(2*np.cos(np.arange(1,S+1)*np.pi/(S+1)))
        Dg=np.diag(PHI**(2*np.arange(S))); P=np.eye(S,k=1)+np.eye(S,k=-1)
        sim=np.max(np.abs(M-Dg@P@np.linalg.inv(Dg)))
        print(f"   S={S}: max|eig(M)-2cos(k pi/(S+1))| = {np.max(np.abs(ev-ref)):.1e};  max|M - Dg P Dg^-1| = {sim:.1e}"
              "  (flat: the scalar dilation is a gauge on this tree; each in-shell square has hop product phi^2*phi^-2 = 1)")
    # (iii) simple-cubic control
    g=np.arange(-8,9); C=np.array(np.meshgrid(g,g,g,indexing='ij')).reshape(3,-1).T.astype(float)
    C=C[np.linalg.norm(C,axis=1)<=7.2];
    report("CONTROL simple cubic (expect 8 species at low L)",C,1.05)
    big=quasilattice(6); print(f"\ncut-and-project quasilattice K=6: {len(big)} vertices")
    for n in [300,700,1300]:
        report(f"icosahedral quasicrystal",crop_ball(big,n),0.78)
