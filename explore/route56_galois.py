"""
Decisive Galois test. The 120-icosian set is Galois-invariant (sqrt5->-sqrt5 permutes it), so on the SAME
points we can build either branch of the connection:
  phi-branch: neighbours at overlap phi/2=cos(pi/5),  c=phi/2
  psi-branch: neighbours at overlap psi/2=-1/(2phi),   c=psi/2    (the Galois conjugate)
Claim: the Dirac kernel flips {1,2',3'} (phi) <-> {1,2,3} (psi). Only sqrt5->-sqrt5 does this.
"""
import numpy as np, itertools
from itertools import permutations
phi=(1+5**0.5)/2; psi=(1-5**0.5)/2    # psi = -1/phi
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
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex); I2=np.eye(2,dtype=complex)
Q=np.array([V[k,0]*I2-1j*(V[k,1]*sx+V[k,2]*sy+V[k,3]*sz) for k in range(N)])
G=V@V.T
labels={round(12,3):"1",round(6*phi,3):"2",round(4*phi,3):"3",round(3,3):"4",round(0,3):"5",
        round(-2,3):"6",round(-4/phi,3):"3'",round(-3,3):"4'",round(6*psi,3):"2'"}

def branch(cval):
    s=np.sqrt(1-cval*cval)
    Adj=(np.abs(G-cval)<1e-6).astype(float); np.fill_diagonal(Adj,0)
    deg=Adj.sum(1)
    def g(i,j): return (Q[j]@Q[i].conj().T-cval*I2)/s
    D=np.zeros((2*N,2*N),complex); chk=0
    for i in range(N):
        for j in np.where(Adj[i]>0)[0]:
            gij=g(i,j); chk=max(chk,np.max(np.abs(gij@gij+I2))); D[2*i:2*i+2,2*j:2*j+2]=gij
    ev,U=np.linalg.eigh(D); ker=U[:,np.abs(ev)<1e-6]
    M=np.zeros((N,N),complex)
    for m in range(ker.shape[1]):
        R=ker[:,m].reshape(N,2); M+=R@R.conj().T
    wA,UA=np.linalg.eigh(Adj); vals,idx=np.unique(np.round(wA,3),return_inverse=True)
    out={}
    for vi,lam in enumerate(vals):
        cols=np.where(idx==vi)[0]; P=UA[:,cols]@UA[:,cols].conj().T
        w=np.real(np.trace(P@M))
        if w>1e-3: out[labels.get(round(lam,3),f"?{lam:.2f}")]=round(w,1)
    return int(deg.min()),int(deg.max()),ker.shape[1],chk,out

for name,cval in [("phi-branch (c=phi/2= %.4f)"%(phi/2), phi/2),
                  ("psi-branch (c=psi/2= %.4f)"%(psi/2), psi/2)]:
    dmin,dmax,kd,chk,out=branch(cval)
    print(f"[{name}]  degree {dmin}..{dmax}  gamma^2+I err {chk:.0e}  kernel dim {kd}")
    print(f"     kernel irrep weights: {out}")
print("\n[expected] phi-branch kernel {1,2',3'};  psi-branch kernel {1,2,3}  (the Galois flip).")
