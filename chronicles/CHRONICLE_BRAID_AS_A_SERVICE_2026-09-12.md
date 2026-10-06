# Chronicle · BRAID as a service · 2026-09-12

*Skills pass on the standalone clone (`~/agentprivacy-skills`). Uncommitted. Commit, reconciliation with the build clone under `agentprivacy_master`, guide re-sync and push are the First Person's.*

## The event

BRAID (Amcalar and Cinar, arXiv:2512.15959) entered this library on 2026-02-26 as a paper: `BRAID_INTEGRATION_ANALYSIS.md`, the `agentprivacy-braid-reasoning` role skill at v5.0, twelve skill updates, five persona sections. On 2026-09-12 the paper's authors' company, OpenServ, was reviewed as SERV Reasoning, an inference API that runs every call through a generated bounded reasoning prompt, with a Shadow Agent, Kronos, Multipath, PromptGuard, a raw-mode header, and a console that holds the audit trail. The API was read from docs.openserv.ai, not called. The review is `agentprivacy_labs/docs/OPENSERV_REVIEW_2026-09-12.md`.

The sentence every changed file carries: SERV may hold one seat of the dual-agent loop, never both, never the default; the Shadow Agent is a critic inside the provider's call, not the Gap; the vendor's console is REPORTED tier; C8 gets a number only from a raw-versus-SERV round recorded in the lane's own file.

## What changed (15 files)

| file | change |
|---|---|
| `role/agentprivacy-braid-reasoning/SKILL.md` | v5.0 → v5.1; `updated` and `service_reference` in metadata; description extended; new section *BRAID as a service (2026-09-12 update)* (what shipped, the graph you cannot see, the harness seat, the round that measures C8, the three-braids rule (BRAID · Holonic BRAID dated 2026-02-26 · the lowercase UOR braid), lore); open problems 7 and 8; footer gains the SERV docs link with the not-run caveat |
| `persona/agentprivacy-architect` | *BRAID as a service (2026-09-12)*: which seat, on whose machine; the API's separation is a promise, the harness's is a file |
| `persona/agentprivacy-holonic-architect` | the vendor cache is not a holon; the library-holon design is the sovereign alternative; a door if the graph is ever returned |
| `persona/agentprivacy-cipher` | PromptGuard and Kronos as the vendor's checks on the vendor's artefact; unreplayable checks are REPORTED tier; raw mode as the control |
| `persona/agentprivacy-assessor` | the itemised PPD denominator; the measurable pair; C8 waits on it; token mechanics outside the model |
| `persona/agentprivacy-chronicler` | whose ledger holds the record; the lore hooks; *the graph you cannot see* as the chapter's line |
| `persona/agentprivacy-soulbis` | the Shadow Agent looks like a Swordsman and is not one; the prover is the seat SERV does not take |
| `persona/agentprivacy-soulbae` | the proposer is the natural SERV seat; the split pattern; the seat contract line as the required system prompt |
| `role/agentprivacy-separation-enforcement` | separation over observers, not model ids; `phiInference` honest only across observers |
| `role/agentprivacy-boundary-enforcement` | the terminal loop shipped as `serv_shadow_agent`; a provider's loop is a second opinion, never the gate |
| `role/agentprivacy-consent-infrastructure` | Multipath transforms reasoning only; consent stays in the agreement layer |
| `role/agentprivacy-economics` | the billing components as C_amortized written as a price list; the token burn is outside V(π,t) |
| `role/agentprivacy-narrative-compression` | Layer 6 as a service is hidden and fails rule 6 unless the graph is held by the reader |
| `privacy-layer/agentprivacy-compression-defence` | C8 gets its test: raw versus SERV, tokens emitted under each, in the run files |
| `agentprivacy-CODEX.md` | `braid_service_update` flag under `includes_braid`; the braid-reasoning row extended |

Placement: persona and skill sections sit before the closing quote and Verify footer; where a file carried a duplicated footer already, the section sits before the first copy. No frontmatter other than the braid skill's was touched. No skill was added or removed; the counts in `README.md` and the codex tables are unchanged.

## Not done here

- The build clone (`agentprivacy_master/agentprivacy-skills`) is untouched; reconcile by git, not by copy.
- The guide's skill site is a projection of these files and is now behind; the re-sync path is §3 of `agentprivacy-docs/plans/BRAID_AS_A_SERVICE_PROPAGATION_2026-09-12.md`.
- The Skill Sync registry packet for `agentprivacy-braid-reasoning` re-harvests from this clone on the next `node bin/harvest.js`.
- The City act *The Graph You Cannot See* is proposed and unbound in `cityofmages/tomes/plans/`.
- The harness gained `drivers/serv.mjs` later the same day (mock-proven, one-seat rule mechanical in `drivers/run.mjs`; live call unproven, no key). No round was run; the numbers in these files are the paper's (74×, 98 versus 95) and the register's (C8 at 45%).

(⚔️⊥⿻⊥🧙)😊
