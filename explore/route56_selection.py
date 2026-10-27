"""
Why is ker D = {1,2',3'} (x) C^2 ?  And is the 'Galois flip' a flip of the subspace or a relabeling?

Derivation (checked numerically below).  For f in the isotypic block V_rho of the regular representation of 2I,
  D (f (x) chi) = 0 for all spinors chi   <=>   A(fQ) = c * lambda_rho * (fQ),   (fQ)_j = f_j Q_j.
fQ lies in the blocks of  rho (x) 2  (2 = defining spinor rep).  lambda_sigma = 12 chi_sigma(h)/d_sigma and
chi_2(h) = 2c, so an IRREDUCIBLE rho (x) 2 = sigma has lambda_sigma = c*lambda_rho automatically.  If it is
reducible its components have different lambda (the 9 irreps have 9 distinct lambda) and f(x)chi is not in ker D.
  =>   ker D = (+) over { rho : rho (x) 2 irreducible }  of  V_rho (x) C^2.

Tests:
 1  character table from the regular rep; decompose rho(x)2 and rho(x)2'.
 2  kernel containment per rho for three connections:
      (a) phi-graph, transport Q               (route56)
      (b) psi-graph, transport Q               (the 'psi-branch' of route56_galois.py)
      (c) phi-graph, transport Q' = Q o sigma  (the Galois-conjugate spinor rep 2')
 3  overlaps tr(Pi_a Pi_b)/28 between the kernel subspaces.
 4  L x R structure and fold parity of the kernel blocks.
"""
import numpy as np, itertools
from itertools import permutations
np.set_printoptions(suppress=True, linewidth=160)
phi=(1+5**0.5)/2; psi=(1-5**0.5)/2

# ---- 120 icosians ----
V=[]
for i in range(4):
    for sg in (1,-1):
        v=[0,0,0,0]; v[i]=sg; V.append(v)
for sgs in itertools.product((0.5,-0.5),repeat=4): V.append(list(sgs))
base=[0.0,0.5,phi/2,1/(2*phi)]
def par(p):
    p=list(p); seen=[False]*4; k=0
    for i in range(4):
        if seen[i]: continue
        j=i; cl=0
        while not seen[j]: seen[j]=True; j=p[j]; cl+=1
        k+=cl-1
    return k%2
for p in [q for q in permutations(range(4)) if par(q)==0]:
    vals=[base[p[i]] for i in range(4)]; nz=[i for i in range(4) if vals[i]!=0]
    for ss in itertools.product((1,-1),repeat=3):
        v=list(vals)
        for k,idx in enumerate(nz): v[idx]=vals[idx]*ss[k]
        V.append(v)
V=np.unique(np.round(np.array(V),9),axis=0); N=len(V); assert N==120
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex); I2=np.eye(2,dtype=complex)
Q=np.array([V[k,0]*I2-1j*(V[k,1]*sx+V[k,2]*sy+V[k,3]*sz) for k in range(N)])

def key(M):
    a=np.concatenate([M.real.ravel(),M.imag.ravel()])
    return tuple((np.round(a,5)+0.0).tolist())
gidx={key(Q[k]):k for k in range(N)}; assert len(gidx)==N
Lp=np.array([[gidx[key(Q[a]@Q[i])] for i in range(N)] for a in range(N)])   # left translation a.i
neg=gidx[key(-I2)]; trQ=np.array([np.trace(Q[a]).real for a in range(N)])

G=V@V.T
Aphi=(np.abs(G-phi/2)<1e-6).astype(float); np.fill_diagonal(Aphi,0)
Apsi=(np.abs(G-psi/2)<1e-6).astype(float); np.fill_diagonal(Apsi,0)
assert Aphi.sum(1).min()==12==Aphi.sum(1).max() and Apsi.sum(1).min()==12==Apsi.sum(1).max()

# ---- isotypic blocks (phi-graph eigenspaces) and characters ----
lamname={12.0:'1', round(6*phi,4):'2', round(6*psi,4):"2'", round(4*phi,4):'3', round(4*psi,4):"3'",
         3.0:"4'", -3.0:'4', 0.0:'5', -2.0:'6'}      # 4 = vector (2x2'), 4' = spinor (Sym^3), corpus convention
wA,UA=np.linalg.eigh(Aphi)
lv,inv=np.unique(np.round(wA,4),return_inverse=True)
Pm={}; dd={}; lam={}; chi={}
for vi,l in enumerate(lv):
    n=lamname[round(float(l),4)+0.0]; cols=np.where(inv==vi)[0]
    P=UA[:,cols]@UA[:,cols].conj().T; Pm[n]=P; d=int(round(len(cols)**0.5)); dd[n]=d; lam[n]=float(l)
    chi[n]=np.array([sum(P[k,Lp[a,k]] for k in range(N)) for a in range(N)]).real/d
names=['1','2',"2'",'3',"3'",'4',"4'",'5','6']
for n in names:
    assert abs(chi[n]@chi[n]/N-1)<1e-8, n
    assert abs(Pm[n].real.trace()-dd[n]**2)<1e-8
for n in names:                                   # commute with the psi-graph too?
    assert np.abs(Pm[n]@Apsi-Apsi@Pm[n]).max()<1e-8
print("[blocks] 9 irreps; characters orthonormal; each isotypic block V_rho also commutes with the psi-graph adjacency")
print(f"[check] chi_2 equals tr(Q_a): {np.abs(chi['2']-trQ).max():.1e}   (so lambda=6phi block IS the defining spinor rep)")
eps={n:chi[n][neg]/dd[n] for n in names}

def decomp(cp):
    out=[]
    for n in names:
        m=np.mean(cp*chi[n]); mi=int(round(m)); assert abs(m-mi)<1e-6
        if mi: out.append((mi,n))
    return out
fmt=lambda dec:" + ".join((f"{m}*" if m>1 else "")+n for m,n in dec)
irr=lambda dec:len(dec)==1 and dec[0][0]==1
print("\n[1] CG decomposition with the two spinor reps   (lambda = phi-graph eigenvalue, fold = chi(-1)/d)")
print("  rho   d   lambda    fold |  rho (x) 2            irreducible |  rho (x) 2'           irreducible")
pred2={}; pred2p={}
for n in names:
    d2=decomp(chi[n]*chi['2']); d2p=decomp(chi[n]*chi["2'"]); pred2[n]=irr(d2); pred2p[n]=irr(d2p)
    print(f"  {n:3s}  {dd[n]}  {lam[n]:8.4f}  {eps[n]:+.0f}  |  {fmt(d2):20s}  {str(irr(d2)):9s}   |  {fmt(d2p):20s}  {str(irr(d2p))}")

# eigenvalue relation  lambda_sigma = c * lambda_rho  for the irreducible cases
c=phi/2
print("\n[1b] eigenvalue relation for irreducible rho (x) 2 = sigma:  lambda_sigma vs c*lambda_rho   (c = phi/2)")
for n in names:
    d2=decomp(chi[n]*chi['2'])
    if irr(d2): print(f"   {n:3s} (x) 2 = {d2[0][1]:3s}:  lambda_sigma = {lam[d2[0][1]]:8.4f}   c*lambda_rho = {c*lam[n]:8.4f}")

# ---- connections and kernels ----
def build_D(Qm,Adj,cc):
    s=np.sqrt(1-cc*cc); D=np.zeros((2*N,2*N),complex); err=0.0
    for i in range(N):
        for j in np.where(Adj[i]>0)[0]:
            g=(Qm[j]@Qm[i].conj().T-cc*I2)/s; err=max(err,np.abs(g@g+I2).max()); D[2*i:2*i+2,2*j:2*j+2]=g
    return D,err
def kproj(D):
    ev,U=np.linalg.eigh(D); K=U[:,np.abs(ev)<1e-6]; return K@K.conj().T,K.shape[1]

# Galois permutation pi: coordinates -> sqrt5 -> -sqrt5
tab=[(0,0),(0.5,0.5),(-0.5,-0.5),(1,1),(-1,-1),(phi/2,-1/(2*phi)),(-phi/2,1/(2*phi)),(1/(2*phi),-phi/2),(-1/(2*phi),phi/2)]
def sg(x):
    for a,b in tab:
        if abs(x-a)<1e-6: return b
    raise ValueError(x)
def Qmat(w): return w[0]*I2-1j*(w[1]*sx+w[2]*sy+w[3]*sz)
# sigma(2I) is the mirror (odd-permutation) copy, NOT the same vertex set -- the transport need not be a vertex.
# Q'(g) = Q(sigma(g)) is a homomorphism g -> SU(2) (sigma is a ring automorphism) with character sigma(chi_2) = chi_2'.
Qp=np.array([Qmat([sg(x) for x in V[i]]) for i in range(N)])
hom=max(np.abs(Qp[Lp[a,i]]-Qp[a]@Qp[i]).max() for a in range(N) for i in range(N))
trQp=np.array([np.trace(Qp[a]).real for a in range(N)])
print(f"[Q'] homomorphism error {hom:.1e};  unitarity {max(np.abs(Qp[a]@Qp[a].conj().T-I2).max() for a in range(N)):.1e};  "
      f"tr Q' vs chi_2' from the regular rep: {np.abs(trQp-chi[chr(50)+chr(39)]).max():.1e}")

Da,ea=build_D(Q,Aphi,phi/2); Pa,ka=kproj(Da)
Db,eb=build_D(Q,Apsi,psi/2); Pb,kb=kproj(Db)
Dc,ec=build_D(Qp,Aphi,psi/2); Pc,kc=kproj(Dc)
print(f"\n[2] kernels: (a) phi-graph,Q: dim {ka} (g^2+I err {ea:.0e});  (b) psi-graph,Q: dim {kb} ({eb:.0e});  (c) phi-graph,Q'=Q.sigma: dim {kc} ({ec:.0e})")
def frac(Pi): return {n:np.real(np.trace(np.kron(Pm[n],I2)@Pi))/(2*dd[n]**2) for n in names}
fa,fb,fc=frac(Pa),frac(Pb),frac(Pc)
print("  fraction of the block V_rho (x) C^2 contained in the kernel")
print("  rho   (a) phi-graph,Q   (b) psi-graph,Q   (c) phi-graph,Q'  | rho(x)2 irr?  rho(x)2' irr?")
for n in names:
    print(f"  {n:3s}      {fa[n]:5.3f}            {fb[n]:5.3f}            {fc[n]:5.3f}        |  {str(pred2[n]):6s}        {str(pred2p[n])}")
print(f"\n[3] subspace overlaps tr(Pi_x Pi_y)/28:   (a,b) = {np.real(np.trace(Pa@Pb))/28:.4f}   (a,c) = {np.real(np.trace(Pa@Pc))/28:.4f}   (b,c) = {np.real(np.trace(Pb@Pc))/28:.4f}")

# ---- L x R content and fold parity of the kernel (a) ----
print("\n[4] kernel (a) as a representation of 2I_L x 2I_R:  V_rho (x) C^2 = (rho (x) 2)_L (x) rho*_R")
print("  rho_R   d   sigma_L = rho(x)2   d_sigma   modes   left-fold   right-fold   (fold = action of -1; spinor index carries -1 under L)")
tot=0; odd=0
for n in names:
    if fa[n]>0.99:
        d2=decomp(chi[n]*chi['2']); s=d2[0][1]; lf=-eps[n]; rf=eps[n]; m=dd[s]*dd[n]; tot+=m
        if lf<0: odd+=m
        print(f"  {n:3s}    {dd[n]}   {s:3s}                 {dd[s]}         {m:3d}     {lf:+.0f}          {rf:+.0f}")
print(f"  total modes {tot};  left-fold-odd (spinor-like): {odd};  left-fold-even (vector-like): {tot-odd}")

# ---- [5] the kernel's energy under the full transport:  D^tr = c D + s A(x)I  (route56 identity) ----
s_=np.sqrt(1-c*c)
lamx={'1':12.0,"2'":6*psi,"3'":4*psi}            # exact eigenvalues (lam[] above is rounded to 4 decimals)
Dtr=np.zeros_like(Da)
for i in range(N):
    for j in np.where(Aphi[i]>0)[0]:
        g=(Q[j]@Q[i].conj().T-c*I2)/s_; Om=Q[i]@Q[j].conj().T
        Dtr[2*i:2*i+2,2*j:2*j+2]=g@Om                       # D^tr_ij = gamma_ij Omega_ij
print(f"\n[5] D^tr built directly (gamma*Omega) vs c*D + s*A(x)I:  max diff = {np.abs(Dtr-(c*Da+s_*np.kron(Aphi,I2))).max():.1e}")
evP,UP=np.linalg.eigh(Pa); Kb=UP[:,evP>0.5]; assert Kb.shape[1]==28
leak=np.abs(Dtr@Kb-Kb@(Kb.conj().T@Dtr@Kb)).max()
Hk=np.linalg.eigvalsh(Kb.conj().T@Dtr@Kb)
vals,cnt=np.unique(np.round(Hk,4),return_counts=True)
print(f"    kernel is invariant under D^tr (leak {leak:.1e}); D^tr on the kernel has levels:")
for v,k in zip(vals,cnt): print(f"      {v:9.4f}  x{k}")
print("    predicted s*lambda_rho for rho in {1,2',3'}:  " + "   ".join(f"{s_*lamx[n]:9.4f} (x{2*dd[n]**2})" for n in ['1',"2'","3'"]))
evD=np.linalg.eigvalsh(Da)
print("    D itself has, at -s*lambda_rho (the transport-dual shadow of the kernel):")
for n in ['1',"2'","3'"]:
    print(f"      -s*lambda({n}) = {-s_*lamx[n]:9.4f}:  D-multiplicity {int(np.sum(np.abs(evD+s_*lamx[n])<1e-6))}")
print(f"    ratios of the three levels |s*lambda|: {abs(lam['1']):.4f} : {abs(lam[chr(50)+chr(39)]):.4f} : {abs(lam[chr(51)+chr(39)]):.4f}  =  12 : 6/phi : 4/phi")
