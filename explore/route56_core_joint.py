"""
Joint 2I_L x 2I_R decomposition of the n=1 28-mode kernel of the route56 Dirac operator on the 120-vertex carrier (extends route56_core.py, which gave left and right contents separately).
Builds T_g (left mult, spinor rotated) and R_h (right mult) as 240x240 unitaries, chi(g,h)=tr(K^dag T_g R_h K) on the kernel K, multiplicity m(rho,tau)=sum chi(g,h) conj rho(g) conj tau(h)/120^2.
Also the commutant dimension sum m^2 (a non-abelian commutant would be needed for a continuous gauge algebra acting on the core).    Usage: py -3 -I -u route56_core_joint.py
"""
import numpy as np, io, contextlib, sys, os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
with contextlib.redirect_stdout(io.StringIO()): import route56_core as rc
sd=rc.sd; V=rc.V; CH=rc.CH
P,E=sd.subdivide(V,1); N=len(P); assert N==120
Q=np.array([sd.Qmat(p) for p in P]); key={tuple(np.round(p,6)+0.0):i for i,p in enumerate(P)}
nbr=[[] for _ in range(N)]
for a,b in E: nbr[a].append(b); nbr[b].append(a)
D=np.zeros((2*N,2*N),complex)
for i in range(N):
    for j in nbr[i]:
        c=float(np.clip(P[i]@P[j],-1,1)); s=np.sqrt(1-c*c); D[2*i:2*i+2,2*j:2*j+2]=(Q[j]@Q[i].conj().T-c*sd.I2)/s
w,U=np.linalg.eigh(D); K=U[:,np.abs(w)<1e-8]; print("kernel dim",K.shape[1])
def mats(side,g):
    Qg=sd.Qmat(g); M=np.zeros((2*N,2*N),complex)
    for i,p in enumerate(P):
        X=(Qg@Q[i]) if side=='L' else (Q[i]@Qg); v,w0=rc.qvec(X); j=key[tuple(np.round(np.array([w0,*v]),6)+0.0)]
        M[2*j:2*j+2,2*i:2*i+2]=Qg if side=='L' else np.eye(2)
    return M
TL=[mats('L',g) for g in V]; TR=[mats('R',g) for g in V]
KL=[K.conj().T@T@K for T in TL]; KR=[K.conj().T@T@K for T in TR]
print("kernel invariant under T,R: ",max(np.linalg.norm(T@K-K@(K.conj().T@T@K)) for T in TL[:5]+TR[:5]))
chi=np.zeros((120,120))
for a in range(120):
    for b in range(120): chi[a,b]=np.trace(KL[a]@KR[b]).real
names=list(CH); tot=0; comm=0
print("joint multiplicities m(left rho, right tau) on the 28-core:")
for r in names:
    for t in names:
        m=CH[r]@chi@CH[t]/120**2
        if abs(m)>0.02:
            dr=int(r.rstrip("sg'")); dt=int(t.rstrip("sg'")); print(f"   ({r}, {t}): m = {m:.4f}, dim {dr*dt}"); tot+=m*dr*dt; comm+=round(m)**2
print("total dimension",round(tot,4),"; commutant dimension sum m^2 =",comm)
