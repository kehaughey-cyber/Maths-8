"""
Zeros of F(k) = sum_j n_j sin(k.d_j)/(4a) on the locally-FCC (A3) lattice (a=1): the low-energy species of the route56 operator on the refined carrier.
k = (pi/sqrt2) kappa;  reciprocal lattice G (BCC) = {kappa_i +- kappa_j in 4Z}.  Newton/least-squares root search from a 0.25 grid in the cube [0,4)^3 (two BZ), roots reduced mod G;
for each distinct root: singular values of the velocity matrix M=dF/dk and chirality sign(det M).  A zero singular value means a nodal LINE, not a point.   No fit.
Usage: py -3 -I -u route56_fcc_nodes.py
"""
import numpy as np, itertools
n=[]
for i,j in itertools.combinations(range(3),2):
    for si in (1,-1):
        for sj in (1,-1):
            v=np.zeros(3); v[i]=si; v[j]=sj; n.append(v/np.sqrt(2))
n=np.array(n); S=np.pi/np.sqrt(2)
F=lambda c:(n*np.sin(n@(S*c))[:,None]).sum(0)/4
M=lambda c: S*sum(np.outer(nj,nj)*np.cos(nj@(S*c)) for nj in n)/4          # dF/dkappa
def reduce(c):                                           # canonical rep mod G: kappa -> kappa - g, g in G, within [-2,2)^3 box
    best=None
    for g in itertools.product((-4,-2,0,2,4),repeat=3):
        if all(((g[i]+g[j])%4==0 and (g[i]-g[j])%4==0) for i,j in ((0,1),(1,2),(0,2))):
            r=c-np.array(g); key=tuple(np.round(r,5))
            if best is None or (np.linalg.norm(r),key)<(np.linalg.norm(best),tuple(np.round(best,5))): best=r
    return best
roots=[]
for c0 in itertools.product(np.arange(0,4,.25),repeat=3):
    c=np.array(c0)
    for _ in range(60):
        f=F(c)
        if np.linalg.norm(f)<1e-13: break
        Mk=M(c); dc=np.linalg.lstsq(Mk,-f,rcond=1e-8)[0]; c=c+np.clip(dc,-.3,.3)
    if np.linalg.norm(F(c))<1e-10:
        r=reduce(c)
        if not any(np.linalg.norm(r-q)<1e-4 for q in roots): roots.append(r)
print(f"distinct zero-energy k-points modulo the reciprocal lattice (the roots can lie on nodal lines; each found root listed): {len(roots)}")
pts=[];lines=[]
for r in sorted(roots,key=lambda r:(np.linalg.norm(r),tuple(np.round(r,3)))):
    sv=np.linalg.svd(M(r),compute_uv=False); d=np.linalg.det(M(r))
    (pts if sv.min()>1e-6 else lines).append((r,sv,d))
print(f"  isolated Weyl points (full-rank M): {len(pts)};  points on nodal lines/surfaces (rank-deficient M): {len(lines)}")
for r,sv,d in pts: print(f"   kappa={np.round(r,4)}  singular values {np.round(sv,4)}  det M={d:+.4f}  chirality {np.sign(d):+.0f}")
print("  sum of chiralities of the isolated points:",int(sum(np.sign(d) for _,_,d in pts)))
for r,sv,d in lines[:6]: print(f"   (rank-deficient) kappa={np.round(r,3)}  singular values {np.round(sv,4)}")
