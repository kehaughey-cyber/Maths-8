"""
Test the closed formula for the whole spectrum of the Clifford connection on any class-shell graph:
      level(rho -> sigma) = ( c' * lambda_rho  -  lambda_sigma ) / s' ,   multiplicity d_rho * d_sigma
over channels  sigma in (rho (x) tau),  tau = transport rep (2 or 2'),  lambda_X = |C| chi_X(h_c)/d_X  (class-sum eigenvalue
of the shell graph on irrep X),  c' = c (tau=2) or sigma(c) (tau=2'),  s' = sqrt(1-c'^2).
Also: (i) zero channels beyond the core; (ii) antipodal shells  c <-> -c :  level_{-c} = eps_sigma * level_c .
"""
import os
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'route56_shells.py')).read().split("shells=[")[0]
exec(src)
shells=[("n=1 order10",phi/2),("n=2 order5 ",1/(2*phi)),("order6     ",0.5),("order4     ",0.0),
        ("order3     ",-0.5),("n=3 order10",-1/(2*phi)),("n=4 order5 ",-phi/2)]
neg=gidx[key(-I2)]
eps={n:chi[n][neg]/dd[n] for n in names}

def formula_levels(c,tname):
    cT=c if tname=='2' else sg(c); sT=np.sqrt(1-cT*cT)
    Adj=(np.abs(G-c)<1e-6); deg=int(Adj.sum(1)[0]); h=int(np.argmin(np.abs(trQ/2-c)))
    lam={n:deg*chi[n][h]/dd[n] for n in names}
    ch={}; lst=[]
    for r in names:
        for m,s2 in decomp(chi[r]*chitau[tname]):
            v=(cT*lam[r]-lam[s2])/sT; ch[(r,s2)]=v; lst+= [v]*(m*dd[r]*dd[s2])
    return np.sort(np.array(lst)),ch

print("formula  vs  numerics  (max |sorted difference| over all 240 levels)")
chd={}
for label,c in shells:
    for tname,T in (('2',Q),("2'",Qp)):
        cT=c if tname=='2' else sg(c)
        Adj=(np.abs(G-c)<1e-6).astype(float); np.fill_diagonal(Adj,0)
        D,_=build_D(T,Adj,cT); ev=np.sort(np.linalg.eigvalsh(D))
        fl,ch=formula_levels(c,tname); chd[(label,tname)]=ch
        zeros=sorted([k for k,v in ch.items() if abs(v)<1e-9])
        print(f"  {label} c={c:+.4f} tau={tname:2s}:  len {len(fl)}  max diff {np.abs(ev-fl).max():.1e}   zero channels: {['%s->%s'%k for k in zeros]}")

print("\nantipodal shells (c, -c):  level_{-c}(rho->sigma) = eps_sigma * level_c(rho->sigma)  [eps = fold parity of the left irrep]")
for a,b in (("n=1 order10","n=4 order5 "),("n=2 order5 ","n=3 order10"),("order6     ","order3     ")):
    bad=0; tot=0
    for k,v in chd[(a,'2')].items():
        w=chd[(b,'2')][k]; e=eps[k[1]]; tot+=1; bad+= abs(w-e*v)>1e-9
    print(f"  {a.strip()} <-> {b.strip()}: {tot-bad}/{tot} channels satisfy it")
