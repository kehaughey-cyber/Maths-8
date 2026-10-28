"""
Fixed subalgebra of e8 under pairs of separately-homomorphic lifts of 2I_L and 2I_R (the lifts of L and R do not commute exactly, see route56_e8_d.out; the group they generate is a torus extension, and its fixed algebra is F_L cap F_R).
For all 4096 x 4096 pairs: dimension of F_L cap F_R from the singular values of the overlap matrix (count of singular values equal to 1).   Usage: py -3 -I -u route56_e8_e.py
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
def fixed_basis(Ms,Mt,V):
    out=[]
    for (fs,ft) in V:
        Am=np.vstack([Phi(Ms,fs[0],fs[1])-np.eye(248),Phi(Mt,ft[0],ft[1])-np.eye(248)]); u,sv,vt=np.linalg.svd(Am); k=int((sv<1e-9).sum()); out.append(vt[-k:])
    return out
FL=[];FR=[]
for side,F in (('L',FL),('R',FR)):
    Ms,Mt,V=valid_lifts(side); F.extend(fixed_basis(Ms,Mt,V)); print(side,"fixed dims",Counter(len(f) for f in F),flush=True)
A=np.array(FL); B=np.array(FR)
cnt=Counter(); ngrid=0
for i0 in range(0,len(A),256):
    Gm=np.einsum('iak,jbk->ijab',A[i0:i0+256],B)
    # singular values of 2x2: eigenvalues of Gm Gm^T
    tr=(Gm**2).sum((2,3)); det=(Gm[...,0,0]*Gm[...,1,1]-Gm[...,0,1]*Gm[...,1,0])**2
    disc=np.sqrt(np.maximum(tr**2-4*det,0)); l1=(tr+disc)/2; l2=(tr-disc)/2
    d=(l1>1-1e-8).astype(int)+(l2>1-1e-8).astype(int)
    cnt.update(d.ravel().tolist())
print("intersection dimension of F_L and F_R over all 4096x4096 lift pairs:",dict(cnt))
# max overlap (largest singular value) distribution when intersection is 0
