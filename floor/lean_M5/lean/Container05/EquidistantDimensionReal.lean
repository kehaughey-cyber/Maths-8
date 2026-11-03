/-
  CONTAINER 05 -- rung 5, the general all-N EQUIDISTANT-DIMENSION theorem, proved IN-REPO.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  This module retires container 05's OWED item 5.6(1). The Mathlib-free core (GeometricBridge.lean)
  proves the CONCRETE cases N = 2,3,4 by exact integer Gram determinant (line/plane/volume), which is
  all the bridge needs; the GENERAL all-N statement was maths-4's Mathlib THEOREM
  (RUNG5-EQUIDISTANT-DIMENSION) and was CITED while Maths 5 had no Mathlib. With Mathlib set up it is
  PROVED here, for ALL N: pairwise-equidistant points are affinely independent, so N such points force
  finrank >= N-1.

  AXIOM TIER: this module `import Mathlib`, so its theorems widen to Mathlib's three standard axioms
  (propext, Classical.choice, Quot.sound) -- confirmed by `#print axioms` below. This does NOT affect
  GeometricBridge.lean, which imports no Mathlib and stays zero-axiom. Proofs are ported from maths-4
  formal/Rung5/EquidistantDimension.lean (same Lean/Mathlib pins).

  NOT claimed here either: the UPPER bound (dim = 3 exactly) -- container 03's open thread. This is
  purely the LOWER bound dim >= N-1, general in N.
-/

import Mathlib

open scoped RealInnerProductSpace

namespace Container05

/-- Pairwise-equidistant families are affinely independent. The engine: r > 0 equal pairwise
    distances force affine independence, with NO assumption on which "shape" the points form -- the
    shape is a CONSEQUENCE. General over the index type and the real inner product space. -/
theorem equidistant_affineIndependent {V : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
    {ι : Type*} [Fintype ι] [DecidableEq ι] (p : ι → V) (r : ℝ) (hr : 0 < r) (i1 : ι)
    (heq : ∀ i j, i ≠ j → dist (p i) (p j) = r) :
    AffineIndependent ℝ p := by
  rw [affineIndependent_iff_linearIndependent_vsub ℝ p i1]
  rw [Fintype.linearIndependent_iff]
  intro g hg
  set v : { x : ι // x ≠ i1 } → V := fun i => p i.1 -ᵥ p i1 with hv
  have hnorm : ∀ i : { x : ι // x ≠ i1 }, ‖v i‖ = r := by
    intro i
    show ‖p i.1 - p i1‖ = r
    rw [← dist_eq_norm]
    exact heq i.1 i1 i.2
  have hinner_ne : ∀ i j : { x : ι // x ≠ i1 }, i ≠ j → ⟪v i, v j⟫ = r ^ 2 / 2 := by
    intro i j hij
    have hij' : i.1 ≠ j.1 := fun h => hij (Subtype.ext h)
    have hd : dist (p i.1) (p j.1) = r := heq i.1 j.1 hij'
    have key : ‖v i - v j‖ ^ 2 = ‖v i‖ ^ 2 - 2 * ⟪v i, v j⟫ + ‖v j‖ ^ 2 := norm_sub_sq_real _ _
    have hvij : v i - v j = p i.1 -ᵥ p j.1 := vsub_sub_vsub_cancel_right _ _ _
    rw [hvij] at key
    have hdist : ‖p i.1 -ᵥ p j.1‖ = r := by rw [← dist_eq_norm_vsub]; exact hd
    rw [hdist, hnorm i, hnorm j] at key
    linarith [key]
  have hterm : ∀ j i : { x : ι // x ≠ i1 }, g i * ⟪v i, v j⟫
      = r ^ 2 / 2 * g i + (if i = j then r ^ 2 / 2 * g i else 0) := by
    intro j i
    by_cases h : i = j
    · subst h
      rw [if_pos rfl, real_inner_self_eq_norm_sq, hnorm i]
      ring
    · rw [if_neg h, hinner_ne i j h]
      ring
  set S : ℝ := ∑ i, g i with hS
  have main : ∀ j : { x : ι // x ≠ i1 }, g j = -S := by
    intro j
    have step : ∑ i, g i * ⟪v i, v j⟫ = 0 := by
      have h2 := congrArg (fun w => ⟪w, v j⟫) hg
      simpa [sum_inner, real_inner_smul_left, hv] using h2
    have expand : ∑ i, g i * ⟪v i, v j⟫ = r ^ 2 / 2 * S + r ^ 2 / 2 * g j := by
      simp_rw [hterm j]
      rw [Finset.sum_add_distrib, ← Finset.mul_sum, ← hS,
        Finset.sum_ite_eq' Finset.univ j (fun i => r ^ 2 / 2 * g i)]
      simp
    rw [expand] at step
    have hr2 : (r ^ 2 / 2 : ℝ) ≠ 0 := by positivity
    have hfac : r ^ 2 / 2 * (S + g j) = 0 := by linarith [step]
    rcases mul_eq_zero.mp hfac with h | h
    · exact absurd h hr2
    · linarith [h]
  have hSsum : S = (Fintype.card { x : ι // x ≠ i1 } : ℝ) * (-S) := by
    calc S = ∑ i : { x : ι // x ≠ i1 }, g i := hS
      _ = ∑ _i : { x : ι // x ≠ i1 }, (-S) := Finset.sum_congr rfl (fun i _ => main i)
      _ = (Fintype.card { x : ι // x ≠ i1 } : ℝ) * (-S) := by
          rw [Finset.sum_const, nsmul_eq_mul, Finset.card_univ]
  have hpos : (0 : ℝ) < (Fintype.card { x : ι // x ≠ i1 } : ℝ) + 1 := by positivity
  have hfactor : S * ((Fintype.card { x : ι // x ≠ i1 } : ℝ) + 1) = 0 := by nlinarith [hSsum]
  have hS0 : S = 0 := by
    rcases mul_eq_zero.mp hfactor with h | h
    · exact h
    · exact absurd h (by linarith [hpos])
  intro j
  rw [main j, hS0, neg_zero]

/-- The GENERAL dimension bound (all N): N pairwise-equidistant points in a finite-dimensional real
    inner product space force `N <= finrank + 1`, i.e. the ambient dimension is at least N - 1. This
    is the all-N statement that container 05's Mathlib-free core witnesses only at N = 2,3,4. -/
theorem equidistant_card_le_finrank_succ {V : Type*} [NormedAddCommGroup V]
    [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] {n : ℕ} (p : Fin n → V) (r : ℝ)
    (hr : 0 < r) (heq : ∀ i j, i ≠ j → dist (p i) (p j) = r) :
    n ≤ Module.finrank ℝ V + 1 := by
  rcases n with _ | m
  · omega
  have hai : AffineIndependent ℝ p :=
    equidistant_affineIndependent p r hr 0 heq
  have h1 := hai.card_le_finrank_succ
  rw [Fintype.card_fin] at h1
  have h2 : Module.finrank ℝ (vectorSpan ℝ (Set.range p)) ≤ Module.finrank ℝ V :=
    Submodule.finrank_le _
  omega

/-- Two equidistant points force at least a line (d >= 1). -/
theorem two_equidistant_force_line {d : ℕ} (p : Fin 2 → EuclideanSpace ℝ (Fin d)) (r : ℝ)
    (hr : 0 < r) (heq : ∀ i j, i ≠ j → dist (p i) (p j) = r) : 1 ≤ d := by
  have := equidistant_card_le_finrank_succ p r hr heq
  rwa [finrank_euclideanSpace_fin, Nat.succ_le_succ_iff] at this

/-- Three mutually equidistant points force at least a plane (d >= 2). -/
theorem three_equidistant_force_plane {d : ℕ} (p : Fin 3 → EuclideanSpace ℝ (Fin d)) (r : ℝ)
    (hr : 0 < r) (heq : ∀ i j, i ≠ j → dist (p i) (p j) = r) : 2 ≤ d := by
  have := equidistant_card_le_finrank_succ p r hr heq
  rwa [finrank_euclideanSpace_fin, Nat.succ_le_succ_iff] at this

/-- Four mutually equidistant points force three dimensions (d >= 3) -- "the tetrahedron is genuinely
    3-D", the fourth point FORCED out of the plane by equal separations alone. -/
theorem four_equidistant_force_volume {d : ℕ} (p : Fin 4 → EuclideanSpace ℝ (Fin d)) (r : ℝ)
    (hr : 0 < r) (heq : ∀ i j, i ≠ j → dist (p i) (p j) = r) : 3 ≤ d := by
  have := equidistant_card_le_finrank_succ p r hr heq
  rwa [finrank_euclideanSpace_fin, Nat.succ_le_succ_iff] at this

#print axioms equidistant_affineIndependent
#print axioms equidistant_card_le_finrank_succ
#print axioms two_equidistant_force_line
#print axioms three_equidistant_force_plane
#print axioms four_equidistant_force_volume

end Container05
