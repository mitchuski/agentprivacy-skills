---
name: agentprivacy-holonic-identity
description: >
  Identity-independent data structures for 0xagentprivacy. Activates when
  discussing GUIDs not derived from any provider, the three-layer identity model
  (data GUID / relationship VRC / principal DID), ProviderUniqueStorageKey as
  commitment map, identity vs commitments separation at the data layer, immutable
  vs versioned holons, or how data identity persists when storage infrastructure
  changes. Use when designing systems where identity must outlive any single
  backend, chain, or registry.
license: Apache-2.0
metadata:
  version: "5.0"
  category: "role"
  origin: "0xagentprivacy + OASIS Holonic Architecture"
  author: "Mitchell Travers"
  affiliation: "0xagentprivacy, BGIN, First Person Network"
  status: "working_paper"
  target_context: "Decentralised identity architects, DID/VC implementers, data sovereignty designers, chain-agnostic identity builders"
  equation_term: "A(τ) (identity that persists across migrations), Identity vs Commitments (data-layer separation)"
  template_references: "holonic-architect, architect, gatekeeper, priest, ambassador, witness"
  holonic_source: "OASIS Holonic Architecture Whitepaper v1.2 (Gershfield, Feb 2026)"
---

# PVM-V4 Skill — Holonic Identity-Independent Data Structures

**Source:** Privacy Value Model V4 + OASIS Holonic Architecture + W3C DIDs + VRC Protocol
**Target context:** Decentralised identity architects, DID/VC implementers, data sovereignty designers, chain-agnostic builders
**Architecture:** [agentprivacy.ai](https://agentprivacy.ai) · **Sync:** [sync.soulbis.com](https://sync.soulbis.com) · **Contact:** mage@agentprivacy.ai

---

## What this is

Identity in current systems is almost always derived from infrastructure: a MongoDB ObjectId, a Solana account address, an IPFS CID, an Ethereum address. Change the infrastructure, lose the identity. This creates lock-in, fragility, and sovereignty loss — the exact conditions the surveillance economy exploits.

Holonic architecture introduces identity-independent data structures: every holon has a globally unique identifier (GUID) assigned at creation that is immutable for the lifetime of the entity and not derived from any single provider, chain, or database. The GUID IS the identity. Everything else — the MongoDB ObjectId, the Solana address, the IPFS CID — are *commitments*: evidence of where the entity has been stored, not what it is.

This skill specifies how identity-independent data structures integrate with the 0xagentprivacy identity ecosystem (VRCs, DIDs, RPP) to create a complete, three-layer identity model.

## The three-layer identity model

The agentprivacy + holonic integration produces three distinct identity layers, each solving a different problem:

**Layer 1: Data Identity (Holonic GUID).** What the data IS. A globally unique identifier for every persistable entity — agent memory, reasoning graphs, credential stores, configuration, conversation history. Not tied to any chain, database, or network. Immutable. The anchor.

**Layer 2: Relationship Identity (VRC).** What the entity MEANS in context. A Verifiable Relationship Credential records a bilateral relationship between principals. VRCs are themselves stored as holons (with GUIDs), but their semantic content — the proverb, the trust assertion, the relationship record — is the identity of the *connection*, not the *container*.

**Layer 3: Principal Identity (DID/Agent ID).** WHO the entity belongs to. W3C DIDs for persons. ERC-8004 for trustless agent identity. These identify the *actors* — the Swordsman, the Mage, the Person — not the data they produce or the relationships they hold.

**Why three layers matter.** Conflating these layers creates the vulnerabilities that surveillance capitalises on:
- If data identity = infrastructure key (MongoDB ObjectId), changing infrastructure loses the data's history. No A(τ).
- If relationship identity = platform account, deplatforming destroys trust records. No bilateral sovereignty.
- If principal identity = chain address, chain migration requires rebuilding reputation from zero.

Three separate layers mean: infrastructure can change (GUID persists), platforms can change (VRCs persist), chains can change (DIDs resolve across registries). Sovereignty at every level.

## Identity vs commitments

The holonic model makes explicit what Promise Theory implies: identity and commitments are separate concerns.

**Identity (stable):**
- `Id` (GUID) — what the holon IS
- `HolonType` — what kind of entity
- `ParentHolonId` — structural position
- `MetaData` — semantic content

**Commitments (mutable):**
- `ProviderUniqueStorageKey` — where it's stored (MongoDB ObjectId, Solana address, IPFS CID)
- `ProviderMetaData` — transaction hashes, document versions, TEE attestations
- `CreatedProviderType` / `InstanceSavedOnProviderType` — provenance

This mirrors the PVM-V4 principle: what you ARE (privacy preferences, relationship patterns, demonstrated understanding) is not the same as where you are STORED (which chain, which database, which TEE). Commitments change when infrastructure changes. Identity does not.

**Promise Theory connection.** Each provider makes a voluntary promise: "I will store and retrieve this holon faithfully." The holon does not impose — it offers a standard interface. The provider's commitment (storing the holon under its native key) is evidence of that promise. Multiple providers making the same promise about the same holon create redundancy through voluntary cooperation, not centralised mandate.

## Immutable vs versioned holons

Not all holons need the same persistence semantics:

**Immutable holons** — for commitments that must never change:
- ZK proof holons (Groth16 verification keys, circuit outputs)
- VRC issuance records
- Zcash inscription holons (proverb inscriptions)
- Ceremony records (key generation events)
- Published credential holons

**Versioned holons** — for state that evolves:
- Agent memory holons (conversation history, learned preferences)
- Reputation score holons (updated with each interaction)
- Configuration holons (privacy preferences, delegation scope)
- Reasoning graph holons (refined through use)

`HolonType` distinguishes the two. `Version`, `PreviousVersionId`, and `PreviousVersionProviderUniqueStorageKey` create an auditable history chain for versioned holons. For immutable holons, version is always 1 and modification is rejected.

## Integration with VRC lifecycle

VRCs stored as holons gain holonic properties:

**Issuance.** VRC created as an immutable holon. GUID assigned. Stored on Zcash (shielded memo field) and Ethereum (public registry, if selective disclosure permits). ProviderUniqueStorageKey maps: `ZcashOASIS → tx_hash`, `EthereumOASIS → contract_address`.

**Verification.** Verifier loads VRC holon by GUID or by provider key. HyperDrive handles failover: if Ethereum node is down, Zcash transaction provides the same VRC.

**Revocation.** Revocation is a new holon (immutable) pointing to the original VRC holon's GUID. Not modification — creation. The original VRC holon remains unchanged (audit trail). The revocation holon is its own entity with its own GUID.

**Migration.** VRC moves from one chain to another. New ProviderUniqueStorageKey entry added. Old entry retained for provenance. GUID unchanged. The VRC's identity outlives any single chain.

## The sovereignty preservation principle

Identity independence is sovereignty preservation at the data layer:

**Without holonic identity:** Migrating from Ethereum to NEAR requires new addresses, new identity anchors, rebuilding credential graphs. The person must re-prove who they are. Sovereignty restarts from zero.

**With holonic identity:** Migrating from Ethereum to NEAR adds a new entry to ProviderUniqueStorageKey. The GUID persists. The VRC holons persist. The reputation holons persist. A(τ) — temporal memory — is unbroken. Sovereignty compounds rather than resets.

This is the data-layer expression of the PVM-V4 temporal integral: V(π,t) = ∫₀^∞ because identity never restarts.

## Open problems

1. GUID collision probability and resolution across billions of holons.
2. Cross-system GUID discovery: how does an external system find a holon by GUID without knowing which provider to query?
3. GUID-to-DID binding: formally linking a holon's GUID to its owner's DID without creating a surveillance surface.
4. Privacy of the ProviderUniqueStorageKey map: the key map itself reveals which providers (chains) a person uses.
5. Identity persistence through provider compromise: if a provider is compromised, which holon properties can be trusted?
6. GUID as dark-forest liability: unique identifiers enable correlation. How to use holonic identity without creating trackable fingerprints?

---

**Verify:** [agentprivacy.ai](https://agentprivacy.ai) · [sync.soulbis.com](https://sync.soulbis.com) · [github.com/mitchuski/agentprivacy-docs](https://github.com/mitchuski/agentprivacy-docs)
