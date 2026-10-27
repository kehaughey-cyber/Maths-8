"""
Wave-packet (Rayleigh) test of the route56 connection on the icosahedral quasicrystal.  Replaces the failed ball-DOS test (route56_quasi.py):
that test counted modes of an open ball, where truncated stencils at the surface generate O(1) boundary modes (the simple-cubic control itself
gave 42 zero modes and slope 0.08, so the pipeline was not a valid Weyl counter).  Here no eigen-decomposition and no boundary: a Gaussian wave
packet psi = g(x) e^{ik.x} u_pm(k) (u = helicity spinor of sigma.k^) is placed at the centre of a ball whose edge lies > 4 widths away, and
    E = <psi|D|psi>/<psi|psi>,   resid = ||(D - E) psi|| / ||psi||
are compared with the continuum Weyl value E = pm|k| (operator D = -i sigma.grad).  Operators as in route56_quasi.py: A = -i n.sigma unit weight
(scale kappa = mean over centre-region vertices of sum_j r_ij/3), B = least-squares consistent (scale 1).
CONTROL: simple-cubic lattice, where B is the central difference and E(k) = pm |(sin kx, sin ky, sin kz)| exactly (up to the envelope).
No fit.  Usage: py -3 -I -u route56_quasi2.py
"""
import numpy as np
import importlib.util, os
spec=importlib.util.spec_from_file_location('rq',os.path.join(os.path.dirname(os.path.abspath(__file__)),'route56_quasi.py')); rq=importlib.util.module_from_spec(spec); spec.loader.exec_module(rq)
SIG=rq.SIG
rng=np.random.default_rng(3)

def edges(pts,cutoff):
    N=len(pts); cell=np.floor(pts/cutoff).astype(int); d={}
    for i,c in enumerate(map(tuple,cell)): d.setdefault(c,[]).append(i)
    I=[];J=[];CA=[];CB=[];kap=np.zeros(N); deg=np.zeros(N,int)
    offs=[(a,b,c) for a in (-1,0,1) for b in (-1,0,1) for c in (-1,0,1)]
    for i in range(N):
        cand=[]; ci=tuple(cell[i])
        for o in offs: cand+=d.get((ci[0]+o[0],ci[1]+o[1],ci[2]+o[2]),[])
        cand=np.array([j for j in cand if j!=i]); v=pts[cand]-pts[i]; r=np.linalg.norm(v,axis=1); m=r<=cutoff
        cand=cand[m]; v=v[m]; r=r[m]; deg[i]=len(cand)
        if len(cand)<3: continue
        n=v/r[:,None]; W=v@np.linalg.pinv(v.T@v); kap[i]=r.sum()/3
        I+= [i]*len(cand); J+=list(cand); CA.append(n); CB.append(W)
    return np.array(I),np.array(J),np.vstack(CA),np.vstack(CB),kap,deg

def apply(I,J,C,psi,N,B):
    # (D psi)_i = sum_j -i (c_ij . sigma) (psi_j - B psi_i)
    out=np.zeros((N,2),complex)
    for a in range(3):
        t=np.einsum('ab,eb->ea',SIG[a],psi[J]-(psi[I] if B else 0))*(-1j*C[:,a])[:,None]
        np.add.at(out,I,t)
    return out

def packet_test(pts,cutoff,label,expected,wid=1.8,kmags=(0.4,0.7,1.0,1.4),ndir=8,extra_dirs=()):
    R=4.2*wid; keep=np.linalg.norm(pts,axis=1)<=R; P=pts[keep]; N=len(P)
    I,J,CA,CB,kap,deg=edges(P,cutoff)
    core=np.linalg.norm(P,axis=1)<2*wid; ka=kap[core].mean()
    print(f"\n== {label}: N={N}, packet width {wid}, ball radius {R:.2f}, interior degree {deg[core].mean():.2f}, kappa(core)={ka:.4f}")
    g=np.exp(-np.sum(P**2,axis=1)/(2*wid**2))
    dirs=[v/np.linalg.norm(v) for v in rng.normal(size=(ndir,3))]+list(extra_dirs)
    print("   |k|     op   <E/E_cont> over dirs & helicity (mean, min, max)   mean resid/|k|   (E_cont = continuum Weyl value; cubic: lattice dispersion)")
    for km in kmags:
        for opname,C,B,sc in (("A/kap",CA,False,ka),("B",CB,True,1.0)):
            rat=[];res=[]
            for kd in dirs:
                k=km*kd; sk=sum(k[a]*SIG[a] for a in range(3)); w,U=np.linalg.eigh(sk)
                for h in (0,1):
                    u=U[:,h]; psi=(g*np.exp(1j*P@k))[:,None]*u[None,:]
                    D=apply(I,J,C,psi,N,B)/sc
                    nn=np.vdot(psi,psi).real; E=np.vdot(psi,D).real/nn; r=np.linalg.norm(D-E*psi)/np.sqrt(nn)
                    Ec=expected(k)*(1 if h==1 else -1); rat.append(E/Ec); res.append(r/km)
            print(f"   {km:4.2f}   {opname:5s} {np.mean(rat):.4f}  {np.min(rat):.4f}  {np.max(rat):.4f}      {np.mean(res):.3f}")

if __name__=="__main__":
    g=np.arange(-8,9); C=np.array(np.meshgrid(g,g,g,indexing='ij')).reshape(3,-1).T.astype(float)
    packet_test(C,1.05,"CONTROL simple cubic (exact central-difference dispersion)",lambda k:np.linalg.norm(np.sin(k)))
    big=rq.quasilattice(6); R0=1.8*4.2
    print(f"\nquasilattice K=6: {len(big)} vertices; max |x| of available points {np.max(np.linalg.norm(big,axis=1)):.2f} (need >= {R0:.1f})")
    packet_test(big,0.78,"icosahedral quasicrystal (continuum E = |k|)",lambda k:np.linalg.norm(k))
    packet_test(big,0.78,"icosahedral quasicrystal, wider packet 2.4",lambda k:np.linalg.norm(k),wid=2.4,kmags=(0.4,0.7,1.0))
