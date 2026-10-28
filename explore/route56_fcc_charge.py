"""
Charge balance of the FCC route56 operator's zero set.  F(k) = sum_j n_j sin(k.d_j)/4 (a=1, d_j = n_j the 12 nearest-neighbour vectors (+-1,+-1,0)/sqrt2 and permutations; cubic cell side sqrt2).
Poincare-Hopf on the 3-torus: the indices (chiralities sign det dF/dk) of the isolated zeros of a generic vector field sum to chi(T^3) = 0.  Nodal LINES of the symmetric F carry no point charge, so the
isolated Gamma (+1) and L points (-1 x 4) do not sum to 0 by themselves.  Test: add a small symmetry-breaking but periodic term  eps * sum_i u_i sin(k.e_i)  (e_i = sqrt2 x the three cubic axes, lattice vectors; u_i fixed generic directions) to open the lines into isolated zeros; find ALL zeros by vectorised Newton from a 0.125 grid plus 300k random starts and clusters around the X-type points, in kappa (k = (pi/sqrt2) kappa), reduce modulo the reciprocal lattice
G = {kappa_i +- kappa_j in 4Z}, count chiralities.  Expect total 0 and the missing +3 on points that came from the lines.   Usage: py -3 -I -u route56_fcc_charge.py
"""
import numpy as np, itertools
n=[]
for i,j in itertools.combinations(range(3),2):
    for si in (1,-1):
        for sj in (1,-1):
            v=np.zeros(3); v[i]=si; v[j]=sj; n.append(v/np.sqrt(2))
n=np.array(n); S=np.pi/np.sqrt(2); E3=np.sqrt(2)*np.eye(3); U3=np.array([[0.3,0.5,0.8],[-0.6,0.2,0.4],[0.1,-0.7,0.5]])
def FM(K,eps):                                    # K: (m,3) in k units
    ph=K@n.T                                       # (m,12)
    F=np.einsum('mj,ja->ma',np.sin(ph),n)/4
    M=np.einsum('mj,ja,jb->mab',np.cos(ph),n,n)/4          # dF_a/dk_b
    for e_,u_ in zip(E3,U3):
        pe=K@e_; F=F+eps*np.sin(pe)[:,None]*u_[None,:]; M=M+eps*np.cos(pe)[:,None,None]*u_[None,:,None]*e_[None,None,:]
    return F,M
inG=lambda c: all(abs(((c[i]+c[j]+2)%4)-2)<1e-4 and abs(((c[i]-c[j]+2)%4)-2)<1e-4 for i,j in ((0,1),(1,2),(0,2)))
g=np.arange(0,4,0.125); K0=np.array(list(itertools.product(g,repeat=3)))*S
rng=np.random.default_rng(0); K0=np.vstack([K0,rng.uniform(0,4,size=(300000,3))*S,
    np.vstack([np.array(x)+rng.normal(scale=0.4,size=(40000,3)) for x in ([2,0,0],[0,2,0],[0,0,2],[2,2,0],[2,0,2],[0,2,2],[2,2,2])])*S])
def run(eps):
    K=K0.copy(); ok=np.ones(len(K),bool)
    for _ in range(100):
        F,M=FM(K,eps); d=np.linalg.det(M); good=np.abs(d)>1e-12
        step=np.zeros_like(K); step[good]=-np.linalg.solve(M[good],F[good][...,None])[...,0]
        nrm=np.linalg.norm(step,axis=1); step[nrm>0.4]*=(0.4/nrm[nrm>0.4])[:,None]; K=K+step
    F,M=FM(K,eps); conv=(np.linalg.norm(F,axis=1)<1e-11)&(np.abs(np.linalg.det(M))>1e-9)
    roots=[]; ch=[]
    for k,m in zip(K[conv],M[conv]):
        c=k/S
        if not any(inG(tuple(c-r)) for r in roots): roots.append(c); ch.append(int(np.sign(np.linalg.det(m))))
    # F is odd in k for every eps here (sin terms), so -root is also a zero with the same chirality (M is even): add and verify the partners
    for c in list(roots):
        k=-c*S; F,M=FM(k[None,:],eps)
        for _ in range(30):
            F,M=FM(k[None,:],eps); k=k-np.linalg.solve(M[0],F[0])
        F,M=FM(k[None,:],eps)
        if np.linalg.norm(F[0])<1e-11 and abs(np.linalg.det(M[0]))>1e-9 and not any(inG(tuple(k/S-r)) for r in roots):
            roots.append(k/S); ch.append(int(np.sign(np.linalg.det(M[0]))))
    return roots,ch
for eps in (0.0,0.01,0.03,0.1):
    roots,ch=run(eps); print(f"eps={eps}: isolated nondegenerate zeros per Brillouin zone found: {len(roots)};  chirality + : {ch.count(1)},  - : {ch.count(-1)},  total {sum(ch)}")
    if eps in (0.03,):
        for r,c in zip(roots,ch): print(f"    kappa={np.round(r,3)}  chirality {c:+d}")
# self-paired (inversion-fixed) points: 2*kappa in G.  Evaluate F and det M there directly (these can carry an unpaired index).
print("\nself-paired points kappa (2 kappa in G, mod G) with F=0 at eps=0.03:")
seen=[]
for c in itertools.product(np.arange(0,4,0.5),repeat=3):
    c=np.array(c)
    if not inG(tuple(2*c)): continue
    if any(inG(tuple(c-r)) for r in seen): continue
    seen.append(c); F,M=FM((c*S)[None,:],0.03)
    print(f"   kappa={c}: |F|={np.linalg.norm(F[0]):.1e}  det M={np.linalg.det(M[0]):+.5f}")
