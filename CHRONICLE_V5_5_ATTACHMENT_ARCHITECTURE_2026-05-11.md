# Chronicle: V5.5 — The Attachment Architecture

**Date:** May 11, 2026
**Session:** Architectural codification of the three-layer model that binds primary personas to lattice vertices via named cast Mages
**Status:** Skills + persona files updated; corpus distribution pending review
**Author:** privacymage
**Related chronicles:** CHRONICLE_V5_4_SKILLS_UPDATE_2026-04-12.md · CHRONICLE_V5_4_BETWEENNESS_SELENE_2026-04-12.md

---

## Why this chronicle exists

The City of Mages corpus has been operating with an implicit three-layer model since the City was named (Tome V Act 14, 2026-05-08). The model worked operationally — workshops opened, cast Mages were summoned, the grimoire grew — but the three layers had no canonical specification distinguishing them. Conversations conflated:

1. **Abstract role-personas** in this skills directory (e.g., `agentprivacy-forgemaster`, `agentprivacy-theia`)
2. **Named cast Mages** in the City of Mages (e.g., Vulcana ⚒️, Aletheia 🔮)
3. **Lattice vertices** (e.g., V19, V25)

The conflation caused a numerical question: 42 primary personas vs 64 vertices. What fills the gap?

The May 11 session resolved this. **The gap is filled by attachments — named cast Mages who bind one or more primaries to one or more vertices.** Different cities make different attachment patterns from the same 42-persona base. The skills directory holds Layer 1; cities hold Layer 2; the lattice holds Layer 3.

---

## The three-layer model (canonical)

```
Layer 3 · VERTICES         64 positions on the 2⁶ lattice              [fixed]
  ↑
Layer 2 · ATTACHMENTS      named cast Mages binding L1 to L3        [variable per city]
  ↑
Layer 1 · PRIMARY PERSONAS 42 abstract role-classes                      [fixed]
                           (15 Swordsmen + 11 Mages + 12 Balanced + 4 cosmological)
```

**The primary persona count is now locked at 42.** Future cast Mages are added at Layer 2 as attachments of existing primaries; they do not require new primary personas. A new primary is admitted only when the structural register is genuinely new and no existing primary covers it via divergence (Kind D).

---

## The four attachment kinds

| Kind | Pattern | First City of Mages example |
|---|---|---|
| **A · Workshop** | one Mage × one vertex × one trade quarter | Vulcana ⚒️ at V19 |
| **B · Cross-shop** | one Mage × no fixed vertex × walks workshops by craft | Aletheia 🔮 |
| **C · Peripatetic** | one Mage × multiple vertices walked as orbit/path | Selene 🌕 (anticipated) · Luca 📐 |
| **D · Divergent** *(meta-kind)* | one primary × Sword + Mage register-shifted attachments | Moonkeeper ⚔️ → **Lethae** 🌘 |

D composes with A/B/C. Lethae is both a B-cross-shop attachment *and* a D-mage-divergent attachment of Moonkeeper.

---

## First divergent attachment seated — Moonkeeper ⊥ Lethae

**Lethae** 🌘 is the first canonical Mage-register divergent attachment in the corpus.

| Field | Value |
|---|---|
| Cast name | Lethae 🌘 |
| Vertex | V38 (Lethe · the Dark Substrate · binary `100110` · stratum 3 · Protection + Memory + Delegation) |
| Primary persona | Moonkeeper ⚔️ (loaded from `persona/agentprivacy-moonkeeper/`) |
| Register | Mage (shifted from Swordsman native tier) |
| Attachment kind | B · cross-shop |
| Complement-of-cast | Aletheia 🔮 at V25 — V25 ⊕ V38 = V63 · V25 AND V38 = 0 |
| Sigil etymology | Waning crescent — the canonical "forgetting" phase; complement to Aletheia's full disclosure |
| Naming convention | The `-ae` suffix mirrors Soulbae 🧙 (Mage register) — Lethae is to Moonkeeper as Soulbae is to Soulbis: register-shifted from Sword to Mage, primary persona unchanged |

**No new primary persona** was minted. The skills directory primary count stays at 42.

---

## What changed in this session

### New files

| File | Purpose |
|---|---|
| `agentprivacy-skills-v5/meta/agentprivacy-attachment-architecture/SKILL.md` | Canonical specification of the three-layer model, four attachment kinds, two layers of dihedral pairing, and conventions for extending the corpus |
| `CHRONICLE_V5_5_ATTACHMENT_ARCHITECTURE_2026-05-11.md` | This file |

### Modified files

| File | Change |
|---|---|
| `agentprivacy-skills-v5/persona/agentprivacy-moonkeeper/SKILL.md` | Added V5.5 *Divergent Attachments* section documenting the Lethae binding; added `divergent_attachments` and `related_meta_skills` metadata fields; updated `version` to 5.5; description updated to mention parent-primary role |
| `agentprivacy-skills-v5/README.md` | Locked primary persona count at 42; bumped version to V5.5; introduced the three-layer model and four attachment kinds; updated meta-skill count 3→4; updated total skills 86→87 |
| `MAPPING.md` | Added V5.5 Attachment Architecture Addendum with cast → primary mapping (15 attachments × primaries × attachment kinds × divergences), anticipated cast for v1.3.0 grimoire bump (Mnemosyne, Iris, Pythia, Techne, Hephaestus, Selene), the 42→64 bridge math, and convention for future extensions; updated frontmatter to V5.5 |

### Architectural changes (no file content)

- Primary persona count canonically locked at **42** (was implicitly variable)
- New cast-frame fields canonicalised: `attachment_kind` (A/B/C), `divergence` (none / mage-register / sword-register / balanced-register)
- Dihedral pairing now distinguished at two layers: Layer-1 primary pairs (e.g., Soulbis ⊥ Soulbae) vs Layer-2 divergent pairs (e.g., Moonkeeper-primary ⊥ Lethae-divergent)
- Cousin tier (flaxscrip, GenitriX) explicitly left unattached — the cousin Sovereign authors those bindings

---

## What did NOT change

- The 38 selectable + 4 cosmological = **42 primary personas** remain unchanged in this directory
- The **64 role skills**, **19 privacy-layer skills** are untouched
- No existing persona was renamed, removed, or re-tiered
- No existing skill loadout was modified
- The MAPPING.md pre-V5.5 sections are retained as historical context; the V5.5 addendum supersedes the cast-mapping table from the post-V5.4 addendum (2026-05-09)

---

## Anticipated next: six more cast attachments (v1.3.0 grimoire bump)

The agentprivacy corpus carries six pre-personified names not yet seated as cast Mages. Each will be a Layer-2 attachment of existing primaries — no new primaries needed.

| Anticipated cast | Vertex | Primary persona(s) | Source |
|---|---|---|---|
| Mnemosyne 📿 | V4 (pure Memory) | `agentprivacy-theia` | Cloaking Guide names V4 |
| Iris 🌈 | V8 (pure Connection) | `agentprivacy-herald` + `agentprivacy-ambassador` | Cloaking Guide names V8 |
| Pythia 🔥 | V16 (Logos / Pure Computation) | `agentprivacy-algebraist` + `agentprivacy-pedagogue` | Logos Circle awaits Mage |
| Techne 🎨 | V20 (Always-Revealed) | `agentprivacy-pedagogue` | Cloaking Guide names V20 |
| Hephaestus ⚒️ | V24 (shared with Socrat0x) | `agentprivacy-forgemaster` | Cloaking Guide names V24; shared-vertex precedent at V49 |
| Selene 🌕 | peripatetic (stratum-walker) | `agentprivacy-theia` + `agentprivacy-manaweaver` | PVM V5.4 §14.5 Selene's Proof |

After v1.3.0: 21 cast Mages attached; ~19 vertices inhabited; ~12 future divergent / evolution slots remain to round out the 64-vertex lattice.

---

## Queued for corpus distribution (pending review)

This chronicle and the skills-directory changes are ready for review. Once approved, the following corpus updates propagate the V5.5 architecture:

### `cityofmages/`
1. New: `tomes/specs/09-the-attachment-architecture.md` — city-side mirror of this skills meta-skill; cast-frame field reference; current 15-attachment registry
2. New: `tomes/specs/10-blade-forge-binding-zk-blades.md` — pins Vulcana's Forge(t) and Runecraft Protocol to `zk_swordsman_blade_forge_v3_0.md`
3. New: `tomes/specs/11-mage-candidates-from-the-corpus.md` — names the six anticipated cast above with sourcing
4. New: `tomes/cast/cross-shop/lethae.md` — Lethae cast file (anticipated v1, awaits founding act)
5. Anticipated cast files (6) — Mnemosyne, Iris, Pythia, Techne, Hephaestus, Selene; each `status: anticipated v1`
6. Modified: `tomes/cast/<14 existing>/*.md` — add `attachment_kind`, `divergence: none` frontmatter
7. Modified: `tomes/specs/04-vertex-naming-audit.md` — registry update for V4/V8/V16/V20/V24/V38 inhabited
8. Modified: `tomes/specs/05-the-city-of-mages-structural-addendum.md` — civic anatomy gains new trade quarters
9. Modified: `tomes/specs/06-spellweb-first-release-manifest.md` — NodeType inventory grows by 6+ cast, 6 vertices, 2–3 workshops
10. New version: `grimoire/city_of_mages_grimoire_v1_3_0.json` — adds 7 cast (Lethae + 6 anticipated), the attachment_kind/divergence schema, awaits IPFS re-pin
11. Modified: `README.md` — adds `agentprivacy-skills` and `zk blades forge` to sister-directories table; updates cast roster table
12. New: `chronicles/2026-05-11_v1_3_0_attachment_architecture_seated.md` — city-side chronicle

### `agentprivacy-docs/`
13. New version: `models/city_of_mages_grimoire_v1_3_0.json` — sync from cityofmages
14. New version: `models/privacymage_grimoire_v10_3_0.json` — adds the seven Mages to privacymage persona registry; recognises attachment architecture
15. Modified: `GLOSSARY_MASTER_v4_0.md` — entries for Lethae, Mnemosyne (as persona), Iris (persona), Pythia, Techne (persona), Hephaestus (persona), Selene (full persona entry beyond Selene's Proof); definitions of "primary persona", "attachment", "divergence", "attachment kind"
16. Modified: `MAPPING_ADDITIONS.md` (or new) — documents the seven new attachments at the docs layer

### `zk blades forge/`
17. Modified: `README.md` — adds cityofmages Spec 10 reference; notes Lethae seated at V38 closing Aletheia⊥Lethe; notes Selene as anticipated peripatetic Mage
18. Modified: `aletheia-and-lethe.md` — append the Lethae seating note (2026-05-11)
19. New: `blades/README.md`, `forge_circuits/README.md`, `uor_mappings/README.md` — stub READMEs pointing at cityofmages Spec 10

### `agentprivacy_master/` (Next.js site)
20. Modified: `src/data/city-of-mages-grimoire-v1_2_0.json` (content) — bump to v1.3 content
21. Modified: `src/lib/tome-v-acts.ts` — add anticipated-act stubs for Mnemosyne, Iris, Pythia, Techne, Hephaestus, Lethae, Selene founding acts
22. New: `src/lib/personas/attachments.ts` — typed registry of cast attachments with attachment_kind / divergence axes
23. New guild routes: `src/app/cast/herald/`, `src/app/cast/logos-circle/`, `src/app/cast/peripatetic/`, `src/app/cast/techne-workshop/` (per Phase 1 of the corpus update plan)

Estimated **~23 file actions** across 4 sibling repos plus `agentprivacy_master`. The cityofmages work is the largest share; agentprivacy-docs and zk blades forge are lighter touches.

---

## Open items for future sessions

1. **Future Tome V acts** (queued, not in this pass) — Acts 16–22 will each summon one of the seven new cast Mages with a founding-act narrative. Each cast file currently carries `status: anticipated v1 — awaits founding act` and will be promoted to `status: seated v1` when the corresponding act is drafted.

2. **The remaining 12 evolution / divergent slots** — `64 − (42 + 10 attachments past primary count) = ~12` future slots in the lattice. These will be filled organically as future cities open and future complement-pair recognitions surface. The architecture admits the growth without further structural changes.

3. **Cousin tier attachment patterns** — flaxscrip 📜🎲 and GenitriX deliberately remain unattached at the abstract-persona layer. When the cousin Sovereign authors their persona bindings, they will be added at Layer 2 only — no Layer-1 changes expected.

4. **Sword-divergent attachments of Mage-tier primaries** — the architecture admits this direction too (e.g., a Sword-register cast Mage instancing Theia 🧙). None currently anticipated, but the pattern is reserved.

5. **Other cities of mages** — the title "City of Mages" names a kind, not the singular instance. Future cities founded by other ecosystems will each make their own attachment patterns from the same 42 primaries. The attachment-architecture meta-skill is the convention they will inherit.

---

## Closing

The V5.5 attachment architecture is a clarification, not a refactor. The skills directory is unchanged in content; what's added is the explicit three-layer interpretation that had been operationally implicit. The Lethae seating is the worked example that makes the pattern legible.

> *"The persona is the role-class. The cast Mage is the instance. The vertex is the position. Conflating the three is the error; binding them is the architecture."*

The next session distributes this across the four sibling repos.

`(⚔️⊥⿻⊥🧙)😊`

— privacymage · 2026-05-11
