/-
  CONTAINER 07 -- ORDINAL (RELATIONAL) DYNAMICS . rung 4.5, rests on 02 and 04

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  The elemental object is a DIRECTED WALK on the relational line: change (Container02)
  taking a signed step (Container04's +1 / -1) per tick, the ticks ordered by the integer
  order (Container04). Positions are INTEGERS (relational counts -- which registration),
  never spatial coordinates. DERIVED: succession is 04's total order over container-02
  changes; the step directions are distinct; net & RATE compute (rate = a ratio = the
  RATIONALS, by cross-multiply); a balanced walk returns to the counterpoint. POSTULATE:
  observer-relativity of the origin. OWED: metric dynamics -- needs the bridge.
-/

import Container02.RegistrationEvent
import Container04.Integers

namespace Container07
open Container04

/-! ### succession -- change ordered by the integer order -- step 7.1, DERIVED -/

/-- The tick order is total: every pair of moments is comparable (before/after). This IS
    04's total order (Nat.le on the tick indices). -/
theorem tick_order_total (i j : Nat) : i ≤ j ∨ j ≤ i := Nat.le_total i j

/-- Each entry of a history is a container-02 CHANGE (the registration event stabilising).
    The dependency on rung 2, in the kernel -- the elemental dynamics seat IS the change. -/
theorem history_entry_is_change :
    Container00.isDistinction Container02.afterEvent = true :=
  Container02.event_stabilises

/-! ### the directed step -- each change carries a direction -- step 7.2, DERIVED -/

/-- A step is one of 04's two directions. That they are DISTINCT (+1 is not -1) is exactly
    Container04.plus_one_ne_minus_one -- the directed step inherits 04's orientation. -/
theorem step_directions_distinct : ¬ IntEquiv onePair negOnePair :=
  Container04.plus_one_ne_minus_one

/-! ### the walk, its net, and its RATE -- step 7.3, DERIVED (headline) -/

/-- A walk: a sequence of signed steps. The net is their sum under 04's addPair, folded
    from the counterpoint zeroPair -- change accumulated, still purely integer. -/
def netWalk (w : List IntPair) : IntPair := w.foldl addPair zeroPair

/-- The sample walk: +1 +1 -1 +1 -1 +1, net +2 over 6 ticks (from the derivation). -/
def walk : List IntPair := [onePair, onePair, negOnePair, onePair, negOnePair, onePair]
/-- Its double-speed half-cousin: +1 +1 -1, net +1 over 3 ticks -- the SAME rate 1/3. -/
def half : List IntPair := [onePair, onePair, negOnePair]
/-- A balanced cycle: +1 +1 -1 -1, net 0 -- it returns. -/
def cycle : List IntPair := [onePair, onePair, negOnePair, negOnePair]

/-- The net of the sample walk is +2 (= ofNatPair 2). Change accumulates to a definite
    integer displacement. -/
theorem walk_net : IntEquiv (netWalk walk) (ofNatPair 2) := by unfold IntEquiv; decide

/-- Scale an integer displacement by a count: k copies of the walk go k times as far. -/
def scaleN (p : IntPair) (k : Nat) : IntPair := (p.1 * k, p.2 * k)

/-- The RATE of a walk: its net displacement per tick, as a (net, ticks) pair. -/
def rate (w : List IntPair) : IntPair × Nat := (netWalk w, w.length)

/-- Two rates are equal iff they are equal as RATIOS -- cross-MULTIPLY, exactly mirroring
    how integers compare by cross-ADD (Container04.IntEquiv). This is the rationals. -/
def rateEquiv (r s : IntPair × Nat) : Prop := IntEquiv (scaleN r.1 s.2) (scaleN s.1 r.2)

/-- THE HEADLINE: the walk and its double-speed cousin have the SAME rate. Rate is a genuine
    ratio (1/3 here), not a raw pair -- dynamics-as-rate forces the RATIONALS, the
    number-object between the integers (04) and the reals (which arrive only at the bridge),
    and it is still pre-geometric (a ratio of counts). -/
theorem rate_is_a_ratio : rateEquiv (rate walk) (rate half) := by unfold rateEquiv IntEquiv; decide

/-! ### cyclic return -- the first periodic dynamics -- step 7.4, DERIVED -/

/-- A balanced walk RETURNS: its net is the counterpoint (net ~ 0). The first dynamics that
    closes -- the seat of cycles and clocks. (The SPECIFIC period 12 is OWED to container 02
    / the clocks, not forced here.) -/
theorem cycle_returns : IntEquiv (netWalk cycle) zeroPair := by unfold IntEquiv; decide

-- POSTULATE (step 7.5, NOT proven): the walk records STEPS (differences), so its absolute
-- ORIGIN is not part of it -- a different observer (container 02's observer/observed
-- co-emergence) sees the same walk from a shifted origin. All observers agree on the
-- DIRECTION of each step and the NET displacement between ticks (the invariants); the
-- absolute position they need not. The seed of RELATIVITY -- Galilean, ordinal, pre-metric.
--
-- OWED (step 7.6, NOT built): metric dynamics -- velocity as distance/time, acceleration, a
-- continuous trajectory. Needs POSITIONS IN A METRIC SPACE = the geometric-balance bridge.
-- Comes AFTER the bridge (Kevin's ladder: ordinal -> bridge -> metric). Deferred, not smuggled.

#print axioms tick_order_total
#print axioms history_entry_is_change
#print axioms step_directions_distinct
#print axioms walk_net
#print axioms rate_is_a_ratio
#print axioms cycle_returns

end Container07
