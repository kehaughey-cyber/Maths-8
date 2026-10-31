# Independent replay of the Amplitude tab of lab/spine_lab.html (amplitudes only). New file; nothing fitted.
# Checks: (1) random exit shrinks the first moment of the vertex marginal by exactly phi/2 per tick; (2) T alone returns after 10 ticks;
# (3) reinjection into that mode every 30 ticks gives 1/(1-(phi/2)^30); (4) sag eps*zeta30/(864 phi^2); (5) arrival times along the order chain.
# Run: py -3 -I -X utf8 -u explore/amplitude_histories_check.py > explore/amplitude_histories_check.out
import numpy as np
from math import sqrt, pi, acos, log
exec(open('explore/lattice_physical_map.py', encoding='utf-8').read().split('c = 299792458.0')[0].replace('print(', '(lambda *a, **k: None)('))
n = len(V); Vn = np.array(V)
DE = [(u, s) for u in range(n) for s in ADJ[u]]; ID = {e: i for i, e in enumerate(DE)}
def near(q):
    i = idx(list(q)); return i
TN = []
for u, s in DE:
    t = near([PHI*V[s][c] - V[u][c] for c in range(4)]); TN.append(ID[(s, t)])
RX = [[ID[(s, x)] for x in ADJ[s]] for u, s in DE]
def step(psi, m):
    out = np.zeros_like(psi)
    for h, v in enumerate(psi):
        if v == 0: continue
        if m < 1: out[TN[h]] += (1 - m)*v
        if m > 0:
            for r in RX[h]: out[r] += v*m/12
    return out
def moment(psi):
    p = np.zeros(n)
    for h, v in enumerate(psi): p[DE[h][1]] += v
    return np.linalg.norm(p @ Vn)
h0 = ID[(0, ADJ[0][0])]
psi = np.zeros(len(DE)); psi[h0] = 1
ms = [moment(psi)]
for _ in range(8): psi = step(psi, 1.0); ms.append(moment(psi))
print('random exit (m = 1): first-moment ratios per tick: ' + ' '.join('%.9f' % (ms[i + 1]/ms[i]) for i in range(8)) + ' ; phi/2 = %.9f' % (PHI/2))
psi = np.zeros(len(DE)); psi[h0] = 1
for _ in range(10): psi = step(psi, 0.0)
print('T only (m = 0): amplitude on the start history after 10 ticks = %.1f' % psi[h0])
q = (PHI/2)**30
psi = np.zeros(len(DE)); psi[h0] = 1
for t in range(1, 121):
    psi = step(psi, 1.0)
    if t % 30 == 0: psi[h0] += 1; print('after reinjection at tick %d: |M|/size = %.9f' % (t, moment(psi)))
print('1/(1-(phi/2)^30) = %.9f' % (1/(1 - q)))
eps = 2*pi - 5*acos(1/3)
print('eps = %.9f ; sag = eps/(1-q)/(864 phi^2) = %.6e rad (floor: 5.686e-5)' % (eps, eps/(1 - q)/(864*PHI**2)))
TP = 1.616255e-35/299792458.0
def arr(j, k): return 5*TP*PHI**k if j == k else TP*(PHI**(max(j, k) + 1) - PHI**(min(j, k) + 1))/(PHI - 1)
for j, k in ((0, 117), (0, 291), (291, 120), (96, 117)):
    print('inject k=%d, seen k=%d: arrival %.4e s = %.4f ticks of the observer order; faster-than-light check: size-difference light time %.4e s' % (j, k, arr(j, k), arr(j, k)/(TP*PHI**k), abs(TP*PHI**k - TP*PHI**j)))
