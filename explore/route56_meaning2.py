"""
Corrected flatness test.  route56_meaning.py built the twisted adjacency with blocks Q_j Q_i^dag (push-forward); matrix products
of those multiply transports in the wrong order, so that T2 failed for a TEST-DESIGN reason.  Path composition needs the pull-back
transport  Omega_ij = Q_i Q_j^dag = c I - s gamma_ij  (route56's 'full return transport').
Tests:
  a) Omega-adjacency  TO(A)_ij = A_ij Q_i Q_j^dag  composes:  TO(A_1)^n = sum_c m_n(c) TO(A_c)   (same walk counts as A_1^n).
  b) it is PURE GAUGE:  TO(A) = W (A (x) I) W^dag,  W = diag(Q_i)   (the proper holonomy is trivial: F6).
  c) hence  D_c = ( c A_c (x) I  -  TO(A_c) ) / s_c   exactly.   (explains the channel formula (c lambda_rho - lambda_sigma)/s)
  d) distance-layer operators Lambda_d (hop distance d) as polynomials in A_1: minimal degree.
  e) extra: mixing ONLY order-6 and order-3 shells keeps the 18 extra zero channel (kernel 46).
"""
import os
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'route56_shells.py')).read().split("shells=[")[0]
exec(src)
shells=[("n=1 order10",phi/2),("n=2 order5 ",1/(2*phi)),("order6     ",0.5),("order4     ",0.0),
        ("order3     ",-0.5),("n=3 order10",-1/(2*phi)),("n=4 order5 ",-phi/2)]
cls_all=[("identity",1.0)]+[(l.strip(),c) for l,c in shells]+[("antipode",-1.0)]
Acl={c:(np.abs(G-c)<1e-6).astype(float) for _,c in cls_all}
for c in Acl:
    if abs(c-1)>1e-9: np.fill_diagonal(Acl[c],0) if abs(c+1)>1e-9 else None
A1=Acl[phi/2]
def TO(Am):
    T=np.zeros((2*N,2*N),complex)
    for i in range(N):
        for j in np.where(Am[i]>0)[0]: T[2*i:2*i+2,2*j:2*j+2]=Q[i]@Q[j].conj().T
    return T
TOcl={c:TO(Acl[c]) for _,c in cls_all}
W=np.zeros((2*N,2*N),complex)
for i in range(N): W[2*i:2*i+2,2*i:2*i+2]=Q[i]
print("b) pure gauge:  max |TO(A_c) - W (A_c (x) I) W^dag| over all 9 classes = %.1e" %
      max(np.abs(TOcl[c]-W@np.kron(Acl[c],I2)@W.conj().T).max() for _,c in cls_all))
print("a) composition:  TO(A_1)^n  vs  sum_c m_n(c) TO(A_c)")
T1=TOcl[phi/2]
for n in (2,3,4,5):
    An=np.linalg.matrix_power(A1,n); Tn=np.linalg.matrix_power(T1,n)
    m={c:An[0,np.where(np.abs(G[0]-c)<1e-6)[0][0]] for _,c in cls_all}
    rec=sum(m[c]*TOcl[c] for _,c in cls_all)
    print(f"   n={n}: err {np.abs(Tn-rec).max():.1e}   walk counts m_n(c) = "+", ".join(f"{m[c]:.0f}" for _,c in cls_all))
print("c) D_c = (c A_c (x) I - TO(A_c))/s_c :")
for l,c in cls_all[1:-1]:
    Adj=Acl[c]; D,_=build_D(Q,Adj,c); s=np.sqrt(1-c*c)
    print(f"   {l:12s} c={c:+.4f}:  max|D_c - (c A_c(x)I - TO(A_c))/s| = {np.abs(D-(c*np.kron(Adj,I2)-TOcl[c])/s).max():.1e}")
# d) layers
dist=np.full(N,-1); dist[0]=0; fr=[0]
while fr:
    nx=[]
    for i in fr:
        for j in np.where(A1[i]>0)[0]:
            if dist[j]<0: dist[j]=dist[i]+1; nx.append(j)
    fr=nx
D_=np.full((N,N),-1)
for i in range(N):                                   # all-pairs distance by BFS
    d=np.full(N,-1); d[i]=0; fr=[i]
    while fr:
        nx=[]
        for a in fr:
            for b in np.where(A1[a]>0)[0]:
                if d[b]<0: d[b]=d[a]+1; nx.append(b)
        fr=nx
    D_[i]=d
lam1=np.array([np.real(np.trace(Pm[n]@A1))/dd[n]**2 for n in names])
print("d) hop-distance layer operators Lambda_d as polynomials in the 1-hop A_1:")
for dlay in range(0,6):
    Lam=(D_==dlay).astype(float); lamL=np.array([np.real(np.trace(Pm[n]@Lam))/dd[n]**2 for n in names])
    for deg in range(0,9):
        Vd=np.vander(lam1,deg+1,increasing=True); coef=np.linalg.lstsq(Vd,lamL,rcond=None)[0]
        if np.abs(Vd@coef-lamL).max()<1e-8: break
    print(f"   distance {dlay}: layer size {int(Lam[0].sum()):3d}, minimal polynomial degree in A_1 = {deg}")
# e) order-6 + order-3 only
s6=[k for k,(l,c) in enumerate(shells) if l.strip() in ("order6","order3")]
Dl=[]
for k in s6:
    D,_=build_D(Q,(np.abs(G-shells[k][1])<1e-6).astype(float),shells[k][1]); Dl.append(D)
for w in ((1.0,1.0),(1.0,0.37),(2.0,-1.3)):
    ev=np.linalg.eigvalsh(w[0]*Dl[0]+w[1]*Dl[1]); print(f"e) order6+order3 mix w={w}: kernel dim {int(np.sum(np.abs(ev)<1e-6))}")
