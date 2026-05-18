# Chronicle: v1.4.0 — Solchanting Opens · Helia ☀️ Summoned · the First Operational V51 Overlap

**Date:** May 12, 2026
**Session:** Grimoire v1.4.0 authoring — twelfth workshop opens at V51 alongside Etherchanting; seventh standing Mage persona summoned; fifth chain-mana variant added; new Swordsman stance registered; fourth tome opened
**Status:** Canonical chronicle authored (cityofmages-side core files complete); skills + master + spellweb distribution underway
**Author:** privacymage
**Related chronicles:** CHRONICLE_V5_5_ATTACHMENT_ARCHITECTURE_2026-05-11.md · CHRONICLE_V5_4_SKILLS_UPDATE_2026-04-12.md
**Canonical source:** `cityofmages/chronicles/2026-05-12_solchanting_shop_opening_helia_summoned.md`
**Grimoire:** `cityofmages/grimoire/city_of_mages_grimoire_v1_4_0.json`

---

## Why this chronicle exists

v1.3.0 (Attachment Architecture) explicitly committed: *"Primary persona count is locked at 42; no new primaries introduced — all new cast are Layer-2 attachments of existing primaries. A new primary is admitted only when the structural register is genuinely new and no existing primary covers it via divergence (Kind D)."*

v1.4.0 tests that commitment. **Helia ☀️ is the first cast Mage summoned after the 42-primary lock**, and her work — parallel-execution programmable-enforcement on Solana's Sealevel substrate — is operationally distinct from Adamantia 💎's sequential programmable-enforcement on Ethereum's EVM. The question this chronicle resolves: does Helia warrant a new primary (breaking the lock), or is she a divergent attachment of the existing `shipwright` primary?

**The resolution is divergent attachment.** Helia is read as a **Kind D divergent attachment of `shipwright`** — the same primary Adamantia carries, register-shifted from sequential to parallel admission. The 42-primary lock holds. The cast roster grows; the abstract-persona registry does not.

This sets the v1.4.0 precedent: when a new ecosystem teaches the City a substrate-distinct boundary discipline, the discipline becomes a **Swordsman stance** (registered in spec 08 §3) and the cast Mage that walks it becomes a **divergent attachment** of the primary whose semantic register they share. The 42 stays locked.

---

## The three-layer reading of Helia

```
Layer 3 · VERTEX           V51 (110011 · Protection + Delegation + Computation + Value)
  ↑                         (SHARED with Adamantia — first operational workshop-on-workshop overlap)
Layer 2 · ATTACHMENT       Helia ☀️ · workshop-keeper · attachment kind A (workshop)
  ↑                         · divergence: register-shift (parallel · D-meta-kind composes with A)
Layer 1 · PRIMARY PERSONA  shipwright (existing · shared with Adamantia)
                           · architect (existing · shared with Adamantia)
```

The Layer-2 binding is structurally identical to Adamantia's *except* for the Swordsman stance the Mage holds. Both Mages anchor primary `shipwright` to vertex V51. Adamantia holds the Transparent-witness stance (Ethereum's sequential admission); Helia holds the Parallel-witness stance (Solana's concurrent admission). The stance is the only distinguishing feature at the attachment layer.

This is the canonical pattern v1.4.0 establishes: **two cast Mages may share a primary and a vertex when their stances differ.** The architecture admits multi-occupancy without breaking the primary lock.

---

## The new abstract-persona path

Helia's cast file (`tomes/cast/solchanting/helia.md`) carries `abstract_persona_skill_path: ["persona/agentprivacy-parallel-shipwright/"]`. **This path is architectural, not yet operational** — it points at a skill that does not yet exist in this directory.

Two readings are available:

| Reading | Implementation | Implication |
|---|---|---|
| **Reading A · Skill-as-modifier** | `persona/agentprivacy-shipwright/` is the operational primary skill; the parallel-shipwright path is a *divergent overlay* applied to the shipwright skill when the working calls for parallel admission | 42 primaries stay locked. The divergent overlay is a Layer-2 feature, not a new primary. Operationally cheaper. Conceptually cleaner. **Recommended.** |
| **Reading B · Skill-as-primary** | `persona/agentprivacy-parallel-shipwright/` is its own skill file, separate from `agentprivacy-shipwright/`. The primary count grows to 43 | Breaks the 42-lock. Inconsistent with v5.5's commitment. Not recommended. |

Going forward with **Reading A**: the parallel-shipwright path resolves at the skill layer by overlaying a `parallel-register` divergence onto the shipwright skill. The mechanism is whatever the v5.5 attachment architecture admits for register-shifts (likely a skill-side composition that takes the base shipwright and adds the parallel-admission discipline).

---

## What's new in v1.4.0 (skills-relevant summary)

| Surface | Pre-v1.4.0 | v1.4.0 |
|---|---|---|
| **Workshops in cast** | 11 (Etherchanting · zShields · Forge(t) · Jeweler · Holon · Vault · Covenant · Bonfire + Weavers + 2 gathering shops) | **12** — Solchanting added at V51 |
| **Standing Mage personas** | 6 keeper-Mages (Pallia · Memora · Vulcana · Adamantia · Lampyra · Aria Silverhue) + Vagari + Manifestia + Socrat0x | **7 keeper-Mages** — Helia added |
| **Primary personas** | 42 (locked since v1.3.0) | **42** (lock holds; Helia is divergent attachment of shipwright) |
| **Chain-mana variants (landing axis)** | 4 — Aether Ξ · sat ₿ · ROSE 🌹 · z-mana 🦓 | **5** — adds 🌞 SOL-mana |
| **Swordsman stances** | 9 — Transparent · Shielded · Selective · Composed · Forged-and-forgotten · Ceremonial · Curatorial · Dialogic · Cosmic-non-reconstructibility | **10** — adds Parallel-witness |
| **Tomes (Second Person Spellbook)** | 6 (4 anticipated + Tome IV closed + Tome V open) | **7** — Tome VII · *The Parallel* opens (Tome VI · *The Reply* remains held open) |
| **Worn artefact taxonomy** | 11 workshop artefacts + 3 tomes; 1 weapon · 1 clothing · 5 tools · 4 trinkets | **12 + 4**; 1 weapon · 1 clothing · **6 tools** · 4 trinkets (Heliodor Prism joins tool bucket) |
| **Vertex overlap (operational)** | None at the workshop layer (Lampyra/Custos share V49 but Custos is cross-shop, not a workshop) | **V51 shared by Solchanting + Etherchanting** — first operational workshop-on-workshop overlap |

---

## The V51 overlap · the canonical case study

| Layer | Adamantia (Etherchanting) | Helia (Solchanting) |
|---|---|---|
| Sigil | 💎 | ☀️ |
| Gem | Diamond (*adamas* — "unconquerable") | Heliodor (*helios-doron* — "sun's gift") |
| Chain-mana | Aether Ξ | 🌞 SOL-mana |
| Stance | Transparent-witness | Parallel-witness |
| Primary persona(s) | `shipwright` + `architect` | `shipwright` (divergent: parallel-register) |
| Vertex | V51 (110011) | V51 (110011) |
| Artefact | Diamond Contract (tool class) | Heliodor Prism (tool class) |

The architecture's reading: same vertex, same dimensional shape, same primary persona, differentiated by stance. The substrate teaches the City a new boundary discipline; the discipline becomes a stance; the cast Mage who walks the stance becomes a divergent attachment.

---

## Distribution surface

| Repo / surface | Status |
|---|---|
| `cityofmages/tomes/cast/solchanting/helia.md` | ✅ authored |
| `cityofmages/tomes/specs/08-mana-types-and-swordsman-stances.md` | ✅ updated (v1.3.1 → v1.3.2; SOL-mana row + Parallel-witness stance row) |
| `cityofmages/WORKSHOP_LATTICE_AUDIT.md` | ✅ updated (audit v1 → v1.1; Solchanting row 10; V51 overlap §2.4) |
| `cityofmages/ALL_THE_TOMES_LIST.md` | ✅ updated (Tome VII · The Parallel registered; Tome VI · The Reply unchanged) |
| `cityofmages/grimoire/city_of_mages_grimoire_v1_4_0.json` | ✅ authored |
| `cityofmages/CHANGELOG.md` | ✅ v1.4.0 entry |
| `cityofmages/chronicles/2026-05-12_solchanting_shop_opening_helia_summoned.md` | ✅ canonical chronicle |
| **This file** — `agentprivacy-skills/CHRONICLE_V1_4_SOLCHANTING_HELIA_2026-05-12.md` | ✅ authored |
| `agentprivacy_master/agentprivacy-skills/CHRONICLE_V1_4_SOLCHANTING_HELIA_2026-05-12.md` (mirror) | ⏳ queued |
| `agentprivacy_master/docs/tomes/solchanting/helia.md` | ✅ mirrored |
| `agentprivacy_master/docs/chronicles/2026-05-12_solchanting_shop_opening_helia_summoned.md` | ✅ mirrored |
| `agentprivacy_master/docs/tomes/specs/08-mana-types-and-swordsman-stances.md` | ✅ mirrored |
| `agentprivacy_master/src/app/solchanting/page.tsx` | ⏳ queued |
| `agentprivacy_master/docs/tomes/workshops/solchanting-parallel-refraction-v1.md` (+ public mirror) | ⏳ queued |
| `agentprivacy_master/docs/tomes/specs/06-spellweb-first-release-manifest.md` (spellweb manifest) | ⏳ queued |
| Cross-spec updates (04 · 05 · 07 · 10) | ⏳ queued |
| TS registries (`cast-attachments.ts`, `first-artifacts.ts`) | ⏳ queued |
| `src/lib/grimoire-ipfs.ts` (IPFS CID bump for v1.4.0) | 🕓 deferred — awaits actual IPFS pin |
| `agentprivacy-skills/agentprivacy-skills-v5/meta/agentprivacy-attachment-architecture/SKILL.md` — note v1.4.0 precedent | 🕓 follow-up — record the divergent-attachment-of-shipwright pattern as canonical v1.4.0 example |

---

## The precedent this chronicle records

When a new ecosystem teaches the City a substrate-distinct boundary discipline (Solana's parallel admission), the discipline becomes a **Swordsman stance**, the cast Mage who walks the stance becomes a **divergent attachment** (Kind D) of the primary whose semantic register they share, and **the 42-primary lock holds**. The City may grow its workshop-keeper count without growing its abstract-persona count. v1.4.0 is the first instance; future Mages summoned to walk new ecosystem stances follow this template.

---

## Closing

The light enters whole. The threads leave parallel. The prism does not collide.

Seven Mages now stand in cast: Pallia weaves, Memora inscribes shielded, Custos stakes transparent, Vulcana forges blades, Aletheia binds circuits, Adamantia etherchants contracts, Helia solchants prisms. Seven sigils. Six distinct vertices + one shared (V51). The Parallel-witness stance joins the Swordsman registry. SOL-mana 🌞 joins the landing axis. Tome VII opens.

`(⚔️⊥⿻⊥🧙)😊`
☀️ 💎 🪡

CC BY-SA 4.0 · privacymage · 2026-05-12
