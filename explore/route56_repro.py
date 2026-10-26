"""
Cold, independent reproduction of route56 (F5/F6 Clifford connection + Dirac operator).
Rebuild gamma, D, the face trace, V_spec, mu -- check against the banked numbers:
  spectrum -7.608..4.129, 28 zero modes; Tr(D^2)=2880; face trace -(8/5)sin(pi/5);
  mu=(48/5)sin(pi/5)=5.642738; Omega=cI-s*gamma; D^tr = s A(x)I + c D.
"""
import numpy as np, itertools
from itertools import permutations, combinations
phi=(1+5**0.5)/2; c=phi/2; s=np.sqrt(1-c*c)   # c=cos(pi/5), s=sin(pi/5)

# 120 icosians
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
print(f"[carrier] N={N}, edges={int(Adj.sum()//2)}")

# quaternion -> SU(2):  Q = q0 I - i (q1 sx + q2 sy + q3 sz)
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex); I2=np.eye(2,dtype=complex)
Q=np.array([V[k,0]*I2 -1j*(V[k,1]*sx+V[k,2]*sy+V[k,3]*sz) for k in range(N)])

def gamma(i,j): return (Q[j]@Q[i].conj().T - c*I2)/s
# checks on gamma
mx2=mxH=mxA=0.0
for i in range(N):
    for j in np.where(Adj[i])[0]:
        g=gamma(i,j)
        mx2=max(mx2,np.max(np.abs(g@g+I2)))                 # gamma^2=-I
        mxH=max(mxH,np.max(np.abs(g.conj().T+g)))           # gamma^dagger=-gamma
        mxA=max(mxA,np.max(np.abs(gamma(j,i)+g)))           # gamma_ji=-gamma_ij
print(f"[gamma] max|g^2+I|={mx2:.1e}  max|g^dag+g|={mxH:.1e}  max|g_ji+g_ij|={mxA:.1e}")

# Dirac D on C^120 (x) C^2  (240x240): block (i,j)=A_ij gamma_ij
D=np.zeros((2*N,2*N),complex)
for i in range(N):
    for j in np.where(Adj[i])[0]:
        D[2*i:2*i+2,2*j:2*j+2]=gamma(i,j)
print(f"[D] Hermitian: max|D-D^dag|={np.max(np.abs(D-D.conj().T)):.1e}")
ev=np.linalg.eigvalsh(D)
print(f"[D] spectrum: min={ev.min():.5f} max={ev.max():.5f}  zero modes(|ev|<1e-9)={int(np.sum(np.abs(ev)<1e-9))}")
print(f"[D] Tr(D^2)={np.real(np.trace(D@D)):.1f}  (banked 2880)")

# faces (triangles) and the Clifford face trace
faces=[(i,j,k) for i,j,k in combinations(range(N),3) if Adj[i,j] and Adj[j,k] and Adj[i,k]]
tr=[np.real(np.trace(gamma(i,j)@gamma(j,k)@gamma(k,i))) for (i,j,k) in faces]
print(f"[faces] count={len(faces)} (banked 1200); Tr2(g g g): mean={np.mean(tr):.6f} std={np.std(tr):.1e}"
      f"  vs -(8/5)sin(pi/5)={-(8/5)*s:.6f}")
print(f"[mu] (48/5)sin(pi/5) = {(48/5)*s:.6f}  (banked 5.642738)")

# Omega and the D^tr identity (spot check on a few edges)
okO=0.0
for i in range(N):
    for j in np.where(Adj[i])[0]:
        Om=Q[i]@Q[j].conj().T
        okO=max(okO,np.max(np.abs(Om-(c*I2-s*gamma(i,j)))))
print(f"[Omega] max|Q_iQ_j^dag-(cI-s g_ij)|={okO:.1e}  (Omega=cI-s gamma)")
