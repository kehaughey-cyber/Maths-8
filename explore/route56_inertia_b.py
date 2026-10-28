"""
Follow-up to route56_inertia.py (reuses its definitions by exec of the header).
D) Co-definition: the zero set of V(k,k') (E=0) on the 8-torus. For random physical k, does an internal k' exist with E(k,k')=0?  Rank of the 4x8 Jacobian there.
   If yes, E = |V| is the mismatch from the nodal manifold {V=0} (4-dimensional): the cost of a physical momentum is the failure of the internal label to co-define with it.
E) Locked label: near the node at fixed k', the inertia M^-1 = H_kk.  Conical E=|v(k')(k-k*)| gives E*eig(H_kk) = (v^2 on the 3 directions transverse to the motion, 0 along it), i.e. M_T = E/v^2.
   Test that on the real lattice at several |k'| including near v->0 (|k'| ~ 3.9), and compare v^2 with the static (m/12)^2.
Usage: py -3 -I -u route56_inertia_b.py
"""
import numpy as np, os, sys
here=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(here,'route56_inertia.py')).read().split("rng=np.random.default_rng(8)")[0]
exec(compile(src,'route56_inertia_header','exec'))
rng=np.random.default_rng(11)

print("=== D) nodal manifold: for random physical k, solve V(k,k')=0 for k' (Newton on 4 equations, 40 random starts k' in [-6,6]^4) ===")
def solve_kp(k):
    for s in range(40):
        kp=rng.uniform(-6,6,4)
        for _ in range(120):
            q=np.concatenate([k,kp]); v=V(q)
            if np.linalg.norm(v)<1e-13: return kp,True
            Jp=Jac(q)[:,4:]; kp=kp+np.linalg.lstsq(Jp,-v,rcond=1e-12)[0]
            if np.linalg.norm(kp)>1e3: break
    return None,False
for kn in (0.1,0.5,1,2,3,5):
    ok=0; rk=[]; N=40
    for t in range(N):
        d=rng.normal(size=4); d/=np.linalg.norm(d); k=kn*d
        kp,f=solve_kp(k)
        if f:
            ok+=1; q=np.concatenate([k,kp]); sv=np.linalg.svd(Jac(q),compute_uv=False); rk.append(sv.min())
    print(f"  |k|={kn}: node exists in k' for {ok}/{N} random directions;  smallest singular value of the 4x8 Jacobian at those nodes: min {min(rk) if rk else float('nan'):.3e}, median {np.median(rk) if rk else float('nan'):.3e}")

print("\n=== E) locked label: inertia near the node at fixed k' ===")
print("  |k'|   delta   E            eig(E*H_kk) (4)                       conical prediction eig J^T(1-VhVh^T)J (4)               meas/pred (largest)   (m/12)/mean(v(k'))   max|eig(Jnode)-eig(v(k'))|")
def node(kp):
    k=np.zeros(4)
    for _ in range(100):
        q=np.concatenate([k,kp]); v=V(q)
        if np.linalg.norm(v)<1e-15: break
        k=k+np.linalg.lstsq(Jac(q)[:,:4],-v,rcond=1e-14)[0]
    return k
for r in (0.5,1,2,3,3.5,3.8,4,5):
    d=rng.normal(size=4); d/=np.linalg.norm(d); kp=r*d; ks=node(kp)
    vv0=np.linalg.eigvalsh(vmat(kp)); vv=np.linalg.eigvalsh(c0*Jac(np.concatenate([ks,kp]))[:,:4])   # velocity matrix AT the node (k*,k'); equals v(k') at k=0 to O(|k*|)
    for dl in (1e-4,0.02,0.1):
        e=rng.normal(size=4); e/=np.linalg.norm(e); q=np.concatenate([ks+dl*e,kp])
        E,g,H=Eh(q); w=np.linalg.eigvalsh(E*H[:4,:4]); wt=np.sort(w)[::-1]
        Jn=c0*Jac(q)[:,:4]; vh=V(q)/np.linalg.norm(V(q)); vt=np.sort(np.linalg.eigvalsh(Jn.T@(np.eye(4)-np.outer(vh,vh))@Jn))[::-1]   # conical prediction: eig of J^T (1-Vhat Vhat^T) J at q
        ratio=wt[0]/vt[0]; MT=0
        print(f"  {r:4}  {dl:5}  {E:11.4e}  {np.round(wt,5)}  {np.round(vt,5)}   {ratio:8.4f}     {mstat(np.concatenate([np.zeros(4),kp]))/12/np.mean(vv0):8.4f}   {np.abs(vv-vv0).max():.3e}")

print("\n  rest of the picture at the v->0 surface: scan |k'| along 4 random rays, det v and smallest |eig v|, and the locked-label inertia 1/(E H_kk transverse) for a fixed small energy")
for t in range(4):
    d=rng.normal(size=4); d/=np.linalg.norm(d)
    row=[]
    for r in (3.0,3.5,3.8,3.9,4.0,4.2):
        vv=np.linalg.eigvalsh(vmat(r*d)); row.append(f"r={r}: min|v|={np.abs(vv).min():.4f}")
    print("   ray",t,"; ".join(row))
