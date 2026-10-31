# Search for numbers in [128,137] among the rung ratios, tower-step differences, and lattice counts. New file; raw values; no fitting.
# Run: py -3 -I -X utf8 -u explore/ratios_128_137.py > explore/ratios_128_137.out
import math, itertools
from math import sqrt, log, pi
PHI=(1+sqrt(5))/2; hc=1.973269804e-7
R=[('tau Compton',hc/1776.93e6),('proton Compton',hc/938.27208816e6),('nucleon r_p',0.84075e-15),('muon Compton',hc/105.6583755e6),('12C charge radius',2.4702e-15),
('electron Compton',hc/0.51099895e6),('C5+ 1s radius',5.29177210903e-11/6),('Bohr radius',5.29177210903e-11),('diamond C-C',3.56683e-10*sqrt(3)/4),('diamond a',3.56683e-10),('1 g radius',4.0808074e-3),('Hubble c/H0 (recalled)',4.4e26)]
lo,hi=128,137.5
print('Pairwise size ratios (larger/smaller) in [%g,%g]:'%(lo,hi))
for (a,x),(b,y) in itertools.combinations(R,2):
    r=max(x,y)/min(x,y)
    if lo<=r<=hi: print('  %s / %s = %.6f'%((a,b) if x>y else (b,a)+( ) if False else ((a,b) if x>y else (b,a))+(r,)))
print('Tower-step differences log_phi(R_j/R_i) in [%g,%g]:'%(lo,hi))
for (a,x),(b,y) in itertools.combinations(R,2):
    d=abs(log(x/y))/log(PHI)
    if lo<=d<=hi: print('  %s -> %s: %.4f steps'%((a,b) if x<y else (b,a))+(d,)) if False else print('  %s <-> %s: %.4f steps'%(a,b,d))
print('Orders (k from l_P, edge anchor) in the range: none of the table is listed unless within range; k values:')
lP=1.616255e-35
for n,x in R:
    k=log(x/lP)/log(PHI)
    if lo<=k<=hi: print('  %s k=%.4f'%(n,k))
print('Lattice counts and combinations of them in the range:')
cands={'120+12':132,'120+12+... 12 neighbours + 120 vertices':132,'600/ (something)':None,'720/5.4':None,'1440/ 10.5':None}
cnt={'vertices':120,'edges':720,'cells':600,'faces':1200,'directed edges':1440,'neighbours':12,'ten-cycles':144,'clock length':30,'clocks':4,'diameter':5}
for n,v in cnt.items():
    if lo<=v<=hi: print('  %s = %d'%(n,v))
print('  direct combinations (sums, differences, products, ratios of two counts) in range:')
for (a,x),(b,y) in itertools.combinations(cnt.items(),2):
    for op,v in (('+',x+y),('-',abs(x-y)),('*',x*y),('/',max(x,y)/min(x,y))):
        if lo<=v<=hi: print('    %s %s %s = %.4f'%(a,op,b,v))
print('Powers of phi and 2pi-type numbers near the range: phi^10 = %.4f, phi^10+... ; 2^7=128; 4pi*... ; 12^2 - ... = 144; 60*pi/... '%(PHI**10))
alpha_inv=137.035999177
print('1/alpha (CODATA 2022) = %.9f'%alpha_inv)
a0=5.29177210903e-11; lc=hc/0.51099895e6
print('Bohr radius / electron reduced Compton length = %.6f (identity: = 1/alpha)'%(a0/lc))
print('phi^k closest to 1/alpha: k=%.4f ; 1/alpha / phi^10 = %.5f ; 1/alpha / phi^10 residual'%(log(alpha_inv)/log(PHI),alpha_inv/PHI**10))
