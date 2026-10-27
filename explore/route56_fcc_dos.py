"""
Does the FCC (A3) zero set of F explain the low-mode excess on the refined S^3?  Expected number of eigenvalues with |lambda| < 1 (continuum units) on a lattice of N sites,
edge angle a, if the local band structure is the flat FCC one:  2 N P_k(|F(k)| < a),  P_k = fraction of the Brillouin zone with |F| < a (Monte Carlo over one period, 4e6 points),
split by distance of k from Gamma (smooth species) and the rest.  Compare with the measured counts #|lambda|<1: 382 (A), 364 (B) at n=2 (N=840, a=.32288) and 704 (A), 734 (B) at n=3 (N=2760, a=.21664)
(LIVE_WEB_RESULTS §14).  No fit.   Usage: py -3 -I -u route56_fcc_dos.py
"""
import numpy as np, itertools
n=[]
for i,j in itertools.combinations(range(3),2):
    for si in (1,-1):
        for sj in (1,-1):
            v=np.zeros(3); v[i]=si; v[j]=sj; n.append(v/np.sqrt(2))
n=np.array(n); S=np.pi/np.sqrt(2)
rng=np.random.default_rng(1); K=rng.uniform(0,4,size=(4_000_000,3))*S          # cube [0,4)^3 in kappa = 2 unit cells (reciprocal volume 32 vs 64)
f=np.zeros_like(K)
for nj in n: f+=nj[None,:]*np.sin(K@nj)[:,None]/4
E=np.linalg.norm(f,axis=1)
# distance to Gamma modulo G: G = BCC (kappa_i+-kappa_j in 4Z); Gamma images at kappa in G
def near_gamma(K,rad):
    c=K/S; best=np.full(len(c),9.0)
    for g in itertools.product((0,4),repeat=3):
        for h in ((0,0,0),(2,2,2)):
            for sg in itertools.product((1,-1),repeat=3):
                pass
    # simpler: Gamma images are kappa in {4Z^3} U {(2,2,2)+4Z^3}; distance in kappa units
    d1=np.abs(c-4*np.round(c/4)); d2=np.abs((c-2)-4*np.round((c-2)/4))
    return np.minimum(np.linalg.norm(d1,axis=1),np.linalg.norm(d2,axis=1))<rad
dg=near_gamma(K,0.8)
for tag,N,a in (("n=2",840,0.32288),("n=3",2760,0.21664),("n=5",12600,0.13043)):
    p=np.mean(E<a); pg=np.mean((E<a)&dg)
    print(f"{tag}: N={N}, a={a}: P(|F|<a) = {p:.5f};  predicted #|lambda|<1 = {2*N*p:.0f}  (of which near Gamma, kappa-radius<0.8: {2*N*pg:.0f}; smooth continuum has 2)")
