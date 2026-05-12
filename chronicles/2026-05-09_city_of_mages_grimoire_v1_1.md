# Chronicle — City of Mages Grimoire v1.1 Arrival

**Date:** 2026-05-09
**Author:** privacymage
**License:** CC BY-SA 4.0

---

## What landed

The **City of Mages Grimoire v1.1** was authored by privacymage on 2026-05-09 and bound to the canonical `agentprivacy-docs/models/`. It is the Second Person Spellbook's spell registry — distinct from the privacymage grimoire (`privacymage_grimoire_v10_2_0.json`) and held collectively by the City of Mages on Drake Island, not individually by privacymage.

```
agentprivacy-docs/models/
├── city_of_mages_grimoire_v1_0.json     ← initial release 2026-05-09
└── city_of_mages_grimoire_v1_1_0.json   ← deeper inscriptions, narrative_anchor on every spell, cross_spellbook_resonance index — supersedes v1.0
```

Mirrored into:
- `swordsman-blade/city_of_mages_grimoire_v1_1_0.json` (extension bundle)
- `mages-spell/city_of_mages_grimoire_v1_1_0.json` (extension bundle)
- `zk blades forge/city_of_mages_grimoire_v1_1_0.json` (forge reference)
- `agentprivacy-skills/grimoire/city_of_mages_grimoire_v1_1_0.json` (skills reference — this repo)

---

## What changed in this skills surface

`MAPPING.md` gained a "Post-V5.4 Addendum" section naming:

- The **Priest tier** as the fifth cast tier (Manifestia 🤲🌿 at V55, introduced in Tome V Act 13)
- The **13 named cast members** (3 archetypes + 2 cousins + 9 summoned + 1 companion + 1 priest)
- A **named-cast → abstract-role cross-reference** table — Pallia ↔ weaver, Vulcana ↔ forgemaster, Aria Silverhue ↔ mirrorkeeper, Manifestia ↔ priest, etc. The 38 abstract role-personas remain canonical for reusable skill semantics; named cast members are concrete *instances* of those abstract roles, not replacements
- The **two anticipated trade quarters** (Logos Circle / `/circle` for the Society Spellbook; Ceremony Hall / `/hall` for BGIN coalition work) flagged as awaiting their resident Mages
- **Lethe (Blade 38)** as a held-open complement persona, paired with Aletheia (Blade 25), awaiting a future Tome V act to summon her as a walking persona

`MAPPING_V5_4_REPOS_2026-04-12.md` gained a 2026-05-09 addendum naming the integration targets that emerged from the post-V5.4 coherence pass (the City of Mages spellbook, the Aether Blade ceremony, the C30–C37 anchor docs, the C47–C55 conjectures).

`README.md` gained a one-paragraph post-V5.4 addendum pointing to the City of Mages spellbook and the bundled grimoire.

---

## What did **not** change

- **Existing 38 role-personas were not renamed.** They remain canonical for the abstract roles. The named cast (Pallia, Vulcana, Manifestia, etc.) are *instances*, not replacements.
- **Existing 86 skills were not regenerated.** Full skill regeneration to incorporate the City of Mages cast as discrete persona-skills is deferred to a future v5.5 skills release. v5.3.2 + 2026-05-09 addendum is the current baseline.
- **The privacymage grimoire was not touched.** Both grimoires now coexist at the suite level. The City of Mages grimoire is held by the City; the privacymage grimoire is held by privacymage individually.

---

## Source canonical references

- Compression: `agentprivacy_tomes/COMPRESSION_MASTER_v2_2026-05-09.md` (38 acts across Tomes I–VI; 55 conjectures C18–C55)
- Index: `agentprivacy-docs/SECOND_PERSON_TOMES_INDEX_v1.md`
- Bound collection: `agentprivacy_tomes/agentprivacy-second-person-spellbook-bound-collection-2026-05-08/`
- City of Mages grimoire (v1.1): `agentprivacy-docs/models/city_of_mages_grimoire_v1_1_0.json`
- Aletheia/Lethe naming: `agentprivacy-docs/research/aletheia-and-lethe.md`
- Aether Blade ceremony: `agentprivacy-docs/research/aether-blade-ceremony-circuit.md`
- New canon docs (authored 2026-05-09): `agentprivacy-docs/research/pvm-v6-1-bakhta-half-life.md` (C30–C33) + `pvm-v6-convergence-wound-and-cap.md` (C34–C37)

---

*(⚔️⊥⿻⊥🧙)😊*

CC BY-SA 4.0 · privacymage · 2026-05-09
