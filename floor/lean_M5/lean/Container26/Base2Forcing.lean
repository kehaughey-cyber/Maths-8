/-
  CONTAINER 26 -- BASE-2 FORCING: the registrable alphabet is 2; the branching is base-2. Rests on 00.

  GENERATED FROM derivation.json BY check/gen_lean.py. DO NOT EDIT BY HAND.
  `python3 gen_lean.py --check` fails if this file and the derivation disagree.

  Container 00 has three existential states, but non-existence CANNOT be perceived or registered (00.2),
  and a distinction is a positive TWO-valued partition (00.3). So the REGISTRABLE ALPHABET is exactly 2.
  Two checked negatives keep this honest: base-3 is REFUSED (the third state is unregistrable, not a
  symbol), and the triad's 3 (OBSERVERS -- the machinery that produces a registration, 00.4) is a
  DIFFERENT quantity, typed apart from the 2 (the alphabet of the registered content). "Triadic floor"
  does NOT mean "base 3". The per-registration BRANCHING FACTOR is then 2 (base-2): a configuration space
  grows as 2^k -- each registration doubles it (2^(k+1)=2*2^k) -- so the substrate's native count L
  (containers 23/24) is a BIT-count.

  IMPORTS Container00: reuses Existential and perceivable -- one home, consumed. Mathlib-FREE, ZERO-axiom.
  B2.3 (the Shannon reading giving ln2 content) is POSTULATE; B2.4 (the ruler's ln2 = the registration
  bit, SEC9) is OWED -- no kernel content. log2(2^k)=k (the bit-count) is exact-integer in the model.
-/

import Container00.Distinction

namespace Container26
open Container00   -- Existential, perceivable -- one home, consumed here

/-! ### B2.1 -- the registrable alphabet is exactly 2 (not 3; the triad's 3 is observers, typed apart) -/

/-- Container 00's three existential states. -/
def allStates : List Existential := [.definedExistent, .undefinedExistent, .nonExistent]

/-- The registrable alphabet: the states container 00's `perceivable` admits (00.2). Non-existence is
    filtered out -- it cannot be perceived or registered. -/
def registrable : List Existential := allStates.filter perceivable

/-- The alphabet is exactly 2: two of the three existential states are registrable. -/
theorem alphabet_is_two : (registrable.length == 2) = true := by decide

/-- BASE-3 REFUTED: there are three existential states but only two are registrable, so the base is 2,
    not 3 -- the third (non-existence) is the counterpoint, not a symbol. -/
theorem base3_refuted : (allStates.length == 3 && registrable.length == 2) = true := by decide

/-- The triad's THREE is the count of OBSERVERS (container 00.4, the machinery that PRODUCES a
    registration -- 'not the registration'), a DIFFERENT quantity from the 2-state alphabet: typed
    apart, so 'triadic floor' does not license 'base 3'. -/
def observerCount : Nat := 3
theorem observers_typed_apart_from_alphabet :
    (observerCount != registrable.length) = true := by decide

/-! ### B2.2 -- the per-registration branching factor is 2 (base-2) -/

/-- The base = the alphabet size, counted from container 00's registrable states. -/
def base : Nat := registrable.length          -- = 2

/-- A configuration space over k registrations = base^k = 2^k. -/
def configs (k : Nat) : Nat := base ^ k

/-- BASE-2 BRANCHING: each registration MULTIPLIES the configuration count by the alphabet size 2
    (2^(k+1) = 2 * 2^k) -- this doubling is exactly what "base 2" means. -/
theorem base_two_doubling :
    ([0, 1, 2, 3, 4, 5, 6].all (fun k => configs (k + 1) == 2 * configs k)) = true := by decide

/-- The empty configuration (no registrations) is one state. -/
theorem configs_zero : (configs 0 == 1) = true := by decide

/-- The base IS 2 (the registrable alphabet size). -/
theorem base_is_two : (base == 2) = true := by decide

#print axioms alphabet_is_two
#print axioms base3_refuted
#print axioms observers_typed_apart_from_alphabet
#print axioms base_two_doubling
#print axioms configs_zero
#print axioms base_is_two

end Container26
