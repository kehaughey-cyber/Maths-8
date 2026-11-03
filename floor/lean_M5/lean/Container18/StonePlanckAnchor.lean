/-
  CONTAINER 18 -- STONE: THE PLANCK ANCHOR. Compton meets Schwarzschild. EXTERNAL, QUARANTINED.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Step 6, the second STONE. EXTERNAL physics re-derived COLD (our own proof, NOT importing maths-4's
  PlanckAnchor.lean, which used Mathlib `ring` at the bridge tier). Mathlib-FREE, ZERO-axiom.

  P.1 the CROSSOVER: given R*(m c)=hbar (Compton) and R*(c c)=2 G m (Schwarzschild) for the same R,m,
      then hbar*c = 2 G m^2 -- mass squared, factor 2 from the Schwarzschild radius. Cleared against the
      Planck mass (m_P^2 G = hbar c): m_P^2 G = 2 G m^2. Zero-axiom -- Nat comm/assoc HAND-PROVED.

  The div-by-G (m_P^2 = 2 m^2), and the sqrt readings m = m_P/sqrt2, R = sqrt2 l_P, are routine scalar
  steps over R, cited. P.2/P.3/P.4 (ladder, Kevin's flagged hypothesis, owed) have nothing to prove.
-/

namespace Container18

/-- Associativity of Nat multiplication, hand-proved (Nat.mul_assoc carries propext here). -/
theorem natMulAssoc (a b c : Nat) : a * b * c = a * (b * c) := by
  induction c with
  | zero => rfl
  | succ c ih => rw [Nat.mul_succ, Nat.mul_succ, Nat.mul_add, ih]

/-- Commutativity of Nat multiplication, hand-proved (to avoid Mathlib `ring`/bridge-tier axioms). -/
theorem natMulComm (a b : Nat) : a * b = b * a := by
  induction b with
  | zero => rw [Nat.mul_zero, Nat.zero_mul]
  | succ b ih => rw [Nat.mul_succ, Nat.succ_mul, ih]

/-- "R = hbar/(m c)" without division: R*(m c) = hbar (the reduced Compton radius). -/
def IsComptonRadius (R m hbar c : Nat) : Prop := R * (m * c) = hbar
/-- "R = 2 G m / c^2" without division: R*(c c) = 2 G m (the Schwarzschild radius). -/
def IsSchwarzschildRadius (R G m c : Nat) : Prop := R * (c * c) = 2 * G * m
/-- "m_P^2 = hbar c / G" without division: m_P^2 * G = hbar c (the Planck mass, squared). -/
def IsPlanckMassSq (mP2 hbar c G : Nat) : Prop := mP2 * G = hbar * c

/-- THE CROSSOVER (P.1): one R that is simultaneously the reduced Compton radius and the Schwarzschild
    radius of the same mass m gives hbar*c = 2 G m^2 -- the factor 2 inherited from the Schwarzschild
    radius. Proved fresh here, zero-axiom (comm/assoc hand-proved). -/
theorem compton_schwarzschild_crossover {R m hbar c G : Nat}
    (hC : IsComptonRadius R m hbar c) (hS : IsSchwarzschildRadius R G m c) :
    hbar * c = 2 * G * (m * m) := by
  unfold IsComptonRadius at hC
  unfold IsSchwarzschildRadius at hS
  calc hbar * c = (R * (m * c)) * c := by rw [hC]
    _ = R * ((m * c) * c)   := natMulAssoc R (m * c) c
    _ = R * (m * (c * c))   := by rw [natMulAssoc m c c]
    _ = R * ((c * c) * m)   := by rw [natMulComm m (c * c)]
    _ = (R * (c * c)) * m   := (natMulAssoc R (c * c) m).symm
    _ = (2 * G * m) * m     := by rw [hS]
    _ = 2 * G * (m * m)     := natMulAssoc (2 * G) m m

/-- The crossover read against the Planck mass, cleared: m_P^2 * G = 2 G m^2 (i.e. m_P^2 = 2 m^2 once
    G>0 is cleared -> m = m_P/sqrt2, the routine sqrt step). -/
theorem crossover_planck_cleared {R m hbar c G mP2 : Nat}
    (hC : IsComptonRadius R m hbar c) (hS : IsSchwarzschildRadius R G m c)
    (hP : IsPlanckMassSq mP2 hbar c G) :
    mP2 * G = 2 * G * (m * m) := by
  unfold IsPlanckMassSq at hP
  rw [hP]; exact compton_schwarzschild_crossover hC hS

/-- A concrete witness (R=1, c=2, m=2 -> G=1, hbar=4): hbar*c = 8 = 2*G*m^2, and m_P^2 = 8 = 2*m^2. -/
theorem crossover_witness : ((4 * 2 == 2 * 1 * (2 * 2)) && (8 == 2 * (2 * 2))) = true := by decide

#print axioms natMulAssoc
#print axioms natMulComm
#print axioms compton_schwarzschild_crossover
#print axioms crossover_planck_cleared
#print axioms crossover_witness

end Container18
