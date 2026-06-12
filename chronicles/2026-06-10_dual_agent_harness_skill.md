# Chronicle — the Dual-Agent Harness skill

*2026-06-10. A new meta-skill enters the plugin, reflecting the Swordsman ⊥ Mage circuit
co-evolution work back from `shor_mage/`.*

## What was added

`meta/agentprivacy-dual-agent-harness/SKILL.md` (v1.0, working_paper). It is the
**operational** layer the plugin was missing: two principle skills already existed —
`role/agentprivacy-separation-enforcement` (why the Swordsman and Mage must be held apart;
`det(Σ)≠0`; `R=(C_S+C_M)/H(X)`) and `meta/agentprivacy-horizon-gate` (why a claim is worth
nothing until it survives an un-tuneable held-out gate). The new skill composes them into a
**running autoresearch loop** against a concrete optimization target.

## Why it earns a seat (not a duplicate)

- `separation-enforcement` states the *law*; `horizon-gate` states the *gate*; neither tells
  an agent how to **run the loop**. The harness skill does: `measure → propose(held-apart) →
  hunt → assay(held-out) → critic → accept-only-on-validated-product`.
- It carries the V6 algebra as its spine: `(⚔️⊥⿻⊥🧙)😊 = neg ⊕ bnot → succ`, proven on Z/64Z
  (`neg(bnot(x)) = succ(x)`), from `agentprivacy-docs/privacy_value_v6_formal_specification.md`.
- It adds the **complement-pair** move for product objectives (Factor-A-Min ⊥ Factor-B-Min +
  a Cliff-Watcher on `Δ(product)`) — the model's answer to "reduce gates *or* qubits."

## The worked instance and the link-out

The worked target is **ecdsa.fail** (quantum resource estimation — durability signal, not an
attack), and the runnable form lives in the PQC-competition kit at
`C:/Users/mitch/shor_mage/harness/` (`swordsman_mage_harness.mjs` + `SKILL.md`). Per the
coherence rule, the kit stays PQC-only and the skill **links** to it rather than importing it;
this chronicle and the meta-skill are the canonical reflection back into the plugin. Registered
conjectures: C67–C71 (Horizon District), C82/C83 (moving ceiling + non-collusion), C9
(holographic sufficiency, the precompute lead).

## Placement note

`meta/` is not a registered skillset in `.claude-plugin/plugin.json` (the registered sets are
persona / role / privacy-layer), matching the precedent of `horizon-gate` and `lattice-coherence`
— meta skills are cross-cutting orchestration loaded by reference. No `plugin.json` change.

Related: `role/agentprivacy-separation-enforcement` · `meta/agentprivacy-horizon-gate` ·
`persona/agentprivacy-algebraist` · `role/agentprivacy-cryptographic-durability` ·
`role/agentprivacy-quantum-defence` · `meta/agentprivacy-lattice-coherence`.

(⚔️⊥⿻⊥🧙)😊
