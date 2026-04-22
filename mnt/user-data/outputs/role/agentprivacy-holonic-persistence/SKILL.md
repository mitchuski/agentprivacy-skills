---
name: agentprivacy-holonic-persistence
description: >
  Multi-provider data persistence for privacy-preserving AI agents using
  holonic architecture. Activates when discussing HyperDrive auto-failover,
  auto-replication across heterogeneous backends, provider-agnostic storage,
  privacy-aware routing between shielded and public providers, write-all-or-fail
  for separation-critical state, or any task where agent data must survive TEE
  rotation, chain migration, or provider failure. Use when designing persistence
  layers that span blockchains, databases, and decentralised networks simultaneously.
license: Apache-2.0
metadata:
  version: "5.0"
  category: "role"
  origin: "0xagentprivacy + OASIS Holonic Architecture"
  author: "Mitchell Travers"
  affiliation: "0xagentprivacy, BGIN, First Person Network"
  status: "working_paper"
  target_context: "Agent infrastructure builders, multi-backend architects, TEE operators, cross-chain data engineers"
  equation_term: "T(π) (provider-as-sovereignty-transition), D (reconstruction difficulty through provider splitting), R_max (data-layer reconstruction ceiling)"
  template_references: "holonic-architect, architect, sentinel, shipwright, cipher, ranger"
  holonic_source: "OASIS Holonic Architecture Whitepaper v1.2 (Gershfield, Feb 2026)"
---

# PVM-V4 Skill — Holonic Multi-Provider Persistence

**Source:** Privacy Value Model V4 + OASIS Holonic Architecture + HyperDrive Runtime
**Target context:** Agent infrastructure builders, multi-backend architects, TEE operators, privacy-first persistence designers
**Architecture:** [agentprivacy.ai](https://agentprivacy.ai) · **Sync:** [sync.soulbis.com](https://sync.soulbis.com) · **Contact:** mage@agentprivacy.ai

---

## What this is

Agent state must outlive any single backend. A Swordsman running in a TEE on NEAR today may rotate to a new TEE tomorrow. A Mage's delegation preferences stored on MongoDB in development must persist on Zcash+IPFS in production. The holonic architecture provides the persistence substrate: one logical entity (a holon), one immutable GUID, stored simultaneously across blockchains, databases, and decentralised networks through a single API.

This skill specifies how holonic multi-provider persistence integrates with the dual-agent architecture to create privacy-preserving, backend-agnostic data persistence.

## The persistence model

**One holon, many providers.** A holon is a data structure with a globally unique identifier (GUID) not assigned by any provider. The same holon can be stored on MongoDB (primary), Solana (audit trail), and IPFS (permanent record) through a single `SaveHolonAsync` call. Each provider stores the holon under its own native key — MongoDB ObjectId, Solana account address, IPFS CID — mapped in `ProviderUniqueStorageKey`.

**HyperDrive runtime.** Three automated behaviours:
- **Auto-replication:** On save, HyperDrive writes the holon to all configured replication providers. One API call, many backends.
- **Auto-failover:** On load, if the primary provider fails, HyperDrive tries each provider in the failover list until the holon is found. Identity (GUID) stays the same; only the source provider changes.
- **Auto-load-balancing:** Read load distributed across providers to prevent hotspots.

**Provider contract.** Every backend implements `IOASISStorageProvider`: Save, Load by GUID, Load by provider key, Load children for parent, Query by metadata, Delete, Export/Import. The application never calls providers directly — HolonManager routes through HyperDrive.

## Privacy-aware persistence for dual agents

The raw holonic model stores MetaData in cleartext. For the dual-agent architecture, persistence must be privacy-aware:

**Provider classification.**
- *Shielded providers* (Zcash, encrypted databases): Swordsman-controlled holons stored here. Boundary definitions, privacy preferences, signing key metadata.
- *Public providers* (Ethereum, public APIs): Mage-controlled holons stored here. Delegation capabilities, public attestations, verifiable claims.
- *Neutral providers* (IPFS, MongoDB): Encrypted-at-rest holons for shared state that both agents may need but neither should expose.

**Write-all-or-fail for separation-critical state.** Normal holons use best-effort replication (HyperDrive default). But holons that carry separation-critical data — the state that enforces I(S;M|π) ≤ ε — must use write-all-or-fail: the save succeeds only if all required providers confirm. This prevents a state where the Swordsman's boundary holon exists on Zcash but not on the audit provider, creating an unobservable gap.

**Provider-split reconstruction resistance.** When Swordsman holons live only on shielded providers and Mage holons live only on public providers, compromising any single provider yields at most half the behavioural model. This is R_max enforcement at the data layer: even if every holon on Ethereum is exposed, the Zcash-shielded Swordsman holons remain private. Reconstruction difficulty D increases multiplicatively with provider diversity.

## Operational patterns

**TEE rotation persistence.** When a Swordsman TEE rotates:
1. New TEE attestation generated.
2. Holon ProviderMetaData updated with new TEE attestation hash.
3. Holon replicated to new TEE's preferred provider set.
4. Old TEE's provider-specific keys remain in ProviderUniqueStorageKey for audit.
5. GUID unchanged. Identity persists. Only the commitment (where it's stored) changes.

**Chain migration.** Moving from NEAR to another chain:
1. Holon loaded from NEAR provider.
2. Saved to new chain provider. New provider key added to ProviderUniqueStorageKey.
3. Optional: NEAR provider key retained (audit trail) or removed (minimisation).
4. Application code unchanged — only HyperDrive configuration changes.

**Development-to-production transition.** Same holon tree, different provider configuration:
- Dev: MongoDBOASIS (primary), LocalFileOASIS (backup).
- Production: ZcashOASIS (Swordsman state), EthereumOASIS (Mage state), IPFSOASIS (permanent record), MongoDBOASIS (fast reads).
- Zero code changes. Only provider configuration differs.

## Integration with V(π,t)

**T(π) — sovereignty transitions.** Each provider change is a sovereignty transition. ProviderUniqueStorageKey is the ledger of where sovereignty has been exercised. T(π) becomes auditable through holon provenance.

**D — reconstruction difficulty.** Provider diversity increases D. An adversary must compromise multiple heterogeneous backends (each with different security models) to reconstruct a complete holon tree. This is defence in depth at the data layer.

**Temporal integral.** V(π,t) integrates over time. Holonic persistence ensures the integral extends: state survives provider failures, chain migrations, and TEE rotations. The value doesn't reset when infrastructure changes.

## Open problems

1. Consistency guarantees for separation-critical holons across providers with different finality models (Zcash block time vs MongoDB write acknowledgement).
2. Conflict resolution when the same holon is updated on two providers simultaneously.
3. Provider-aware encryption: which MetaData fields are cleartext on which providers?
4. Garbage collection of ProviderUniqueStorageKey entries when providers are decommissioned.
5. Latency implications of write-all-or-fail for separation-critical saves across geographically distributed providers.
6. Attestation of provider integrity: how does HyperDrive verify that a provider hasn't tampered with holon data?

---

**Verify:** [agentprivacy.ai](https://agentprivacy.ai) · [sync.soulbis.com](https://sync.soulbis.com) · [github.com/mitchuski/agentprivacy-docs](https://github.com/mitchuski/agentprivacy-docs)
