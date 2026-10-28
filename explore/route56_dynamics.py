"""
Dynamics of the internal label k' (follows route56_inertia.py; ledger section 33).
Exact structure used: on a plane wave the chiral block is W(q) = (1/30) sum_{120 units} Q(u) exp(i q.X_u) = i*c0*(V0 - i V.sigma) with V(q)=sum_{60 pairs} P sin(q.X), Q(u)=u0-i u.sigma; H(q)=[[0,W],[W^dag,0]], H^2=E^2, E=c0|V|.
A uniform force F on the physical coordinate (potential -F.x, x the physical embedding of the site) is exactly q(t)=q0+(F t,0) in the R^8 momentum (Bloch acceleration theorem on the lattice: the potential is linear in the integer site coordinates). E is periodic under the dual lattice L*, so the physical line (F t,0) is dense in the 8-torus.
Parts:
 1) ergodicity: time fractions of E<eps along a long physical-force line vs the uniform 8-torus average (same torus sampler as route56_window.py); also the passage minima list.
 2) exact 4x4 Schroedinger evolution through a node passage at force f (impact parameter delta = min E along the path), measured probability to leave the upper band vs the Landau-Zener value exp(-pi delta^2/alpha), alpha = f c0 |Jac_k d| (E-slope along the path). The H(q) is verified against the 120-unit sum first.
 3) torus density of states g(E) (exponent near 0) and what a white (site-uncorrelated) perturbation, which transfers any momentum, would do in golden-rule (rate ~ w^2 g(E)).
No fitting.  Usage: py -3 -I -u route56_dynamics.py
"""
import numpy as np, os
here=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(here,'route56_inertia.py')).read().split("rng=np.random.default_rng(8)")[0]
exec(compile(src,'route56_inertia_header','exec'))
rng=np.random.default_rng(34)
sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
def Wq(q):                                           # 2x2 from the pair formula
    v=V(q); return 1j*c0*(v[0]*np.eye(2)-1j*(v[1]*sig[0]+v[2]*sig[1]+v[3]*sig[2]))
def Wfull(q):                                        # brute force over all 120 units
    W=np.zeros((2,2),complex)
    for a in range(120):
        u=Pall[a]; Q=u[0]*np.eye(2)-1j*(u[1]*sig[0]+u[2]*sig[1]+u[3]*sig[2])
        W+=Q*np.exp(1j*(np.concatenate([Pall[a],Sall[a]])@q))
    return W/30
q=rng.normal(size=8)*2
print("check W(pairs) vs W(120 units): max abs diff =",np.abs(Wq(q)-Wfull(q)).max()," singular values",np.linalg.svd(Wfull(q),compute_uv=False)," E =",Eg(q)[0])
def Hq(q):
    W=Wq(q); H=np.zeros((4,4),complex); H[:2,2:]=W; H[2:,:2]=W.conj().T; return H

print("\n=== 1) ergodicity of the physical-force line in the 8-torus ===")
def Eof(Q):                                           # Q: (8,n)
    th=X@Q; return c0*np.linalg.norm(P.T@np.sin(th),axis=0)
Uf=h.U.reshape(120,8)[first].astype(float)
NT=4_000_000; Et=[]
for i in range(8):
    th=rng.uniform(0,2*np.pi,size=(NT//8,8)); ph=th@Uf.T; Et.append(c0*np.linalg.norm(np.sin(ph)@P,axis=1))
Et=np.concatenate(Et)
d=rng.normal(size=4); d/=np.linalg.norm(d); q0=rng.uniform(-3,3,8)
ds=0.004; Ltot=4000.0; chunk=100000
Es=[]
for st in range(0,int(Ltot/ds),chunk):
    s=(np.arange(st,min(st+chunk,int(Ltot/ds)))*ds)
    Q=np.tile(q0[:,None],(1,len(s))); Q[:4]+=np.outer(d,s); Es.append(Eof(Q))
Es=np.concatenate(Es); nb=10; blocks=np.array_split(Es,nb)
print(f"  line: {len(Es)} points, arclength {Ltot}, step {ds}; torus: {len(Et)} random points.  mean E: line {Es.mean():.5f}  torus {Et.mean():.5f}  (max line {Es.max():.5f}, max torus {Et.max():.5f})")
print("  eps      line fraction (block std)         torus fraction (sqrt(p/N))        ratio")
for e in (0.05,0.1,0.2,0.4,0.8):
    fl=np.array([np.mean(b<e) for b in blocks]); pt=np.mean(Et<e)
    print(f"  {e:5.2f}  {fl.mean():.5e} (+-{fl.std()/np.sqrt(nb):.1e})   {pt:.5e} (+-{np.sqrt(pt/len(Et)):.1e})   {fl.mean()/pt:7.3f}")
# passage minima
mi=np.where((Es[1:-1]<Es[:-2])&(Es[1:-1]<=Es[2:]))[0]+1
em=Es[mi]
print("  local minima of E along the line:",len(mi)," with E_min<0.2:",int((em<0.2).sum())," <0.1:",int((em<0.1).sum())," <0.05:",int((em<0.05).sum())," <0.02:",int((em<0.02).sum()))
print("  smallest ten passage minima:",np.round(np.sort(em)[:10],5))

# expected band-flip events per unit physical momentum from the measured passage list and the LZ law validated in part 2 (isolated, slow passages)
sl=np.array([c0*np.linalg.norm(Jac(np.concatenate([q0[:4]+d*(mi[j]*ds),q0[4:]]))[:,:4]@d) for j in range(len(mi))])
print("  expected band-flip events per unit physical momentum, sum_i exp(-pi delta_i^2/(f*slope_i))/L over all passage minima:")
for f in (1e-4,1e-3,1e-2):
    pf=np.exp(-np.pi*em**2/(f*sl))
    print(f"   f={f:g}: {pf.sum()/Ltot:.5f} flips per unit k;  fraction of passages with P_flip>0.5: {np.mean(pf>0.5):.4f};  mean passage spacing in k: {Ltot/len(mi):.2f}")
print("\n=== 2) exact evolution through a node passage vs Landau-Zener ===")
def evolve(qa,qb,f,dt0=0.1):
    """q(t)=qa+(qb-qa)/|qb-qa| f t, from t=0 to the end; start in a random state of the upper band; return weight left in the upper band at the end."""
    L=np.linalg.norm(qb-qa); T=L/f; n=int(np.ceil(T/dt0)); dt=T/n; u=(qb-qa)/L
    H0=Hq(qa); w,vv=np.linalg.eigh(H0); up=vv[:,w>0]; c=rng.normal(size=2)+1j*rng.normal(size=2); psi=up@(c/np.linalg.norm(c))
    for i in range(n):
        qm=qa+u*f*(i+0.5)*dt; Hm=Hq(qm); Em=c0*np.linalg.norm(V(qm))
        psi=np.cos(Em*dt)*psi-1j*np.sin(Em*dt)*(Hm@psi)/Em
    w2,v2=np.linalg.eigh(Hq(qb)); upb=v2[:,w2>0]
    return 1-np.linalg.norm(upb.conj().T@psi)**2, np.linalg.norm(psi)
def node(kp):
    k=np.zeros(4)
    for _ in range(100):
        qq=np.concatenate([k,kp]); v=V(qq)
        if np.linalg.norm(v)<1e-15: break
        k=k+np.linalg.lstsq(Jac(qq)[:,:4],-v,rcond=1e-14)[0]
    return k
print("  |k'|  delta=min E      alpha=f*slope   f          target P  LZ P_flip=exp(-pi d^2/alpha)  exact P_flip (vector1)  (vector2)  norm")
rows=[]
for r in (0.5,1.0,2.0):
    dd=rng.normal(size=4); dd/=np.linalg.norm(dd); kp=r*dd; ks=node(kp)
    for b in (0.004,0.012):
        dpath=rng.normal(size=4); dpath/=np.linalg.norm(dpath)
        pp=rng.normal(size=4); pp-=pp@dpath*dpath; pp/=np.linalg.norm(pp)
        kc=ks+b*pp                                   # path passes the node at transverse offset b in k
        s=np.linspace(-0.3,0.3,60001); Q=np.tile(np.concatenate([kc,kp])[:,None],(1,len(s))); Q[:4]+=np.outer(dpath,s); Ee=Eof(Q)
        im=np.argmin(Ee); delta=Ee[im]; qmin=Q[:,im]; slope=c0*np.linalg.norm(Jac(qmin)[:,:4]@dpath)
        for tp in (0.2,0.5,0.8):
            alpha=np.pi*delta**2/(-np.log(tp)); f=alpha/slope
            qa=Q[:,0]; qb=Q[:,-1]
            p1,n1=evolve(qa,qb,f); p2,n2=evolve(qa,qb,f)
            print(f"  {r:4}  {delta:.6e}  {alpha:.4e}  {f:.4e}  {tp:5.2f}   {np.exp(-np.pi*delta**2/alpha):10.5f}                  {p1:10.5f}              {p2:10.5f}   {n1:.6f}",flush=True)
            rows.append((tp,p1,p2))
rows=np.array(rows); print("  max |exact - LZ target| over all cases:",np.abs(np.concatenate([rows[:,1]-rows[:,0],rows[:,2]-rows[:,0]])).max())

print("\n=== 3) torus density of states and golden-rule rate for a white perturbation ===")
es=np.array([0.02,0.04,0.08,0.16,0.32,0.64,1.0]); cum=np.array([np.mean(Et<e) for e in es])
print("  eps    P(E<eps)       local exponent d ln P/d ln eps (to previous)")
for i,e in enumerate(es): print(f"  {e:5.2f}  {cum[i]:.5e}  {np.log(cum[i]/cum[i-1])/np.log(es[i]/es[i-1]) if i and cum[i-1]>0 else float('nan'):8.3f}")
cnt,edges=np.histogram(Et,bins=np.linspace(0,1.45,59)); g=cnt/len(Et)/(edges[1]-edges[0]); ec=0.5*(edges[1:]+edges[:-1])
print("  density g(E) (per unit E, torus-normalised):")
for i in range(0,58,4): print(f"   E={ec[i]:.3f}  g={g[i]:.5f}  g/E^3={g[i]/ec[i]**3:9.4f}")
