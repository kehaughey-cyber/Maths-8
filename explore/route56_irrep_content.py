"""
Content of the lattice Weyl-block zero modes and of the physical sector under 2I_L x 2I_R (exact characters, no fitting).
Internal coordinates carry (2',2') (Galois-conjugate embedding of SU(2)_L x SU(2)_R restricted to 2I x 2I); harmonic polynomials of degree n in sigma(x) are Sym^n(2')_L x Sym^n(2')_R,
dimension (n+1)^2, so their 2I_L x 2I_R content is a_rho^n * a_tau^n with a^n = multiplicity of rho in Sym^n(2') (characters sin((n+1)b)/sin b, cos b = sigma(w0)).
Physical sector (2,2): Sym^n(2) likewise with cos a = w0.   Irreps of 2I: 1,2,2',3,3',4s,4g,5,6 (character orthonormality asserted).
Usage: py -3 -I -u route56_irrep_content.py
"""
import numpy as np, importlib.util, os, io, contextlib
here=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('h',os.path.join(here,'route56_hecke.py')); h=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(h)
phi=(1+5**.5)/2; psi=1-phi
w0p=np.array([(int(u[0,0])+int(u[0,1])*phi)/2 for u in h.U]); w0s=np.array([(int(u[0,0])+int(u[0,1])*psi)/2 for u in h.U])
def sym(d,w):
    a=np.arccos(np.clip(w,-1,1)); out=np.empty(len(w))
    for i,x in enumerate(a):
        if abs(x)<1e-9: out[i]=d
        elif abs(x-np.pi)<1e-9: out[i]=d*(-1)**(d-1)
        else: out[i]=np.sin(d*x)/np.sin(x)
    return out
CH={"1":sym(1,w0p),"2":sym(2,w0p),"3":sym(3,w0p),"4s":sym(4,w0p),"5":sym(5,w0p),"6":sym(6,w0p),"2'":sym(2,w0s),"3'":sym(3,w0s),"4g":sym(2,w0p)*sym(2,w0s)}
for a in CH:
    for b in CH: assert abs(np.sum(CH[a]*CH[b])/120-(1 if a==b else 0))<1e-6,(a,b)
print("2I irreps 1,2,2',3,3',4s,4g,5,6: orthonormal over 120 elements (asserted)\n")
def dec(chi): return {k:int(round(np.sum(chi*CH[k])/120)) for k in CH if abs(np.sum(chi*CH[k])/120)>0.02}
tot_dim=0
for name,w in (("INTERNAL  Sym^n(2')",w0s),("PHYSICAL  Sym^n(2) ",w0p)):
    print(name)
    for n in range(0,9):
        chi=sym(n+1,w); d=dec(chi); assert sum(int(k.rstrip("sg'")) *v for k,v in d.items())==n+1,(n,d)
        print(f"  n={n}: dim {n+1}  = {d}")
print("\nInternal harmonic degree n, left x right content a_rho a_tau, dimension (n+1)^2; zero modes = n=0..6 (x C^2 spinor), n=7 first obstruction.")
cum=0
for n in range(0,8):
    cum+=(n+1)**2; print(f"  n={n}: (n+1)^2={(n+1)**2}  cumulative harmonic dimension {cum}")
print("\nSpinor C^2 = the '2' of the physical Q-rep.  Left-right split of the 28-core (route56_core): left 2x1, 6x3, 4g x2 ; right 1x2, 2'x4, 3'x6.")
# product 2' x 2' , 2 x 2', etc.
def prod(a,b): return dec(CH[a]*CH[b])
for a,b in (("2'","2'"),("2","2'"),("3'","2"),("3'","2'"),("3'","3'"),("2","3'")): print(f"  {a} x {b} = {prod(a,b)}")
