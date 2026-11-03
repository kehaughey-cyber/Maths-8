"""
Independent check of one route-56 claim (spine IV.1, LIVE_WEB_RESULTS section 28): the internal harmonics are Sym^n(2') of the binary icosahedral group 2I,
and n = 7 is the first n for which Sym^n(2') contains the physical spinor 2.  New file (2026-11-03).  Uses only the 120 unit icosians (built from scratch) and
character theory; does not read any route56 output.
Conventions: 2I = the 120 unit icosians in H = R^4 acting on C^2 by the standard SU(2) embedding (this is the rep "2");  "2'" is the Galois conjugate (sqrt5 -> -sqrt5)
of "2".  Character of Sym^n(V) from the eigenvalues e^{+-i t} of a group element: chi_n = sin((n+1)t)/sin(t) (t=0 -> n+1, t=pi -> (-1)^n (n+1)).
Galois conjugation of an icosian with real parts a+b*phi -> a+b*(1-phi) gives rotation angle t' with cos t' = conj(cos t).
Usage: py -3 -I -X utf8 -u explore/spine_route56_check.py
"""
import itertools, math
import numpy as np
phi = (1+5**0.5)/2
# 120 unit icosians as quaternions (a,b,c,d) with coefficients in Z[phi]: represent as pairs (x,y) = x + y*phi, kept exact as sympy would; use floats for geometry, pairs for Galois.
# Generation: 8 of (+-1,0,0,0) perms, 16 of (+-1/2,+-1/2,+-1/2,+-1/2), 96 even permutations of (0,+-1/2,+-phi/2,+-1/(2phi)).
half = (0.5, 0.0)   # (rational part, phi part)
def mul_pair(p, q):   # (a+b phi)(c+d phi) = ac + (ad+bc) phi + bd phi^2, phi^2 = phi + 1
    a,b = p; c,d = q
    return (a*c + b*d, a*d + b*c + b*d)
# elements as 4-tuples of pairs
els = set()
one = (1.0,0.0); zero=(0.0,0.0)
for i in range(4):
    for s in (1,-1):
        v=[zero]*4; v[i]=(float(s),0.0); els.add(tuple(v))
for sg in itertools.product((1,-1),repeat=4):
    els.add(tuple((0.5*s,0.0) for s in sg))
# 1/phi = phi - 1 -> pair (-1,1);  phi/2 -> (0,0.5);  1/(2phi) -> (-0.5,0.5)
base = [zero,(0.5,0.0),(0.0,0.5),(-0.5,0.5)]
def parity(p):
    p=list(p); s=1
    for i in range(len(p)):
        while p[i]!=i:
            j=p[i]; p[i],p[j]=p[j],p[i]; s=-s
    return s
for perm in itertools.permutations(range(4)):
    if parity(perm)!=1: continue
    for sg in itertools.product((1,-1),repeat=3):
        v=[None]*4; k=0
        for pos in range(4):
            val=base[perm[pos]]
            if perm[pos]==0: v[pos]=val
            else: v[pos]=(val[0]*sg[k],val[1]*sg[k]); k+=1
        els.add(tuple(v))
els=sorted(els)
print('group order', len(els))
def num(p): return p[0]+p[1]*phi
def conj(p): return p[0]+p[1]*(1-phi)
# real part a0 = cos t (unit quaternion), rotation angle on C^2: eigenvalues e^{+-i t}
res=[]
for e in els:
    c  = num(e[0]); cc = conj(e[0])
    res.append((c,cc))
def chi(n, c):
    c=max(-1.0,min(1.0,c)); t=math.acos(c)
    if abs(math.sin(t))<1e-9: return (n+1)*(1 if c>0 else (-1)**n)
    return math.sin((n+1)*t)/math.sin(t)
# check the Galois-conjugate parts are legitimate unit-norm characters: |cc|<=1
assert all(abs(cc)<=1+1e-9 for c,cc in res), 'conjugate real part outside [-1,1]'
def mult_in(rep_chars, n, target):    # multiplicity of target (list of chars over group) in Sym^n of rep
    sym=[chi(n,c) for c in rep_chars]
    return sum(s*t for s,t in zip(sym,target))/len(sym)
two  = [2*c for c,_ in res]     # character of 2 (self-conjugate real chars)
twop = [2*cc for _,cc in res]   # character of 2'
# sanity: inner products
ip=lambda a,b: sum(x*y for x,y in zip(a,b))/len(a)
print('<2,2>=%.6f  <2\',2\'>=%.6f  <2,2\'>=%.6f   (expect 1, 1, 0)' % (ip(two,two), ip(twop,twop), ip(two,twop)))
print('\nmultiplicity of the physical spinor 2 in Sym^n(2\'), n = 0..13')
first=None
for n in range(0,14):
    symc=[chi(n,cc) for _,cc in res]
    m = ip(symc,two)
    dim=n+1
    print(f' n={n:2d}  dim {dim:2d}  mult of 2 = {m:.6f}')
    if first is None and abs(m)>1e-6 and n>0: first=n
print('\nfirst n>0 with 2 in Sym^n(2\') :', first, ' (claim: 7)')
# also the trivial rep: lowest n>0 with an invariant
firstinv=None
for n in range(1,14):
    symc=[chi(n,cc) for _,cc in res]
    if abs(ip(symc,[1]*len(res)))>1e-6: firstinv=n; break
print('first n>0 with the trivial rep in Sym^n(2\'):', firstinv, '  (Klein icosahedral invariants: degree 12 in the binary form)')
print('RESULT', 'PASS' if first==7 else 'FAIL')
