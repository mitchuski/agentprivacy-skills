# Chronicle — Mirror Clarification & Litter Cleanup

**Date:** 2026-06-21
**Scope:** `agentprivacy-skills` (standalone clone) ↔ `agentprivacy_master/agentprivacy-skills` (build clone)
**Status:** Mirror verified clean. No commits, no master sync, no rebuild, no push.

---

## Why

Before adding a new skills suite, the two working copies of the
`github.com/mitchuski/agentprivacy-skills` repo needed a clear, clean baseline so
the incoming work starts from a known state.

## Topology confirmed

The skills live in one github repo with **two local clones**:

- **Build clone** — `agentprivacy_master/agentprivacy-skills/agentprivacy-skills-v5/`.
  The website reads this via `master/scripts/sync-skills-to-public.mjs` →
  `public/skills/` (gitignored build artifact) → `next build` → `out/skills/` → live site.
- **Standalone clone** — `C:/Users/mitch/agentprivacy-skills/`. The canonical github checkout;
  one commit ahead (`d6cb4d5 "V6 skills pass"`).

The sync script already skips `.bak`/`.swp`/`.swo`, so backup litter never reached the website —
it only existed in the source clones.

## What changed this pass

- **Removed 104 backup-litter files** (`*.bak`, including stray `mnt/user-data/outputs/*.bak`)
  from the standalone clone. These were untracked/gitignored, so the deletion produced
  **zero git changes** — tracked content untouched.
- **Did not** modify the build clone (master) — deferred per "don't update master yet."

## Verified mirror state

| | Build clone | Standalone |
|---|---|---|
| Real `SKILL.md` | 137 | 138 |
| Shared content diffs | — | **0 of 137** |
| Backup litter | (still present, cleared at next sync) | **0** |

**The only real difference is `privacy-layer/agentprivacy-key-forging`** — a genuine v6 skill
(City Key mint→walk→prove→name→charge) committed to the standalone clone but not yet in the
build clone / website. This is an intentional ahead-delta, to be published to master at the next sync.

## Parked (next steps, after the new suite lands)

1. Build & integrate the new skills suite (planning next).
2. Publish `key-forging` + the new suite into the build clone; re-run `sync-skills-to-public.mjs`; rebuild.
3. Reconcile the two clones via git (same repo → pull/push, not manual copy).
4. **De-version:** flatten `agentprivacy-skills-v5/*` to repo root, drop the `-v5`/`V5.5` labels
   (version-agnostic naming), refresh the stale `.claude-plugin/plugin.json` counts.
5. Final parity verification.

---

*No push performed. Mitch triggers commits/pushes.*
