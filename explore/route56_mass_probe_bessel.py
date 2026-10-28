"""Compare the velocity renormalisation measured in route56_mass_probe.out, v(r)^2 = 1 + (E^2-|k|^2)/|k|^2 at |k| = 0.01, with the S^3 average 2 J_1(r)/r of cos(k'.y) over the unit 3-sphere (the large-design limit of mean_u cos(k'.sigma u))."""
from mpmath import mp, besselj, sqrt
mp.dps=20
meas={1:(-2.256372e-5,-2.2535342e-5),2:(-6.8168595e-5,-6.7478341e-5),3:(-9.0081188e-5,-9.7877759e-5)}
for r,(a,b) in meas.items():
    for x in (a,b):
        v2=1+x/1e-4; print(f"r={r}: measured v^2 = {v2:.5f}, v = {float(sqrt(v2)):.5f};  2 J1(r)/r = {float(2*besselj(1,r)/r):.5f}")
