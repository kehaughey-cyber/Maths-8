"""
Bring the relational web alive (the D-arc joint action) and PUSH on it:
kick a mode and measure how much of the kick energy the live web absorbs into
re-co-definition (edge motion). That absorption is the candidate "inertia" --
the web's reluctance to re-co-define. Then see what it tracks: the Laplacian
eigenvalue mu (= registration-rate ordering) or the Galois mass {12,4,4,0}.

Reuses the D-arc constitutive choices verbatim (exp weights, kappa stiffness),
so no stiffness is re-added by hand. Honest first diagnostic, not a derived law.
"""
import numpy as np, itertools
from itertools import permutations
np.set_printoptions(suppress=True)

phi=(1+5**0.5)/2; psi_g=-1/phi

# ---- carrier: 120 icosians, 720 edges (overlap phi/2) ----
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
V=np.unique(np.round(np.array(V),9),axis=0)
N=len(V); assert N==120
Gr=V@V.T
Adj=(np.abs(Gr-phi/2)<1e-6); np.fill_diagonal(Adj,False)
edges=[(i,j) for i in range(N) for j in range(i+1,N) if Adj[i,j]]
Ei=np.array([e[0] for e in edges]); Ej=np.array([e[1] for e in edges])
E=len(edges); print(f"[carrier] N={N}, edges={E}, degree={Adj.sum(1).min()}..{Adj.sum(1).max()}")

L0=np.diag(Adj.sum(1).astype(float))-Adj.astype(float)   # unweighted Laplacian
muvals,U=np.linalg.eigh(L0)

# Galois mass by matter-lattice sector, keyed by adjacency eigenvalue lambda=12-mu
galois={12.0:12.0, round(4*phi,4):4.0, round(-4/phi,4):4.0, 0.0:0.0}
def gal_for(mu):
    lam=round(12-mu,4)
    return galois.get(lam, None)

def Lw(y,psi):                 # weighted Laplacian action
    w=np.exp(y); d=psi[Ei]-psi[Ej]; f=np.zeros_like(psi)
    np.add.at(f,Ei, w*d); np.add.at(f,Ej,-w*d); return f

def run(u, kappa, live, mu, alpha=1.0, vkick=0.3, dt=0.02, steps=2000):
    u=u/np.linalg.norm(u)
    psi=alpha*u.copy(); psi0=psi.copy()
    d0=psi[Ei]-psi[Ej]; y=np.zeros(E)
    for _ in range(300): y=-(0.5/kappa)*np.exp(y)*d0**2   # static edge balance
    psidot=vkick*u.copy()        # the kick: a velocity along the mode
    ydot=np.zeros(E)
    def Fpsi(psi,y): return -Lw(y,psi)
    def Fy(psi,y):
        d=psi[Ei]-psi[Ej]; return -kappa*y-0.5*np.exp(y)*d*d
    def Vpot(psi,y):
        d=psi[Ei]-psi[Ej]; return 0.5*np.sum(np.exp(y)*d*d)+0.5*kappa*np.sum(y*y)
    dK=0.5*vkick*vkick            # kinetic energy added (u unit norm)
    H0=0.5*psidot@psidot+0.5*ydot@ydot+Vpot(psi,y)
    ap=Fpsi(psi,y); ay=Fy(psi,y)
    webkin=[]; moderet=[]; Hs=[]
    for t in range(steps):
        psi=psi+psidot*dt+0.5*ap*dt*dt
        if live: y=y+ydot*dt+0.5*ay*dt*dt
        ap2=Fpsi(psi,y); ay2=Fy(psi,y)
        psidot=psidot+0.5*(ap+ap2)*dt
        if live: ydot=ydot+0.5*(ay+ay2)*dt
        ap,ay=ap2,ay2
        webkin.append(0.5*ydot@ydot)                      # web in motion (>=0; frozen=0)
        a=u@(psi-psi0); adot=u@psidot                     # mode deviation from background
        moderet.append(0.5*adot*adot+0.5*mu*a*a)          # coherent mode energy
        Hs.append(0.5*psidot@psidot+0.5*ydot@ydot+Vpot(psi,y))
    return np.mean(webkin)/dK, np.mean(moderet)/dK, (max(Hs)-min(Hs))/abs(H0)

print("\n[push] kick each mode; LIVE web response vs FROZEN. (kappa=1, alpha=1.0, vkick=0.3, dt=0.02, 2000 steps)")
print("  web-kinetic = mean(1/2||dy||^2)/kickE  (web driven into motion; frozen=0)")
print("  mode-retain = mean(mode coherent energy)/kickE  (how much stays in the kicked mode)\n")
print("  mu       lambda   Galois   web-kinetic(LIVE)   mode-retain LIVE / FROZEN    H-drift")
seen=set(); rows=[]
for k in range(N):
    mu=round(muvals[k],4)
    if mu in seen: continue
    seen.add(mu); u=U[:,k]
    wk,mr,hd=run(u,1.0,True,mu)
    wk0,mr0,_=run(u,1.0,False,mu)
    gm=gal_for(mu); gms=f"{gm:4.0f}" if gm is not None else "  . "
    rows.append((mu,wk,mr));
    print(f"  {mu:7.4f}  {12-mu:7.4f}   {gms}    {wk:12.5e}     {mr:7.4f} / {mr0:7.4f}      {hd:.1e}")

mus=np.array([r[0] for r in rows]); wks=np.array([r[1] for r in rows]); mrs=np.array([r[2] for r in rows])
print(f"\n[trend] corr(web-kinetic, mu) = {np.corrcoef(mus,wks)[0,1]:+.4f}   "
      f"corr(mode-retain_LIVE, mu) = {np.corrcoef(mus,mrs)[0,1]:+.4f}")
print(f"  uniform mode mu=0 (Galois mass 12): web-kinetic={wks[np.argmin(mus)]:.2e}, retain={mrs[np.argmin(mus)]:.4f}")
print("  => if web-loading is inertia, it rises with mu (registration-rate ordering), NOT with the Galois mass.")
