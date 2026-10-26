"""
Connect route56 (the SU(2)/Clifford Dirac operator D=A.gamma, with PINNED mu=(48/5)sin(pi/5))
to the mass gap.

- count D's zero modes at a sane tolerance (banked 28).
- thread the pentagon-epsilon frustration flux (my U(1) theta: holonomy eps per pentagon) and measure
  (a) the SCALAR Laplacian gap (my earlier 0.011), and
  (b) its energy in route56's PINNED non-abelian normalization: V_spec = mu * sum_faces (1-cos F),
      F = face flux = C theta. This gives the frustration-mass a NON-ARBITRARY energy cost.
- also apply the same flux to the Dirac operator (D_a = e^{i theta} D) and report the smallest |eig|.
"""
import numpy as np, itertools
from itertools import permutations, combinations
phi=(1+5**0.5)/2; c=phi/2; s=np.sqrt(1-c*c); EPS=2*np.pi-5*np.arccos(1/3); mu=(48/5)*s

V=[]
for i in range(4):
    for sg in (1,-1):
        v=[0,0,0,0]; v[i]=sg; V.append(v)
for sgs in itertools.product((0.5,-0.5),repeat=4): V.append(list(sgs))
base=[0.0,0.5,phi/2,1/(2*phi)]
def par(p):
    p=list(p); seen=[False]*4; k=0
    for i in range(4):
        if seen[i]:continue
        j=i;cl=0
        while not seen[j]: seen[j]=True;j=p[j];cl+=1
        k+=cl-1
    return k%2
for p in [q for q in permutations(range(4)) if par(q)==0]:
    vals=[base[p[i]] for i in range(4)]; nz=[i for i in range(4) if vals[i]!=0]
    for ss in itertools.product((1,-1),repeat=3):
        v=list(vals)
        for k,idx in enumerate(nz): v[idx]=vals[idx]*ss[k]
        V.append(v)
V=np.unique(np.round(np.array(V),9),axis=0); N=len(V)
Adj=(np.abs(V@V.T-c)<1e-6); np.fill_diagonal(Adj,False)
edges=[(i,j) for i in range(N) for j in range(i+1,N) if Adj[i,j]]; E=len(edges); eidx={e:k for k,e in enumerate(edges)}
deg=Adj.sum(1).astype(float)
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex); I2=np.eye(2,dtype=complex)
Q=np.array([V[k,0]*I2-1j*(V[k,1]*sx+V[k,2]*sy+V[k,3]*sz) for k in range(N)])
def gamma(i,j): return (Q[j]@Q[i].conj().T-c*I2)/s

# Dirac D and its zero modes at a sane tolerance
D=np.zeros((2*N,2*N),complex)
for i in range(N):
    for j in np.where(Adj[i])[0]: D[2*i:2*i+2,2*j:2*j+2]=gamma(i,j)
ev=np.linalg.eigvalsh(D)
for tol in (1e-9,1e-7,1e-6,1e-5):
    print(f"[D zero modes] |ev|<{tol:g}: {int(np.sum(np.abs(ev)<tol))}")
print(f"  (banked 28; smallest |ev| sorted: {np.round(np.sort(np.abs(ev))[:6],2e0 if False else 8)})")

# pentagons (edge-link 5-cycles) and pentagon-flux theta: holonomy eps per pentagon
def order_cycle(K):
    sub={a:[b for b in K if Adj[a,b]] for a in K}
    if any(len(sub[a])!=2 for a in K): return None
    o=[K[0]]; prev=None
    while len(o)<len(K):
        nx=[b for b in sub[o[-1]] if b!=prev]
        if not nx: return None
        prev=o[-1]; o.append(nx[0])
    return o if Adj[o[-1],o[0]] else None
pents={}
for (i,j) in edges:
    K=[k for k in range(N) if Adj[i,k] and Adj[j,k]]
    o=order_cycle(K)
    if o and len(o)==5: pents[frozenset(o)]=o
pents=list(pents.values())
Bp=np.zeros((len(pents),E))
for r,o in enumerate(pents):
    for a in range(5):
        x,y=o[a],o[(a+1)%5]
        if x<y: Bp[r,eidx[(x,y)]]+=1.0
        else:   Bp[r,eidx[(y,x)]]-=1.0
theta,_,_,_=np.linalg.lstsq(Bp,EPS*np.ones(len(pents)),rcond=None)

# (a) scalar Laplacian gap with this flux
def scal(th):
    Ath=np.zeros((N,N),complex)
    for k,(i,j) in enumerate(edges): Ath[i,j]=np.exp(1j*th[k]); Ath[j,i]=np.conj(Ath[i,j])
    return np.linalg.eigvalsh(np.diag(deg)-Ath)
gap_scalar=scal(theta)[0]

# (b) V_spec = mu * sum_faces (1-cos F), F = face flux
faces=[(i,j,k) for i,j,k in combinations(range(N),3) if Adj[i,j] and Adj[j,k] and Adj[i,k]]
def faceflux(th):
    F=np.empty(len(faces))
    for r,(i,j,k) in enumerate(faces):
        F[r]=th[eidx[(i,j)]]+th[eidx[(j,k)]]-th[eidx[(i,k)]]
    return F
F=faceflux(theta); Vspec=mu*np.sum(1-np.cos(F))

# (c) Dirac with the same abelian flux: D_a = e^{i theta} D
Da=D.copy()
for k,(i,j) in enumerate(edges):
    Da[2*i:2*i+2,2*j:2*j+2]*=np.exp(1j*theta[k]); Da[2*j:2*j+2,2*i:2*i+2]*=np.exp(-1j*theta[k])
eva=np.linalg.eigvalsh(Da)
print(f"\n[pentagon-eps flux]  mean pentagon holonomy={np.mean(Bp@theta):.4f} (target eps={EPS:.4f})")
print(f"  (a) scalar Laplacian gap (vacuum mode) = {gap_scalar:.6f}")
print(f"  (b) V_spec = mu*sum(1-cosF) = {Vspec:.5f}   mu={mu:.6f} (PINNED)   sum(1-cosF)={np.sum(1-np.cos(F)):.5f}")
print(f"      mean|F| per face = {np.mean(np.abs(F)):.4f}")
print(f"  (c) Dirac smallest |eig| with flux = {np.min(np.abs(eva)):.6f}  (was ~0 for D)")

# scaling with flux strength f (does V_spec and the gap track together, both pinned?)
print("\n[flux sweep]  f*eps per pentagon:   scalar-gap     V_spec(pinned mu)   Dirac min|eig|")
for f in (0.0,0.5,1.0,2.0):
    th,_,_,_=np.linalg.lstsq(Bp,f*EPS*np.ones(len(pents)),rcond=None)
    Ff=faceflux(th); Vf=mu*np.sum(1-np.cos(Ff)); g=scal(th)[0]
    Da2=D.copy()
    for k,(i,j) in enumerate(edges):
        Da2[2*i:2*i+2,2*j:2*j+2]*=np.exp(1j*th[k]); Da2[2*j:2*j+2,2*i:2*i+2]*=np.exp(-1j*th[k])
    dmin=np.min(np.abs(np.linalg.eigvalsh(Da2)))
    print(f"  {f:4.2f}                       {g:10.6f}     {Vf:12.5f}      {dmin:10.6f}")
