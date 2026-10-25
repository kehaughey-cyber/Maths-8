"""
Co-definition driver on the PENTAGONAL 5-cycle circulation carrying the frustration epsilon.

Unit: each edge e=(i,j) has exactly 5 common neighbours (the 5 tetrahedra around the edge in
{3,3,5}); they form a pentagon (5-cycle). The field's "change" seen by edge e is its circulation
around that pentagon, C_e(psi)=Im sum_a conj(psi[p_a]) psi[p_{a+1}] (needs phase: a 3+-body loop,
'3 to perceive change'). The geometric frustration epsilon = 2pi-5 arccos(1/3) is the pentagon's
out-of-plane non-closure, carried additively: Phi_e = epsilon + C_e.

Co-definition (first-order relaxational, rate Gamma): y_e -> target -beta*Phi_e^2; w_e=exp(y_e).
Propagation: psi'' = -L[w]psi (complex Hermitian). Contrast three drivers for a chiral excitation:
  '2body'  target -beta|Dpsi_e|^2            (difference; the old driver)
  'pent0'  target -beta C_e^2                (pentagon circulation, epsilon=0)
  'penteps' target -beta(epsilon+C_e)^2      (pentagon circulation carrying epsilon)
"""
import numpy as np, itertools
from itertools import permutations
phi=(1+5**0.5)/2; EPS=2*np.pi-5*np.arccos(1/3)

# ---- carrier ----
V=[]
for i in range(4):
    for s in (1,-1):
        v=[0,0,0,0]; v[i]=s; V.append(v)
for s in itertools.product((0.5,-0.5),repeat=4): V.append(list(s))
base=[0.0,0.5,phi/2,1/(2*phi)]
def par(p):
    p=list(p); seen=[False]*4; k=0
    for i in range(4):
        if seen[i]:continue
        j=i;c=0
        while not seen[j]: seen[j]=True;j=p[j];c+=1
        k+=c-1
    return k%2
for p in [q for q in permutations(range(4)) if par(q)==0]:
    vals=[base[p[i]] for i in range(4)]; nz=[i for i in range(4) if vals[i]!=0]
    for ss in itertools.product((1,-1),repeat=3):
        v=list(vals)
        for k,idx in enumerate(nz): v[idx]=vals[idx]*ss[k]
        V.append(v)
V=np.unique(np.round(np.array(V),9),axis=0); N=len(V)
Adj=(np.abs(V@V.T-phi/2)<1e-6); np.fill_diagonal(Adj,False)
edges=[(i,j) for i in range(N) for j in range(i+1,N) if Adj[i,j]]
Ei=np.array([e[0] for e in edges]); Ej=np.array([e[1] for e in edges]); E=len(edges)
L0=np.diag(Adj.sum(1).astype(float))-Adj.astype(float); muvals,U=np.linalg.eigh(L0)

# ---- per-edge pentagon: 5 common neighbours ordered as a 5-cycle ----
def order_cycle(K):
    K=list(K); sub={a:[b for b in K if Adj[a,b]] for a in K}
    if any(len(sub[a])!=2 for a in K): return None    # not a clean 5-cycle
    order=[K[0]]; prev=None
    while len(order)<len(K):
        nxts=[b for b in sub[order[-1]] if b!=prev]
        if not nxts: return None
        prev=order[-1]; order.append(nxts[0])
    return order if Adj[order[-1],order[0]] else None
pent=np.zeros((E,5),dtype=int); okcyc=0; sizes=[]
for e,(i,j) in enumerate(edges):
    K=[k for k in range(N) if Adj[i,k] and Adj[j,k]]; sizes.append(len(K))
    o=order_cycle(K)
    if o is not None and len(o)==5: pent[e]=o; okcyc+=1
    else: pent[e]=(K+[K[0]]*5)[:5]
print(f"[pentagon] edges={E}; common-neighbours per edge: min {min(sizes)} max {max(sizes)} (expect 5);"
      f" edges whose 5 common-nbrs form a clean 5-cycle: {okcyc}/{E}")
print(f"[epsilon]  2pi-5arccos(1/3) = {EPS:.6f} rad = {np.degrees(EPS):.4f} deg")

P0=pent; P1=np.roll(pent,-1,axis=1)   # consecutive pentagon pairs
def circ(psi):                        # C_e for every edge
    return np.imag(np.sum(np.conj(psi[P0])*psi[P1],axis=1))
def Lw(y,psi):
    w=np.exp(y); d=psi[Ei]-psi[Ej]; f=np.zeros(N,complex)
    np.add.at(f,Ei,w*d); np.add.at(f,Ej,-w*d); return f

# sanity: uniform-phase real mode has zero circulation; a chiral mode does not
u1=U[:,np.argmin(np.abs(muvals-5.5279))]; u2=U[:,np.argmin(np.abs(muvals-9.0))]
print(f"[sanity] circulation of a uniform-phase field: {np.max(np.abs(circ((u1+0j)))):.2e} (expect ~0)")
chi=(u1+1j*u2); chi/=np.linalg.norm(chi)
print(f"[sanity] circulation of a chiral field u1+i*u2: mean|C_e|={np.mean(np.abs(circ(chi))):.4e} (nonzero)")

def run(driver,A,beta=0.5,Gamma=1.0,dt=0.01,steps=4000):
    psi=A*chi.copy(); psidot=np.zeros(N,complex)
    d=psi[Ei]-psi[Ej]
    if driver=='2body': ytar=-beta*np.abs(d)**2
    elif driver=='pent0': ytar=-beta*circ(psi)**2
    else: ytar=-beta*(EPS+circ(psi))**2
    y=ytar.copy()
    ap=-Lw(y,psi); a=np.empty(steps,complex); Cbar=[]
    for t in range(steps):
        psi=psi+psidot*dt+0.5*ap*dt*dt
        d=psi[Ei]-psi[Ej]
        if driver=='2body': ytar=-beta*np.abs(d)**2
        elif driver=='pent0': ytar=-beta*circ(psi)**2
        else: ytar=-beta*(EPS+circ(psi))**2
        y=y+dt*(-Gamma*(y-ytar))
        ap2=-Lw(y,psi); psidot=psidot+0.5*(ap+ap2)*dt; ap=ap2
        a[t]=np.vdot(A*chi,psi)/(A*A)
        if t%20==0: Cbar.append(np.mean(np.abs(circ(psi))))
    # frequency from Re(a) zero-crossings; damping from |a| peak decay
    r=np.real(a)-np.mean(np.real(a)); tt=np.arange(steps)*dt
    s=np.sign(r); c=np.where(np.diff(s)!=0)[0]
    tc=np.array([tt[k]+(r[k]/(r[k]-r[k+1]))*dt for k in c]); half=np.diff(tc)
    omega=np.pi/np.median(half) if len(half)>3 else np.nan
    mag=np.abs(a); pk=np.array([(tt[i],mag[i]) for i in range(1,steps-1)
                                if mag[i]>mag[i-1] and mag[i]>=mag[i+1] and mag[i]>1e-9])
    gamma=np.nan
    if len(pk)>4: g,_=np.polyfit(pk[:,0],np.log(pk[:,1]),1); gamma=-g
    return omega,gamma,np.mean(Cbar)

print("\n[contrast] chiral excitation u1+i*u2, beta=0.5, Gamma=1")
print("  A     driver     omega     gamma(damping)   mean|C_e|")
for A in (1.0,2.0):
    for drv in ('2body','pent0','penteps'):
        w,g,cb=run(drv,A)
        print(f" {A:4.1f}  {drv:8s}  {w:8.4f}  {g:11.6f}    {cb:.4e}")
