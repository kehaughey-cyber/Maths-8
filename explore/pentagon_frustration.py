"""
Ground the structure the user named: the pentagonal vertex-figure (5 triangles around a point)
and its out-of-plane frustration deficit, in the actual carrier.
"""
import numpy as np, itertools
from itertools import permutations
phi=(1+5**0.5)/2
V=[]
for i in range(4):
    for s in (1,-1):
        v=[0,0,0,0]; v[i]=s; V.append(v)
for s in itertools.product((0.5,-0.5),repeat=4): V.append(list(s))
base=[0.0,0.5,phi/2,1/(2*phi)]
def par(p):
    p=list(p); seen=[False]*4; k=0
    for i in range(4):
        if seen[i]:continue
        j=i;c=0
        while not seen[j]: seen[j]=True;j=p[j];c+=1
        k+=c-1
    return k%2
for p in [q for q in permutations(range(4)) if par(q)==0]:
    vals=[base[p[i]] for i in range(4)]; nz=[i for i in range(4) if vals[i]!=0]
    for ss in itertools.product((1,-1),repeat=3):
        v=list(vals)
        for k,idx in enumerate(nz): v[idx]=vals[idx]*ss[k]
        V.append(v)
V=np.unique(np.round(np.array(V),9),axis=0); N=len(V)
Adj=(np.abs(V@V.T-phi/2)<1e-6); np.fill_diagonal(Adj,False)

# take one vertex, look at its 12-neighbour shell (the vertex figure)
v0=0; nb=np.where(Adj[v0])[0]
print(f"vertex {v0}: {len(nb)} neighbours (expect 12 = icosahedron)")
sub=Adj[np.ix_(nb,nb)]
deg=sub.sum(1)
nedges=int(sub.sum()//2)
# triangles in the shell, and pentagonal vertex-figures (each shell-vertex's 5 neighbours form a 5-cycle)
tri=sum(int(np.sum(sub[a]&sub[b])) for a in range(12) for b in range(a+1,12) if sub[a,b])//3
print(f"  shell subgraph: {nedges} edges, degree {deg.min()}..{deg.max()} (expect 5-regular), {tri} triangles (expect 20)")
# a shell vertex and its 5 neighbours within the shell = a pentagon of 5 triangles (apex = that vertex)
w=0; ring=np.where(sub[w])[0]
print(f"  shell-vertex {w}: {len(ring)} neighbours in shell (expect 5 = the pentagon)")

# the frustration: 5 tetrahedral-dihedral wedges around the axis fall short of 2pi
a3=np.arccos(1/3)
eps=2*np.pi-5*a3
print(f"\narccos(1/3) = {np.degrees(a3):.4f} deg  (tetrahedral dihedral)")
print(f"5*arccos(1/3) = {np.degrees(5*a3):.4f} deg  -> short of 360 by")
print(f"  epsilon (frustration deficit) = 2pi - 5*arccos(1/3) = {np.degrees(eps):.4f} deg = {eps:.6f} rad")
print(f"per-vertex angle deficit (5 equilateral faces) = 360 - 5*60 = 60 deg = pi/3 = 2 radits")
print(f"\nSame epsilon that set the electron mass: m_e = deficit (2pi/120 - eps/10) in the earlier work.")
