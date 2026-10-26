# Formally verified parts of this repository

Sealed in the κ registry: formal_mage evidence bundle `evidence/2026-10-26_75`, root `sha256:d4d42f9e333323b20d5b649525cbe28f8885fa2cb0cdd10943a04cac3793b9da` (75 theorems, 75/75 within the standard axioms; re-derive with `python kappa_evidence_mage/verify_bundle.py` or `node tools/kappa_evidence.mjs verify`).

Statements in these skills that carry a machine-checked receipt in `formal_mage` (Lean 4, core library, kernel-checked, axiom-audited). `node tools/formal_census.mjs <this repo>` in formal_mage fails if a tag names a theorem outside the audited census. Correspondence of each theorem to the skill's prose is stated in its doc comment.

| Claim | Skill | Status | Tag |
|---|---|---|---|
| Every edge of Q₆ changes the stratum by one (no lateral edges) | edge-value | proved | formal: proved formal_mage:Formal.Lattice.q6_no_lateral |
| Every vertex has degree 6 | edge-value | proved | formal: proved formal_mage:Formal.Lattice.q6_regular |
| At stratum k: 6 − k up, k down | edge-value | proved | formal: proved formal_mage:Formal.Lattice.up_down_split |
| Q₆ has 192 edges | ring-algebra, holographic-bound | proved | formal: proved formal_mage:Formal.Lattice.q6_edge_count |
| Complement pairs are at Hamming distance 6 | ring-algebra | proved | formal: proved formal_mage:Formal.Lattice.bnot_distance_six |
| neg moves the stratum (neg 1 = 63) | ring-algebra | proved | formal: proved formal_mage:Formal.Lattice.neg_moves_stratum |
| bnot is a cube automorphism; neg and succ are not | dihedral-sovereignty | proved | formal: proved formal_mage:Formal.Lattice.bnot_cube_automorphism · formal: proved formal_mage:Formal.Lattice.neg_not_cube_automorphism |
| Two witnesses per transition | dihedral-sovereignty | proved | formal: proved formal_mage:Formal.Dihedral.exactly_two_witnesses |
| det Σ orientation (all ones → 0; one entangled pair → 0) | tetrahedral-sovereignty | proved | formal: proved formal_mage:Formal.Model.det_all_ones · formal: proved formal_mage:Formal.Model.det_one_pair_collapses |
| 100 at stratum 3 do not beat 2,000 at stratum 1 | network-topology | refuted | formal: refuted formal_mage:Formal.Model.guild_vs_crowd |
| For fixed head-count, all at stratum 3 maximises Σwᵢnᵢ | network-topology | proved | formal: proved formal_mage:Formal.Model.concentrate_at_three |
| Nearest blade to 1/φ is 39 | disclosure-phi | proved | formal: proved formal_mage:Formal.Model.nearest_blade_is_39 |
