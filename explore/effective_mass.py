"""
Effective mass of a mode in the LIVE relational web, by free-ring-down frequency shift.

For each mode (Laplacian eigenvalue mu), excite at amplitude A and measure three
frequencies:
  omega_bare   = sqrt(mu)                 (w=1, no background)
  omega_static = edges balanced to A but HELD FIXED  (isolates stiffness change)
  omega_live   = edges moving (the dynamic back-reaction)
Effective mass (stiffness pinned at the static value): m_eff = (omega_static/omega_live)^2.
m_eff > 1 means the live web makes the mode harder to accelerate (heavier).
Ring-down envelope gives gamma = leakage/radiation damping (energy from the mode
into the web + other modes; total H is still conserved).

Swept over amplitude A (nonlinear onset) and kappa (stiffness of co-definition).
Reuses the D-arc joint action verbatim. Honest diagnostic.
"""
import numpy as np, itertools
from itertools import permutations
phi=(1+5**0.5)/2

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
L0=np.diag(Adj.sum(1).astype(float))-Adj.astype(float)
muvals,U=np.linalg.eigh(L0)
print(f"[carrier] N={N} edges={E}")

def Lw(y,psi):
    w=np.exp(y); d=psi[Ei]-psi[Ej]; f=np.zeros_like(psi)
    np.add.at(f,Ei,w*d); np.add.at(f,Ej,-w*d); return f
def Vpot(psi,y,kappa):
    d=psi[Ei]-psi[Ej]; return 0.5*np.sum(np.exp(y)*d*d)+0.5*kappa*np.sum(y*y)

def ring(u,mu,A,kappa,mode,dt=0.01,steps=5000):
    """mode: 'static' (freeze edges at balance) or 'live' (edges move)."""
    u=u/np.linalg.norm(u)
    psi=A*u.copy(); d0=psi[Ei]-psi[Ej]; y=np.zeros(E)
    for _ in range(400): y=-(0.5/kappa)*np.exp(y)*d0**2     # balance at turning point
    psidot=np.zeros(N); ydot=np.zeros(E)
    live=(mode=='live')
    def Fy(psi,y):
        d=psi[Ei]-psi[Ej]; return -kappa*y-0.5*np.exp(y)*d*d
    ap=-Lw(y,psi); ay=Fy(psi,y)
    H0=0.5*psidot@psidot+0.5*ydot@ydot+Vpot(psi,y,kappa); Hmax=H0;Hmin=H0
    a=np.empty(steps)
    for t in range(steps):
        psi=psi+psidot*dt+0.5*ap*dt*dt
        if live: y=y+ydot*dt+0.5*ay*dt*dt
        ap2=-Lw(y,psi); ay2=Fy(psi,y)
        psidot=psidot+0.5*(ap+ap2)*dt
        if live: ydot=ydot+0.5*(ay+ay2)*dt
        ap,ay=ap2,ay2
        a[t]=u@psi
        if live and (t%50==0):
            H=0.5*psidot@psidot+0.5*ydot@ydot+Vpot(psi,y,kappa); Hmax=max(Hmax,H);Hmin=min(Hmin,H)
    a=a-a.mean(); tt=np.arange(steps)*dt
    # frequency from zero crossings (interpolated)
    s=np.sign(a); cidx=np.where(np.diff(s)!=0)[0]
    tc=np.array([tt[c]+ (a[c]/(a[c]-a[c+1]))*dt for c in cidx])
    half=np.diff(tc); omega=np.pi/np.median(half) if len(half)>3 else np.nan
    # damping from successive positive-peak decay
    pk=[(tt[i],a[i]) for i in range(1,steps-1) if a[i]>a[i-1] and a[i]>=a[i+1] and a[i]>1e-9]
    pk=np.array(pk)
    gamma=np.nan
    if len(pk)>4:
        g,_=np.polyfit(pk[:,0],np.log(pk[:,1]),1); gamma=-g
    Hdr=(Hmax-Hmin)/abs(H0) if live else 0.0
    return omega,gamma,Hdr

def eigvec(mu_target):
    k=np.argmin(np.abs(muvals-mu_target)); return U[:,k], muvals[k]

modes=[2.2918,5.5279,9.0000,12.0000]     # mu values (span)
print("\n[amplitude sweep]  kappa=1.  m_eff=(w_static/w_live)^2  (>1 = live web makes the mode heavier)")
print("  mu      A      w_bare   w_static   w_live    m_eff     gamma_live   (gamma_static)   H-drift")
for mt in modes:
    u,mu=eigvec(mt)
    for A in (0.3,1.0,2.0):
        ws,gs,_=ring(u,mu,A,1.0,'static')
        wl,gl,hd=ring(u,mu,A,1.0,'live')
        meff=(ws/wl)**2 if (ws==ws and wl==wl) else np.nan
        print(f"  {mu:6.3f}  {A:4.1f}   {np.sqrt(mu):7.4f}  {ws:8.4f}  {wl:8.4f}  {meff:7.4f}  {gl:10.5f}   {gs:10.5f}    {hd:.1e}")

print("\n[kappa sweep]  mode mu=9.0, A=2.0.  (softer kappa = easier to re-co-define)")
print("  kappa    w_static   w_live    m_eff     gamma_live    H-drift")
u,mu=eigvec(9.0)
for kap in (0.25,0.5,1.0,2.0,4.0):
    ws,gs,_=ring(u,mu,2.0,kap,'static')
    wl,gl,hd=ring(u,mu,2.0,kap,'live')
    meff=(ws/wl)**2
    print(f"  {kap:5.2f}   {ws:8.4f}  {wl:8.4f}  {meff:7.4f}  {gl:10.5f}    {hd:.1e}")
