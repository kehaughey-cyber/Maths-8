"""
The 28-mode core and the non-smooth low modes of the route56 operator A on the refined 600-cell, classified by the symmetry 2I_L x 2I_R (exact, not tuned).
D_A = [(Q_j Q_i^dag - c)/s] commutes with  (T_g psi)(g p) = Q_g psi(p)   (left multiplication, spinor rotated)  and  (R_g psi)(p g) = psi(p)  (right multiplication)
for every g in the 120 icosians, because the refined point set is invariant under both.  For a subspace S (an eigenspace window) the character is chi_S(g) = tr(V^dag T_g V),
and the multiplicity of irrep rho is (1/120) sum_g chi_S(g) conj(chi_rho(g)).  Irreps: Sym^(d-1) (d = 1..6, chain; 4s = Sym^3), Galois conjugates 2', 3' = 2'^2-1, and 4g = 2 x 2'.
Character orthonormality over the 120 elements is asserted.  Windows: kernel (|lambda| < 1e-8); the lowest nonzero modes (|lambda|/kappa < 0.5, 'non-smooth low'); smooth-comparison levels.
Usage: py -3 -I -u route56_core.py [n ...]
"""
import numpy as np, importlib.util, os, sys
here=os.path.dirname(os.path.abspath(__file__))
def load(name):
    sp=importlib.util.spec_from_file_location(name,os.path.join(here,name+'.py')); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
sd=load('route56_subdiv'); PHI=sd.phi; PSI=1-PHI; sig=[sd.sx,sd.sy,sd.sz]
V=sd.carrier()
def qvec(M): return np.array([(1j*np.trace(s@M)/2).real for s in sig]), (np.trace(M)/2).real
def chars():
    w0=V[:,0]*0
    # w0 of each icosian g (Q(g) = w0 I - i w.sigma): w0 = g[0]
    w0=V[:,0]; al=np.arccos(np.clip(w0,-1,1))
    def sym(d):
        out=np.empty(120)
        for i,a in enumerate(al):
            out[i]=d*(1 if abs(a)<1e-9 else (-1)**(d-1)) if (abs(a)<1e-9 or abs(a-np.pi)<1e-9) else np.sin(d*a)/np.sin(a)
        return out
    conj={0:0.0}
    def sigma(t):                                   # Galois conjugate of t = 2 w0 in Z[phi]
        for a in range(-2,3):
            for b in range(-2,3):
                if abs(t-(a+b*PHI))<1e-9: return a+b*PSI
        raise ValueError(t)
    c2p=np.array([sigma(2*x) for x in w0])
    ch={"1":sym(1),"2":sym(2),"3":sym(3),"4s":sym(4),"5":sym(5),"6":sym(6),"2'":c2p,"3'":c2p**2-1,"4g":sym(2)*c2p}
    return ch
CH=chars()
for a in CH:
    for b in CH:
        ip=np.sum(CH[a]*CH[b])/120
        assert abs(ip-(1 if a==b else 0))<1e-6,(a,b,ip)
print("character table: 9 irreps orthonormal over the 120 icosians (asserted)")
def mult(chi,L): return {k:round(float(np.sum(chi*CH[k])/120),3) for k in CH if abs(np.sum(chi*CH[k])/120)>0.02}

def run(n):
    P,E=sd.subdivide(V,n); N=len(P); Q=np.array([sd.Qmat(p) for p in P]); key={tuple(np.round(p,6)+0.0):i for i,p in enumerate(P)}
    nbr=[[] for _ in range(N)]
    for a,b in E: nbr[a].append(b); nbr[b].append(a)
    D=np.zeros((2*N,2*N),complex); ths=[]
    for i in range(N):
        s_=0
        for j in nbr[i]:
            c=float(np.clip(P[i]@P[j],-1,1)); s=np.sqrt(1-c*c); D[2*i:2*i+2,2*j:2*j+2]=(Q[j]@Q[i].conj().T-c*sd.I2)/s; s_+=np.arccos(c)
        ths.append(s_/3)
    kap=np.mean(ths); w,U=np.linalg.eigh(D); w=w/kap
    def perm(side,g):
        Qg=sd.Qmat(g); idx=np.empty(N,int)
        for i,p in enumerate(P):
            M=(Qg@Q[i]) if side=='L' else (Q[i]@Qg); v,w0_=qvec(M); q=np.array([w0_,*v]); idx[i]=key[tuple(np.round(q,6)+0.0)]
        return idx,Qg
    print(f"\n==== n={n}: N={N}, kappa={kap:.5f}; symmetry check:",end=" ")
    idxL,QgL=perm('L',V[7]); T=np.zeros(2*N,complex)
    Dpsi=lambda psi:D@psi
    rng=np.random.default_rng(0); psi=rng.normal(size=2*N)+1j*rng.normal(size=2*N)
    def TL(idx,Qg,psi):
        X=psi.reshape(N,2); out=np.zeros((N,2),complex); out[idx]=X@Qg.T; return out.reshape(-1)
    print(f"[D,T_g] residual {np.linalg.norm(D@TL(idxL,QgL,psi)-TL(idxL,QgL,D@psi))/np.linalg.norm(D@psi):.1e}",end="; ")
    idxR,_=perm('R',V[7]); XR=lambda psi:(lambda X:(lambda o:(o.__setitem__(idxR,X),o)[1])(np.zeros((N,2),complex)).reshape(-1))(psi.reshape(N,2))
    print(f"[D,R_g] residual {np.linalg.norm(D@XR(psi)-XR(D@psi))/np.linalg.norm(D@psi):.1e}",flush=True)
    perms=[(perm('L',g),perm('R',g)) for g in V]
    def chi(Vs):
        cl=np.zeros(120,complex); cr=np.zeros(120,complex)
        for k,((iL,Qg),(iR,_)) in enumerate(perms):
            for col in range(Vs.shape[1]):
                v=Vs[:,col]; cl[k]+=np.vdot(v,TL(iL,Qg,v)); X=v.reshape(N,2); o=np.zeros((N,2),complex); o[iR]=X; cr[k]+=np.vdot(v,o.reshape(-1))
        return cl.real,cr.real
    wins=[("kernel (|lam|<1e-8)",np.abs(w)<1e-8*max(1,np.abs(w).max()))]
    ae=np.abs(w); wins.append(("0 < |lam| < 0.5 (lattice units/kappa-scaled)",(ae>=1e-8)&(ae<0.5)))
    wins.append(("0.5 <= |lam| < 1.0",(ae>=0.5)&(ae<1.0)))
    wins=[wins[0],("0 < |lam| < 0.02",(ae>=1e-8)&(ae<0.02)),("0.02 <= |lam| < 0.1",(ae>=0.02)&(ae<0.1))]+wins[1:]
    for name,m in wins:
        Vs=U[:,m]; cl,cr=chi(Vs); print(f"  {name}: dim {Vs.shape[1]};  left-2I content {mult(cl,'L')};  right-2I content {mult(cr,'R')}",flush=True)
if __name__=="__main__":
    for n in [int(a) for a in sys.argv[1:]] or [1,2]: run(n)
