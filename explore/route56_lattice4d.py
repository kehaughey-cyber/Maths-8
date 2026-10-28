"""
Two things, both exact.
 (A) What the Hecke T_p graph is.  For a unit u, the set {g u : g an icosian of norm 𝔭} is the whole shell X_𝔭 (right multiplication by a unit permutes the shell), so the 'T_𝔭 neighbours of u'
     are ALL 720 edge-midpoint icosians for 𝔭 = sqrt5: the V-E Hecke graph is the complete bipartite K_{120,720}, not local on S^3 (it is the expander side of the picture).
 (B) The concurrent operator.  The additive Cayley graph of the icosian lattice I with the 120 units as generators, x ~ x+u, contains every shell at once (E = V+V, F = V+V+V, C = ...), is
     120-regular, invariant under 2I_L x 2I_R, Galois covariant (sigma permutes the units), translation invariant (the lattice has rank 8: physical R^4 x internal R^4), and local in R^4 (step length 1).
     Chiral Weyl block  (W f)(x) = sum_u Q(u) f(x+u),  Q(u) = u0 - i sigma.(u1,u2,u3);  Q(-u) = -Q(u).  Plane wave e^{i(k.x + k'.sigma(x))}:  W = 2i sum_{pairs +-u} Q(u) sin(k.u + k'.sigma u),
     a scaled quaternion, so the two singular values coincide and  E(k,k') = 2 | sum_pairs u sin(k.u + k'.sigma u) |_{R^4}  exactly.  Normalised E^ = E/30 (sum over 120 units of u u^T = 30 I; 11-design).
     Reported: velocity at small k (k'=0); E^ at k=0 for small k' (the internal-space sector); the zero set of V(kappa) = sum_pairs u sin(.) in the 8-torus by Gauss-Newton (4 equations, 8 unknowns);
     band top; fraction of the 8-torus with E^ < eps.   No fit.   Usage: py -3 -I -u route56_lattice4d.py
"""
import numpy as np, importlib.util, os, io, contextlib
here=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('h',os.path.join(here,'route56_hecke.py')); h=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(h)
U=h.U; PHI=h.PHI; PSI=h.PSI
print("(A) Hecke T_p neighbours of a unit, norm sqrt5:")
E=h.SH["E"]; key={e.tobytes() for e in E}
prod={h.qmul(g[None],U[0][None])[0].tobytes() for g in E}
print(f"    {{g*u : g in X_sqrt5}} has {len(prod)} elements, all in X_sqrt5: {prod<=key}  -> every unit is joined to every one of the {len(E)} midpoints: K_(120,{len(E)})")
phy=h.phys(U); per=h.perp(U)                       # (120,4) physical and internal coordinates of the units
first=[i for i in range(120) if next(x for x in phy[i] if abs(x)>1e-9)>0]; assert len(first)==60
P=phy[first]; S=per[first]                         # 60 representatives of +-u
def Vvec(k,kp): return (P*np.sin(P@k+S@kp)[:,None]).sum(0)
def Eh(k,kp): return 2*np.linalg.norm(Vvec(k,kp))/30
print("\n(B) E^(k,k') = 2|sum_pairs u sin(k.u + k'.sigma u)|/30")
rng=np.random.default_rng(0)
print("   k' = 0, small k: E^/|k| at |k| = 1e-3 along 6 random directions (should be 1):",", ".join(f"{Eh(1e-3*d/np.linalg.norm(d),np.zeros(4))/1e-3:.6f}" for d in rng.normal(size=(6,4))))
print("   k = 0, small k': E^ and E^/|k'|^p for p = 1,3,5 (random directions, mean of 12):")
for r in (0.05,0.1,0.2,0.4,0.8):
    vals=[Eh(np.zeros(4),r*d/np.linalg.norm(d)) for d in rng.normal(size=(12,4))]
    print(f"      |k'|={r}: mean E^ = {np.mean(vals):.3e}  (max {np.max(vals):.3e}), E^/r = {np.mean(vals)/r:.3e}, E^/r^3 = {np.mean(vals)/r**3:.3e}, E^/r^5 = {np.mean(vals)/r**5:.3e}")
# zero set by Gauss-Newton
def J(kappa):
    k,kp=kappa[:4],kappa[4:]; c=np.cos(P@k+S@kp); return np.hstack([(P.T*c)@P,(P.T*c)@S])
found=[]; 
for t in range(4000):
    x=rng.uniform(-np.pi,np.pi,size=8)*1.0
    for _ in range(60):
        f=Vvec(x[:4],x[4:])
        if np.linalg.norm(f)<1e-12: break
        x=x-np.linalg.pinv(J(x),rcond=1e-9)@f
    if np.linalg.norm(Vvec(x[:4],x[4:]))<1e-10: found.append(x.copy())
found=np.array(found); print(f"\n   zero set of V(kappa) (Gauss-Newton from 4000 random starts): {len(found)} converged")
if len(found):
    rk=[np.linalg.matrix_rank(J(x),tol=1e-6) for x in found]; print("   Jacobian rank at the zeros:",dict(zip(*np.unique(rk,return_counts=True))))
    nk=np.linalg.norm(found[:,:4],axis=1); nkp=np.linalg.norm(found[:,4:],axis=1)
    print(f"   |k| over zeros: min {nk.min():.3f} median {np.median(nk):.3f}; |k'|: min {nkp.min():.3f} median {np.median(nkp):.3f}")
# band top and measure of low energies
def top():
    best=0
    for _ in range(300):
        x=rng.uniform(-np.pi,np.pi,size=8); v=Eh(x[:4],x[4:]); step=.3
        while step>1e-4:
            imp=False
            for d in np.vstack([np.eye(8),-np.eye(8)]):
                y=x+step*d; w=Eh(y[:4],y[4:])
                if w>v: x,v,imp=y,w,True
            if not imp: step/=2
        best=max(best,v)
    return best
print(f"\n   band top: max E^ = {top():.6f} (units where small-k velocity is 1 and the step length is 1);  k'=0 physical sector alone: ",end="")
b=0
for _ in range(300):
    k=rng.uniform(-np.pi,np.pi,size=4); b=max(b,Eh(k,np.zeros(4)))
print(f"max over 300 random k = {b:.4f}")
th=rng.uniform(0,2*np.pi,size=(400000,8))
# phase of unit u = sum_j theta_j e_j(u), e_j the 8 integer doubled coordinates; torus of ZZ^8 covers the Brillouin zone of I
Eint=U[first].reshape(60,8).astype(float)
ph=th@Eint.T                                       # (m,60)
Ek=2*np.linalg.norm(np.einsum('mj,ja->ma',np.sin(ph),P),axis=1)/30
print("   uniform 8-torus (4e5 samples): fraction with E^ < eps: "+", ".join(f"eps={e}: {np.mean(Ek<e):.2e}" for e in (0.02,0.05,0.1,0.2,0.5))+f";  mean {Ek.mean():.3f}, max {Ek.max():.3f}")
