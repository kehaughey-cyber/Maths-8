"""
(1) Does any weighted mix of shell connections keep the 28-mode core massless?
(2) Does the shell family mean anything physically?  Tests that can fail:
    T1  shells vs graph-distance (hop) layers of the 1-hop adjacency
    T2  flatness: is the multi-hop shell transport the COMPOSITION of 1-hop transports?
        (T_1^n = sum_c m_n(c) T_c with the same walk counts m_n(c) as A_1^n = sum_c m_n(c) A_c ?)
        and then: is every shell operator a polynomial of the single 1-hop pair (A_1, T_1), degree = hop distance?
    T3  continuum limit: is the lattice formula the shell-sampled teleparallel Dirac operator on S^3 ?
"""
import os
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'route56_shells.py')).read().split("shells=[")[0]
exec(src)
rng=np.random.default_rng(7)
shells=[("n=1 order10",phi/2),("n=2 order5 ",1/(2*phi)),("order6     ",0.5),("order4     ",0.0),
        ("order3     ",-0.5),("n=3 order10",-1/(2*phi)),("n=4 order5 ",-phi/2)]
Adjs=[]; Ds=[]
for label,c in shells:
    Adj=(np.abs(G-c)<1e-6).astype(float); np.fill_diagonal(Adj,0); Adjs.append(Adj)
    D,_=build_D(Q,Adj,c); Ds.append(D)
core=sum(np.kron(Pm[n],I2) for n in ('1',"2'","3'"))         # projector onto the 28-dim core (blocks 1, 2', 3' (x) C^2)
assert abs(np.trace(core).real-28)<1e-8
print("=== (1) WEIGHTED MIXES of shell connections  D_mix = sum_c w_c D_c   (transport 2) ===")
print(f"  core projector trace {np.trace(core).real:.0f};  ||D_c P_core|| per shell: " + "  ".join(f"{np.abs(D@core).max():.0e}" for D in Ds))
def kdim(Dm): ev=np.linalg.eigvalsh(Dm); return int(np.sum(np.abs(ev)<1e-6))
rows=[]
for kind in ("positive","signed","sparse-signed"):
    dims=[]; leak=0.0
    for t in range(60):
        w=rng.uniform(0.1,2,7) if kind=="positive" else rng.normal(size=7)
        if kind=="sparse-signed": w=w*(rng.random(7)<0.5)
        Dm=sum(wi*Di for wi,Di in zip(w,Ds)); dims.append(kdim(Dm)); leak=max(leak,np.abs(Dm@core).max())
    vals,cnt=np.unique(dims,return_counts=True)
    print(f"  {kind:14s}: 60 random weight vectors -> kernel dims {dict(zip(vals.tolist(),cnt.tolist()))};  max ||D_mix P_core|| = {leak:.1e}")
print("  mixes of ONLY the 'special' shells (order6, order4, order3) -> kernel dim:",
      [kdim(sum(wi*Ds[k] for wi,k in zip(rng.uniform(0.1,2,3),(2,3,4)))) for _ in range(3)])
# mix level = sum of formula levels?  (one sample, check eigenvalue sets)
w=rng.normal(size=7); Dm=sum(wi*Di for wi,Di in zip(w,Ds))
print(f"  mix is block-scalar on channels, so levels add: spectrum of D_mix has {len(np.unique(np.round(np.linalg.eigvalsh(Dm),5)))} distinct values (<=16 channels)")
# mixing the two Galois transports: D^(2)_c + D^(2')_c
Dp,_=build_D(Qp,Adjs[0],sg(phi/2))
print("  mixing the two spinor transports on the n=1 shell,  a*D^(2) + b*D^(2'):")
for a,b in ((1,1),(1,0.3),(1,-2)):
    Dm=a*Ds[0]+b*Dp; sing=np.kron(Pm['1'],I2)
    print(f"      (a,b)=({a},{b}):  kernel dim {kdim(Dm)};  singlet block (1)(x)C^2 in kernel: {np.abs(Dm@sing).max():.1e}")

print("\n=== (2) DOES THE SHELL FAMILY MEAN ANYTHING PHYSICALLY? ===")
# ---- T1: hop-distance layers ----
A1=Adjs[0]; P=np.eye(N); dist=np.full((N,N),-1)
for n in range(0,7):
    reach=(P>0.5)
    newm=reach&(dist<0); dist[newm]=n
    P=P@A1; P=(P>0.5).astype(float)@np.eye(N) if False else P
# robust BFS
dist=np.full(N,-1); dist[0]=0; frontier=[0]
while frontier:
    nxt=[]
    for i in frontier:
        for j in np.where(A1[i]>0)[0]:
            if dist[j]<0: dist[j]=dist[i]+1; nxt.append(j)
    frontier=nxt
print("T1  hop-distance layers from vertex 0 (1-hop = the n=1 shell): sizes "+str({d:int((dist==d).sum()) for d in range(6)}))
cls_all=[("identity",1.0)]+[(l.strip(),c) for l,c in shells]+[("antipode",-1.0)]
print("    each shell (overlap c) sits at hop-distance:")
for l,c in cls_all:
    members=np.where(np.abs(G[0]-c)<1e-6)[0]; ds=sorted(set(dist[members].tolist()))
    print(f"      {l:12s} c={c:+.4f}  |C|={len(members):3d}  hop-distance {ds}")

# ---- T2: flatness => shells are compositions of 1-hop transports ----
Acl={c:(np.abs(G-c)<1e-6).astype(float) for _,c in cls_all}
def Tmat(Am):                                  # twisted adjacency  (T)_{ij} = A_ij Q_j Q_i^dag
    T=np.zeros((2*N,2*N),complex)
    for i in range(N):
        for j in np.where(Am[i]>0)[0]: T[2*i:2*i+2,2*j:2*j+2]=Q[j]@Q[i].conj().T
    return T
Tcl={c:Tmat(Acl[c]) for _,c in cls_all}
T1=Tcl[phi/2]
print("\nT2  flatness test.  A_1^n = sum_c m_n(c) A_c  (walk counts m_n);  is  T_1^n = sum_c m_n(c) T_c  with the SAME m_n ?")
for n in (2,3,4):
    An=np.linalg.matrix_power(A1,n); Tn=np.linalg.matrix_power(T1,n)
    m={}; ok=True
    for l,c in cls_all:
        row=An[0,np.where(np.abs(G[0]-c)<1e-6)[0]]; m[c]=row[0]; ok&=np.allclose(row,row[0])
    recA=sum(m[c]*Acl[c] for _,c in cls_all); recT=sum(m[c]*Tcl[c] for _,c in cls_all)
    print(f"    n={n}: A-side reconstruction err {np.abs(An-recA).max():.1e} (counts constant on classes: {ok});  T-side err {np.abs(Tn-recT).max():.1e}")
print("    (T_0 = identity block, T_antipode = -perm (x) I.)  If these are ~1e-9 the transport is path-independent: multi-hop shell = composed 1-hop.")

# polynomial degree of each shell operator in the 1-hop operator
lam1=np.array([np.real(np.trace(Pm[n]@A1))/dd[n]**2 for n in names])
print("    minimal polynomial degree p_c with A_c = p_c(A_1), and does T_c = p_c(T_1) with the same p_c ?")
I240=np.eye(2*N)
for l,c in cls_all:
    lamc=np.array([np.real(np.trace(Pm[n]@Acl[c]))/dd[n]**2 for n in names])
    for deg in range(0,9):
        Vd=np.vander(lam1,deg+1,increasing=True); coef,res,_,_=np.linalg.lstsq(Vd,lamc,rcond=None)
        if np.abs(Vd@coef-lamc).max()<1e-8: break
    pT=sum(coef[k]*np.linalg.matrix_power(T1,k) for k in range(deg+1))
    print(f"      {l:12s} c={c:+.4f}:  degree {deg};  ||T_c - p_c(T_1)|| = {np.abs(Tcl[c]-pT).max():.1e}")

# ---- T3: continuum limit ----
print("\nT3  continuum limit.  Sym-chain irreps (d=1,2,3,4',5,6) are SU(2) spin (d-1)/2 restricted to 2I, so  lambda^c_d = |C| sin(d th)/(d sin th).")
chain={1:'1',2:'2',3:'3',4:"4'",5:'5',6:'6'}
mx=0.0
for l,c in cls_all[1:-1]:
    th=np.arccos(c); deg=int(Acl[c][0].sum()); h=int(np.argmin(np.abs(trQ/2-c)))
    for d,n in chain.items():
        lat=deg*chi[n][h]/dd[n]; su2=deg*np.sin(d*th)/(d*np.sin(th)); mx=max(mx,abs(lat-su2))
print(f"    max |lattice lambda - SU(2) closed form| over all shells and the 6 chain irreps = {mx:.1e}")
print("    => on the chain, the lattice formula IS the SU(2) shell formula sampled at theta_n.  Small-angle limit of its channels:")
print("       level(d->d+1)/(|C| th/3) -> d-1 ;  level(d->d-1)/(|C| th/3) -> -(d+1)   (eigenvalues of 2 sigma.J : the teleparallel (left-invariant-frame) Dirac operator on S^3)")
print("       exact SU(2) ratio level/(|C| th/3) at shrinking angles:")
print("         theta     d=2->3 (->1)   d=2->1 (->-3)   d=3->4 (->2)   d=3->2 (->-4)   d=5->6 (->4)   d=5->4 (->-6)")
for th in (np.radians(36),0.3,0.1,0.03,0.01):
    c=np.cos(th); s=np.sin(th)
    lam=lambda d: np.sin(d*th)/(d*np.sin(th))          # per unit |C|
    lev=lambda dr,ds: (c*lam(dr)-lam(ds))/s/(th/3)
    print(f"        {th:7.4f}  {lev(2,3):12.4f}  {lev(2,1):14.4f}  {lev(3,4):13.4f}  {lev(3,2):13.4f}  {lev(5,6):13.4f}  {lev(5,4):13.4f}")
print("    Riemannian Dirac on unit S^3 has eigenvalues +(d+1/2) [d->d+1] and -(d-1/2) [d->d-1], i.e. teleparallel + 3/2:  (d-1)+3/2 = d+1/2 ; -(d+1)+3/2 = -(d-1/2).")
print("    Zero of the teleparallel operator in the continuum: only d=1 -> 2 (the constant spinor).  The core channels 2'->4 and 3'->6 have NO SU(2) analogue (not Sym-chain).")
# lattice levels vs continuum prediction at the actual n=1 angle, for the chain channels
th=np.arccos(phi/2); Cn=12
print("    lattice (n=1 shell, th=36deg) vs continuum teleparallel prediction |C|th/3*(d-1), -(d+1):")
for (r,s_),(dr,ds) in {('2','3'):(2,3),('2','1'):(2,1),('3',"4'"):(3,4),("4'",'3'):(4,3),("4'",'5'):(4,5),('5',"4'"):(5,4)}.items():
    lamr=Cn*chi[r][int(np.argmin(np.abs(trQ/2-phi/2)))]/dd[r]; lams=Cn*chi[s_][int(np.argmin(np.abs(trQ/2-phi/2)))]/dd[s_]
    lat=(phi/2*lamr-lams)/np.sin(th); cont=Cn*th/3*((dr-1) if ds==dr+1 else -(dr+1))
    print(f"        {r:>2s}->{s_:<2s} (d {dr}->{ds}):  lattice {lat:9.4f}   continuum {cont:9.4f}   ratio {lat/cont:6.3f}")
