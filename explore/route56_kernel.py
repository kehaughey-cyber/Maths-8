"""
Characterize the 28 massless Dirac modes (ker D, D=A*gamma): which carrier sector/irreps do they occupy?
Project the kernel's spatial reduced density onto the adjacency eigenspaces (= the 2I irreps = the
mass sectors: lambda=12 -> irrep1/mass12, lambda=0 -> irrep5/mass0, etc.). Also the spinor polarization.
"""
import numpy as np, itertools
from itertools import permutations
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
Adj=(np.abs(V@V.T-c)<1e-6).astype(float); np.fill_diagonal(Adj,0)
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex); I2=np.eye(2,dtype=complex)
Q=np.array([V[k,0]*I2-1j*(V[k,1]*sx+V[k,2]*sy+V[k,3]*sz) for k in range(N)])
def gamma(i,j): return (Q[j]@Q[i].conj().T-c*I2)/s
D=np.zeros((2*N,2*N),complex)
for i in range(N):
    for j in np.where(Adj[i]>0)[0]: D[2*i:2*i+2,2*j:2*j+2]=gamma(i,j)

evD,UD=np.linalg.eigh(D)
ker=UD[:,np.abs(evD)<1e-6]   # 240 x 28
print(f"kernel dim = {ker.shape[1]} (expect 28)")

# spatial reduced density of the kernel projector (trace over spinor)
M=np.zeros((N,N),complex)
for m in range(ker.shape[1]):
    R=ker[:,m].reshape(N,2)          # (vertex, spinor)
    M+=R@R.conj().T
print(f"Tr(M) = {np.real(np.trace(M)):.4f} (= kernel dim)")

# project onto adjacency eigenspaces (the irreps / mass sectors)
wA,UA=np.linalg.eigh(Adj)
irrep={round(12,4):("1",12.0),round(6*phi,4):("2",None),round(4*phi,4):("3",4.0),round(3,4):("4",None),
       round(0,4):("5",0.0),round(-2,4):("6",None),round(-4/phi,4):("3'",4.0),round(-3,4):("4'",None),
       round(6*psi,4):("2'",None)}
print("\n[kernel content by carrier irrep]  adjacency-eigenvalue -> (irrep, Galois mass) : weight of the 28")
vals,idxs=np.unique(np.round(wA,4),return_inverse=True)
for vi,lam in enumerate(vals):
    cols=np.where(idxs==vi)[0]; P=UA[:,cols]@UA[:,cols].conj().T
    w=np.real(np.trace(P@M))
    name,mass=irrep.get(round(lam,4),("?",None))
    mt="mass %s"%("%g"%mass if mass is not None else "-")
    print(f"   lambda={lam:8.4f}  (irrep {name:2s}, {mt:8s})  d^2={len(cols):2d} :  weight = {w:7.4f}")

# spinor polarization of the kernel
S=np.zeros((2,2),complex)
for m in range(ker.shape[1]):
    R=ker[:,m].reshape(N,2); S+=R.conj().T@R
print(f"\n[spinor density] (trace {np.real(np.trace(S)):.3f}) eigenvalues {np.round(np.real(np.linalg.eigvalsh(S)),4)}  "
      f"(equal = unpolarized)")
