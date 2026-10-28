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
s5=5**.5
best=[]
for p in range(-12,13):
    for q in range(-12,13):
        for den in (1,2,5,10):
            # c=(p+q*phi)/den ; sigma(c)=(p+q*psi)/den ; also try c/sqrt5 variants
            for tag,cc,cs in (("plain",(p+q*PHI)/den,(p+q*PSI)/den),("/sqrt5",(p+q*PHI)/den/s5,-(p+q*PSI)/den/s5)):
                if cc<=0 or cs<=0: continue
                G=cc*G0+cs*G1
                Gi=np.rint(G)
                if np.abs(G-Gi).max()<1e-9 and np.all(np.diag(Gi)%2==0) and abs(round(np.linalg.det(Gi))-1)<1e-6: best.append((tag,p,q,den,cc,cs))
print("c with even unimodular Gram:",best[:10], len(best))
