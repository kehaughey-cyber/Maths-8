"""
Clean test of the 28-core on the exact icosian structure (the 4D icosian ring I = Z[phi]-span of the 120 units, with Galois conjugation sigma: phi -> psi = 1-phi).
Point sets are unions of full 2I_L x 2I_R orbits of icosians of prescribed reduced norm ('Hecke shells'):
   X_1 = units (120 vertices of the 600-cell),  X_r5 = u+v for adjacent units (|q|^2 = 2+phi, norm 5: edge midpoints, expected 720),
   X_3 = u+v+w for a mutually adjacent triple (|q|^2 = 3 phi^2: face centres, expected 1200),  X_2 = sum of a mutually adjacent quadruple (|q|^2 = 2 phi^4: cell centres, expected 600).
All arithmetic is exact: a coordinate (a + b phi)/2 is stored as the integer pair (a,b); the product is integer and divided by 2 (asserted even).
Transport replacing Q_j Q_i^dag:  the quaternion ratio t_ij = q_j q_i^{-1} (exact in Q(sqrt5), non-unit), whose unit part is Q of the NORMALISED points; gamma_ij = (Q_j Q_i^dag - c I)/s with the
physical unit vectors p = q/|q|  (phi-branch), and the same expression with the internal unit vectors p' = sigma(q)/|sigma(q)| (psi-branch).  Edge rule (invariant under both groups; it depends only on
the pair's invariants): x ~ y iff angle(x,y) <= 1.06 * min(nn(x), nn(y)) with nn(.) the point's own nearest-neighbour angle in the set.  The rule reproduces the geodesic n=2 graph on X_1 u X_r5 (checked: edge count).
Reports per set: size, degrees by orbit, kernel of D^phi and of D^psi (dimension, overlap of the two kernel subspaces), and the right-2I irreps of the D^phi kernel.   Usage: py -3 -I -u route56_hecke.py
"""
import numpy as np, importlib.util, os, sys, itertools, io, contextlib
here=os.path.dirname(os.path.abspath(__file__))
def load(name):
    sp=importlib.util.spec_from_file_location(name,os.path.join(here,name+'.py')); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
sd=load('route56_subdiv')
with contextlib.redirect_stdout(io.StringIO()): core=load('route56_core')
CH=core.CH; PHI=sd.phi; PSI=1-PHI; V=sd.carrier()
def exact_pairs(v):
    for (a,b) in ((0,0),(2,0),(-2,0),(1,0),(-1,0),(0,1),(0,-1),(-1,1),(1,-1)):
        if abs(v-(a+b*PHI)/2)<1e-9: return (a,b)
    raise ValueError(v)
U=np.array([[exact_pairs(x) for x in v] for v in V],dtype=np.int64)      # (120,4,2)
def pm(x,y):                                                              # (a1+b1 phi)(a2+b2 phi) -> (A,B)
    return np.stack([x[...,0]*y[...,0]+x[...,1]*y[...,1], x[...,0]*y[...,1]+x[...,1]*y[...,0]+x[...,1]*y[...,1]],-1)
def qmul(p,q):                                                            # p,q (...,4,2) doubled coords; result doubled coords
    def c(i,j): return pm(p[...,i,:],q[...,j,:])
    r=[c(0,0)-c(1,1)-c(2,2)-c(3,3), c(0,1)+c(1,0)+c(2,3)-c(3,2), c(0,2)-c(1,3)+c(2,0)+c(3,1), c(0,3)+c(1,2)-c(2,1)+c(3,0)]
    r=np.stack(r,-2); assert np.all(r%2==0); return r//2
def phys(q): return (q[...,0]+q[...,1]*PHI)/2
def perp(q): return (q[...,0]+q[...,1]*PSI)/2
assert np.allclose(phys(U),V)
G=V@V.T; adj=np.abs(G-PHI/2)<1e-6
def orbit(seed):
    L=qmul(U[:,None],seed[None,None]).reshape(-1,4,2)                      # left multiples
    out={}
    for r in range(120):
        R=qmul(L,U[r][None]); 
        for q in R: out[q.tobytes()]=q
    return np.array(list(out.values()))
a=[0];nb=np.where(adj[0])[0]; b=nb[0]; cm=[x for x in nb if adj[b,x]]; c=cm[0]; d=[x for x in cm if x!=c and adj[c,x] and adj[b,x]][0]
Eseed=U[0]+U[b]; Fseed=U[0]+U[b]+U[c]; Cseed=U[0]+U[b]+U[c]+U[d]
SH={"V":U,"E":orbit(Eseed),"F":orbit(Fseed),"C":orbit(Cseed)}
for k,v in SH.items(): print(f"shell {k}: {len(v)} icosians, |q|^2 (phys) = {np.unique(np.round((phys(v)**2).sum(-1),6))}, |sigma q|^2 = {np.unique(np.round((perp(v)**2).sum(-1),6))}")
def build(names,tol=1.06):
    q=np.vstack([SH[n] for n in names]); lab=np.concatenate([[i]*len(SH[n]) for i,n in enumerate(names)])
    pp=phys(q); pp=pp/np.linalg.norm(pp,axis=-1,keepdims=True); pq=perp(q); pq=pq/np.linalg.norm(pq,axis=-1,keepdims=True)
    Gm=pp@pp.T; np.fill_diagonal(Gm,-2); N=len(q)
    ang=np.arccos(np.clip(Gm,-1,1)); nn=ang.min(1)
    # rule uses the PHYSICAL angles; q and -q: antipodal pairs are far, no issue
    adjm=(ang<=tol*np.minimum(nn[:,None],nn[None,:])+1e-12)|(ang<=tol*np.minimum(nn[:,None],nn[None,:])+1e-12)
    adjm=(ang<=tol*nn[:,None]+1e-12)|(ang<=tol*nn[None,:]+1e-12); np.fill_diagonal(adjm,False)
    return q,lab,pp,pq,adjm
def op(P,adjm,kap_scale=False):
    N=len(P); Q=np.array([sd.Qmat(p) for p in P]); D=np.zeros((2*N,2*N),complex)
    for i in range(N):
        for j in np.where(adjm[i])[0]:
            c=float(np.clip(P[i]@P[j],-1,1)); s=np.sqrt(max(1-c*c,1e-30)); D[2*i:2*i+2,2*j:2*j+2]=(Q[j]@Q[i].conj().T-c*sd.I2)/s
    return (D+D.conj().T)/2
def run(names):
    q,lab,pp,pq,adjm=build(names); N=len(q); deg=adjm.sum(1)
    print(f"\n==== set {'+'.join(names)}: N={N}, edges {int(adjm.sum()//2)}; degrees by shell: "+", ".join(f"{n}:{sorted(set(deg[lab==i]))}" for i,n in enumerate(names)),flush=True)
    Dp=op(pp,adjm); Dq=op(pq,adjm); wp,Up=np.linalg.eigh(Dp); wq,Uq=np.linalg.eigh(Dq)
    kp=np.abs(wp)<1e-7; kq=np.abs(wq)<1e-7; Kp=Up[:,kp]; Kq=Uq[:,kq]
    ov=np.linalg.norm(Kp.conj().T@Kq)**2/max(Kp.shape[1],1) if Kp.shape[1] and Kq.shape[1] else float('nan')
    print(f"   kernel dim: phi-branch {Kp.shape[1]}, psi-branch {Kq.shape[1]}; overlap tr(P_phi P_psi)/dim = {ov:.4f}; lowest nonzero |lambda|: phi {np.abs(wp[~kp]).min():.5f}, psi {np.abs(wq[~kq]).min():.5f}",flush=True)
    key={q[i].tobytes():i for i in range(N)}
    chr_=np.zeros(120)
    for k in range(120):
        R=qmul(q,U[k][None]); idx=np.array([key[r.tobytes()] for r in R]); X=Kp.reshape(N,2,-1); out=np.zeros_like(X); out[idx]=X; chr_[k]=np.vdot(Kp,out.reshape(2*N,-1)).real
    cont={k:round(float(np.sum(chr_*CH[k])/120),2) for k in CH if abs(np.sum(chr_*CH[k])/120)>0.05}
    print(f"   right-2I content of the phi-branch kernel: {cont}",flush=True)
if __name__=="__main__":
    sets=[s.split('+') for s in sys.argv[1:]] or [["V"],["V","E"],["V","C"],["V","F"],["V","E","C"],["V","E","F"],["V","E","F","C"]]
    for s in sets: run(s)
