"""
Exact-lattice check of the Schur mechanism: for a polynomial h of degree d in the INTERNAL coordinates y = sigma(x) and any lattice point x,
S_h(x) = sum_{120 units u} Q(u) h(sigma(x)+sigma(u))  (the Weyl block applied to f(x) = h(sigma x) on the infinite lattice) is, for all monomials of degree d and random lattice points x,
(a) ~ 0 for d <= 6 and (b) non-zero at d = 7 (consistent with E ~ |k'|^7).  Control: the same with h a polynomial in the PHYSICAL coordinates (S is then the Weyl derivative, non-zero at d >= 1).
Reports the max over monomials and 8 random points of ||S||_2 relative to the scale sum_u |h(sigma x + sigma u)| (so cancellation is judged against the size of the terms).   Usage: py -3 -I -u route56_internal_poly.py
"""
import numpy as np, importlib.util, os, io, contextlib, itertools
here=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('h',os.path.join(here,'route56_hecke.py')); h=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(h)
sd=h.sd; U=h.U; Qu=np.array([sd.Qmat(p) for p in h.phys(U)]); pu=h.phys(U); su=h.perp(U)
rng=np.random.default_rng(2)
# random lattice points: integer combinations of units
pts=[]
for _ in range(8):
    idx=rng.integers(0,120,size=6); q=U[idx].reshape(6,8).sum(0).reshape(4,2); pts.append((h.phys(q[None])[0],h.perp(q[None])[0]))
def worst(d,which):
    mons=list(itertools.combinations_with_replacement(range(4),d)); w=0
    for xp,xs in pts:
        base=(xs if which=='int' else xp)[None,:]+(su if which=='int' else pu)           # (120,4) coordinates of x+u in the tested space
        for m in mons:
            val=np.prod(base[:,list(m)],axis=1)
            S=np.einsum('a,aij->ij',val,Qu); sc=np.abs(val).sum()+1e-300
            w=max(w,np.linalg.norm(S,2)/sc)
    return w
print("degree d : max ||sum_u Q(u) h(x+u)||/sum|h|  for h(sigma x) [internal]   and   h(x) [physical control]")
for d in range(0,9):
    print(f"  d={d}:   internal {worst(d,'int'):.3e}    physical {worst(d,'phys'):.3e}")
