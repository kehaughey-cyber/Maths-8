/-
  CONTAINER 08 -- METRIC DYNAMICS . rests on 05 (the bridge) and 07 (the ordinal walk)

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  The ladder closes: ordinal dynamics (07) -> the geometric-balance bridge (05) -> METRIC
  dynamics (here). The bridge gives the walk a Euclidean metric, and dim >= 2 lets it TURN,
  so the metric splits 07's single rate into SPEED (path/time) and VELOCITY (net/time, a
  vector). DERIVED, Mathlib-free: straight => |net|^2 = T^2; a turn => |net|^2 < T^2 and
  |net|^2 = 2 (distance sqrt2, THE REALS); a reversal nets zero; the triangle inequality
  |net|^2 <= T^2. Imports Container07 (its rate is the velocity; the metric time = its ticks).
-/

import Container07.Dynamics

namespace Container08

/-! ### exact 2-D metric on the integer lattice -- no Mathlib -/

abbrev Vec := Int × Int

def vadd (u v : Vec) : Vec := (u.1 + v.1, u.2 + v.2)
def dot (u v : Vec) : Int := u.1 * v.1 + u.2 * v.2
def normSq (u : Vec) : Int := dot u u
def netV (w : List Vec) : Vec := w.foldl vadd (0, 0)

/-- Sample trajectories (unit steps; 2-D, because the bridge gives dim >= 2 to turn in). -/
def straight : List Vec := [(1, 0), (1, 0), (1, 0)]   -- net (3,0)
def turned   : List Vec := [(1, 0), (0, 1)]           -- net (1,1)
def reversed : List Vec := [(1, 0), (-1, 0)]          -- net (0,0)
def elbow    : List Vec := [(1, 0), (1, 0), (0, 1), (0, 1)]  -- net (2,2)

/-! ### displacement vs path -- speed vs velocity -- steps 8.2-8.4, DERIVED -/

/-- A STRAIGHT walk: displacement equals path (|net|^2 = T^2). Velocity = speed. -/
theorem straight_disp_eq_path : normSq (netV straight) = 3 * 3 := by decide

/-- A TURNED walk: displacement is strictly less than path (|net|^2 < T^2). The turn
    shortens the net -- velocity < speed. -/
theorem turned_disp_lt_path : normSq (netV turned) < 2 * 2 := by decide

/-- THE REALS: the turned walk's squared displacement is 2, a non-square -- so the distance
    is sqrt 2, irrational. Integers (04) -> rationals (07) -> REALS (here), via the metric. -/
theorem turned_normSq_two : normSq (netV turned) = 2 := by decide

/-- A REVERSED walk moves yet nets nothing: |net|^2 = 0 while path = 2. Full speed, zero
    velocity -- motion without progress, which the ordinal count could not see. -/
theorem reversed_nets_zero : normSq (netV reversed) = 0 := by decide

/-- The triangle inequality (velocity <= speed): displacement^2 <= path^2, on each sample. -/
theorem straight_triangle : normSq (netV straight) ≤ 3 * 3 := by decide
theorem turned_triangle   : normSq (netV turned)   ≤ 2 * 2 := by decide
theorem reversed_triangle : normSq (netV reversed) ≤ 2 * 2 := by decide
theorem elbow_triangle    : normSq (netV elbow)    ≤ 4 * 4 := by decide

/-! ### the tie to ordinal dynamics -- 07's rate is the velocity -- step 8.3 -/

/-- The metric TIME of a trajectory is 07's tick count: the metric reuses the ordinal walk's
    succession. (Container07.rate returns (net, ticks); its ticks is the time here.) 07's
    rate is thereby revealed as the velocity magnitude; the metric adds speed and direction. -/
theorem metric_time_is_ordinal_ticks : (Container07.rate Container07.walk).2 = 6 := by decide

/-! ### DISCRETE ACCELERATION -- the second difference Delta^2 -- step 8.7, DERIVED -/

def vsub (u v : Vec) : Vec := (u.1 - v.1, u.2 - v.2)
/-- Discrete acceleration: the list of second differences of position, equivalently the first
    differences of velocity -- a_t = v_{t+1} - v_t = s_{t+1} - s_t (the change of step). -/
def accel (w : List Vec) : List Vec := (w.zip w.tail).map (fun p => vsub p.2 p.1)

/-- A STRAIGHT walk (constant step) has ZERO acceleration everywhere -- uniform motion, the
    discrete Newton's-first-law, exactly 8.4's 'equality iff straight' seen locally. -/
theorem straight_zero_accel : accel straight = [(0, 0), (0, 0)] := by decide

/-- A TURN has nonzero acceleration: the step changes, so a = s2 - s1 = (-1, 1) != 0. -/
theorem turned_accel : accel turned = [(-1, 1)] := by decide

/-- A REVERSAL is the MAXIMAL single acceleration: a full flip of the unit step, |a|^2 = 4. -/
theorem reversed_accel_magsq_four : (accel reversed).map normSq = [4] := by decide

/-- Acceleration LOCALIZES the bend: the elbow's accelerations are 0, 2, 0 -- zero on the two
    straight segments, nonzero only at the corner. -/
theorem elbow_accel_localizes : (accel elbow).map normSq = [0, 2, 0] := by decide

/-- The accelerations TELESCOPE: their sum is the net change of velocity, v_last - v_first
    (= last step - first step). Shown on the elbow: sum = (0,1) - (1,0) = (-1, 1). -/
theorem elbow_accel_telescopes : netV (accel elbow) = vsub (0, 1) (1, 0) := by decide

-- So discrete acceleration is a first-class, exact, integer-lattice quantity -- the buildable
-- increment. The CONTINUOUS layer stays emergent (8.6), never axiomatized.

-- POSTULATE (8.5): metric motion is the Euclidean IMAGE of ordinal dynamics across the
-- bridge (05); the substrate stays relational -- do not reify the trajectory. The ladder
-- Kevin drew is now complete: ordinal (07) -> bridge (05) -> metric (08).
--
-- OWED (8.6): the DISCRETE half of acceleration is built above (8.7); what remains is a
-- substrate COMMITMENT -- the CONTINUOUS layer (smooth trajectory, derivatives, curvature) is
-- NOT a floor rung. The substrate is QUANTIZED (discrete registrations/ticks/lattice; the
-- reals entered at 8.2 only as algebraic distances like sqrt2, not a continuum), so continuity
-- is EMERGENT -- a large-N limit of the discrete dynamics, to fall out later IF needed.

#print axioms straight_disp_eq_path
#print axioms turned_disp_lt_path
#print axioms turned_normSq_two
#print axioms reversed_nets_zero
#print axioms elbow_triangle
#print axioms metric_time_is_ordinal_ticks
#print axioms straight_zero_accel
#print axioms turned_accel
#print axioms reversed_accel_magsq_four
#print axioms elbow_accel_localizes
#print axioms elbow_accel_telescopes

end Container08
