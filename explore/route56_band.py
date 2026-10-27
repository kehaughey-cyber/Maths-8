"""
Bandwidth and dispersion cap of the route56 lattices (measurement requested 2026-10-27).
Units: hbar = c = 1; E in 1/length, a = mean edge length of each lattice (S^3: arc angle on the unit sphere).
  Part S3 : full spectra of the refined 600-cell (geodesic subdivision n=1,2,3): E_max = max|lambda|, E_max*a, ratio to the first smooth level (1), top-of-band density.
  Part Q  : icosahedral quasicrystal ball: E_max from full spectra (N=700, 1300) with the interior weight of the top eigenvectors (bulk vs surface),
            and the dispersion |d|(k) from wave packets (w=2.4): |d|_est = sqrt(||D psi||^2 - 1.5/w^2) (the linear-dispersion envelope floor).
  Part C  : simple-cubic control (E = |sin k| a^-1 exactly): validates the packet estimator; its band top has m* = E_max.
For each: v_g(k) = d|d|/dk, v_g(0), max v_g, the band-top (E_top, k_top), and the band-top effective mass m* = 1/(-d^2|d|/dk^2) with ratio m*/E_top.
Usage: py -3 -I -u route56_band.py
"""
import numpy as np, importlib.util, os, sys
here=os.path.dirname(os.path.abspath(__file__))
def load(name):
    sp=importlib.util.spec_from_file_location(name,os.path.join(here,name+'.py')); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
sd=load('route56_subdiv'); rq=load('route56_quasi'); q2=load('route56_quasi2'); sc=load('route56_scale')
PHI=sd.phi; sig=[sd.sx,sd.sy,sd.sz]

def s3_ops(n):
    V=sd.carrier(); P,E=sd.subdivide(V,n); N=len(P); Q=np.array([sd.Qmat(p) for p in P]); nbr=[[] for _ in range(N)]
    for a,b in E: nbr[a].append(b); nbr[b].append(a)
    DA=np.zeros((2*N,2*N),complex); DB=np.zeros((2*N,2*N),complex); ths=[]
    for i in range(N):
        vs=[];js=[]
        for j in nbr[i]:
            c=float(np.clip(P[i]@P[j],-1,1)); s=np.sqrt(1-c*c); M=Q[j]@Q[i].conj().T
            DA[2*i:2*i+2,2*j:2*j+2]=(M-c*sd.I2)/s
            nn=np.array([(1j/(2*s))*np.trace(sa@M) for sa in sig]).real; vs.append(np.arccos(c)*nn); js.append(j); ths.append(np.arccos(c))
        vs=np.array(vs); W=vs@np.linalg.inv(vs.T@vs)
        for w,j in zip(W,js):
            blk=-1j*sum(w[a]*sig[a] for a in range(3)); DB[2*i:2*i+2,2*j:2*j+2]+=blk; DB[2*i:2*i+2,2*i:2*i+2]-=blk
    thbar=np.mean(ths); kap=np.mean([sum(np.arccos(np.clip(P[i]@P[j],-1,1)) for j in nbr[i])/3 for i in range(N)])
    return N,DA,(DB+DB.conj().T)/2,thbar,kap

print("PART S3  full spectra of the geodesically refined 600-cell (unit S^3; a = mean edge angle)")
print("   n    N     a(rad)   kappa     op       E_max      E_max*a   E_min(nonzero)  #|lam|>0.9 E_max")
for n in (1,2,3):
    N,DA,DB,a,kap=s3_ops(n)
    for name,D,scl in (("A/kappa",DA,kap),("B",DB,1.0)):
        ev=np.linalg.eigvalsh(D)/scl; ae=np.abs(ev); em=ae.max()
        print(f"   {n}  {N:5d}  {a:.5f}  {kap:.5f}  {name:8s} {em:9.4f}  {em*a:8.4f}  {ae[ae>1e-6].min():.5f}        {int(np.sum(ae>0.9*em))}")

print("\nPART Q  icosahedral quasicrystal, full spectra of balls (a = 3*kappa/degree)")
big=np.vstack([np.zeros((1,3)),rq.quasilattice(6)])
for nn in (700,1300):
    pts=rq.crop_ball(big,nn); R=np.max(np.linalg.norm(pts,axis=1))
    DA,DB,ani,bal,kap,deg=rq.build(pts,0.78); interior=np.linalg.norm(pts,axis=1)<0.6*R
    ka=kap[interior].mean(); a=3*ka/deg[interior].mean()
    for name,D,scl in (("A/kappa",DA,ka),("B",DB,1.0)):
        w,U=np.linalg.eigh(D); w=w/scl; i0=np.argmax(np.abs(w)); top=np.argsort(-np.abs(w))[:6]
        wt=[np.sum(np.abs(U[:,t].reshape(-1,2))**2,axis=1)[interior].sum() for t in top]
        print(f"   N={nn} {name:8s} a={a:.4f}: E_max={np.abs(w).max():.4f}  E_max*a={np.abs(w).max()*a:.4f};  interior weight (r<0.6R, volume fraction 0.22) of the six top eigenvectors: "+", ".join(f"{x:.2f}" for x in wt))

def dispersion(label,pts,cutoff,wid,dirs,ks,ops):
    S=sc.prep(pts,cutoff,wid); floor2=1.5/wid**2; a=3*S['ka']/S['deg']
    print(f"\n   {label}: N={S['N']}, w={wid}, a={a:.4f}, interior degree {S['deg']:.1f}, envelope floor^2 = {floor2:.3f}")
    out={}
    for op in ops:
        for name,d in dirs:
            d=d/np.linalg.norm(d); dd=[]
            for kk in ks:
                E,nm=sc.packet(S,op,kk*d); dd.append(np.sqrt(max(nm**2-floor2,0)))
            dd=np.array(dd); vg=np.gradient(dd,ks); ip=int(np.argmax(dd))
            lo=slice(0,4); v0=np.polyfit(ks[lo],dd[lo],1)[0]
            # band top: quadratic fit in a window around the peak
            sl=slice(max(ip-3,0),min(ip+4,len(ks))); c=np.polyfit(ks[sl],dd[sl],2)
            ktop=-c[1]/(2*c[0]) if c[0]<0 else ks[ip]; Etop=np.polyval(c,ktop) if c[0]<0 else dd[ip]
            mstar=1/(-2*c[0]) if c[0]<0 else float('nan')
            print(f"      {op} {name:8s}: v_g(k->0) = {v0:.3f};  max v_g = {vg.max():.3f};  band top |d|_max = {Etop:.3f} ({Etop*a:.3f}/a) at k = {ktop:.2f} (k a = {ktop*a:.2f});  m* = {mstar:.3f}, m*/E_top = {mstar/Etop:.3f};  |d| at k=1,2,4,6: "+", ".join(f"{dd[np.argmin(abs(ks-x))]:.2f}" for x in (1,2,4,6)))
    return a

print("\nPART C  simple-cubic control (analytic: E = |sin k|, a=1, E_max=1 at k=pi/2, v_g(0)=1, m*=1, m*/E_top=1); packet estimator on the x axis and (111):")
g=np.arange(-12,13); Cc=np.array(np.meshgrid(g,g,g,indexing='ij')).reshape(3,-1).T.astype(float)
Cc=Cc[np.linalg.norm(Cc,axis=1)<=10.2]
ks=np.arange(0.1,3.2,0.1)
dispersion("cubic",Cc,1.05,2.4,[("x axis",np.array([1.,0,0])),("(111)",np.array([1.,1,1]))],ks,("B",))
print("      analytic along x: |sin k| at k=1,2 =",f"{np.sin(1):.3f}, {np.sin(2):.3f}","; along (111) |d| = sqrt(3)|sin(k/sqrt3)|, at k=1,2 =",f"{np.sqrt(3)*np.sin(1/np.sqrt(3)):.3f}, {np.sqrt(3)*np.sin(2/np.sqrt(3)):.3f}")

print("\nPART Q (continued)  dispersion |d|(k) of the quasicrystal from packets")
rng=np.random.default_rng(5)
qd=[("5-fold",np.array([0,1,PHI])),("3-fold",np.array([1,1,1.])),("2-fold",np.array([1,0,0.])),("rand0",rng.normal(size=3)),("rand1",rng.normal(size=3))]
dispersion("icosahedral quasicrystal",big,0.78,2.4,qd,np.arange(0.2,10.01,0.2),("B","A"))
