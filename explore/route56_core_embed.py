"""
Where does the 28-core live on the refined carrier?  (1) n=2: weight of the kernel (dim 30) on the 120 original vertices vs the 720 edge midpoints.
(2) Embed the n=1 kernel (28 vectors on the 120-vertex graph) into the refined point set by zero padding and report ||D_A v|| / ||v|| (D_A raw, unit weights) for each, with
the residual's distribution over point types (original / new).   Usage: py -3 -I -u route56_core_embed.py
"""
import numpy as np, importlib.util, os
here=os.path.dirname(os.path.abspath(__file__))
def load(name):
    sp=importlib.util.spec_from_file_location(name,os.path.join(here,name+'.py')); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
sd=load('route56_subdiv'); V=sd.carrier()
def op(n):
    P,E=sd.subdivide(V,n); N=len(P); Q=np.array([sd.Qmat(p) for p in P]); D=np.zeros((2*N,2*N),complex)
    for a,b in E:
        for i,j in ((a,b),(b,a)):
            c=float(np.clip(P[i]@P[j],-1,1)); s=np.sqrt(1-c*c); D[2*i:2*i+2,2*j:2*j+2]=(Q[j]@Q[i].conj().T-sd.I2*c)/s
    onC=np.array([np.min(np.abs(P[i]@V.T-1))<1e-9 for i in range(N)]); return P,D,onC
P1,D1,on1=op(1); w,U=np.linalg.eigh(D1); K1=U[:,np.abs(w)<1e-8]; print(f"n=1: kernel dim {K1.shape[1]}")
for n in (2,3):
    P,D,on=op(n); N=len(P); ww,UU=np.linalg.eigh(D); Kn=UU[:,np.abs(ww)<1e-8]
    wt=np.sum(np.abs(Kn.reshape(N,2,-1))**2,axis=(1,2)); print(f"\nn={n}: N={N}, kernel dim {Kn.shape[1]}; kernel weight on the 120 original vertices {wt[on].sum()/wt.sum():.4f} (uniform would be {on.sum()/N:.4f})")
    # embed n=1 kernel: map original vertices by coordinates
    key={tuple(np.round(p,6)+0.0):i for i,p in enumerate(P)}; idx=np.array([key[tuple(np.round(p,6)+0.0)] for p in P1])
    res=[]; frac=[]
    for c in range(K1.shape[1]):
        v=np.zeros(2*N,complex); X=K1[:,c].reshape(-1,2)
        for k,ii in enumerate(idx): v[2*ii:2*ii+2]=X[k]
        r=D@v; res.append(np.linalg.norm(r)/np.linalg.norm(v)); rr=np.sum(np.abs(r.reshape(N,2))**2,axis=1); frac.append(rr[on].sum()/rr.sum())
    print(f"   zero-padded n=1 kernel vectors: ||D v||/||v|| min {min(res):.4f} mean {np.mean(res):.4f} max {max(res):.4f};  share of the residual on original vertices {np.mean(frac):.4f}")
    PK=Kn@Kn.conj().T; ov=[]
    for c in range(K1.shape[1]):
        v=np.zeros(2*N,complex); X=K1[:,c].reshape(-1,2)
        for k,ii in enumerate(idx): v[2*ii:2*ii+2]=X[k]
        ov.append(np.linalg.norm(PK@v)/np.linalg.norm(v))
    print(f"   overlap of the zero-padded vectors with the n={n} kernel (1 = inside): min {min(ov):.4f} mean {np.mean(ov):.4f}")
