"""Check that the invariant edge rule of route56_hecke.py on V u E reproduces the geodesic n=2 subdivision graph (same 840 points, same edge set)."""
import numpy as np, importlib.util, os
here=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('h',os.path.join(here,'route56_hecke.py')); h=importlib.util.module_from_spec(sp); sp.loader.exec_module(h)
q,lab,pp,pq,adjm=h.build(["V","E"]); P,E=h.sd.subdivide(h.V,2)
key={tuple(np.round(p,6)+0.0):i for i,p in enumerate(P)}; idx=np.array([key[tuple(np.round(p,6)+0.0)] for p in pp])
S1={tuple(sorted((idx[i],idx[j]))) for i,j in zip(*np.where(np.triu(adjm,1)))}; S2={tuple(sorted(e)) for e in E}
print(f"points: {len(pp)} vs {len(P)}, all matched: {len(set(idx))==len(P)}; edges: rule {len(S1)}, geodesic {len(S2)}, common {len(S1&S2)}")
