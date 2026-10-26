"""
Why is the Dirac kernel {1,2',3'} (the psi-branch) and not {1,2,3} (the phi-branch)?
Test the chirality reading: apply a PARITY (orientation-reversing) reflection of the carrier,
rebuild D, and see whether the kernel flips to the Galois-conjugate branch {1,2,3}.
If parity swaps the kernel's Galois branch, the selection IS a chirality/Galois choice by gamma.
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
def Qof(W): return np.array([W[k,0]*I2-1j*(W[k,1]*sx+W[k,2]*sy+W[k,3]*sz) for k in range(N)])

wA,UA=np.linalg.eigh(Adj)
labels={round(12,4):"1",round(6*phi,4):"2",round(4*phi,4):"3",round(3,4):"4",round(0,4):"5",
        round(-2,4):"6",round(-4/phi,4):"3'",round(-3,4):"4'",round(6*psi,4):"2'"}
def kernel_irreps(Vcoords):
    Q=Qof(Vcoords)
    def g(i,j): return (Q[j]@Q[i].conj().T-c*I2)/s
    D=np.zeros((2*N,2*N),complex)
    for i in range(N):
        for j in np.where(Adj[i]>0)[0]: D[2*i:2*i+2,2*j:2*j+2]=g(i,j)
    ev,U=np.linalg.eigh(D); ker=U[:,np.abs(ev)<1e-6]
    M=np.zeros((N,N),complex)
    for m in range(ker.shape[1]):
        R=ker[:,m].reshape(N,2); M+=R@R.conj().T
    out={}
    vals,idx=np.unique(np.round(wA,4),return_inverse=True)
    for vi,lam in enumerate(vals):
        cols=np.where(idx==vi)[0]; P=UA[:,cols]@UA[:,cols].conj().T
        w=np.real(np.trace(P@M))
        if w>1e-3: out[labels.get(round(lam,4),"?")]=round(w,2)
    return ker.shape[1],out

k0,ir0=kernel_irreps(V)
print(f"[original carrier]      kernel dim {k0}: irrep weights {ir0}")

# PARITY: orientation-reversing reflection (negate q3). It permutes the 120 icosians.
Vp=V.copy(); Vp[:,3]*=-1
same=set(map(tuple,np.round(V,6)))==set(map(tuple,np.round(Vp,6)))
print(f"[parity q3->-q3] permutes the carrier set: {same} (reflection, det -1)")
kp,irp=kernel_irreps(Vp)
print(f"[parity-reflected]      kernel dim {kp}: irrep weights {irp}")

print(f"\n[reading] original selects psi-branch {{1,2',3'}}; 28 = 2*(1^2+2^2+3^2).")
print("  if parity flips to {1,2,3} (phi-branch), the kernel selection IS a chirality/Galois choice.")
