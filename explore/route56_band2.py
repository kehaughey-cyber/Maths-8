"""
Band top of the route56 connection on the refined 600-cell, to higher frequency (continuation of route56_band.py Part S3).
Sparse build + Lanczos (full reorthogonalisation) for the extreme eigenvalues; validated against dense eigvalsh at n=2 (and n=3 if run with 'dense').
Reports E_max (both signs), a = mean edge angle, E_max*a, for operator A/kappa (raw route56 rule, kappa=mean(sum theta)/3) and B (LS control).
No fit.  Usage: py -3 -I -u route56_band2.py [n ...]
"""
import numpy as np, importlib.util, os, sys, time
here=os.path.dirname(os.path.abspath(__file__))
def load(name):
    sp=importlib.util.spec_from_file_location(name,os.path.join(here,name+'.py')); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
sd=load('route56_subdiv'); sig=[sd.sx,sd.sy,sd.sz]

def sparse_ops(n):
    V=sd.carrier(); P,E=sd.subdivide(V,n); N=len(P); Q=np.array([sd.Qmat(p) for p in P]); nbr=[[] for _ in range(N)]
    for a,b in E: nbr[a].append(b); nbr[b].append(a)
    I=[];J=[];BA=[];BB=[];ths=[];kap=0.0
    for i in range(N):
        vs=[];js=[];blkA=[]
        for j in nbr[i]:
            c=float(np.clip(P[i]@P[j],-1,1)); s=np.sqrt(1-c*c); M=Q[j]@Q[i].conj().T
            blkA.append((M-c*sd.I2)/s)
            nn=np.array([(1j/(2*s))*np.trace(sa@M) for sa in sig]).real; vs.append(np.arccos(c)*nn); js.append(j); ths.append(np.arccos(c))
        vs=np.array(vs); W=vs@np.linalg.inv(vs.T@vs); kap+=np.sum(np.linalg.norm(vs,axis=1))/3
        for w,j,ba in zip(W,js,blkA):
            I.append(i);J.append(j);BA.append(ba);BB.append(-1j*sum(w[a]*sig[a] for a in range(3)))
    return N,np.array(I),np.array(J),np.array(BA),np.array(BB),np.mean(ths),kap/N

def make_apply(N,I,J,B,diag):
    def mv(x):
        X=x.reshape(N,2); out=np.zeros((N,2),complex)
        t=np.einsum('eab,eb->ea',B,X[J]); u=np.einsum('eba,eb->ea',B.conj(),X[I])      # D x  and  D^dagger x (on J rows)
        td=np.zeros((N,2),complex); ud=np.zeros((N,2),complex)
        for c in (0,1):
            td[:,c]=np.bincount(I,weights=t[:,c].real,minlength=N)+1j*np.bincount(I,weights=t[:,c].imag,minlength=N)
            ud[:,c]=np.bincount(J,weights=u[:,c].real,minlength=N)+1j*np.bincount(J,weights=u[:,c].imag,minlength=N)
        if diag:                                           # B has -blk on the diagonal block of row i
            sb=np.zeros((N,2,2),complex)
            for a in range(2):
                for b in range(2):
                    sb[:,a,b]=np.bincount(I,weights=B[:,a,b].real,minlength=N)+1j*np.bincount(I,weights=B[:,a,b].imag,minlength=N)
            d1=-np.einsum('nab,nb->na',sb,X); d2=-np.einsum('nba,nb->na',sb.conj(),X)
            td+=d1; ud+=d2
        return ((td+ud)/2).reshape(-1)
    return mv

def lanczos(mv,dim,m=300,seed=0):
    rng=np.random.default_rng(seed); v=rng.normal(size=dim)+1j*rng.normal(size=dim); v/=np.linalg.norm(v)
    Vs=[v]; al=[];be=[]
    for k in range(m):
        w=mv(Vs[-1])
        a=np.vdot(Vs[-1],w).real; al.append(a)
        w=w-a*Vs[-1]-(be[-1]*Vs[-2] if k>0 else 0)
        for u in Vs: w=w-np.vdot(u,w)*u
        for u in Vs: w=w-np.vdot(u,w)*u
        b=np.linalg.norm(w)
        if b<1e-10: break
        be.append(b); Vs.append(w/b)
    T=np.diag(al)+np.diag(be[:len(al)-1],1)+np.diag(be[:len(al)-1],-1); r=np.linalg.eigvalsh(T)
    return r.min(),r.max()

if __name__=="__main__":
    ns=[int(a) for a in sys.argv[1:]] or [2,3,4,5]
    print("n      N        a(rad)    kappa    op       E_min        E_max      E_max*a (max|lam|)   [dense check]")
    for n in ns:
        t0=time.time(); N,I,J,BA,BB,a,kap=sparse_ops(n)
        for name,B,diag,scl in (("A/kappa",BA,False,kap),("B",BB,True,1.0)):
            mv=make_apply(N,I,J,B,diag); dim=2*N
            lo,hi=lanczos(mv,dim); lo/=scl; hi/=scl
            chk=""
            if N<=2800:
                Dm=np.zeros((dim,dim),complex)
                for k in range(dim):
                    e=np.zeros(dim,complex); e[k]=1; Dm[:,k]=mv(e)
                ev=np.linalg.eigvalsh(Dm)/scl; chk=f"dense: {ev.min():.6f} {ev.max():.6f}"
            print(f"{n}  {N:6d}  {a:.5f}  {kap:.5f}  {name:8s} {lo:+.6f}  {hi:+.6f}   {max(abs(lo),abs(hi))*a:.5f}   {chk}   [{time.time()-t0:.0f}s]",flush=True)
