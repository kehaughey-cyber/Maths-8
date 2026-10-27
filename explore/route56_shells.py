"""
The Clifford connection on EVERY class-shell graph of the carrier, with both spinor transports (2 and 2').
Shell graphs: neighbours at overlap c = Re(h) for h in each nontrivial conjugacy class of 2I:
   cos(pi/5)=phi/2 (order 10), cos(2pi/5)=1/(2phi) (order 5), cos(3pi/5)=-1/(2phi) (order 10),
   cos(4pi/5)=-phi/2 (order 5)   [powers n=1..4 of the order-10 element],
   1/2 (order 6), 0 (order 4), -1/2 (order 3).   (c=+1: identity, c=-1: antipode -> s=0, trivial.)
For each: D_c = A_c * gamma, gamma_ij = (T_j T_i^dag - c' I)/s', T = transport rep (Q or Q'), c' = c (Q) or sigma(c) (Q').
Every level of D is labelled by its channel (right irrep rho -> left irrep sigma) using the exact L x R symmetry.
Also: does the block rule  'rho in ker  <=>  every sigma in rho(x)tau has lambda^c_sigma = c' lambda^c_rho'  predict the kernel?
"""
import numpy as np, itertools
from itertools import permutations
np.set_printoptions(suppress=True, linewidth=170)
phi=(1+5**0.5)/2; psi=(1-5**0.5)/2

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
def Qmat(w): return w[0]*I2-1j*(w[1]*sx+w[2]*sy+w[3]*sz)
Q=np.array([Qmat(V[k]) for k in range(N)])
def key(M):
    a=np.concatenate([M.real.ravel(),M.imag.ravel()]); return tuple((np.round(a,5)+0.0).tolist())
gidx={key(Q[k]):k for k in range(N)}; assert len(gidx)==N
Lp=np.array([[gidx[key(Q[a]@Q[i])] for i in range(N)] for a in range(N)])
trQ=np.array([np.trace(Q[a]).real for a in range(N)])
G=V@V.T

# Galois sigma on coordinates and the conjugate transport Q' = Q o sigma (a homomorphism, character chi_2')
tab=[(0,0),(0.5,0.5),(-0.5,-0.5),(1,1),(-1,-1),(phi/2,-1/(2*phi)),(-phi/2,1/(2*phi)),(1/(2*phi),-phi/2),(-1/(2*phi),phi/2)]
def sg(x):
    for a,b in tab:
        if abs(x-a)<1e-6: return b
    raise ValueError(x)
Qp=np.array([Qmat([sg(x) for x in V[i]]) for i in range(N)])

# irreps from the phi-graph eigenspaces (isotypic blocks are graph-independent)
Aphi=(np.abs(G-phi/2)<1e-6).astype(float); np.fill_diagonal(Aphi,0)
lamname={12.0:'1', round(6*phi,4):'2', round(6*psi,4):"2'", round(4*phi,4):'3', round(4*psi,4):"3'",
         3.0:"4'", -3.0:'4', 0.0:'5', -2.0:'6'}
wA,UA=np.linalg.eigh(Aphi); lv,inv=np.unique(np.round(wA,4),return_inverse=True)
Pm={}; dd={}; chi={}
for vi,l in enumerate(lv):
    n=lamname[round(float(l),4)+0.0]; cols=np.where(inv==vi)[0]
    P=UA[:,cols]@UA[:,cols].conj().T; Pm[n]=P; dd[n]=int(round(len(cols)**0.5))
    chi[n]=np.array([sum(P[k,Lp[a,k]] for k in range(N)) for a in range(N)]).real/dd[n]
names=['1','2',"2'",'3',"3'",'4',"4'",'5','6']
chitau={'2':chi['2'],"2'":chi["2'"]}
def decomp(cp):
    out=[]
    for n in names:
        m=np.mean(cp*chi[n]); mi=int(round(m))
        if mi: out.append((mi,n))
    return out

def build_D(T,Adj,cc):
    s=np.sqrt(1-cc*cc); D=np.zeros((2*N,2*N),complex); err=0.0
    for i in range(N):
        for j in np.where(Adj[i]>0)[0]:
            g=(T[j]@T[i].conj().T-cc*I2)/s; err=max(err,np.abs(g@g+I2).max()); D[2*i:2*i+2,2*j:2*j+2]=g
    return D,err
def Umat(a,T):
    U=np.zeros((2*N,2*N),complex)
    for i in range(N): k=Lp[a,i]; U[2*k:2*k+2,2*i:2*i+2]=T[a]
    return U
def charL(Pr,T):
    P4=Pr.reshape(N,2,N,2); out=np.empty(N)
    ar=np.arange(N)
    for a in range(N):
        X=P4[ar,:,Lp[a],:]                    # (N,2,2): Pr[(i,alpha),(a.i,beta)]
        out[a]=np.real(np.einsum('iab,ba->',X,T[a]))
    return out

shells=[("n=1 order10",phi/2),("n=2 order5 ",1/(2*phi)),("order6     ",0.5),("order4     ",0.0),
        ("order3     ",-0.5),("n=3 order10",-1/(2*phi)),("n=4 order5 ",-phi/2)]

def analyse(label,c,T,tname,full):
    cT=c if tname=='2' else sg(c)
    Adj=(np.abs(G-c)<1e-6).astype(float); np.fill_diagonal(Adj,0); deg=int(Adj.sum(1)[0]); assert Adj.sum(1).min()==Adj.sum(1).max()
    D,err=build_D(T,Adj,cT)
    guard=max(np.abs(Umat(a,T)@D-D@Umat(a,T)).max() for a in (5,37,81))
    h=int(np.argmin(np.abs(trQ/2-c)))                                   # an element of the class
    lamc={n:deg*chi[n][h]/dd[n] for n in names}                          # eigenvalue of A_c on V_n
    ev,Uv=np.linalg.eigh(D); lvv,iv=np.unique(np.round(ev,5),return_inverse=True)
    print(f"\n=== shell {label} c={c:+.4f} (|C|={deg}, class element Re={trQ[h]/2:+.4f}) | transport {tname} (c'={cT:+.4f}) | g^2+I err {err:.0e}, [U,D] guard {guard:.0e}")
    # block rule prediction
    pred=[]
    for n in names:
        dec=decomp(chi[n]*chitau[tname])
        if all(abs(lamc[s2]-cT*lamc[n])<1e-6 for _,s2 in dec): pred.append(n)
    # actual kernel blocks
    kc=np.where(np.abs(ev)<1e-5)[0]; Kk=Uv[:,kc]; Pk=Kk@Kk.conj().T
    act=[n for n in names if np.real(np.trace(np.kron(Pm[n],I2)@Pk))>=2*dd[n]**2-0.01]
    part=[(n,round(float(np.real(np.trace(np.kron(Pm[n],I2)@Pk))),2)) for n in names if 0.01<np.real(np.trace(np.kron(Pm[n],I2)@Pk))<2*dd[n]**2-0.01]
    print(f"    kernel dim {len(kc)};  whole blocks in kernel: {act};  block-rule predicts: {pred};  partial blocks: {part}")
    if not full: return
    print("    level      mult   channels (right irrep rho -> left irrep sigma)")
    for k,l in enumerate(lvv):
        cols=np.where(iv==k)[0]; Kc=Uv[:,cols]; Pi=Kc@Kc.conj().T; pcs=[]
        for n in names:
            Pr=np.kron(Pm[n],I2)@Pi
            if np.real(np.trace(Pr))<0.5: continue
            ch=charL(Pr,T); sig=[]
            for sn in names:
                m=np.mean(ch*chi[sn])/dd[n]
                if m>0.5: sig.append(sn if round(m)==1 else f"{round(m)}x{sn}")
            pcs.append(f"{n}->{'+'.join(sig)}")
        print(f"    {l:9.4f}  {len(cols):4d}   {'  '.join(pcs)}")

for label,c in shells:
    analyse(label,c,Q,'2',True)
print("\n\n######## the Galois-conjugate transport 2' on every shell (kernel only) ########")
for label,c in shells:
    analyse(label,c,Qp,"2'",False)
