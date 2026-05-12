# Chronicle — City of Mages Grimoire Pin Sync

**Date:** 2026-05-10
**Author:** privacymage
**License:** CC BY-SA 4.0

---

## What landed

The mirror at `grimoire/city_of_mages_grimoire_v1_1_0.json` was re-synced from the canonical `agentprivacy-docs/models/city_of_mages_grimoire_v1_1_0.json`. The only material diff: the `ipfs_pin_status` field, which now records the live pin instead of the pre-pin placeholder.

```
v1.1 PINNED 2026-05-10 at
https://sync.agentprivacy.ai/ipfs/bafkreidv7cwwlcnuzw3eyhcbbvoccy7do2lmwrmmtrszn62ninzxj3idti
```

Exported as `CITY_OF_MAGES_GRIMOIRE_IPFS_URL` from `agentprivacy_master/src/lib/grimoire-ipfs.ts`. The pin is content-addressed — future v1.2 will get its own CID; the v1.1 CID resolves indefinitely.

---

## What did not change

- `README.md`, `MAPPING.md` Post-V5.4 Addendum, and `MAPPING_V5_4_REPOS_2026-04-12.md` 2026-05-09 addendum already describe the City of Mages cast, the Priest tier, and the grimoire mirror — they make no pre-pin claim that needed correction.
- The 38 abstract role-personas remain canonical. Full skill regeneration to incorporate the named cast as discrete persona-skills is still deferred to a future v5.5 release.

---

## Source canonical references

- Canonical grimoire: `agentprivacy-docs/models/city_of_mages_grimoire_v1_1_0.json`
- Pin chronicle (master): `agentprivacy_master/docs/chronicles/2026-05-10_city_of_mages_grimoire_pinned_chronicle.md`
- Resume document: `agentprivacy_master/docs/chronicles/2026-05-10_resume_here_chronicle.md`

---

*(⚔️⊥⿻⊥🧙)😊*

CC BY-SA 4.0 · privacymage · 2026-05-10
