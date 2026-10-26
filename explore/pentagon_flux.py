"""
epsilon as a FLUX, not a scalar: thread holonomy epsilon through each pentagon (the 5-cycle link
of every edge) as Peierls phases on the carrier edges, then ask whether the frustration flux GAPS
the massless (irrep-5, lambda=0, mult 25) mode of the propagation Laplacian -> a frustration rest-mass.

Peierls phases theta_e (one per edge i<j).  A_theta[i,j]=exp(i theta_ij), Hermitian.
Holonomy around a pentagon = sum of signed theta over its 5 edges; we fit theta (least-squares) so
every pentagon holonomy ~ epsilon.  Because pentagons share edges (and bound tetrahedra), the system
is over-constrained -> the lstsq residual IS the irreducible frustration.  Compare spectrum to flux=0.
"""
import numpy as np, itertools
from itertools import permutations
phi=(1+5**0.5)/2; EPS=2*np.pi-5*np.arccos(1/3)

V=[]
for i in range(4):
    for s in (1,-1):
        v=[0,0,0,0]; v[i]=s; V.append(v)
for s in itertools.product((0.5,-0.5),repeat=4): V.append(list(s))
base=[0.0,0.5,phi/2,1/(2*phi)]
def par(p):
    p=list(p); seen=[False]*4; k=0
    for i in range(4):
        if seen[i]:continue
        j=i;c=0
        while not seen[j]: seen[j]=True;j=p[j];c+=1
        k+=c-1
    return k%2
for p in [q for q in permutations(range(4)) if par(q)==0]:
    vals=[base[p[i]] for i in range(4)]; nz=[i for i in range(4) if vals[i]!=0]
    for ss in itertools.product((1,-1),repeat=3):
        v=list(vals)
        for k,idx in enumerate(nz): v[idx]=vals[idx]*ss[k]
        V.append(v)
V=np.unique(np.round(np.array(V),9),axis=0); N=len(V)
Adj=(np.abs(V@V.T-phi/2)<1e-6); np.fill_diagonal(Adj,False)
edges=[(i,j) for i in range(N) for j in range(i+1,N) if Adj[i,j]]
E=len(edges); eidx={e:k for k,e in enumerate(edges)}
deg=Adj.sum(1).astype(float)

# unique pentagons = the 5-cycle link of each edge (dedup by vertex set)
def order_cycle(K):
    sub={a:[b for b in K if Adj[a,b]] for a in K}
    if any(len(sub[a])!=2 for a in K): return None
    order=[K[0]]; prev=None
    while len(order)<len(K):
        nxts=[b for b in sub[order[-1]] if b!=prev]
        if not nxts: return None
        prev=order[-1]; order.append(nxts[0])
    return order if Adj[order[-1],order[0]] else None
pents={}
for (i,j) in edges:
    K=[k for k in range(N) if Adj[i,k] and Adj[j,k]]
    o=order_cycle(K)
    if o and len(o)==5: pents[frozenset(o)]=o
pents=list(pents.values())
print(f"[pentagons] unique 5-cycles: {len(pents)};  epsilon = {EPS:.6f} rad ({np.degrees(EPS):.3f} deg)")

# signed incidence B (pentagons x edges): holonomy_p = sum signed theta
B=np.zeros((len(pents),E))
for r,o in enumerate(pents):
    for a in range(5):
        x,y=o[a],o[(a+1)%5]
        if x<y: B[r,eidx[(x,y)]]+=1.0
        else:   B[r,eidx[(y,x)]]-=1.0

def spectrum(theta):
    Ath=np.zeros((N,N),complex)
    for k,(i,j) in enumerate(edges):
        Ath[i,j]=np.exp(1j*theta[k]); Ath[j,i]=np.conj(Ath[i,j])
    L=np.diag(deg)-Ath
    return np.linalg.eigvalsh(L)

# sanity: zero flux recovers L0
w0=spectrum(np.zeros(E))
print(f"[sanity] flux=0 lowest eigenvalues: {np.round(w0[:6],4)}  (expect 0 x25 then 3,...)")
print(f"         zero-mode multiplicity: {int(np.sum(np.abs(w0)<1e-8))} (expect 25 = the massless kernel)")

# fit theta so every pentagon holonomy ~ epsilon
theta,res,rk,sv=np.linalg.lstsq(B,EPS*np.ones(len(pents)),rcond=None)
hol=B@theta
print(f"\n[flux fit] target holonomy/pentagon = {EPS:.4f};  achieved mean {hol.mean():.4f}, "
      f"std {hol.std():.4f};  irreducible frustration (rms |hol-eps|) = {np.sqrt(np.mean((hol-EPS)**2)):.4f} rad")

wF=spectrum(theta)
print(f"\n[flux on] lowest eigenvalues: {np.round(wF[:8],4)}")
gap=wF[np.sum(np.abs(w0)<1e-8)-0]  # first state that was in the zero block
print(f"  former massless block (was 0 x25) now spans [{wF[0]:.4f}, {wF[24]:.4f}]")
print(f"  >> massless-mode gap opened by the frustration flux: lowest nonzero = {wF[0]:.5f}  "
      f"(0 if no gap)")

# also sweep a scalar multiple of epsilon to see the gap grow with flux
print("\n[flux sweep]  flux = f*epsilon per pentagon")
print("  f      lowest-eig (gap)   mean holonomy")
for f in (0.0,0.25,0.5,1.0,2.0):
    th,_,_,_=np.linalg.lstsq(B,f*EPS*np.ones(len(pents)),rcond=None)
    wf=spectrum(th)
    print(f"  {f:4.2f}   {wf[0]:12.6f}     {(B@th).mean():.4f}")
