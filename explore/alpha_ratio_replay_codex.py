from pathlib import Path
import hashlib
import mpmath as m
m.mp.dps=60
t=m.mpf('137.036'); p=(1+m.sqrt(5))/2; q=p/2
e=2*m.pi-5*m.acos(m.mpf(1)/3)
s={'one':m.mpf(1),'tick':m.mpf(1)/30,'radit':m.mpf(1)/12,'deficit_cycles':e/(2*m.pi),'gap':1-q,'K':m.log(p)/15,'lean_cycles':m.asin(1/m.sqrt(3))/(2*m.pi),'kappa':(m.pi/3)**2,'G_nat':2*p**2*m.pi**2/9,'delta_nat':4*m.pi/15-m.asin(1/m.sqrt(3)),'gain':1/(1-q**30)}
print('Codex, ChatGPT Work Mode. 60-digit arithmetic; target-directed search, not derivation.')
print('Target inverse',t,'ratio',m.nstr(1/t,60))
print('Grammar (a/b)*q**n; ordered named constants, integer n=-60..60. No continuous parameter solved. No derived coupling law assumed.')
r=[]
for an,a in s.items():
 for bn,b in s.items():
  for n in range(-60,61):
   x=a/b*q**n; r.append((abs(x/t-1),an,bn,n,x))
r.sort()
print('Expressions',len(r),'hits rounding inverse to 137.036',sum(abs(z[4]-t)<m.mpf('.0005') for z in r))
for err,a,b,n,x in r[:12]: print(a,b,n,'inverse',m.nstr(x,60),'ratio',m.nstr(1/x,60),'relative_inverse_error',m.nstr(x/t-1,60))
for name,x in [('375*acos(1/3)/(7*ln(phi))',375*m.acos(m.mpf(1)/3)/(7*m.log(p))),('125*kappa',125*(m.pi/3)**2),('144-7',m.mpf(137)),('exp(2pi)/4',m.exp(2*m.pi)/4),('128pi/3',128*m.pi/3)]: print(name,'inverse',m.nstr(x,60),'ratio',m.nstr(1/x,60),'relative_inverse_error',m.nstr(x/t-1,60))
root=Path(__file__).resolve().parents[1]
for f in ['floor/M6_SPINE_2026-10-19.md','floor/M5_SPINE_10-9-26.md','explore/alpha_candidates.py','explore/alpha_families.py','explore/alpha_ratio_replay_codex.py']: print(f,hashlib.sha256((root/f).read_bytes()).hexdigest())
