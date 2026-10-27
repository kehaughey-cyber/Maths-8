"""
Spin lift along a great circle of the carrier: the decagon g^k (g an icosian at 36 deg from 1, order 10 in 2I).  Per hop the transport is Q_{k+1} Q_k^dag = Q_g, an SO(3) rotation by 2*36 = 72 deg.
Reports Q_g^k for k = 5 (a 2 pi rotation of space) and k = 10 (4 pi), and the arc length / rotation angle.   Usage: py -3 -I -u route56_holonomy.py
"""
import numpy as np, importlib.util, os
here=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('s',os.path.join(here,'route56_subdiv.py')); sd=importlib.util.module_from_spec(sp); sp.loader.exec_module(sd)
V=sd.carrier(); j=[k for k in range(120) if abs(V[k,0]-sd.phi/2)<1e-9]
g=V[j[0]]
Qg=sd.Qmat(g); M=np.eye(2,dtype=complex); print(f"edge arc = {np.degrees(np.arccos(g[0])):.4f} deg, SO(3) rotation per hop = {2*np.degrees(np.arccos(g[0])):.4f} deg")
for k in range(1,11):
    M=M@Qg; ang=2*np.degrees(np.arccos(np.clip(np.trace(M).real/2,-1,1)))
    print(f"  after {k:2d} hops: arc {36*k:3d} deg, rotation angle {72*k:3d} deg, spin-lift matrix = {'+I' if np.allclose(M,np.eye(2),atol=1e-7) else '-I' if np.allclose(M,-np.eye(2),atol=1e-7) else 'neither'}, tr/2 = {np.trace(M).real/2:+.6f}")
