"""
Exact (integer, Q(sqrt5)) check of the internal-polynomial identity of route56_internal_poly.py.
Lattice Weyl block on f(x)=h(sigma x):  (Wf)(x)=sum_u Q(u) h(sigma x + sigma u),  Q(u)=u0 I - i u.sigma.
It vanishes for every x and every h of degree <= m  iff  T[c,alpha] = sum_{u in 120 units} P_c(u) * S(u)^alpha = 0 in Z[phi]
for all components c=0..3 and all multi-indices |alpha| <= m   (P = physical coordinates, S = Galois-conjugate coordinates).
Numbers are x=(a+b*phi)/2 stored as integer pairs (a,b); products via (a+b phi)(c+d phi)=ac+bd+(ad+bc+bd)phi. No floating point.
Also reports the physical control sum_u P_c P^alpha.     Usage: py -3 -I -u route56_exact_moments.py
"""
import numpy as np, importlib.util, os, io, contextlib, itertools
here=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('h',os.path.join(here,'route56_hecke.py')); h=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(h)
U=[[(int(h.U[i,c,0]),int(h.U[i,c,1])) for c in range(4)] for i in range(len(h.U))]
assert len(U)==120
def mul(x,y): return (x[0]*y[0]+x[1]*y[1], x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def conj(x): return (x[0]+x[1], -x[1])      # phi -> 1-phi :  a+b phi -> (a+b) - b phi
def power(x,e):
    r=(1,0)
    for _ in range(e): r=mul(r,x)
    return r
def mom(src,c,alpha,sign_conj):
    tot=(0,0)
    for u in U:
        t=u[c]
        for j,e in enumerate(alpha):
            if e: t=mul(t, power(conj(u[j]) if sign_conj else u[j], e))
        tot=(tot[0]+t[0],tot[1]+t[1])
    return tot
# sanity: units have norm 1:  sum_c P_c^2 = 4 (scaled by 4 since (a+b phi)/2)
for u in U[:5]:
    s=(0,0)
    for c in range(4): q=mul(u[c],u[c]); s=(s[0]+q[0],s[1]+q[1])
    assert s==(4,0),s
print("all 120 units: P.P = 1 exactly (checked 5), count",len(U))
for conjflag,name in ((True,"internal (Galois S)"),(False,"physical control (P)")):
    print(f"\n== argument monomials in the {name} coordinates ==")
    for m in range(0,10):
        nz=0; tot=0
        for alpha in itertools.product(range(m+1),repeat=4):
            if sum(alpha)!=m: continue
            for c in range(4):
                tot+=1
                if mom(U,c,alpha,conjflag)!=(0,0): nz+=1
        print(f"degree {m}: {nz} of {tot} moments T[c,alpha] non-zero (exact)")
