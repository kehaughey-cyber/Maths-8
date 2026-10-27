"""
Scale flow of the route56 Clifford connection under geodesic subdivision of the 600-cell.

Refined carrier at frequency n: every one of the 600 tetrahedral cells (a,b,c,d) is cut into the barycentric lattice
(i a + j b + k c + l d)/n, i+j+k+l = n, and every point is projected to the unit 3-sphere.  Edges = nearest neighbours of that
lattice (differences e_x - e_y, 12 per interior point; at n=1 these are exactly the 720 edges of the 600-cell, so n=1 IS the
inherited n=1 shell graph).  The 12 cones / local angles are untouched; the resolution is the only thing that changes.

Operator A (the connection, same rule as route56, per-edge overlap c_ij = p_i.p_j):
      D_ij = ( Q_j Q_i^dag - c_ij I ) / s_ij  =  -i n_ij.sigma        (Hermitian, gamma^2 = -1),   unit weight per edge.
Operator B (control, consistent first-order discretisation of the same teleparallel operator on the same mesh):
      (X_a f)_i = sum_j (M_i^-1 v_ij)_a (f_j - f_i),  M_i = sum_j v_ij v_ij^T,  v_ij = theta_ij n_ij ;   D_B = sym( -i sum_a sigma_a X_a ).
Continuum target: spectrum of the teleparallel Dirac operator on unit S^3, levels  +/-(d-1) and -/+(d+1) by branch, multiplicity d(d+1), d(d-1)
(overall sign = right- vs left-invariant frame).  Reported scale-free: levels are divided by the mean of the six eigenvalues
nearest the 6-fold first level (one calibration), then the rest are verification.
Usage:  py -3 -I -u route56_subdiv.py [n ...]
"""
import sys, itertools, numpy as np
np.set_printoptions(suppress=True, linewidth=170)
phi=(1+5**0.5)/2
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex); I2=np.eye(2,dtype=complex)
def Qmat(w): return w[0]*I2-1j*(w[1]*sx+w[2]*sy+w[3]*sz)

def carrier():
    V=[]
    for i in range(4):
        for s in (1,-1):
            v=[0,0,0,0]; v[i]=s; V.append(v)
    for ss in itertools.product((0.5,-0.5),repeat=4): V.append(list(ss))
    base=[0.0,0.5,phi/2,1/(2*phi)]
    def par(p):
        p=list(p); seen=[False]*4; k=0
        for i in range(4):
            if seen[i]: continue
            j=i; cl=0
            while not seen[j]: seen[j]=True; j=p[j]; cl+=1
            k+=cl-1
        return k%2
    for p in [q for q in itertools.permutations(range(4)) if par(q)==0]:
        vals=[base[p[i]] for i in range(4)]; nz=[i for i in range(4) if vals[i]!=0]
        for ss in itertools.product((1,-1),repeat=3):
            v=list(vals)
            for k,idx in enumerate(nz): v[idx]=vals[idx]*ss[k]
            V.append(v)
    V=np.unique(np.round(np.array(V),9),axis=0); assert len(V)==120
    return V

def cells(V):
    G=V@V.T; adj=np.abs(G-phi/2)<1e-6; N=len(V); out=[]
    for a in range(N):
        na=[x for x in np.where(adj[a])[0] if x>a]
        for b in na:
            for c in [x for x in na if x>b and adj[b,x]]:
                for d in [x for x in na if x>c and adj[b,x] and adj[c,x]]:
                    if adj[c,d]: out.append((a,b,c,d))
    return out

def subdivide(V,n):
    cl=cells(V); assert len(cl)==600
    pts={}; P=[]
    def idx(x):
        k=tuple(np.round(x,7)+0.0)
        if k not in pts: pts[k]=len(P); P.append(x)
        return pts[k]
    latt=[(i,j,k,n-i-j-k) for i in range(n+1) for j in range(n+1-i) for k in range(n+1-i-j)]
    E=set()
    dirs=[tuple((1 if t==x else -1 if t==y else 0) for t in range(4)) for x in range(4) for y in range(4) if x!=y]
    for (a,b,c,d) in cl:
        loc={}
        for l in latt:
            x=(l[0]*V[a]+l[1]*V[b]+l[2]*V[c]+l[3]*V[d])/n; x=x/np.linalg.norm(x); loc[l]=idx(x)
        for l in latt:
            for dv in dirs:
                m=tuple(l[t]+dv[t] for t in range(4))
                if m in loc and loc[l]<loc[m]: E.add((loc[l],loc[m]))
                elif m in loc: E.add((loc[m],loc[l]))
    return np.array(P),sorted(E)

def clusters(ev,tol=1e-7):
    ev=np.sort(ev); out=[]; cur=[ev[0]]
    for x in ev[1:]:
        if x-cur[-1]<tol: cur.append(x)
        else: out.append((np.mean(cur),len(cur),max(cur)-min(cur))); cur=[x]
    out.append((np.mean(cur),len(cur),max(cur)-min(cur))); return out

def run(n):
    V=carrier(); P,E=subdivide(V,n); N=len(P)
    Q=np.array([Qmat(p) for p in P]); nbr=[[] for _ in range(N)]
    for a,b in E: nbr[a].append(b); nbr[b].append(a)
    deg=np.array([len(x) for x in nbr]); onC=np.array([np.min(np.abs(P[i]@V.T-1)) < 1e-9 for i in range(N)])
    print(f"\n==== frequency n={n}:  {N} vertices ({int(onC.sum())} original), {len(E)} edges, degrees {dict(zip(*np.unique(deg,return_counts=True)))}")
    # local geometry: v_ij, balance and anisotropy
    DA=np.zeros((2*N,2*N),complex); DB=np.zeros((2*N,2*N),complex); th_all=[]; bal=[]; ani=[]
    sig=[sx,sy,sz]
    for i in range(N):
        vs=[]; js=[]
        for j in nbr[i]:
            c=float(np.clip(P[i]@P[j],-1,1)); s=np.sqrt(1-c*c); M=Q[j]@Q[i].conj().T
            g=(M-c*I2)/s; DA[2*i:2*i+2,2*j:2*j+2]=g
            nn=np.array([ (1j/(2*s))*np.trace(sa@M) for sa in sig]).real; vs.append(np.arccos(c)*nn); js.append(j); th_all.append(np.arccos(c))
        vs=np.array(vs); Mi=vs.T@vs; ev=np.linalg.eigvalsh(Mi); ani.append(ev[-1]/ev[0]); bal.append(np.linalg.norm(np.sum(vs/np.linalg.norm(vs,axis=1)[:,None],axis=0)))
        W=vs@np.linalg.inv(Mi)                       # rows: M^-1 v_ij
        for w,j in zip(W,js):
            blk=-1j*sum(w[a]*sig[a] for a in range(3))
            DB[2*i:2*i+2,2*j:2*j+2]+=blk; DB[2*i:2*i+2,2*i:2*i+2]-=blk
    th_all=np.array(th_all); ani=np.array(ani); bal=np.array(bal)
    print(f"  edge angle: min {np.degrees(th_all.min()):.4f}  max {np.degrees(th_all.max()):.4f}  mean {np.degrees(th_all.mean()):.4f} deg;  hermiticity A {np.abs(DA-DA.conj().T).max():.1e}")
    print(f"  local anisotropy lambda_max/lambda_min of sum v v^T: original vertices max {ani[onC].max():.4f} ; new vertices max {(ani[~onC].max() if (~onC).any() else float('nan')):.4f}")
    print(f"  neighbour-direction imbalance |sum n_ij|: original max {bal[onC].max():.3e} ; new max {(bal[~onC].max() if (~onC).any() else float('nan')):.3e}")
    DBs=(DB+DB.conj().T)/2
    kap=np.mean([sum(np.arccos(np.clip(P[i]@P[j],-1,1)) for j in nbr[i])/3 for i in range(N)])
    print(f"  geometric scale kappa = mean_i (sum_j theta_ij)/3 = {kap:.6f}  (A ~ kappa*B on an isotropic mesh; no fit)")
    H=smooth_basis(P,Kmax)
    for name,D,sc in (("A/kappa (route56 rule)",DA,kap),("B (LS control)",DBs,1.0)):
        ev=np.linalg.eigvalsh(D)/sc
        print(f"  -- {name}: kernel dim {int(np.sum(np.abs(ev)<1e-6*np.abs(ev).max()/max(sc,1e-9)*1))}; full-spectrum lowest |levels| (continuum units): "+
              "  ".join(f"{c[0]:+.4f}(x{c[1]})" for c in sorted(clusters(ev),key=lambda c:abs(c[0]))[:10]))
        print(f"     spectral count: #|lambda|<0.5: {int(np.sum(np.abs(ev)<0.5))}   #|lambda|<1.0: {int(np.sum(np.abs(ev)<1.0))}   (of {len(ev)}; smooth continuum has 2 below 0.5, 2+6=8 below 1.5)")
        for K in (3,4,Kmax):
            Hk=H[K]; Dk=D/sc
            C=Hk.conj().T@Dk@Hk; C=(C+C.conj().T)/2
            leak=np.linalg.norm(Dk@Hk-Hk@C,2)
            r=np.linalg.eigvalsh(C)
            cl=clusters(r,tol=2e-3*max(1,0))
            print(f"     smooth subspace d<={K} (dim {Hk.shape[1]}): leakage ||(1-P)D P|| = {leak:.4f};  Ritz levels:")
            print("       "+"  ".join(f"{c[0]:+.3f}(x{c[1]})" for c in cl if abs(c[0])<6))
    return

def smooth_basis(P,K):
    """Sampled SU(2) matrix elements D^{(d)}_{mm'}(p), d=1..K, times C^2; orthonormalised; returns dict K -> (2N x dim) isometry."""
    N=len(P); Q=np.array([Qmat(p) for p in P]); cols=[]; out={}
    for d in range(1,K+1):
        k=d-1
        # symmetric-power rep via isometry V onto the symmetric subspace of (C^2)^{(x)k}
        if k==0: Dp=np.ones((N,1,1),complex)
        else:
            dim=2**k; Sym=[]
            for r in range(k+1):
                v=np.zeros(dim,complex)
                for idx in range(dim):
                    if bin(idx).count('1')==r: v[idx]=1
                Sym.append(v/np.linalg.norm(v))
            Vs=np.array(Sym).T
            Dp=np.empty((N,k+1,k+1),complex)
            for i in range(N):
                T=Q[i]
                for _ in range(k-1): T=np.kron(T,Q[i])
                Dp[i]=Vs.conj().T@T@Vs
        for m in range(d):
            for mp in range(d):
                f=Dp[:,m,mp]
                for s in range(2):
                    v=np.zeros(2*N,complex); v[s::2]=f; cols.append(v)
        B=np.array(cols).T
        U,S,_=np.linalg.svd(B,full_matrices=False); keep=S>1e-8*S[0]
        out[d]=U[:,keep]
    return out

Kmax=6

if __name__=="__main__":
    for n in ([int(a) for a in sys.argv[1:]] or [1,2]): run(n)
