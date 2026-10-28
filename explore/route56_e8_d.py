"""
Exact existence test for a genuine (homomorphic, mutually commuting) lift of 2I_L x 2I_R to Aut(e8), and the fixed subalgebra of every such lift.
Twisting a lift by a torus element is affine over GF(2) in the twist bits, so all constraints (2I_L relations (st)^2=s^3=t^5, same for R, and commutation of the 4 generator pairs) are one affine GF(2) system in 32 unknowns,
solved exactly; solutions are enumerated (or sampled if many) and the fixed subalgebra computed for each. Also: exact intersection dimensions of fixed spaces of separate lifts. Uses the setup of route56_e8_c.py.
Usage: py -3 -I -u route56_e8_d.py
"""
import numpy as np, importlib.util, os, io, contextlib, sys, itertools, time
here=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('h',os.path.join(here,'route56_hecke.py')); h=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(h)
U=h.U; PHI=h.PHI; PSI=h.PSI
src=open(os.path.join(here,'route56_e8_b.py'),encoding='utf-8').read()
# reuse lattice basis + LLL code (lines between markers) and Eu/epsE definitions
M120=U.reshape(120,8).astype(np.int64)
ns=dict(np=np,PHI=PHI,PSI=PSI,M=M120)
exec(src[src.index("def lattice_basis"):src.index("def phy(v)")].replace("M=U.reshape(120,8).astype(np.int64)",""),ns)
Bs=ns['lll'](ns['lattice_basis'](M120))
Gi=np.load(os.path.join(here,'route56_e8_gram.npy')); roots=np.load(os.path.join(here,'route56_e8_roots.npy')); C=np.load(os.path.join(here,'route56_e8_struct.npy')); KS=int(open(os.path.join(here,'route56_e8_kap.txt')).read())
NR=240; rid={tuple(r):i for i,r in enumerate(roots)}; neg=np.array([rid[tuple(-r)] for r in roots]); IP=roots@Gi@roots.T
Eu=np.triu(Gi,1)+np.diag(np.diag(Gi)//2)
epsE=lambda a,b:int(a@Eu@b)%2
pairs=[(i,j) for i in range(NR) for j in range(NR) if IP[i,j]==-1]
sumidx={p:rid[tuple(roots[p[0]]+roots[p[1]])] for p in pairs}
kb=np.array([ (KS*(-1)**epsE(roots[i],roots[neg[i]]))<0 for i in range(NR)],int)
def qm(p,q): return h.qmul(p,q)
Uarr=U.astype(np.int64)
def mat_of(side,g):                       # 8x8 integer matrix: row i = coords (in basis Bs) of g*b_i  or b_i*g
    rows=[]
    for b in Bs:
        bq=b.reshape(4,2)
        pr=qm(g.reshape(4,2),bq) if side=='L' else qm(bq,g.reshape(4,2))
        rows.append(pr.reshape(8))
    Rw=np.array(rows,dtype=float); coords=Rw@np.linalg.inv(Bs.astype(float)); Mi=np.rint(coords).astype(np.int64)
    assert np.abs(coords-Mi).max()<1e-9 and np.allclose(Mi@Bs,Rw); return Mi
def solve_gf2(rows_,rhs,nv):               # rows_: list of int bitmasks over nv vars, rhs bits ; returns particular solution (int bitmask) and nullspace basis (list of bitmasks)
    piv={}; 
    for r,b in zip(rows_,rhs):
        m=r|(b<<nv)
        for pbit,pm in piv.items():
            if (m>>pbit)&1: m^=pm
        low=m&((1<<nv)-1)
        if low==0:
            if (m>>nv)&1: return None
            continue
        pb=low.bit_length()-1
        for k in list(piv):
            if (piv[k]>>pb)&1: piv[k]^=m
        piv[pb]=m
    sol=0
    for pb,pm in piv.items():
        if (pm>>nv)&1: sol|=(1<<pb)
    free=[v for v in range(nv) if v not in piv]; null=[]
    for f in free:
        vec=1<<f
        for pb,pm in piv.items():
            if (pm>>f)&1: vec|=(1<<pb)
        null.append(vec)
    return sol,null
def lift(Mi):                                # returns (perm, eta0 array of +-1, list of twist arrays) for the lattice automorphism r->r@Mi
    perm=np.array([rid[tuple(r@Mi)] for r in roots])
    eqs=[];rhs=[]
    for (i,j) in pairs:
        k=sumidx[(i,j)]; eqs.append((1<<int(i))|(1<<int(j))|(1<<int(k))); rhs.append((epsE(roots[i],roots[j])+epsE(roots[perm[i]],roots[perm[j]]))%2)
    for i in range(NR): eqs.append((1<<int(i))|(1<<int(neg[i]))); rhs.append(int((kb[i]+kb[perm[i]])%2))
    out=solve_gf2(eqs,rhs,NR); assert out is not None
    sol,null=out; bits=lambda m:np.array([(m>>i)&1 for i in range(NR)])
    return perm,1-2*bits(sol),[1-2*bits(n) for n in null]
def Phi(Mi,perm,eta):                        # 248x248 matrix acting on column vectors in basis (e_0..e_239,H_1..H_8):  phi(e_i)=eta_i e_perm(i);  phi(H_i)=sum_j Mi[i,j]H_j
    P=np.zeros((248,248)); 
    for i in range(NR): P[perm[i],i]=eta[i]
    P[NR:,NR:]=Mi.T.astype(float); return P
def check_aut(P,trials=30):
    rng=np.random.default_rng(1); w=0
    for _ in range(trials):
        x,y=rng.integers(-2,3,size=248),rng.integers(-2,3,size=248)
        br=lambda a,b:np.einsum('a,b,abc->c',a,b,C); w=max(w,np.abs(P@br(x,y)-br(P@x,P@y)).max())
    return w
# --- find generators of 2I:  s of order 6 (w0=1/2), t of order 10 (w0=phi/2), st of order 4 (w0=0) with (st)^2=s^3=t^5 ---
w0=lambda g:(g[0,0]+g[0,1]*PHI)/2
def umul(a,b): return qm(a.reshape(4,2),b.reshape(4,2)).reshape(4,2)
ukey={tuple(u.reshape(8)):i for i,u in enumerate(Uarr)}
one=next(u for u in Uarr if tuple(u[0])==(2,0) and not u[1:].any())
def upow(g,n):
    r=one.copy()
    for _ in range(n): r=umul(r,g)
    return r
S6=[u for u in Uarr if abs(w0(u)-0.5)<1e-9]; T10=[u for u in Uarr if abs(w0(u)-PHI/2)<1e-9]
gens=None
for s in S6:
    for t in T10:
        st=umul(s,t)
        if abs(w0(st))<1e-9 and (upow(st,2)==upow(s,3)).all() and (upow(s,3)==upow(t,5)).all(): gens=(s,t); break
    if gens: break
assert gens, "no generator pair"
s,t=gens; print("generators of 2I found: orders 6,10; st order 4; (st)^2=s^3=t^5 =",upow(s,3).reshape(8))
def comp(f2,f1): return (f2[0][f1[0]], f1[1]*f2[1][f1[0]])        # f2 after f1
def eq(a,b): return (a[0]==b[0]).all() and (a[1]==b[1]).all()
def pw(f,n):
    r=(np.arange(NR),np.ones(NR,int))
    for _ in range(n): r=comp(f,r)
    return r
def twists(null):
    T=[]
    for c in itertools.product((0,1),repeat=len(null)):
        e=np.ones(NR,int)
        for ci,nv in zip(c,null):
            if ci: e=e*nv
        T.append(e)
    return T
def valid_lifts(side):
    gs=s if side=='L' else s; 
    Ms=mat_of(side,s); Mt=mat_of(side,t)
    ps,e0s,nls=lift(Ms); pt,e0t,nlt=lift(Mt); print(f"  side {side}: twist freedom dims {len(nls)},{len(nlt)}")
    TS=twists(nls); TT=twists(nlt); out=[]
    for a in TS:
        fs=(ps,e0s*a)
        s3=pw(fs,3)
        for b in TT:
            ft=(pt,e0t*b)
            if not eq(s3,pw(ft,5)): continue
            st=comp(fs,ft)             # s then t : product t*s? use (ts)
            ts=comp(ft,fs)
            if eq(pw(st,2),s3) or eq(pw(ts,2),s3): out.append((fs,ft))
    return Ms,Mt,out
def fixed_dim(mats):
    A=np.vstack([m-np.eye(248) for m in mats]); sv=np.linalg.svd(A,compute_uv=False)
    return int((sv<1e-9).sum()), A
Ms_L,Mt_L=mat_of('L',s),mat_of('L',t); Ms_R,Mt_R=mat_of('R',s),mat_of('R',t)
base={}
for nm,Mi in (("sL",Ms_L),("tL",Mt_L),("sR",Ms_R),("tR",Mt_R)):
    perm,e0,nl=lift(Mi); assert len(nl)==8; base[nm]=(perm,e0,nl)
def gen(nm,bits):
    perm,e0,nl=base[nm]; e=e0.copy()
    for k in range(8):
        if bits[k]: e=e*nl[k]
    return (perm,e)
def residual(x,variant):
    sL,tL,sR,tR=[gen(nm,x[8*i:8*i+8]) for i,nm in enumerate(("sL","tL","sR","tR"))]
    out=[]
    for a,b in ((sL,tL),(sR,tR)):
        st=comp(a,b) if variant==0 else comp(b,a)
        out+= [ (pw(a,3)[1]!=pw(b,5)[1]), (pw(st,2)[1]!=pw(a,3)[1]) ]
        assert (pw(a,3)[0]==pw(b,5)[0]).all() and (pw(st,2)[0]==pw(a,3)[0]).all()
    for a in (sL,tL):
        for b in (sR,tR):
            ab=comp(a,b); ba=comp(b,a); assert (ab[0]==ba[0]).all(); out.append(ab[1]!=ba[1])
    return np.concatenate([np.asarray(o,int) for o in out])
for variant in (0,1):
    x0=np.zeros(32,int); r0=residual(x0,variant); cols=[]
    for k in range(32):
        e=np.zeros(32,int); e[k]=1; cols.append((residual(e,variant)-r0)%2)
    # check affinity on random points
    rng=np.random.default_rng(3); ok=True
    for _ in range(20):
        x=rng.integers(0,2,32); pred=(r0+sum(cols[k] for k in range(32) if x[k]))%2
        ok&=bool((pred==residual(x,variant)).all())
    print(f"variant {variant}: residual is affine in the 32 twist bits: {ok}; base residual weight {r0.sum()}",flush=True)
    nv=32; eqs=[]; rhs=[]
    for i in range(len(r0)):
        m=0
        for k in range(32):
            if cols[k][i]: m|=(1<<k)
        eqs.append(m); rhs.append(int(r0[i]))
    out=solve_gf2(eqs,rhs,nv)
    if out is None: print(f"variant {variant}: NO solution: no exactly commuting homomorphic lift of 2I_L x 2I_R to Aut(e8) in this torus family"); continue
    sol,null=out; print(f"variant {variant}: solvable; solution space dimension {len(null)} (2^{len(null)} lifts)",flush=True)
    xs=np.array([(sol>>k)&1 for k in range(32)])
    dims={}; samples=[xs]
    rng=np.random.default_rng(5)
    for _ in range(min(300,2**len(null))):
        x=xs.copy()
        for nv_ in null:
            if rng.integers(2): x=x^np.array([(nv_>>k)&1 for k in range(32)])
        samples.append(x)
    for x in samples:
        assert residual(x,variant).sum()==0
        gens_=[gen(nm,x[8*i:8*i+8]) for i,nm in enumerate(("sL","tL","sR","tR"))]
        mats=[Phi(Mi,g[0],g[1]) for Mi,g in zip((Ms_L,Mt_L,Ms_R,Mt_R),gens_)]
        A=np.vstack([m-np.eye(248) for m in mats]); sv=np.linalg.svd(A,compute_uv=False); d=int((sv<1e-9).sum()+max(0,248-len(sv)))
        dims[d]=dims.get(d,0)+1
    print(f"variant {variant}: fixed-subalgebra dimension over {len(samples)} consistent lifts ->",dims)
