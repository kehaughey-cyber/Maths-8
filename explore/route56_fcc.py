"""
Closed form for the band top of the route56 operator on an exactly locally-FCC (kissing-12, A3) lattice: the refined S^3 at n -> infinity is locally this lattice.
Edges d_j = a n_j, n_j = (+-1,+-1,0)/sqrt2 and permutations (12).  Sum n n^T = 4 I, so LS weights W_j = n_j/(4a) and operator B(k) = A(k)/kappa (kappa = 12a/3 = 4a):
H(k) = sigma . F(k),  F(k) = sum_j n_j sin(k.d_j) / (4a)   (the cos part cancels in the Hermitised operator).  E(k) = |F(k)|;  band top = max_k |F|.
Reported: E_max*a, the argmax k (units 1/a), and the check of v_g(0)=1.  Also the simple cubic (6 nbrs): E_max*a = 1.   No fit.
Usage: py -3 -I -u route56_fcc.py
"""
import numpy as np, itertools
n=[]
for i,j in itertools.combinations(range(3),2):
    for si in (1,-1):
        for sj in (1,-1):
            v=np.zeros(3); v[i]=si; v[j]=sj; n.append(v/np.sqrt(2))
n=np.array(n); assert len(n)==12 and np.allclose(n.T@n,4*np.eye(3))
def F(k): return (n*np.sin(n@k)[:,None]).sum(0)/4          # a = 1
print("small k: |F|/|k| at k=1e-4 x (1,2,3)/sqrt14:",np.linalg.norm(F(1e-4*np.array([1,2,3])/np.sqrt(14)))/1e-4)
rng=np.random.default_rng(0); best=0;bk=None
for _ in range(200000):
    k=rng.uniform(-np.pi*1.5,np.pi*1.5,3); e=np.linalg.norm(F(k))
    if e>best: best,bk=e,k
# refine by coordinate ascent
k=bk.copy(); step=0.1
for _ in range(4000):
    imp=False
    for d in np.vstack([np.eye(3),-np.eye(3)]):
        k2=k+step*d
        if np.linalg.norm(F(k2))>np.linalg.norm(F(k)): k=k2; imp=True
    if not imp: step/=2
    if step<1e-13: break
print(f"FCC (kissing-12): max_k |F| = E_max*a = {np.linalg.norm(F(k)):.12f} at k*a = {k.round(6)} (|k|a={np.linalg.norm(k):.6f})")
for nm,kk in (("(100)",np.array([1,0,0.])),("(110)",np.array([1,1,0.])/np.sqrt(2)),("(111)",np.array([1,1,1.])/np.sqrt(3))):
    ks=np.linspace(0,6,6001); e=np.array([np.linalg.norm(F(x*kk)) for x in ks]); i=np.argmax(e); print(f"   along {nm}: max |F| = {e[i]:.9f} at k a = {ks[i]:.4f}")
