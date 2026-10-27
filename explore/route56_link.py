"""
Link between the R^3 icosahedral quasicrystal and the S^3 carrier, via the icosian ring (the 4D quasicrystal whose unit shell IS the 600-cell).
  Part 1 (local chart): the 600-cell star of one vertex in the log chart (radius = geodesic angle) vs the quasicrystal's shells around its
         fully icosahedral vertex (the origin).  Shell counts and radius ratios side by side.
  Part 2 (quasicrystal refinement OF S^3): icosians q = u + v (u, v in the 120 units, exact in Z[phi]); direction q/|q| is a point of S^3.
         For a pair at overlap class c:  |q|^2 = 2+2c,  |sigma(q)|^2 = 2+2 sigma(c)  (physical norm, Galois-conjugate / internal norm).
         Norm product 1 => the direction is already one of the 120 vertices (no refinement); otherwise a new point.  The new points are the
         pair midpoints of the classes phi/2 (the n=2 subdivision's edge midpoints), 1/2, 0 and -1/(2phi).
         Route56 rule on this set (Operator B: LS-consistent; Operator A: raw unit weight, scale kappa=mean(sum theta)/3): Ritz levels on the sampled SU(2)
         harmonics (d<=4) against the continuum teleparallel levels, compared with the geodesic subdivision at similar mean edge angle.
Usage: py -3 -I -u route56_link.py
"""
import numpy as np, itertools, importlib.util, os
here=os.path.dirname(os.path.abspath(__file__))
def load(name):
    sp=importlib.util.spec_from_file_location(name,os.path.join(here,name+'.py')); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
sd=load('route56_subdiv'); rq=load('route56_quasi')
PHI=sd.phi; PSI=1-PHI
sig=[sd.sx,sd.sy,sd.sz]

V=sd.carrier()                                        # 120 x 4 float
def exact_pairs(v):                                   # doubled coords (a,b): 2*x = a + b*phi
    out=[]
    for x in v:
        for (a,b) in ((0,0),(2,0),(-2,0),(1,0),(-1,0),(0,1),(0,-1),(-1,1),(1,-1)):
            if abs(x-(a+b*PHI)/2)<1e-9: out.append((a,b)); break
        else: raise ValueError(x)
    return out
EX=np.array([[c for ab in exact_pairs(v) for c in ab] for v in V])          # 120 x 8 integers
def phys(E): return (E[:,0::2]+E[:,1::2]*PHI)/2
def perp(E): return (E[:,0::2]+E[:,1::2]*PSI)/2
assert np.allclose(phys(EX),V)

# ---------------- Part 1: local chart ----------------
G=V@V.T; th=np.degrees(np.arccos(np.clip(G[0],-1,1))); order=np.round(th,4)
print("PART 1  local chart of the 600-cell around vertex 0 (radius = geodesic angle, deg) vs quasicrystal shells around its icosahedral origin")
vals,cnt=np.unique(order[(order>0)&(order<180)],return_counts=True)
print("   600-cell shells (angle:count) = "+", ".join(f"{a:.1f}:{c}" for a,c in zip(vals,cnt))+";  ratios to first: "+", ".join(f"{a/vals[0]:.3f}" for a in vals[:6]))
big=np.vstack([np.zeros((1,3)),rq.quasilattice(6)]); r=np.round(np.linalg.norm(big,axis=1),5)
rv,rc=np.unique(r[(r>0)&(r<2.6)],return_counts=True)
print("   quasicrystal shells around the origin (radius:count) = "+", ".join(f"{a:.3f}:{c}" for a,c in zip(rv[:10],rc[:10]))+";  ratios to first: "+", ".join(f"{a/rv[0]:.3f}" for a in rv[:8]))
print("   (both are unions of orbits of the icosahedral group I: allowed orbit sizes 1, 12, 20, 30, 60, 120; the 600-cell's 12,20,12,30 against the quasicrystal's)")

# ---------------- Part 2: the icosian refinement ----------------
cls={"phi/2":PHI/2,"1/(2phi)":1/(2*PHI),"1/2":0.5,"0":0.0,"-1/2":-0.5,"-1/(2phi)":-1/(2*PHI),"-phi/2":-PHI/2}
def sg(x):
    for a,b in sd_tab:
        if abs(x-a)<1e-9: return b
    raise ValueError(x)
sd_tab=[(0,0),(0.5,0.5),(-0.5,-0.5),(1,1),(-1,-1),(PHI/2,-1/(2*PHI)),(-PHI/2,1/(2*PHI)),(1/(2*PHI),-PHI/2),(-1/(2*PHI),PHI/2)]
print("\nPART 2  icosian pair sums q = u+v:  class c, count of pairs, |q|^2 (physical), |sigma(q)|^2 (internal), product, is the direction an existing vertex?")
newpts={}
for name,c in cls.items():
    ii,jj=np.where(np.triu(np.abs(G-c)<1e-6,1)); Q=EX[ii]+EX[jj]; P=phys(Q); n2=np.sum(P**2,axis=1)[0]; n2p=np.sum(perp(Q)**2,axis=1)[0]
    d=P/np.linalg.norm(P,axis=1)[:,None]; mind=np.min(np.linalg.norm(d[:,None,:]-V[None,:,:],axis=2),axis=1)
    isv=bool(np.all(mind<1e-6)); print(f"   c={name:10s}  pairs {len(ii):5d}  |q|^2={n2:.4f}  |sigma(q)|^2={n2p:.4f}  product={n2*n2p:.4f}  existing vertex: {isv}")
    if not isv: newpts[name]=d
allnew=np.vstack(list(newpts.values())); allnew=np.unique(np.round(allnew,8),axis=0)
pts=np.vstack([V,allnew]); pts=np.unique(np.round(pts,8),axis=0)
print(f"   new directions after dedupe: {len(allnew)};  total set 120 + new = {len(pts)} points on S^3 (n=2 subdivision has 840)")

def run_set(P,label,knn=14,K=4):
    N=len(P); Gm=P@P.T; np.fill_diagonal(Gm,-2)
    nb=[np.argsort(-Gm[i])[:knn] for i in range(N)]
    Q=np.array([sd.Qmat(p) for p in P]); sg_=sig
    I=[];J=[];CA=[];CB=[];ths=[]
    for i in range(N):
        vs=[]
        for j in nb[i]:
            c=float(np.clip(P[i]@P[j],-1,1)); s=np.sqrt(1-c*c); M=Q[j]@Q[i].conj().T
            nn=np.array([(1j/(2*s))*np.trace(sa@M) for sa in sg_]).real; vs.append(np.arccos(c)*nn)
        vs=np.array(vs); W=vs@np.linalg.pinv(vs.T@vs); ang=np.linalg.norm(vs,axis=1)
        for k,j in enumerate(nb[i]): I.append(i);J.append(j);CB.append(W[k]);CA.append(vs[k]/ang[k]);ths.append(ang[k])
    I=np.array(I);J=np.array(J);CA=np.array(CA);CB=np.array(CB);ths=np.array(ths)
    kap=np.mean([ths[I==i].sum()/3 for i in range(N)]); thbar=ths.mean()
    H=sd.smooth_basis(P,K)
    print(f"\n   -- {label}: N={N}, kNN={knn}, mean edge angle {np.degrees(thbar):.3f} deg, kappa={kap:.4f}")
    def Dmul(Hk,C,B,scale):
        out=np.zeros_like(Hk)                                   # Hk: (2N, m), sigma acts on index pairs
        X=Hk.reshape(N,2,-1)
        for a in range(3):
            T=np.einsum('ab,ebm->eam',sig[a],X[J]-(X[I] if B else 0))*(-1j*C[:,a])[:,None,None]
            Z=np.zeros((N,2,Hk.shape[1]),complex); np.add.at(Z,I,T); out+=Z.reshape(2*N,-1)
        return out/scale
    # full spectra: kernel (the 28-core question) and low-mode census
    for opn,C,B,sc in (("A/kappa",CA,False,kap),("B",CB,True,1.0)):
        D=np.zeros((2*N,2*N),complex)
        for e in range(len(I)):
            blk=-1j*sum(C[e,a]*sig[a] for a in range(3))
            D[2*I[e]:2*I[e]+2,2*J[e]:2*J[e]+2]+=blk
            if B: D[2*I[e]:2*I[e]+2,2*I[e]:2*I[e]+2]-=blk
        D=(D+D.conj().T)/2/sc; ev=np.linalg.eigvalsh(D); ae=np.abs(ev)
        print(f"      {opn:8s} full spectrum: kernel (|ev|<1e-6) = {int(np.sum(ae<1e-6))};  #|lambda|<0.5: {int(np.sum(ae<0.5))};  #|lambda|<1.0: {int(np.sum(ae<1.0))} of {len(ev)};  lowest nonzero |lambda| = {ae[ae>1e-6].min():.5f}")
    res={}
    for opn,C,B,sc in (("A/kappa",CA,False,kap),("B",CB,True,1.0)):
        Hk=H[K]; DH=Dmul(Hk,C,B,sc); Cm=Hk.conj().T@DH; Cm=(Cm+Cm.conj().T)/2; r=np.linalg.eigvalsh(Cm)
        cl=sd.clusters(r,tol=2e-3); res[opn]=cl
        print(f"      {opn:8s} Ritz levels (d<=4): "+"  ".join(f"{c[0]:+.3f}(x{c[1]})" for c in cl if abs(c[0])<6))
    return thbar
# reference: geodesic subdivision values from route56_subdiv_all.out for comparison
print("   continuum targets (d<=4): -5(x12) -4(x6) -3(x2) 0(x2) +1(x6) +2(x12) +3(x20)")
print("   geodesic subdivision, from route56_subdiv_all.out (mean edge angle 18.50 deg, n=2): -4.319(x12) -3.728(x6) -2.948(x2) 0 +0.983(x6) +1.864(x12) +2.592(x20)   [A/kappa]")
tb=run_set(pts,"icosian pair-midpoint refinement of S^3")
