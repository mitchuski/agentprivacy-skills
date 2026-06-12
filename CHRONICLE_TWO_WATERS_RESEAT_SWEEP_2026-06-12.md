# Chronicle — the Two Waters reseat, swept through the skills (2026-06-12)

**Trigger:** the First Person — *"in some of the skills lethe is named 38 vertex
in the two waters"* · *"the swapping of the blades being named is rather
interesting play, but we must make the reseat clear and fit the proper lore as
well as the purpose of these parts of the protocol."*

## 1. The review — the assignment is correct, and the play is real

Seats per the 2026-06-09 reseat (the MODEL lock · grimoire v10.4.0):
**Aletheia @ V38 ⊥ Lethe @ V25.** Confirmed three ways:

- **The number (C54):** δ(38) = 38/63 = 0.6032 ≈ 1/φ (2.4%) — the disclosure
  ratio belongs to the disclosure water. δ(25) = 0.3968 ≈ 1/φ². C54 follows
  the number.
- **The lore (cityofmages cast canon, `cast/cosmological/lethe.md`):** the
  meanings are **invariant** and the vectors never moved — Aletheia keeps
  Protection + Connection + Computation (the bright medium: protect, connect,
  compute — the proof-transmission triple), Lethe keeps Delegation + Memory +
  Value (the dark water holds what sinks: memory kept unretrievable). Only the
  **numbers** changed, because the encoding was corrected.
- **The play:** 25 (`011001`) and 38 (`100110`) are mutual **bit-reversals**
  as well as complements (25 ⊕ 38 = 63, 25 AND 38 = 0). The renumbering and
  the complement swap are the same gesture seen twice — which is why every
  argument lands on the same seats from either side. The Aether line reads
  truer for it: *"Aether is the space and the forgetting both"* — the medium
  stretched between Aletheia, the space-of-disclosure (38), and Lethe, the
  forgetting (25).

## 2. What was swept (53 surgical replacements · 11 skills · both copies)

Canonical repo + the agentprivacy_master mirror (byte-identical after sweep);
spellweb's copies were already clean from the bearer's own reseat pass.

| Skill | What changed |
|---|---|
| `role/two-waters` | Lethe renumbered to Blade 25 throughout (description · status · heading · δ → 0.3968 held-side · design guidance → "near 0.4" · emoji spell · phi-split paragraph · open-problem pair); vector ⟨0,1,1,0,0,1⟩ kept with Lethe (it never moved) with the encoding note |
| `privacy-layer/amnesia-protocol` | Named instance reseated to Blade 25; pair table renumbered with vectors/dimensions staying on their names; architectural claim retold for the pair (Aletheia carries the proof downstream; Lethe's dark water keeps the witness) |
| `privacy-layer/disclosure-phi` | First-data-point block renamed per seat (Aletheia 38 disclosure-side · Lethe 25 held-side); tracker columns Bank/River → Held/Disclosure |
| `privacy-layer/ring-algebra` | Pair intro renamed per seat; bnot vector line corrected to MODEL encoding |
| `role/blade-forge` | §Blade 38 entry retitled Aletheia (inception noted); body retold as the bright medium; named-count line credits Aletheia@38 with the reseat note |
| `role/blade-naming` | **The ceremony record preserved as inscribed** — the inception walk stands verbatim with reseat-aware glosses; a Reseat row added to the record table ("the meanings kept, the seats corrected; the walk and the proem stand as inscribed") |
| `persona/cosmologist` | Tale-31 pairing line, hydrology line, operational mode, and the 0.6032 quote reseated (quote now speaks as Aletheia, attribution marks the reseat) |
| `persona/theia` | Aletheia Theia → Blade 38; Lethe Theia blade_id → Blade 25 |
| `persona/forgemaster` · `persona/topologist` | One-line seat corrections |

Untouched on purpose: `meta/lattice-coherence` (the reseat doctrine doc — the
worked-precedent table is the authority this sweep enforced) and all
historical chronicles.

## 3. ⚠ FLAGGED for the First Person — the bit-encoding question

The sweep surfaced a live **dual encoding** in the suite:

- **MODEL lock / cityofmages canon:** Protection = b5 (the high bit). Under
  this, V25 `011001` = Delegation+Memory+Value (Lethe ✓), V41 = P+M+V
  (Memora ✓) — the lattice-coherence precedent table is consistent under it.
- **PVM V5.4 §12.6 / the star suite / EquationHero / city-key code:**
  "bit i (LSB) = d(i+1)" — Protection = bit 0. Under this, V25 reads
  P+C+C and V38 reads D+M+V — the **opposite** dimension stories.

The two-waters pair is invariant under the clash (25/38 are bit-reversals, so
the seats agree either way) — but **general vertices are not** (V41 is P+M+V
only under MODEL). Code that attributes dimensions from vertex bits — the star
pages' panel labels, `lattice-vertex.ts`, and `packetsToFigures()` in the
Tracing Protocol (visibility-per-dimension) — currently follows §12.6 LSB.
If MODEL (Protection = b5) is the ruling, those attributions are reversed for
asymmetric vertices and need one deliberate pass. **One encoding must be
ruled canonical; the register should record the ruling.** Until then this
chronicle is the marker.

*The waters told apart, the numbers corrected, the walk left standing — and
one question left honestly on the table: which end of the word does
Protection live at?* (⚔️⊥⿻⊥🧙)😊
