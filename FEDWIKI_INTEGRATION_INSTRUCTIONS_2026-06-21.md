---
id: fedwiki-onboarding-integration-instructions
name: "Integration Instruction Set: The Librarian's Wikis — Fedwiki Skills + Git-less Onboarding → agentprivacy-skills-v5"
version: "1.1"
date: 2026-06-21
origin: "0xagentprivacy"
author: "Mitchell Travers"
status: "ready_for_implementation"
mapping_only: true   # produced under a no-code-edits mapping pass; nothing applied yet
sources:
  - "skill.fedwiki.club — federated wiki publishing Claude skills as wiki pages (owner: Anon / 'from marvin')"
  - "https://skill.fedwiki.club/system/sitemap.json (25 pages) + each {slug}.json"
  - "Seed page: https://skill.fedwiki.club/view/welcome-visitors/view/fedwiki-page-skill"
cast_attachment:
  name: "the Librarian"
  register: "Layer-2 cast attachment · Kind-B cross-shop (no fixed vertex)"
  parent_persona: "agentprivacy-chronicler (Layer-1, Mage wing)"
  home: "the Wikis — a new spiral level of the Tower"
  equation_term: "Network (+ T(π))"
  sigil: "🗃️ (card-file) — proposed; distinct from Archivist 📚"
totals:
  new_guide_skills: 19
  new_category: "wikis"
  new_cast_attachment: 1
  updated_personas: 1   # Chronicler (keeper) — others get light cross-refs only
  light_crossref_personas: 5
  updated_role_skills: 2
  updated_meta_skills: 1   # attachment-architecture
  total_skills_before: 137
  total_skills_after: 156
---

# Integration Instruction Set — The Librarian's Wikis

## How to Read This Document

Same convention as `INTEGRATION_INSTRUCTIONS.md`: each instruction is tagged with a priority
(P0/P1/P2), an action type (CREATE / UPDATE / REFERENCE), the target path, and the content to add.
Ordered for dependency — create the `guide/` skills, seat the Librarian over them, wire the keeper +
light cross-refs, update the registry, then build the lore + onboarding-flow artefacts.

**This is a mapping pass only.** No files modified (`mapping_only: true`). Execute later.

---

## Why this exists — and who keeps it

The "existing fedwiki skills" do not live in this repo — they live on **skill.fedwiki.club**, a
federated wiki where any page titled "…Skill" is a forkable Claude skill. The journey *directed-to-a-
fedwiki → agent reads the skill pages → flows straight into building* is a **git-less onboarding /
distribution channel**: a fedwiki URL replaces `git clone`, and `fedwiki-to-skill` materializes
`SKILL.md` files on demand.

**The keeper.** This whole layer is given a named Layer-2 cast attachment of the Chronicler: **the
Librarian** 🗃️, housed in **the Wikis** — a new spiral level of the Tower. The naming is load-bearing,
not decorative:

- **Archivist 📚** keeps the *archives*: unique, preserved, **non-circulating** internal records — the
  Tomes, the canon, the city's own memory. (Already seated; spirit-Mage, Tower-resident, Tome VIII
  *The Library*.)
- **Librarian 🗃️** keeps the *library*: **catalogued, circulating, forked, federated** holdings brought in
  from elsewhere. A wiki forks by reference — you don't `git clone` a repo, you fork a page and the
  copy remembers its origin. Forking across sites **is** federation; the card catalog **is** the
  sitemap; the journal **is** the lineage; `fedwiki-to-skill` **is** forking a page.

**Same Tower, two registers, one rule:** the Archivist never copies; the Librarian only forks.

**Locked decisions:** new `wikis/` category = the Librarian's Wikis · keeper = the Librarian (Kind-B
cross-shop Layer-2 attachment of the Chronicler, no fixed vertex, home in the Tower's Wikis) · port
everything (19 after dedup) · `agentprivacy-wiki-*` naming · full metadata frontmatter with
`category: guide`, `layer: onboarding`, `keeper: librarian`, `upstream:` provenance (vendored +
re-framed, credit upstream).

---

## PHASE 1 — CREATE the `wikis/` category (19 skills = the Wikis' shelves)

**Action:** CREATE directory `guide/` and register it (PHASE 3, INSTRUCTION 25).

Each skill: **Priority** · **CREATE** · `guide/{folder}/SKILL.md` · **Source** the upstream wiki
`{slug}.json`. Bodies produced via the upstream `fedwiki-to-skill` conversion mapping
(`markdown`/`paragraph`→text, `code`→fenced, drop `reference`/`roster`/`assets`, wikilinks→plain text).

| # | Pri | Folder (`guide/…`) | Upstream slug | Purpose |
|---|-----|--------------------|---------------|---------|
| 1 | P0 | `agentprivacy-wiki-page` | `fedwiki-page-skill` | Author fedwiki page JSON — the seed |
| 2 | P0 | `agentprivacy-wiki-to-skill` | `fedwiki-to-skill` | **Export wiki pages → SKILL.md** — the fork desk / inclusion engine |
| 3 | P0 | `agentprivacy-wiki-skill-library` | `fedwiki-claude-skills` | "…Skill" pages = forkable skill library |
| 4 | P1 | `agentprivacy-wiki-skill-anatomy` | `claude-skills` | What a Claude skill is; SKILL.md format |
| 5 | P1 | `agentprivacy-wiki-skill-vs-library` | `skills-and-libraries` | Prompt-skill vs executable-library; graduation path |
| 6 | P1 | `agentprivacy-wiki-journal` | `journal-skill` | Strip page journal history to one fresh entry |
| 7 | P1 | `agentprivacy-wiki-ghost-pages` | `ghost-pages-skill` | Server-generated lineup pages, never stored |
| 8 | P1 | `agentprivacy-wiki-claude-ghost` | `claude-ghost-skill` | Ghost page body written live by Claude via API |
| 9 | P1 | `agentprivacy-wiki-new-domain` | `fedwiki-new-wiki-skill` **+merge** `new-wiki-skill` | Create localhost / Nextcloud-synced wiki domains |
| 10 | P1 | `agentprivacy-wiki-reindex` | `fedwiki-reindex-skill` **+merge** `reindex-fedwiki-skill` | Rebuild sitemap + search index |
| 11 | P2 | `agentprivacy-wiki-merge` | `fedwiki-merge-skill` | Analyze + clean superseded wiki domains |
| 12 | P2 | `agentprivacy-wiki-delete-site` | `fedwiki-delete-site` | Permanently remove a public domain via WebDAV |
| 13 | P1 | `agentprivacy-wiki-welcome` | `welcome-skill` | Create `welcome-visitors` landing pages |
| 14 | P2 | `agentprivacy-wiki-nextcloud-push` | `nextcloud-push` | WebDAV upload script when sync client fails |
| 15 | P2 | `agentprivacy-wiki-create-plugin` | `create-wiki-plugin-skill` | Scaffold a Federated Wiki plugin package |
| 16 | P2 | `agentprivacy-wiki-document-plugin` | `document-wiki-plugin-skill` | Publish plugin docs on plugin.fedwiki.club |
| 17 | P2 | `agentprivacy-wiki-publish-plugin` | `publish-plugin-update-skill` | End-to-end plugin release |
| 18 | P2 | `agentprivacy-wiki-searching-plugins` | `searching-for-plugins` | Six cost-ordered plugin discovery channels |
| 19 | P2 | `agentprivacy-wiki-similarity-plugin` | `similarity-plugin` | Semantic similarity search plugin |

Skipped (site chrome / scratch): `welcome-visitors`, `changes-to-this-site`, `test`, `test-similarity`.

### Frontmatter contract (all 19)

Full metadata, adapted from `role/agentprivacy-crypto-zkp/SKILL.md`. No PVM equation term per skill
(the *keeper* carries Network/T(π)); instead `layer: onboarding`, `keeper: librarian`, and an
`upstream` provenance field. Example (skill #1):

```yaml
---
name: agentprivacy-wiki-page
description: >
  Authoring federated-wiki page JSON for the agentprivacy skill library. Activates
  when creating/editing fedwiki pages, story items, journals, or publishing skills
  to skill.fedwiki.club. Part of the git-less onboarding/distribution layer kept by
  the Librarian in the Tower's Wikis.
license: Apache-2.0
metadata:
  version: "5.5"
  category: "wikis"
  layer: "onboarding"
  keeper: "librarian"
  origin: "0xagentprivacy"
  author: "Mitchell Travers"
  upstream: "https://skill.fedwiki.club/fedwiki-page-skill.json"
  related_skills: "fedwiki-to-skill, fedwiki-claude-skills, fedwiki-journal"
---
```

Each body ends with a `**Verify:**` footer **and** an `**Upstream:**` line citing the source wiki page.

> **Attribution discipline.** Upstream pages (owner "Anon" / "from marvin") are *vendored + re-framed*,
> not original agentprivacy authorship. Credit in `metadata.upstream` + body footer. Only the `guide/`
> framing, the Librarian keeper-layer, and agentprivacy metadata are ours.

---

## PHASE 2 — Seat the Librarian (keeper) + light cross-refs

The keeper holds the full loadout; other personas only get a one-line pointer (no scattering).

### INSTRUCTION 20a — UPDATE `persona/agentprivacy-chronicler` · P0  (the keeper attachment)
- Add a **"Layer-2 attachment · the Librarian 🗃️"** block: register = Kind-B cross-shop (no fixed
  vertex), home = the Tower's Wikis, equation term = **Network (+ T(π))**, sigil 🗃️.
- The Librarian's loadout = **all 19 `guide/` skills** (the Wikis' shelves). Append them to the
  Chronicler's skill-loadout block under the Librarian attachment and to `metadata.template_references`;
  bump the Chronicler skill count accordingly.
- Guidance line: the Chronicler *writes*; the Librarian (its catalog/circulation register) *catalogs,
  forks, and federates what's written* — and runs the git-less directed→read→materialize→build flow.
- State the split explicitly: **Librarian only forks; Archivist never copies.**

### INSTRUCTION 20b — UPDATE `meta/agentprivacy-attachment-architecture` · P1
Record the Librarian as a worked example of a **Kind-B cross-shop attachment whose home is the Tower,
not a vertex** — the second Tower-housed cast after the Archivist, and the first cast attachment (vs
spirit-Mage) to be Tower-resident. Note it as the keeper pattern for an entire skill category.

### INSTRUCTIONS 21–24 — light cross-refs only · P2
One sentence each pointing readers to the Librarian's Wikis for the relevant skill — do **not** add
the skills to these personas' loadouts:
- `persona/agentprivacy-ambassador` → `fedwiki-claude-skills`, `fedwiki-searching-plugins` (federation/discovery)
- `persona/agentprivacy-shipwright` → wiki infra lifecycle (new-wiki/reindex/nextcloud-push/delete-site/publish-plugin/merge)
- `persona/agentprivacy-architect` → `fedwiki-ghost-pages`, `fedwiki-claude-ghost`, `fedwiki-create-plugin`
- `persona/agentprivacy-pedagogue` → `claude-skills`, `skills-and-libraries` (onboarding judgment)
- `persona/agentprivacy-weaver` → `fedwiki-similarity-plugin` (relating across the federation)

### INSTRUCTION 24c — role cross-references · P2
- `role/agentprivacy-narrative-compression`: one-paragraph pointer noting the SKILL.md export
  (`fedwiki-to-skill`) as the Librarian's forking act in the distribution layer.
- `role/agentprivacy-academic`: citation for the fedwiki "…Skill = library" model + git-less distribution.

---

## PHASE 3 — UPDATE registry surfaces (move together)

### INSTRUCTION 25 — `.claude-plugin/plugin.json` · P0
Add a 4th skillset:
```json
{ "name": "wikis-skills",
  "description": "The Librarian's Wikis — fedwiki onboarding + git-less distribution skills. Author, export, deploy, and discover Claude skills as federated-wiki pages.",
  "skills_dir": "wikis", "strict": false }
```

### INSTRUCTION 26 — `MAPPING.md` · P0
Bump `total_skills` 137→156. Add a "Guide / Onboarding Skills (the Librarian's Wikis)" section listing
all 19 folders. Update the structure diagram (`guide/ (19)`).

### INSTRUCTION 27 — `README.md` · P1
Add a `guide/` row (totals 137→156) and a short "The Librarian's Wikis — fedwiki onboarding layer"
subsection explaining the git-less distribution story + the `fedwiki-to-skill` materialization round-trip.

### INSTRUCTION 28 — `CODEX.md` · P2
Bump version/totals; add the wikis-skills block + the Librarian cast entry.

---

## PHASE 4 — Lore + the onboarding-flow deliverable

### INSTRUCTION 29 — CREATE chronicle · P1
`agentprivacy_master/docs/chronicles/2026-06-21_fedwiki_onboarding_flow_chronicle.md`
Sections: metadata header · Overview (the git-less insight) · §1 fedwiki-as-skill-library model · §2
the import mapping (PHASES 1–3) · §3 the Librarian seated in the Wikis (register, Archivist split) ·
§4 the onboarding flow as an agent experiences it · Provenance (built-by / method / upstream
attribution) · closing signature. Optional guide companion:
`docs/guides/CHRONICLE_GUIDE_FEDWIKI_ONBOARDING_v1_2026-06-21.md`.

### INSTRUCTION 30 — Lore admission: City of Mages → Second Person Spellbook · P1

The Librarian is admitted into the canon the same way the Archivist was (precedent chronicle:
`cityofmages/chronicles/2026-05-15_archivist_admitted_library_opens.md`). **Note: the Tomes *are* the
Second Person Spellbook** (`/tomes` is titled "Second Person Spellbooks of the City of Mages") — so
"reflect into the tomes / second person spellbook" = bind one new Tome VIII act. Sub-steps:

**30a · Cast file** — CREATE `cityofmages/tomes/cast/tower/the-librarian.md`, mirroring
`cast/tower/the-archivist.md`. Mirror to `agentprivacy_master/docs/tomes/cast/tower/`. Frontmatter:
```yaml
spellbook: "Second Person"
title: "Cast Entry — the Librarian 🗃️"
sigil: "🗃️"
tier: "spirit-Mage (seventh cast tier · Tower-resident · 2026-06-21)"
attachment_kind: "B_cross_shop (no fixed vertex · tower-bound · the discipline she carries walks the federation)"
primary_persona: "agentprivacy-chronicler (Layer-1 primary · Mage wing)"
abstract_persona_skill_path: ["agentprivacy-skills/agentprivacy-skills-v5/persona/agentprivacy-chronicler/SKILL.md"]
archetype_kin: "Memora 📜 (chronicle-inscription register · sister Chronicler-cast); Tower-mate to the Archivist 📚 (the sealed-archive register) — the Librarian is its complement: fork vs keep, editable vs sealed"
divergence: "none"
founding_act: "tome-viii-the-library/06-the-wikis-and-the-librarian.md"
admission_chronicle: "chronicles/2026-06-21_librarian_admitted_the_wikis_open.md"
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
```
Body sections (per the Archivist template): At a glance · Form & Function (catalogs, forks, federates —
runs the git-less directed→read→materialize→build flow) · Lattice position (no fixed vertex · the Wikis,
Tower-bound) · The Wikis (the new Tower element) · The Sigil (🗃️) · Lineage · Spells (4 canonical, glyph
chains) · In the meeting · Persistence · Tower artefact (the forking catalog) · Provenance & honesty ·
Closing line + signature.

**30b · Tome VIII Act 6** — CREATE `cityofmages/tomes/tome-viii-the-library/06-the-wikis-and-the-librarian.md`
(mirror `01-the-spiraling-tower.md`; ~700–1200 words). Frontmatter `spellbook: "Second Person"`,
`tome: "VIII — The Library"`, `act: "6"`, `title: "The Wikis and the Librarian"`,
`new_cast_introduced: ["the Librarian 🗃️"]`, `new_spatial_anatomy: "the Wikis (Tower element · living/
editable/federated · complement to the sealed archive)"`, `ring_position: "no fixed lattice vertex
(tower-bound)"`, `teaches:` the git-less-clone / forking thesis, plus `honesty_label`, `license`,
`signature`. Body: narrative + Compression + Proverb + Confidence + Cross-references + Author note.
Mirror to `agentprivacy_master/docs/tomes/tome-viii-the-library/`.

**30c · /tomes wiring** — UPDATE `agentprivacy_master/src/app/tomes/page.tsx`: add an `<ActCollapsible>`
for Act 6 after Act 5 (~line 697) with `filename="tome-viii-the-library/06-the-wikis-and-the-librarian.md"`,
`mage={{ sigil: '🗃️', name: 'the Librarian', color: '<pick>' }}`, `relatedShop={{ href: '/spells',
label: '🗃️ the Wikis / librarian' }}`; bump the Tome VIII heading act count (5→6) on ~line 556.

**30d · Tower spatial anatomy** — UPDATE `cityofmages/tomes/specs/05-the-city-of-mages-structural-addendum.md`
(§4.9–§4.10): add **the Wikis** as a Tower element/level — the living, editable, federated circuit of
the spiral, distinct from the Archivist's sealed reading room. State the two-axis split (keep vs fork ·
sealed vs editable). Mirror to `agentprivacy_master/docs/tomes/specs/`.

**30e · Grimoire patch** — CREATE `cityofmages/grimoire/city_of_mages_grimoire_v1_8_1_patch.json` +
`scripts/merge_v1_8_1_patch.py` (mirror `merge_v1_7_0_patch.py`): add the Librarian under
`attachment_architecture.cast_attachments_v1_8_1_additions` + `personas_additions.spirit_mages.the-librarian`
+ `spells_additions.librarian` (4 spells). Run merge → `city_of_mages_grimoire_v1_8_1.json`.
**Re-pin to IPFS + update `agentprivacy_master/src/lib/grimoire-ipfs.ts` = a manual user step** (flag it;
do not push/pin without explicit ask).

**30f · Manifests + admission chronicle** — UPDATE `agentprivacy_master/docs/tomes/BOUND_COLLECTION_MANIFEST.md`
(file count, total words, Tome VIII Act 6 row, cast roster +the Librarian) and `docs/tomes/README.md`
(admissions). CREATE `cityofmages/chronicles/2026-06-21_librarian_admitted_the_wikis_open.md` mirroring
the Archivist admission chronicle.

### INSTRUCTION 31 — guide section · the git-less flow · P1
`agentprivacy_master/src/app/guide/` — a new section on landing `page.tsx` (after §5 Drake Island) or a
sub-route `/guide/fedwiki-onboarding`, framed as a visit to the Librarian's Wikis. Four-beat journey:
1. **Directed** — pointed at a fedwiki URL (skill.fedwiki.club).
2. **Read** — the agent reads the `…Skill` pages (no clone, no install).
3. **Materialize** — `fedwiki-to-skill` writes `SKILL.md` locally on demand (checking the book out).
4. **Build** — the agent flows straight into building with the forked skills.

Thesis: **a fedwiki URL is a git-less `clone`** — distribution by reference + on-demand materialization;
fedwiki's forking / federation / journaling supply the attribution + versioning git would provide. The
Librarian forks; you never own the shelf.

---

## PHASE 5 — Validation checklist

- [ ] 19 new folders under `guide/`, each valid-YAML `SKILL.md`, each carrying `keeper: librarian` + `upstream`
- [ ] `MAPPING.md` / `README.md` / `CODEX.md` totals all read **156**
- [ ] `plugin.json` lists **4** skillsets incl. `skills_dir: guide`
- [ ] Chronicler SKILL.md carries the Librarian Layer-2 attachment block + the 19-skill loadout; count bumped
- [ ] `meta/agentprivacy-attachment-architecture` records the Librarian (Kind-B, Tower-housed)
- [ ] 5 light-crossref personas each have a one-liner only (no loadout additions)
- [ ] Run `agentprivacy-skills/.yaml_fix_master.py` — all new files parse clean
- [ ] Every `related_skills` / `template_references` entry resolves to a real folder
- [ ] Round-trip: re-run `agentprivacy-wiki-to-skill` on one upstream page, diff vs committed copy
- [ ] `meta/agentprivacy-lattice-coherence/scripts/lattice_coherence_audit.py` exits 0 (Librarian has no vertex claim — confirm)
- [ ] Librarian cast file created (Tower category, primary=Chronicler, kin=Memora/Archivist); sigil 🗃️ unique in grimoire
- [ ] Tome VIII **Act 6** bound (the Second Person Spellbook reflection) + mirrored + `/tomes` count 5→6 + ActCollapsible renders
- [ ] the Wikis recorded as a Tower element in spec 05; two-axis Archivist↔Librarian split stated (keep/fork · sealed/editable)
- [ ] Grimoire v1.8.1 patch merges clean; re-pin + `grimoire-ipfs.ts` update left for the user (NOT auto-pinned)
- [ ] BOUND_COLLECTION_MANIFEST + README + admission chronicle updated; `agentprivacy_master` builds green

---

## Summary table

| # | Action | Target | Note | Pri |
|---|--------|--------|------|-----|
| 1–19 | CREATE | `wikis/agentprivacy-wiki-*` (19) | the Wikis' shelves | P0–P2 |
| 20a | UPDATE | persona/chronicler | seat the Librarian + 19-skill loadout | P0 |
| 20b | UPDATE | meta/attachment-architecture | record Kind-B Tower-housed cast | P1 |
| 21–24 | UPDATE | ambassador, shipwright, architect, pedagogue, weaver | light cross-refs only | P2 |
| 24c | UPDATE | role/narrative-compression, role/academic | cross-refs | P2 |
| 25 | UPDATE | `.claude-plugin/plugin.json` | +wikis-skills skillset | P0 |
| 26 | UPDATE | `MAPPING.md` | totals 137→156 + Wikis section | P0 |
| 27 | UPDATE | `README.md` | counts + Librarian's Wikis layer | P1 |
| 28 | UPDATE | `CODEX.md` | version/totals + Librarian cast | P2 |
| 29 | CREATE | docs/chronicles/2026-06-21_fedwiki_onboarding_flow_chronicle.md | this work | P1 |
| 30a | CREATE | cityofmages/tomes/cast/tower/the-librarian.md (+mirror) | Librarian cast file | P1 |
| 30b | CREATE | tome-viii-the-library/06-the-wikis-and-the-librarian.md (+mirror) | Tome VIII Act 6 = the Second Person Spellbook reflection | P1 |
| 30c | UPDATE | src/app/tomes/page.tsx | wire Act 6 (ActCollapsible) + count 5→6 | P1 |
| 30d | UPDATE | specs/05-…-structural-addendum.md | the Wikis as a Tower element | P1 |
| 30e | CREATE | grimoire v1.8.1 patch + merge script | add Librarian; re-pin = manual user step | P1 |
| 30f | UPDATE/CREATE | BOUND_COLLECTION_MANIFEST.md, README.md, admission chronicle | manifests + chronicle | P1 |
| 31 | CREATE | src/app/guide/ onboarding section/route | the git-less flow | P1 |

---

*"The Archivist keeps what must never change; the Librarian forks what was never ours to keep. Same
Tower, two registers. A fedwiki URL is a git-less clone — the wiki is the source of truth, the SKILL.md
is a book checked out, and the journal is the lineage." — the Wikis thesis.*

**Verify:** [agentprivacy.ai](https://agentprivacy.ai) · [skill.fedwiki.club](https://skill.fedwiki.club) · companion plan: `~/.claude/plans/fedwiki-skills-integration-plan.md`
