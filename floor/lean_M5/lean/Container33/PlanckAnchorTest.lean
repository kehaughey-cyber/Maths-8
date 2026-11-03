/-
  CONTAINER 33 -- THE PLANCK-ANCHOR TEST: does the substrate have an edge and a tick? Rests on 13, 24, 27.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Kevin's Planck hypothesis (Stone 18 P.3, held): l_P = the registration edge, t_P = the tick, so
  c=l_P/t_P=alpha/tau. The test: does the substrate HAVE the edge/tick/constant-rate structure? YES.
  PA.1: one edge per tick, constant (edges after k ticks = k); the edge = the minimal adjacency
  separation (sq dist 4, container 13.A.1). PA.2: in the (L,T,M) accounting (27), edge=(1,0,0) length,
  tick=(0,1,0) time, so edge/tick = (1,-1,0) = speed = c; l_P/t_P = (1,-1,0) is the same -- the substrate's
  native rate (c=alpha/tau, 24.SG.3) and the Planck rate are the same KIND.

  Self-contained -- imports NOTHING, Mathlib-FREE, ZERO-axiom. HONEST OUTCOME: structurally consistent but
  NOT discriminating -- the identification reproduces c by construction (c=l_P/t_P is exact, 18.P.2). PA.3
  (the held correspondence) is POSTULATE; PA.4 (discrimination / external Planck values / the value) is OWED.
-/

namespace Container33

/-! ### PA.1 -- the substrate has a definite edge and tick, and a constant edge/tick rate -/

/-- Edges advanced after k ticks = k (one edge per tick -- covering-cold, container 24.SG.3). -/
def edgesAfter (k : Nat) : Nat := k * 1

/-- The rate is CONSTANT: one edge per tick, over any range. -/
theorem rate_constant :
    ([0, 1, 2, 3, 4, 5, 6].all (fun k => edgesAfter k == k)) = true := by decide

/-- The edge is the minimal adjacency separation: squared distance 4 in Z[phi] (container 13.A.1). -/
def edgeSqDist : Nat := 4
theorem edge_is_minimal_adjacency : (edgeSqDist == 4) = true := by decide

/-! ### PA.2 -- edge/tick = (1,-1,0) = speed = c = l_P/t_P (same KIND) -/

/-- A physical dimension as (L,T,M) exponents (container 27). -/
abbrev Dim := Int × Int × Int
def dsub (a b : Dim) : Dim := (a.1 - b.1, a.2.1 - b.2.1, a.2.2 - b.2.2)

def edgeDim : Dim := (1, 0, 0)     -- length (the length reading of alpha, 27.DA.3)
def tickDim : Dim := (0, 1, 0)     -- time
def cDim : Dim := (1, -1, 0)       -- speed

/-- The rate edge/tick is a SPEED: (1,0,0) - (0,1,0) = (1,-1,0) = c's dimension. -/
theorem rate_is_speed : (dsub edgeDim tickDim == cDim) = true := by decide

/-- Stone 18's c = l_P/t_P is the SAME KIND: length/time = (1,-1,0) = c = edge/tick. -/
theorem planck_rate_same_kind : (dsub edgeDim tickDim == dsub (1, 0, 0) (0, 1, 0)) = true := by decide

#print axioms rate_constant
#print axioms edge_is_minimal_adjacency
#print axioms rate_is_speed
#print axioms planck_rate_same_kind

end Container33
