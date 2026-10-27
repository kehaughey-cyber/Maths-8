"""
Scale questions on the icosahedral quasicrystal (continuation of route56_quasi2.py).
  (1) phi^n self-similarity of the point set: is phi^n * Lambda a subset of Lambda?  (n = 1,2,3)
  (2) DOUBLER SCAN: packet energy / ||D psi|| over |k| up to the lattice scale, along the 5-,3-,2-fold axes and random directions, vs the
      simple-cubic control whose doublers (k = pi on an axis) are known.  A state near E=0 at finite k shows ||D psi||/||psi|| at the
      k=0 envelope floor sqrt(3/2)/w instead of ~|E|.
  (3) DEVIATION SCALING: delta(w,k) = 1 - E/|k| fitted as  alpha/w^2 + beta k^2 + gamma k^4  (alpha: packet envelope; beta k^2: lattice).
  (4) NOISE-FLOOR ARITHMETIC: the wavelength (in lattice spacings, and in phi^3 inflation steps) at which the lattice deviation falls below a floor.
No fit to any measured value.  Usage: py -3 -I -u route56_scale.py
"""
import numpy as np, importlib.util, os
here=os.path.dirname(os.path.abspath(__file__))
def load(name):
    sp=importlib.util.spec_from_file_location(name,os.path.join(here,name+'.py')); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
rq=load('route56_quasi'); q2=load('route56_quasi2')
PHI=rq.PHI; SIG=rq.SIG
rng=np.random.default_rng(11)

def apply_fast(I,J,C,psi,N,B):
    m0=psi[J,0]-(psi[I,0] if B else 0); m1=psi[J,1]-(psi[I,1] if B else 0)
    cx,cy,cz=C[:,0],C[:,1],C[:,2]
    o0=-1j*(cz*m0+(cx-1j*cy)*m1); o1=-1j*((cx+1j*cy)*m0-cz*m1)
    out=np.zeros((N,2),complex)
    for c,o in ((0,o0),(1,o1)):
        out[:,c]=np.bincount(I,weights=o.real,minlength=N)+1j*np.bincount(I,weights=o.imag,minlength=N)
    return out

def prep(pts,cutoff,wid):
    R=4.2*wid; keep=np.linalg.norm(pts,axis=1)<=R; P=pts[keep]; N=len(P)
    I,J,CA,CB,kap,deg=q2.edges(P,cutoff); core=np.linalg.norm(P,axis=1)<2*wid
    return dict(P=P,N=N,I=I,J=J,CA=CA,CB=CB,ka=kap[core].mean(),deg=deg[core].mean(),g=np.exp(-np.sum(P**2,axis=1)/(2*wid**2)),w=wid)

def packet(S,opname,k,h=1):
    sk=sum(k[a]*SIG[a] for a in range(3)); w_,U=np.linalg.eigh(sk); u=U[:,h]
    psi=(S['g']*np.exp(1j*S['P']@k))[:,None]*u[None,:]
    C,B,sc=(S['CA'],False,S['ka']) if opname=='A' else (S['CB'],True,1.0)
    D=apply_fast(S['I'],S['J'],C,psi,S['N'],B)/sc; nn=np.vdot(psi,psi).real
    E=np.vdot(psi,D).real/nn; return E,np.linalg.norm(D)/np.sqrt(nn)

if __name__=="__main__":
    big=rq.quasilattice(6); big=np.vstack([np.zeros((1,3)),big])           # include the n=0 vertex (origin) that scale.py drops
    # ---- (1) self-similarity
    print(f"(1) phi^n self-similarity of the point set (K=6, {len(big)} points incl. origin)")
    for rmax in (1.0,1.5,2.0,2.5):
        small=big[np.linalg.norm(big,axis=1)<rmax]
        row=[]
        for n in (1,2,3):
            y=small*PHI**n; ok=sum(1 for p in y if np.min(np.linalg.norm(big-p,axis=1))<1e-6); row.append(ok/len(small))
        print(f"    |x|<{rmax} (N={len(small)}): fraction with phi x, phi^2 x, phi^3 x in Lambda = {row[0]:.4f}, {row[1]:.4f}, {row[2]:.4f}   (phi^3 x reaches |.|<{rmax*PHI**3:.2f} of {np.max(np.linalg.norm(big,axis=1)):.2f} available)")
    # ---- (2) doubler scan
    g=np.arange(-8,9); Cc=np.array(np.meshgrid(g,g,g,indexing='ij')).reshape(3,-1).T.astype(float)
    ico_axes={"5-fold":np.array([0,1,PHI]),"3-fold":np.array([1,1,1]),"2-fold":np.array([1,0,0])}
    def scan(label,pts,cutoff,wid,kmax,dk,dirs,ops=("B",)):
        S=prep(pts,cutoff,wid); r0=np.sqrt(1.5)/wid
        print(f"\n(2) doubler scan: {label}: N={S['N']}, w={wid}, interior degree {S['deg']:.1f}, envelope floor ||D psi|| at k=0 -> {r0:.3f}")
        ks=np.arange(dk,kmax+1e-9,dk)
        for op in ops:
            for name,d in dirs:
                d=d/np.linalg.norm(d); Es=[];Ns=[]
                for kk in ks:
                    E,nm=packet(S,op,kk*d); Es.append(E); Ns.append(nm)
                Es=np.array(Es); Ns=np.array(Ns)
                # candidate doublers: |k|>1, local minima of ||D psi|| below 1.3 r0
                cand=[(ks[i],Ns[i],Es[i]) for i in range(1,len(ks)-1) if ks[i]>1.0 and Ns[i]<Ns[i-1] and Ns[i]<=Ns[i+1] and Ns[i]<1.3*r0]
                lin=Es[(ks>=0.3)&(ks<=0.8)]/ks[(ks>=0.3)&(ks<=0.8)]
                sc=[ks[i] for i in range(1,len(ks)) if ks[i]>0.5 and Es[i-1]*Es[i]<0]
                print(f"    {op} {name:8s}: sign changes of E(k) (k>0.5) at {['%.2f'%x for x in sc]};",end=" ")
                print(f"    {op} {name:8s}: E/k at 0.3..0.8 ~ {lin.mean():.3f};  min ||D psi|| for k>1: {Ns[ks>1].min():.3f} at k={ks[ks>1][np.argmin(Ns[ks>1])]:.2f};  "
                      f"candidate zero-energy states (||D psi|| < 1.3 floor): "+(", ".join(f"k={a:.2f} (|D psi|={b:.2f}, E={c:+.2f})" for a,b,c in cand) if cand else "none"))
    cube_dirs=[("x axis",np.array([1.,0,0])),("(110)",np.array([1.,1,0])),("(111)",np.array([1.,1,1]))]
    scan("CONTROL simple cubic (doublers at k=pi on an axis, pi*sqrt2 along (110), pi*sqrt3 along (111))",Cc[np.linalg.norm(Cc,axis=1)<=7.6],1.05,1.8,5.6,0.08,cube_dirs)
    qd=list(ico_axes.items())+[(f"rand{i}",rng.normal(size=3)) for i in range(4)]
    scan("icosahedral quasicrystal",big,0.78,1.8,9.0,0.12,qd,ops=("B","A"))
    # ---- (3) deviation fit
    print("\n(3) deviation scaling delta = 1 - E/|k|  fitted as alpha/w^2 + beta k^2 + gamma k^4 (mean of 4 directions, helicity +)")
    wids=[1.5,1.8,2.4]; ks=[0.3,0.5,0.7,1.0,1.4]; dirs=[v/np.linalg.norm(v) for v in rng.normal(size=(4,3))]
    for op in ("B","A"):
        rows=[];y=[]
        for wid in wids:
            S=prep(big,0.78,wid)
            for kk in ks:
                d=np.mean([1-packet(S,op,kk*dd)[0]/kk for dd in dirs]); rows.append([1/wid**2,kk**2,kk**4]); y.append(d)
        rows=np.array(rows); y=np.array(y); coef,res,_,_=np.linalg.lstsq(rows,y,rcond=None); fit=rows@coef
        print(f"    {op}: alpha={coef[0]:.4f}  beta={coef[1]:.4f}  gamma={coef[2]:.4f};  max |fit - data| = {np.max(np.abs(fit-y)):.4f} over {len(y)} points (delta range {y.min():.4f}..{y.max():.4f})")
        if op=="B": cB=coef; Sref=S
    # lattice spacing: mean edge length in the core
    a_mean=3*Sref['ka']/Sref['deg']
    print(f"    mean edge length a = 3*kappa/degree = {a_mean:.4f} (lattice units);  beta_hat = beta*a^2 = {cB[1]*a_mean**2:.4f}")
    bh=cB[1]*a_mean**2
    # ---- (4) noise-floor arithmetic
    print("\n(4) lattice deviation floor: delta_lat = beta_hat (k a)^2  =>  k a = sqrt(floor/beta_hat);  wavelength lambda/a = 2 pi/(k a);  phi^3-inflation steps above the lattice scale n = ln(lambda/a)/ln(phi^3)")
    print("     floor            k*a            lambda/a         phi^3 steps   phi steps")
    for fl in (1e-2,1e-4,1e-6,1e-9,1e-12,1e-16):
        x=np.sqrt(fl/bh); lam=2*np.pi/x
        print(f"     {fl:8.0e}   {x:12.3e}   {lam:14.3e}   {np.log(lam)/np.log(PHI**3):10.2f}   {np.log(lam)/np.log(PHI):9.2f}")
    print(f"     reference: 1 decade of length = {np.log(10)/np.log(PHI**3):.3f} phi^3 steps = {np.log(10)/np.log(PHI):.3f} phi steps")
