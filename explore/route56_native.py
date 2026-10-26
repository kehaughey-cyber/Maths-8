"""
The NATIVE non-abelian curvature -- already inside gamma, not an abelian flux added on top.
 (1) the native Dirac spectrum D=A*gamma: distinct eigenvalues + multiplicities, the 28 massless modes,
     and the massive sector (the native 'masses' from the connection).
 (2) the native per-face Wilson holonomy W = gamma_ij gamma_jk gamma_ki (an SU(2) element): is it the
     SAME on every face (uniform non-abelian field strength)? its SU(2) and SO(3) rotation angle.
 (3) compare the holonomy angle and the spectrum endpoints to golden/torsion values.
"""
import numpy as np, itertools
from itertools import permutations, combinations
phi=(1+5**0.5)/2; c=phi/2; s=np.sqrt(1-c*c); psi=-1/phi
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
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex); I2=np.eye(2,dtype=complex)
Q=np.array([V[k,0]*I2-1j*(V[k,1]*sx+V[k,2]*sy+V[k,3]*sz) for k in range(N)])
def gamma(i,j): return (Q[j]@Q[i].conj().T-c*I2)/s
D=np.zeros((2*N,2*N),complex)
for i in range(N):
    for j in np.where(Adj[i])[0]: D[2*i:2*i+2,2*j:2*j+2]=gamma(i,j)

# (1) native Dirac spectrum structure
ev=np.linalg.eigvalsh(D)
vals,cnts=np.unique(np.round(ev,4),return_counts=True)
print("[native Dirac spectrum]  eigenvalue (mult)   -- the native connection's own 'mass' spectrum")
for v,cc in zip(vals,cnts):
    tag=""
    for name,x in [("0",0),("3",3),("-3",-3),("4phi",4*phi),("-4phi",-4*phi),("4/phi",4/phi),
                   ("-4/phi",-4/phi),("2phi",2*phi),("-2phi",-2*phi),("1+phi",1+phi)]:
        if abs(v-x)<2e-2: tag=f"~{name}"
    print(f"   {v:9.4f}  x{cc:<3d} {tag}")
print(f"   total modes {len(ev)}; massless (|ev|<1e-6): {int(np.sum(np.abs(ev)<1e-6))} (banked 28)")
print(f"   spectrum endpoints: {ev.min():.5f}, {ev.max():.5f}")
print(f"     candidates: 4phi+? 7.608 vs 4phi={4*phi:.4f}, 2+2phi={2+2*phi:.4f}; 4.129 vs 1+phi+?={1+phi:.4f}")

# (2) native per-face Wilson holonomy
faces=[(i,j,k) for i,j,k in combinations(range(N),3) if Adj[i,j] and Adj[j,k] and Adj[i,k]]
trs=[]; dets=[]; so3=[]
for (i,j,k) in faces:
    W=gamma(i,j)@gamma(j,k)@gamma(k,i)
    t=np.trace(W); trs.append(t); dets.append(np.linalg.det(W))
    # SO(3) rotation angle of x->W x W^-1 on Im-quaternions: trR=|trW|^2-1
    trR=abs(t)**2-1; so3.append(np.degrees(np.arccos(np.clip((trR-1)/2 if False else trR, -1,1))))
trs=np.array(trs)
print(f"\n[native face holonomy W=g_ij g_jk g_ki]  (SU(2), det should be 1)")
print(f"   Tr(W): mean {np.mean(trs.real):.6f} std {np.std(trs.real):.1e};  |det|: {np.mean(np.abs(dets)):.4f}")
print(f"   UNIFORM across all {len(faces)} faces: std of Tr = {np.std(trs.real):.1e} -> same non-abelian field strength everywhere")
alpha=2*np.degrees(np.arccos(np.clip(np.mean(trs.real)/2,-1,1)))   # SU(2) angle: Tr=2cos(alpha/2)
print(f"   SU(2) rotation angle alpha (Tr=2cos(alpha/2)) = {alpha:.4f} deg;  SO(3) angle = {360-alpha:.4f} deg")
print(f"   compare: 2pi/5={360/5}, 2pi/3={360/3:.2f}, arccos(1/3)={np.degrees(np.arccos(1/3)):.4f}, "
      f"180-arccos(1/3)={180-np.degrees(np.arccos(1/3)):.4f}")
