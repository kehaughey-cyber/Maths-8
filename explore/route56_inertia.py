"""
Inertia test on the 4D icosian lattice Weyl block (follows route56_massfork.py, route56_velmap.py; floor: maps/mass_requirements.md, the fork 'static m / dynamic rate / third face live co-definition').
Band energy E(q) = (2/30)|V(q)|, q=(k,k') in R^8, V(q)=sum_{60 pairs} P sin(q.X), X=(P,S) (P physical, S Galois-conjugate coordinates of a unit).
Operational definitions (no assumed form):
  - velocity (first order):   grad_k E ;  generalised velocity matrix J_k(q)=sum P P^T cos(q.X)  (J_k(0,k')=15 v(k')).
  - inertia (second order):   a packet at fixed internal label k' (a physical force moves k only, since a potential smooth in x is the Fourier shift (q,0)) accelerates as dv/dt = H_kk F, H=Hessian of E: M^-1 = H_kk.
  - rest state:               grad_k E = 0 with E>0 (physical group velocity zero, positive rest energy);  fully standing: grad_q E = 0 (all 8).
  - co-definition:            force on k with k' allowed to respond: Schur complements of the 8x8 Hessian.
Parts: A) is there a gap at fixed k'? (zeros of V(k) at fixed k', Newton) ; B) physical rest states at fixed k' ; C) fully stationary points of E on R^8 (discrete spectrum E_s, signatures, H_kk, H_k'k', Schur), compared with the static Galois mass m(q)=sqrt|lam(k,k')lam(k',k)| of route56_massfork.py and with v.
Usage: py -3 -I -u route56_inertia.py
"""
import numpy as np, importlib.util, os, io, contextlib
here=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('h',os.path.join(here,'route56_hecke.py')); h=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(h)
U=h.U; phi=(1+5**.5)/2; psi=1-phi
Pall=np.array([[(int(u[c,0])+int(u[c,1])*phi)/2 for c in range(4)] for u in U]); Sall=np.array([[(int(u[c,0])+int(u[c,1])*psi)/2 for c in range(4)] for u in U])
first=[i for i in range(120) if next(x for x in Pall[i] if abs(x)>1e-9)>0]
P=Pall[first]; S=Sall[first]; X=np.hstack([P,S]); c0=2/30
N12=np.where(np.abs(Pall[:,0]-phi/2)<1e-9)[0]
lam=lambda k,kp: np.exp(1j*(Pall[N12]@k+Sall[N12]@kp)).sum()
mstat=lambda q: np.sqrt(abs(lam(q[:4],q[4:])*lam(q[4:],q[:4])))
def V(q): return P.T@np.sin(X@q)
def Jac(q): return (P*np.cos(X@q)[:,None]).T@X                      # 4x8
def Eg(q):
    v=V(q); n=np.linalg.norm(v); J=Jac(q); return c0*n, c0*J.T@v/n
def Eh(q):
    th=X@q; v=P.T@np.sin(th); n=np.linalg.norm(v); J=(P*np.cos(th)[:,None]).T@X; g=J.T@v
    t3=-(X*((P@(v/n))*np.sin(th))[:,None]).T@X
    return c0*n, c0*g/n, c0*(J.T@J/n-np.outer(g,g)/n**3+t3)
def newton(q,idx,tol=1e-12,it=80):
    """Newton on grad_idx E = 0 over the coordinates idx of q."""
    q=q.copy()
    for _ in range(it):
        E,g,H=Eh(q); r=g[idx]
        if np.linalg.norm(r)<tol: return q,True
        step=np.linalg.lstsq(H[np.ix_(idx,idx)],-r,rcond=1e-12)[0]
        s=1.0; r0=np.linalg.norm(r)
        while s>1e-4:
            qn=q.copy(); qn[idx]+=s*step;
            if np.linalg.norm(Eg(qn)[1][idx])<r0: break
            s/=2
        else: return q,False
        q=qn
    return q,np.linalg.norm(Eg(q)[1][idx])<tol
def vmat(kp): return (P*np.cos(S@kp)[:,None]).T@P/15
rng=np.random.default_rng(8)
print("c0 =",c0,";  60 pairs;  E(0,0)=",Eg(np.zeros(8))[0] if np.linalg.norm(V(np.zeros(8)))>0 else 0.0)

print("\n=== A) gap at fixed k'?  Newton for V(k)=0 (4 eqs, 4 unknowns) at fixed k', starting from k=0 and from 20 random k ===")
def nodes(kp):
    found=[]
    for s in range(21):
        k=np.zeros(4) if s==0 else rng.normal(size=4)*1.5
        for _ in range(100):
            q=np.concatenate([k,kp]); v=V(q)
            if np.linalg.norm(v)<1e-14: break
            Jk=Jac(q)[:,:4]; k=k+np.linalg.lstsq(Jk,-v,rcond=1e-14)[0]
        q=np.concatenate([k,kp]); found.append((np.linalg.norm(V(q))*c0,np.linalg.norm(k)))
    return found
for r in (0.5,1,2,3):
    for t in range(2):
        d=rng.normal(size=4); d/=np.linalg.norm(d); kp=r*d; q0=np.concatenate([np.zeros(4),kp])
        f=nodes(kp); ok=[x for x in f if x[0]<1e-12]
        print(f"  |k'|={r} dir{t}: E(0,k')={c0*np.linalg.norm(V(q0)):.6e}   Newton from k=0: E at end={f[0][0]:.3e}, |k*|={f[0][1]:.4e};  {len(ok)}/21 starts reach a node E<1e-12; smallest |k*| among them={min([x[1] for x in ok]) if ok else float('nan'):.4e}")

print("\n=== B) physical rest states at fixed k': grad_k E = 0 with E>0, Newton in k over 4 coordinates, 400 starts per k' ===")
Bres={}
for r in (1,2,3):
    d=rng.normal(size=4); d/=np.linalg.norm(d); kp=r*d; sols=[]
    for s in range(400):
        q=np.concatenate([rng.uniform(-5,5,4),kp]); q,ok=newton(q,np.arange(4))
        if ok:
            E,g,H=Eh(q)
            if E>1e-6: sols.append((E,np.linalg.eigvalsh(H[:4,:4])))
    Es=np.array([s[0] for s in sols]);
    print(f"  |k'|={r}: {len(sols)}/400 converged to rest states with E>1e-6;  distinct E (6 d.p.): {len(set(np.round(Es,6)))};  E range [{Es.min() if len(Es) else float('nan'):.6f},{Es.max() if len(Es) else float('nan'):.6f}]")
    nmin=sum(1 for s in sols if s[1].min()>1e-9); nmax=sum(1 for s in sols if s[1].max()<-1e-9)
    print(f"     physical-Hessian definite: minima {nmin}, maxima {nmax}, saddles {len(sols)-nmin-nmax}")
    for E,ev in sorted(sols,key=lambda x:x[0])[:6]: print(f"     E={E:.8f}  eig H_kk={np.round(ev,6)}")

print("\n=== C) fully stationary points of E on R^8 (grad_q E = 0, E>0): Newton from 20000 random starts ===")
NS=20000; sols=[]
for s in range(NS):
    q=rng.uniform(-6,6,8); q,ok=newton(q,np.arange(8))
    if ok:
        E,g,H=Eh(q)
        if E>1e-6: sols.append((q,E,H))
print(f"  converged to stationary points with E>1e-6: {len(sols)} of {NS}")
Es=np.array([s[1] for s in sols]); keys=np.round(Es,7); uniq=sorted(set(keys))
print(f"  distinct stationary energies (7 d.p.): {len(uniq)}")
rows=[]
for e in uniq:
    idx=[i for i,k in enumerate(keys) if k==e]; q,E,H=sols[idx[0]]
    w=np.linalg.eigvalsh(H); npos=int((w>1e-9).sum()); nneg=int((w<-1e-9).sum())
    Hkk=H[:4,:4]; Hpp=H[4:,4:]; Hkp=H[:4,4:]
    sch_ok=abs(np.linalg.det(Hpp))>1e-14
    sch=np.linalg.eigvalsh(Hkk-Hkp@np.linalg.solve(Hpp,Hkp.T)) if sch_ok else None
    Jk=Jac(q)[:,:4];
    rows.append((E,len(idx),npos,nneg,np.linalg.eigvalsh(Hkk),np.linalg.eigvalsh(Hpp),sch,mstat(q),np.linalg.eigvalsh(vmat(q[4:])),np.linalg.svd(Jk,compute_uv=False)))
print("  E_s            mult  (+,-)  m_static   eig H_kk                       eig H_k'k'                     eig Schur(k|k')                  smallest sv J_k")
for E,mu,npos,nneg,hk,hp,sch,ms,vv,sv in rows[:40]:
    print(f"  {E:.9f} {mu:5d}  ({npos},{nneg})  {ms:8.4f}  {np.round(hk,4)} {np.round(hp,4)} {np.round(sch,4) if sch is not None else 'singular H_k\'k\''}  {sv.min():.3e}")
if len(rows)>40: print(f"  ... {len(rows)-40} more distinct energies not listed")
Ea=np.array([r[0] for r in rows])
print("\n  stationary-energy summary: min %.9f  max %.9f  (E at global max over the torus: %.9f);  signature counts:"%(Ea.min(),Ea.max(),max(r[0] for r in rows)))
from collections import Counter
print("  ",dict(Counter((r[2],r[3]) for r in rows)))
Emax_global=max(Eg(rng.uniform(-8,8,8))[0] for _ in range(200000))
print("  sampled max of E over 200000 random q:",Emax_global)
# relations at the stationary points: does E_s * H_kk have any relation to v^2 or to m_static?
print("\n  relation tests at the stationary points (E_s*eig(H_kk) = c_eff^2 if M=E/c^2 held with M^-1=H_kk):")
for E,mu,npos,nneg,hk,hp,sch,ms,vv,sv in rows[:12]:
    print(f"   E={E:.6f}  E*eig(H_kk)={np.round(E*hk,4)}   m_static={ms:.4f}  eig v(k')={np.round(vv,4)}")
print("  corr(E_s, m_static) over distinct stationary energies:",np.corrcoef(Ea,[r[7] for r in rows])[0,1] if len(rows)>2 else None)
