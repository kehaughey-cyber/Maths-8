"""
Fixed subalgebras of e8 under the lifts of SINGLE lattice automorphisms (cyclic subgroups), the right question after the full-group test of route56_e8_c/d/e was shown to be the wrong one (a group of order 14400 acting freely on the lattice leaves nothing).
Elements: left mult L_g, conjugation x->g x g^-1 = L_g R_{g^-1}, and products L_a R_b of the floor tick type. For each: lattice order N, char poly factors via eigenvalue angles, then over all 2^8 torus twists the lifts with phi^N = id and their fixed-subalgebra dimensions.
Usage: py -3 -I -u route56_e8_f.py
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
from collections import Counter
def inv(g): c=g.copy().reshape(4,2); c[1:]=-c[1:]; return c.reshape(4,2)
def Mof(factors):                                  # factors: list of (side,g) applied in the order given
    M=np.eye(8,dtype=np.int64)
    for side,g in factors: M=M@mat_of(side,g)
    return M
def order_of(M):
    P=np.eye(8,dtype=np.int64)
    for n in range(1,200):
        P=P@M
        if (P==np.eye(8)).all(): return n
def analyse(name,M):
    N=order_of(M); ev=np.linalg.eigvals(M.astype(float)); ang=sorted(set(np.round(np.degrees(np.angle(ev))%360,3)))
    perm,e0,nl=lift(M); dims=Counter(); tot=0
    for c in itertools.product((0,1),repeat=8):
        e=e0.copy()
        for ci,nv in zip(c,nl):
            if ci: e=e*nv
        f=(perm,e); pN=pw(f,N)
        if not ((pN[0]==np.arange(NR)).all() and (pN[1]==1).all()): continue
        tot+=1; A=Phi(M,perm,e)-np.eye(248); sv=np.linalg.svd(A,compute_uv=False); dims[int((sv<1e-9).sum())]+=1
    print(f"{name}: lattice order {N}; eigenangles(deg) {ang}; twists with phi^N=id: {tot}/256; fixed-subalgebra dim -> count {dict(sorted(dims.items()))}",flush=True)
sg=lambda w:[u for u in Uarr if abs(w0(u)-w)<1e-9][0]
o3=sg(-0.5)                                         # order 3: w0=cos(2pi/3)?  (w0=-1/2 has order 3)
o6=sg(0.5); o5=[u for u in Uarr if abs(w0(u)-(-PHI/2+0.5)*0-(PHI-1)/2)<1e-9]  # w0=(phi-1)/2=0.309 -> order 5
o5=o5[0]; o10=sg(PHI/2); o4=[u for u in Uarr if abs(w0(u))<1e-9][0]
def ordg(g):
    r=one.copy()
    for n in range(1,130):
        r=umul(r,g)
        if (r==one).all(): return n
print("element orders:",{k:ordg(v) for k,v in dict(o3=o3,o5=o5,o6=o6,o10=o10,o4=o4).items()})
for nm,g in (("o3",o3),("o5",o5),("o10",o10),("o4",o4)):
    analyse(f"L_{nm}",Mof([('L',g)]))
    analyse(f"conj_{nm} (x->g x g^-1)",Mof([('L',g),('R',inv(g))]))
for na,a in (("o5",o5),("o10",o10),("o4",o4),("o3",o3)):
    for nb,b in (("o6",o6),("o3",o3),("o4",o4),("o10",o10)):
        analyse(f"L_{na} R_{nb}",Mof([('L',a),('R',b)]))
