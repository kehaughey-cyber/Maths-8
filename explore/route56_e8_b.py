"""
Step E8-a: the icosian ring I with the weighted trace form B(x,y)=Tr_{Q(sqrt5)/Q}(c <x,y>) is the E8 lattice for a suitable totally positive c; find c exactly and the 240 roots.
"""
import numpy as np, importlib.util, os, io, contextlib, sys, itertools
here=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('h',os.path.join(here,'route56_hecke.py')); h=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(h)
U=h.U; PHI=h.PHI; PSI=h.PSI
M=U.reshape(120,8).astype(np.int64)
def lattice_basis(M):                                   # integer row reduction to a basis of the Z-span
    M=[list(r) for r in M]; basis=[]
    for col in range(8):
        rows=[r for r in M if r[col]!=0]
        while len(rows)>1:
            rows.sort(key=lambda r:abs(r[col])); p=rows[0]
            for r in rows[1:]:
                q=r[col]//p[col]
                for t in range(8): r[t]-=q*p[t]
            rows=[r for r in rows if r[col]!=0]
        if rows: basis.append(rows[0]); M=[r for r in M if r is not rows[0] and any(r)]
    return np.array(basis,dtype=np.int64)
Bs=lattice_basis(M); assert Bs.shape==(8,8) and abs(round(np.linalg.det(Bs.astype(float))))>0
# every unit must be an integer combination of the basis
cf=np.rint(np.linalg.solve(Bs.T.astype(float),M.T.astype(float))).T; assert np.allclose(cf@Bs,M)
def _emb(Bm):
    v=Bm.reshape(-1,4,2); return np.hstack([((v[...,0]+v[...,1]*PHI)/2),((v[...,0]+v[...,1]*PSI)/2)])
def lll(Bm,delta=0.99):                                 # LLL on the rows (embedded in R^8 with the lattice metric), integer ops mirrored on Bm
    Bm=Bm.copy(); n=len(Bm)
    def gs():
        Ev=_emb(Bm); Q=np.zeros_like(Ev); mu=np.zeros((n,n))
        for i in range(n):
            Q[i]=Ev[i]
            for j in range(i): mu[i,j]=Ev[i]@Q[j]/(Q[j]@Q[j]); Q[i]-=mu[i,j]*Q[j]
        return Q,mu
    k=1
    while k<n:
        Q,mu=gs()
        for j in range(k-1,-1,-1):
            q=int(round(mu[k,j]))
            if q: Bm[k]-=q*Bm[j]; Q,mu=gs()
        if Q[k]@Q[k] >= (delta-mu[k,k-1]**2)*(Q[k-1]@Q[k-1]): k+=1
        else: Bm[[k,k-1]]=Bm[[k-1,k]]; k=max(k-1,1)
    return Bm
Bs=lll(Bs)
def phy(v): return (v.reshape(-1,4,2)[...,0]+v.reshape(-1,4,2)[...,1]*PHI)/2
def per(v): return (v.reshape(-1,4,2)[...,0]+v.reshape(-1,4,2)[...,1]*PSI)/2
Pm=phy(Bs); Sm=per(Bs)
G0=Pm@Pm.T; G1=Sm@Sm.T
print("basis det check, euclid Gram det:",np.linalg.det(G0+G1))
# ---- E8 lattice: weight c = 2 phi/sqrt5  (cP=2phi/sqrt5, cS=sigma(c)=-2 psi/sqrt5) ----
s5=5**.5; cP=2*PHI/s5; cS=-2*PSI/s5
G=cP*G0+cS*G1; Gi=np.rint(G).astype(np.int64); assert np.abs(G-Gi).max()<1e-9
assert np.all(np.diag(Gi)%2==0) and round(np.linalg.det(Gi))==1
print("Gram (E8, even unimodular) verified; det =",round(np.linalg.det(Gi)))
Lc=np.linalg.cholesky(Gi.astype(float)); R=Lc.T
roots=[]
def rec(level,partial,n,Qmax=2.0):
    if level<0:
        if abs(partial-Qmax)<1e-6: roots.append(n.copy())
        return
    s=sum(R[level,j]*n[j] for j in range(level+1,8)); rem=Qmax-partial+1e-9
    if rem<0: return
    r=np.sqrt(rem)/R[level,level]; c=-s/R[level,level]
    for v in range(int(np.ceil(c-r)),int(np.floor(c+r))+1):
        n[level]=v; t=R[level,level]*v+s; rec(level-1,partial+t*t,n)
    n[level]=0
rec(7,0.0,np.zeros(8,dtype=np.int64)); roots=np.array(roots); NR=len(roots)
print("number of norm-2 vectors:",NR); assert NR==240
rid={tuple(r):i for i,r in enumerate(roots)}; neg=np.array([rid[tuple(-r)] for r in roots])
IP=roots@Gi@roots.T
# cocycle exponent  eps(a,b)=(-1)^(sum_{i<j} a_i b_j G_ij + sum_i a_i b_i G_ii/2)
Eu=np.triu(Gi,1)+np.diag(np.diag(Gi)//2)
def epsE(a,b): return int(a@Eu@b)%2
# structure: pairs with (r,s)=-1
pairs=[(i,j) for i in range(NR) for j in range(NR) if IP[i,j]==-1]
sumidx={(i,j):rid[tuple(roots[i]+roots[j])] for i,j in pairs}
EPS={(i,j):epsE(roots[i],roots[j]) for i,j in pairs}
KAP={i:(1 if True else 0) for i in range(NR)}
def build_ad(kap_sign):
    # basis: e_0..e_239 then h_1..h_8 (h_i = lattice basis vector i, as H_i); [h(x),e_r]=(x,r)e_r ; [e_r,e_-r]= kap_sign*(-1)^{eps(r,-r)}... h(r)
    dim=NR+8; C=np.zeros((dim,dim,dim),dtype=np.int64)    # C[a,b,:] = [x_a,x_b]
    for i in range(NR):
        for k in range(8):
            v=(Gi[k]@roots[i]); C[NR+k,i,i]=v; C[i,NR+k,i]=-v
    for (i,j) in pairs: C[i,j,sumidx[(i,j)]]=(-1)**EPS[(i,j)]
    for i in range(NR):
        j=neg[i]; e=epsE(roots[i],roots[j]); sg=kap_sign*(-1)**e
        C[i,j,NR:]=sg*roots[i]       # h(r) in the lattice basis: coefficients of r = roots[i]
    return C
def jacobi_err(C,trials=400):
    rng=np.random.default_rng(0); dim=C.shape[0]; worst=0
    for _ in range(trials):
        x,y,z=[rng.integers(-3,4,size=dim) for _ in range(3)]
        br=lambda a,b: np.einsum('a,b,abc->c',a,b,C)
        t=br(x,br(y,z))+br(y,br(z,x))+br(z,br(x,y)); worst=max(worst,np.abs(t).max())
    return worst
CS=None
for sg in (1,-1):
    C=build_ad(sg); je=jacobi_err(C,60); print(f"[e_r,e_-r] = {sg:+d}*(-1)^eps(r,-r) h(r): max Jacobi defect {je}")
    if je==0: CS=C; KS=sg; break
assert CS is not None
np.save('route56_e8_struct.npy',CS)
np.save('route56_e8_roots.npy',roots); np.save('route56_e8_gram.npy',Gi); open('route56_e8_kap.txt','w').write(str(KS))
