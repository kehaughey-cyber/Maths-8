"""
Two floor-grounded link-response laws, contrasted with the D-arc (exp/kappa) and the frozen web.

Law A -- ADIABATIC: the relation IS a readout of the states, w_e = exp(-beta|Dpsi_e|^2), with NO
  independent edge d.o.f. and NO kappa.  The force is the FULL variation of
      V(psi) = 1/2 sum_e exp(-beta s_e) s_e,     s_e = |psi_i-psi_j|^2,
  i.e. it INCLUDES dw/dpsi.  Effective edge weight W_eff(s) = exp(-beta s)(1-beta s).
  (psi''=-L[w]psi would drop the (1-beta s) part -- verified below against finite differences.)
  Conservative -> expect NO dissipation; isolates the stiffness effect.

Law B -- FIRST-ORDER RELAXATIONAL, clocked by a rate Gamma (the tick), toward the same target:
      y' = -Gamma (y - y_target),  y_target = -beta s_e,  w_e = exp(y_e),  psi'' = -L[w]psi.
  Here w is an independent relaxing field (so psi-force = -L[w]psi is correct, no dw/dpsi).
  First-order => DISSIPATIVE (the structural arrow F2/F3) -> expect damping with rate ~ Gamma.

Real psi (standing modes) suffices for the resistance (ring-down) measurement.
"""
import numpy as np, itertools
from itertools import permutations
phi=(1+5**0.5)/2

# ---- carrier ----
V4=[]
for i in range(4):
    for s in (1,-1):
        v=[0,0,0,0]; v[i]=s; V4.append(v)
for s in itertools.product((0.5,-0.5),repeat=4): V4.append(list(s))
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
        V4.append(v)
V4=np.unique(np.round(np.array(V4),9),axis=0); N=len(V4)
Adj=(np.abs(V4@V4.T-phi/2)<1e-6); np.fill_diagonal(Adj,False)
edges=[(i,j) for i in range(N) for j in range(i+1,N) if Adj[i,j]]
Ei=np.array([e[0] for e in edges]); Ej=np.array([e[1] for e in edges]); E=len(edges)
L0=np.diag(Adj.sum(1).astype(float))-Adj.astype(float)
muvals,U=np.linalg.eigh(L0)
# triangles (3-body structures = the floor's "change" units): common neighbours per edge
tri=0
for (i,j) in edges: tri+=int(np.sum(Adj[i]&Adj[j]))
tri//=3
print(f"[carrier] N={N} edges={E} triangles={tri}  (triangle = minimal 3-body 'change' unit)")

def diff(psi): return psi[Ei]-psi[Ej]
def scatter(contrib):
    g=np.zeros(N); np.add.at(g,Ei,contrib); np.add.at(g,Ej,-contrib); return g

# ---------- Law A: adiabatic, full variational force ----------
def V_A(psi,beta):
    s=diff(psi)**2; return 0.5*np.sum(np.exp(-beta*s)*s)
def force_A(psi,beta):             # = -gradV ; W_eff = exp(-beta s)(1-beta s)
    d=diff(psi); s=d*d; Weff=np.exp(-beta*s)*(1-beta*s); return -scatter(Weff*d)

# verify the analytic force against finite differences of V_A
rng=np.random.default_rng(0); pt=rng.standard_normal(N); beta_chk=0.7
g_an=-force_A(pt,beta_chk); g_fd=np.zeros(N); h=1e-6
for i in range(N):
    e=np.zeros(N); e[i]=h
    g_fd[i]=(V_A(pt+e,beta_chk)-V_A(pt-e,beta_chk))/(2*h)
print(f"[verify] Law A analytic gradV vs finite-diff: max abs err = {np.max(np.abs(g_an-g_fd)):.2e}  "
      f"(psi''=-L[w]psi would differ by the dropped (1-beta s) term)")

def ringA(u,mu,A,beta,dt=0.01,steps=6000):
    u=u/np.linalg.norm(u); psi=A*u.copy(); psidot=np.zeros(N)
    ap=force_A(psi,beta); a=np.empty(steps)
    H0=0.5*psidot@psidot+V_A(psi,beta); Hmx=H0;Hmn=H0
    for t in range(steps):
        psi=psi+psidot*dt+0.5*ap*dt*dt
        ap2=force_A(psi,beta); psidot=psidot+0.5*(ap+ap2)*dt; ap=ap2
        a[t]=u@psi
        if t%40==0:
            H=0.5*psidot@psidot+V_A(psi,beta); Hmx=max(Hmx,H);Hmn=min(Hmn,H)
    return measure(a,dt)+((Hmx-Hmn)/abs(H0),)

# ---------- Law B: first-order relaxational, clocked by Gamma ----------
def Lw(y,psi):
    w=np.exp(y); d=diff(psi); return scatter(w*d)
def ringB(u,mu,A,beta,Gamma,dt=0.01,steps=6000):
    u=u/np.linalg.norm(u); psi=A*u.copy(); psidot=np.zeros(N)
    s=diff(psi)**2; y=-beta*s                    # start at the relaxed target
    ap=-Lw(y,psi); a=np.empty(steps)
    for t in range(steps):
        psi=psi+psidot*dt+0.5*ap*dt*dt
        s=diff(psi)**2; ytar=-beta*s
        y=y+dt*(-Gamma*(y-ytar))                 # first-order relaxation (dissipative)
        ap2=-Lw(y,psi); psidot=psidot+0.5*(ap+ap2)*dt; ap=ap2
        a[t]=u@psi
    return measure(a,dt)

def measure(a,dt):
    a=a-a.mean(); tt=np.arange(len(a))*dt
    s=np.sign(a); c=np.where(np.diff(s)!=0)[0]
    tc=np.array([tt[k]+(a[k]/(a[k]-a[k+1]))*dt for k in c])
    half=np.diff(tc); omega=np.pi/np.median(half) if len(half)>3 else np.nan
    pk=np.array([(tt[i],a[i]) for i in range(1,len(a)-1) if a[i]>a[i-1] and a[i]>=a[i+1] and a[i]>1e-9])
    gamma=np.nan
    if len(pk)>4:
        g,_=np.polyfit(pk[:,0],np.log(pk[:,1]),1); gamma=-g
    return omega,gamma

def ev(mt): k=np.argmin(np.abs(muvals-mt)); return U[:,k],muvals[k]

print("\n[Law A  adiabatic, conservative]  omega vs bare, m_eff=(bare/live)^2, gamma (expect ~0)")
print("  mu     A    beta   omega_bare  omega_A   m_eff    gamma      H-drift")
for mt in (5.5279,9.0,12.0):
    u,mu=ev(mt)
    for A,beta in ((1.0,0.5),(2.0,0.5)):
        w,g,hd=ringA(u,mu,A,beta)
        meff=(np.sqrt(mu)/w)**2
        print(f" {mu:6.3f} {A:4.1f}  {beta:4.2f}  {np.sqrt(mu):9.4f}  {w:8.4f}  {meff:6.4f}  {g:9.5f}  {hd:.1e}")

print("\n[Law B  first-order relaxational, clocked by Gamma]  mu=9, A=2, beta=0.5")
print("  Gamma    omega_B   gamma(damping)   (Gamma=tick-rate fixes this, not free)")
u,mu=ev(9.0)
for G in (0.25,0.5,1.0,2.0,4.0,8.0):
    w,g=ringB(u,mu,2.0,0.5,G)
    print(f"  {G:5.2f}   {w:8.4f}   {g:10.5f}")

print("\n[contrast] mu=9, A=2:  bare sqrt(mu)=%.4f" % np.sqrt(9.0))
u,mu=ev(9.0)
wA,gA,_=ringA(u,mu,2.0,0.5); wB,gB=ringB(u,mu,2.0,0.5,1.0)
print(f"  Law A adiabatic (conservative): omega={wA:.4f}  gamma={gA:.5f}")
print(f"  Law B relaxational  (Gamma=1):  omega={wB:.4f}  gamma={gB:.5f}")
print("  => adiabatic shifts frequency (stiffness) with ~no damping; relaxational adds the damping.")
