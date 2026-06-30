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
only under MODEL).

## 4. RULED AND UNIFIED (the First Person, same day)

*"do a pass on the bit locations… it must be unified."* **Ruling: the MODEL
encoding — d₁ Protection is the HIGH bit (2⁵); d_k carries weight 2^(6−k);
a vertex's binary string reads d₁…d₆ left to right.** The pinned grimoire
seats and deployed vertex numbers derive under it; code labels are cheap,
pinned canon is not.

The unification pass (2026-06-12):

- **Already conformant, untouched:** `agentprivacy_master/src/lib/
  lattice-vertex.ts` (vertexToBits is MSB-first, Protection weight 32 — every
  master surface that uses it was correct all along) · `spellweb-blade-bridge`
  · spellweb's vertex nodes (V41 P+M+V, V38 Aletheia P+C+C) · all popcount /
  neighbour-flip code (convention-free) · /star's 3D lattice embedding (bits
  drive geometry positions, not labels — deliberately untouched).
- **Fixed to MODEL:** soulbis `/lattice` (panel bitrow emoji + held-list) and
  `/sigil` (held/open inspect) — both pages' §12.6 comments rewritten with the
  ruling + the three worked anchors; dimensions now listed d₁-first; star
  CLAUDE.md canon paragraph rewritten ("never read d₁ at the low bit");
  `packetsToFigures()` in the Tracing Protocol now attributes visibility per
  dimension at bit (5−i); Tracing spec §14.3 carries the encoding note.
- **The ruling stated in the formal spec:** PVM V6 formal specification §12.6
  gains the *Numeric encoding* paragraph (MSB-first, weights, the three
  anchors, "any surface reading d₁ at the low bit is in erratum") —
  consistent with §12.8's own Aletheia/Lethe prose, which was already MODEL.
- **Verified:** V38 → 🛡️🔗⚡, V25 → 🤝📜💎, V41 → 🛡️📜💎 through the actual
  page code and the figures derivation; tsc clean; the five suite pages
  byte-identical to soulbis; academic PDFs rebuilt with the ruling.

*The waters told apart, the numbers corrected, the walk left standing — and
the word now reads one way: Protection lives at the high end.* (⚔️⊥⿻⊥🧙)😊
