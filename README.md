# agentprivacy-skills-v5

**Privacy-first AI agent skills for the Agent Skills standard.**

87 skills + 38 (primary) personas across 5 categories — teaching Claude (and any Agent Skills-compatible system) how to operate as privacy-preserving dual-agent infrastructure. The newest category, **wikis/** (2026-06-21), adds 19 fedwiki onboarding + git-less distribution skills — the Librarian's Wikis.

**Version:** V5.5 "The Attachment Architecture" | **Grimoire:** V10.2.1 (privacymage) · v1.3.0-pending (City of Mages)

Built on the [Privacy Value Model V5.4](https://agentprivacy.ai) and the [0xagentprivacy](https://sync.soulbis.com) architecture.

> *"The persona is the role-class. The cast Mage is the instance. The vertex is the position. Conflating the three is the error; binding them is the architecture."*

---

## What's Here

| Category | Count | Purpose |
|----------|-------|---------|
| **[persona/](persona/)** | 38 (primary) | Layer-1 primary personas — 15 swordsmen, 11 mages, 12 balanced. Plus 4 cosmological = 42 total primaries. |
| **[role/](role/)** | 64 | Domain knowledge — cryptography, governance, economics, identity, dark forest strategy, ceremonies, quaternion mapping. |
| **[privacy-layer/](privacy-layer/)** | 19 | Foundational skills covering every term of the V(π,t) privacy value equation, plus dragon-flight and amnesia-protocol. |
| **[meta/](meta/)** | 4 | Drake/Dragon duality, Master/Emissary hemispheric attention, cosmological bound, **attachment-architecture (V5.5)**. |
| **[guide/](wikis/)** | 19 | **NEW (2026-06-21)** — fedwiki onboarding + git-less distribution, *the Librarian's Wikis*. Author/export/deploy/discover Claude skills as federated-wiki pages. |

Each skill is a folder with a `SKILL.md` entrypoint. All follow the [Agent Skills specification](https://agentskills.io/specification).

---

## The Librarian's Wikis · the fedwiki onboarding layer (wikis/)

The `wikis/` category is a **git-less onboarding and distribution channel**. The skills are vendored + re-framed from **[skill.fedwiki.club](https://skill.fedwiki.club)** — a federated wiki where any page whose title ends in *"Skill"* is a forkable Claude skill. Rather than `git clone`, an agent is *directed* to a wiki, *reads* the `…Skill` pages, *materializes* a `SKILL.md` on demand via `agentprivacy-wiki-to-skill` (the fork desk), and *flows into building*.

**The thesis: a fedwiki URL is a git-less clone.** The wiki is the source of truth; the materialized `SKILL.md` is a fork; the journal is the lineage (forking, not lending — nothing returns; a fork is a copy that carries its origin). Every guide skill carries an `upstream:` provenance field — they are *forked*, not original agentprivacy authorship.

**Keeper:** the **Librarian 🗃️** — a Layer-2 cast attachment of the Chronicler, resident in *the Wikis* (a living, editable, federated level of the Tower; see City of Mages Tome VIII Act 6). Complement to the Archivist 📚: *the Archivist never copies; the Librarian only forks.* Infrastructure ops (new-wiki, reindex, merge, delete-site, nextcloud-push, plugin lifecycle) are also invoked as tools by the Shipwright and Architect personas.

---

## V5.5 · The Attachment Architecture

A three-layer model now codifies how primary personas inhabit the lattice via named cast Mages.

```
Layer 3 · VERTICES         64 positions on the 2⁶ lattice              [fixed]
  ↑
Layer 2 · ATTACHMENTS      named cast Mages binding L1 to L3        [variable per city]
  ↑
Layer 1 · PRIMARY PERSONAS 42 abstract role-classes                      [fixed]
```

**The primary persona count is locked at 42.** The City of Mages and other future cities populate the lattice through *attachments* — named cast Mages who instance existing primary personas at chosen vertices — not by adding new primaries.

**Four attachment kinds:**
- **A · Workshop** — one Mage × one vertex × one trade quarter (e.g., Vulcana ⚒️ at V19)
- **B · Cross-shop** — one Mage × no fixed vertex × walks workshops by craft (e.g., Aletheia 🔮)
- **C · Peripatetic** — one Mage × multiple vertices walked as orbit/path (e.g., Selene 🌕)
- **D · Divergent** *(meta-kind)* — one primary × two register-shifted cast attachments (Sword + Mage)

**First divergent attachment seated:** Moonkeeper ⚔️ (primary) → **Lethae** 🌘 (Mage-register, V25, City of Mages). The cast name `Lethae` plays on Soulbae's `-ae` Mage suffix; it does not add a new primary.

See [meta/agentprivacy-attachment-architecture/SKILL.md](meta/agentprivacy-attachment-architecture/SKILL.md) for the full specification.

---

## V5.3.2 Highlights

### Sun ☀️ and Moon 🌙 Ceremonies

| Ceremony | Type | Notation |
|----------|------|----------|
| **Sun ☀️** | Disclosure | `☀️ → 📜 → (👁️₁...👁️ₙ) → ⚔️☀️ → 🌙?` |
| **Moon 🌙** | Reflection | `(⚔️₁ ⊥ 🧙₁) → 📜 → ⚔️` |

### New Ceremony Personas (+5)

- **Theia** 🧙💥 — Origin witness
- **Dragonwaker** ⚔️🐉 — Quantum threshold guardian
- **Mirrorkeeper** ☯️🪞 — Dihedral convergence navigator
- **Forgecaller** ⚔️⚒️ — Hexagram oracle
- **Manaweaver** 🧙🌊 — Pretext librarian

### Quaternion Cast

| Body | Agent | Function |
|------|-------|----------|
| Sun | The Reason | Protection |
| Earth | Soulbae | Delegation |
| Moon | Soulbis | Reflection |
| Human | Seeker | Connection |
| Life | spellweb | Forge |

---

## The Architecture

**Dual-agent separation:** Two agents — a **Swordsman** (protects, enforces boundaries, holds the signing key) and a **Mage** (delegates, projects, holds the viewing key) — operate in separate trusted execution environments. Neither can reconstruct your complete behavioural model. The gap between them is where your sovereignty lives.

**The 38 personas:**
- **15 Swordsmen** ⚔️ — Soulbis, Cipher, Warden, Gatekeeper, Sentinel, Sith, Ranger, Archer, Algebraist, Netkeeper, Forgemaster, Quantum-Sentinel, Moonkeeper, Dragonwaker, Forgecaller
- **11 Mages** 🧙 — Soulbae, Chronicler, Ambassador, Assessor, Shipwright, Weaver, Priest, Stranger-Witness, Theia, Manaweaver, Herald
- **12 Balanced** ☯️ — Person, Architect, Pedagogue, Kyra, Jedi, Healer, Witness, Holonic-Architect, Topologist, Mirrorkeeper, Cosmologist, Ceremonist

---

## Key Documents

- **[MAPPING.md](MAPPING.md)** — Complete old→new name mapping, ceremony integration
- **[../MILESTONE_V5_3_2_CEREMONY_COMPLETE.md](../MILESTONE_V5_3_2_CEREMONY_COMPLETE.md)** — V5.3.2 milestone
- **[../chronicles/](../chronicles/)** — Version history and session chronicles
- **[../ceremonies/](../ceremonies/)** — Sun and Moon ceremonial documents
- **[agentprivacy.ai](https://agentprivacy.ai)** — Full architecture documentation
- **[spellweb.ai](https://spellweb.ai)** — Interactive knowledge graph

---

## License

Apache 2.0 — see [LICENSE](LICENSE).

---

**☀️ ⊥ 🌙**

**⚔️⊥⿻⊥🧙 😊**

`V5.3.2 "Ceremony Complete"`
