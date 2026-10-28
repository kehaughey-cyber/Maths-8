"""
Mass-fork test on the 4D icosian lattice (floor: maps/mass_requirements.md; floor C2.1 'Galois reading m(lambda)=sqrt|lambda sigma(lambda)|, shell values 12,4,4,0'; spine: static Galois mass and dynamic propagation rate 'invert').
Static (Galois) reading, lattice form. N12 = the 12 units with w0=phi/2 (the carrier's nearest neighbours). sigma (phi->psi) is an automorphism of 2I carrying N12 to the 12 units N12' with w0=(phi-1)/2.
On the plane wave f=exp(i(k.x+k'.sigma x)) the operator A=sum_{u in N12} T_u has eigenvalue lam(k,k')=sum_{N12} exp(i(k.u+k'.sigma u)); its Galois conjugate sigma(A)=sum_{N12'} T_u has eigenvalue lam(k',k) (reindex u=sigma v).
So  m(k,k') = sqrt|lam(k,k') lam(k',k)|  is the lattice form of the Galois mass; m(0,0)=12 as in the floor's uniform mode.
Dynamic reading: the Weyl-block energy E^(k,k') = 2|sum_pairs P sin(k.P+k'.S)|/30 of route56_lattice4d.py and its velocity matrix v(k') of route56_velmap.py.
Tests: (1) k=0, k' along rays: m, mean eigenvalue of v, and E^(small k)/|k|; (2) correlation of m with v over random k'; (3) correlation of m with E^ over random (k,k').  No fitting.
Usage: py -3 -I -u route56_massfork.py
"""
import numpy as np, importlib.util, os, io, contextlib
here=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('h',os.path.join(here,'route56_hecke.py')); h=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(h)
U=h.U; phi=(1+5**.5)/2; psi=1-phi
Pall=np.array([[(int(u[c,0])+int(u[c,1])*phi)/2 for c in range(4)] for u in U]); Sall=np.array([[(int(u[c,0])+int(u[c,1])*psi)/2 for c in range(4)] for u in U])
w0=Pall[:,0]
N12=np.where(np.abs(w0-phi/2)<1e-9)[0]; N12p=np.where(np.abs(w0-(phi-1)/2)<1e-9)[0]
print("N12:",len(N12),"  N12':",len(N12p)," ; sigma(N12) subset N12' :", set(map(tuple,np.round(Sall[N12],6)))<=set(map(tuple,np.round(Pall[N12p],6))))
first=[i for i in range(120) if next(x for x in Pall[i] if abs(x)>1e-9)>0]
P=Pall[first]; S=Sall[first]; PP=np.einsum('ia,ib->iab',P,P)
lam=lambda k,kp: np.exp(1j*(Pall[N12]@k+Sall[N12]@kp)).sum()
mstat=lambda k,kp: np.sqrt(abs(lam(k,kp)*lam(kp,k)))
vmat=lambda kp: np.einsum('i,iab->ab',np.cos(S@kp),PP)/15
Edyn=lambda k,kp: 2*np.linalg.norm((P*np.sin(P@k+S@kp)[:,None]).sum(0))/30
print("m(0,0) =",mstat(np.zeros(4),np.zeros(4)),"(floor uniform-mode Galois mass 12)")
rng=np.random.default_rng(2)
print("\n(1) k=0 rays: |k'|, m_static, mean eig v(k'), E^(k=0.05 d)/0.05 at that k'  [3 rays]")
for t in range(3):
    d=rng.normal(size=4); d/=np.linalg.norm(d); e=rng.normal(size=4); e/=np.linalg.norm(e)
    for r in (0,0.5,1,1.5,2,3,3.5,4,5,6):
        kp=r*d; print(f"  ray{t} r={r:4}: m={mstat(np.zeros(4),kp):9.5f}  v={np.linalg.eigvalsh(vmat(kp)).mean():9.5f}  E/|k|={Edyn(0.05*e,kp)/0.05:9.5f}")
# (2) correlations over random k'
ks=[rng.normal(size=4)*rng.uniform(0,4) for _ in range(4000)]
m=np.array([mstat(np.zeros(4),k) for k in ks]); v=np.array([np.linalg.eigvalsh(vmat(k)).mean() for k in ks]); rr=np.array([np.linalg.norm(k) for k in ks])
print("\n(2) random k' (4000): corr(m, v) =",np.corrcoef(m,v)[0,1]," corr(m,|k'|)=",np.corrcoef(m,rr)[0,1]," corr(v,|k'|)=",np.corrcoef(v,rr)[0,1])
for lo,hi in ((0,1),(1,2),(2,3),(3,4),(4,6),(6,9)):
    s=(rr>=lo)&(rr<hi)
    if s.sum()>5: print(f"   |k'| in [{lo},{hi}): n={s.sum():4d}  mean m={m[s].mean():8.4f}  mean v={v[s].mean():8.4f}  corr(m,v)={np.corrcoef(m[s],v[s])[0,1] if s.sum()>3 else float('nan'):7.3f}")
# (3) random full (k,k')
K=[(rng.normal(size=4)*0.5,rng.normal(size=4)*rng.uniform(0,4)) for _ in range(4000)]
m3=np.array([mstat(a,b) for a,b in K]); E3=np.array([Edyn(a,b) for a,b in K]); k3=np.array([np.linalg.norm(a) for a,b in K])
print("\n(3) random (k,k') (4000): corr(m,E^) =",np.corrcoef(m3,E3)[0,1],"; corr(m, E^/|k|) =",np.corrcoef(m3,E3/np.maximum(k3,1e-9))[0,1])
# (4) is m a function of E^ or v ? binned means of v against m at k=0
o=np.argsort(m); qs=np.array_split(o,8)
print("\n(4) k'-samples sorted by static m, octiles: mean m, mean v, mean |k'|")
for q in qs: print(f"   m {m[q].mean():8.4f}   v {v[q].mean():8.4f}   |k'| {rr[q].mean():6.3f}")
