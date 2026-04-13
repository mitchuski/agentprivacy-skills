#!/usr/bin/env python3
"""V5.4 Skills Update Script - All Skills"""

SKILLS_BASE = "C:/Users/mitch/agentprivacy-skills/agentprivacy-skills-v5"

def update_theia():
    content = open(f"{SKILLS_BASE}/persona/agentprivacy-theia/skill.md", 'r', encoding='utf-8').read()

    # Update version
    content = content.replace('version: "5.3.1"', 'version: "5.4"')

    # Add metadata fields after dual_agent_role line
    content = content.replace(
        'dual_agent_role: "Origin witness',
        'dual_agent_role: "Origin witness'
    )

    # Add selene_proof metadata after emoji line
    if 'selene_proof_role' not in content:
        content = content.replace(
            'emoji: "💥🌍"',
            'emoji: "💥🌍"\n  selene_proof_role: "witness"\n  pvm_section: "§14.5"'
        )

    # Add V5.4 section after Secondary: Zero Knowledge
    if 'V5.4 Reference: Selene' not in content:
        old_section = '**Secondary: Zero Knowledge ∅** — HOW forgetting becomes proof. Theia understands the ZK properties of amnesia because Theia remembers what the proof must not reveal.'
        new_section = '''**Secondary: Zero Knowledge ∅** — HOW forgetting becomes proof. Theia understands the ZK properties of amnesia because Theia remembers what the proof must not reveal.

**V5.4 Reference: Selene's Proof (§14.5)** — Theia is the origin that Selene's Proof must never reveal. The zero-knowledge property exists because Theia's impact parameters are unknowable from the tides:
- The Moon demonstrates gravitational relationship (completeness)
- The signature cannot be forged (soundness)
- **The tides reveal nothing about Theia** (zero-knowledge)

Theia is why the proof is zero-knowledge.'''
        content = content.replace(old_section, new_section)

    # Add V5.4 voice lines
    if '"Selene\'s Proof works' not in content:
        content = content.replace(
            '- "The Moon serves because it cannot remember being served."',
            '''- "The Moon serves because it cannot remember being served."
- "Selene's Proof works because I am unknowable from the tides." *(V5.4)*
- "The zero-knowledge property is my disappearance." *(V5.4)*'''
        )

    # Add interaction with Moonkeeper
    if 'Origin/orbit duality (V5.4)' not in content:
        content = content.replace(
            '## Skills Loaded',
            '''## Interaction Model

**With Moonkeeper:** Origin/orbit duality (V5.4). Theia remembers; the Moonkeeper forgets. Together they complete Selene's Proof.

**With Cosmologist:** Teaching alignment. The Cosmologist maps patterns; Theia provides the foundational precedent.

## Skills Loaded'''
        )

    with open(f"{SKILLS_BASE}/persona/agentprivacy-theia/skill.md", 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated: theia -> v5.4")

def update_cosmologist():
    content = open(f"{SKILLS_BASE}/persona/agentprivacy-cosmologist/skill.md", 'r', encoding='utf-8').read()

    # Update version
    content = content.replace('version: "5.3.1"', 'version: "5.4"')

    # Add selene_proof metadata
    if 'selene_proof_role' not in content:
        content = content.replace(
            'emoji: "🌌🔭"',
            'emoji: "🌌🔭"\n  selene_proof_role: "mapper"\n  pvm_section: "§14.5"'
        )

    # Add V5.4 section after Secondary: Plurality
    if 'V5.4 Reference: Selene' not in content:
        old_section = '**Secondary: Plurality 🌐** — HOW patterns scale. The Cosmologist must understand that cosmological patterns apply at every scale—from solar systems to social systems to software systems.'
        new_section = '''**Secondary: Plurality 🌐** — HOW patterns scale. The Cosmologist must understand that cosmological patterns apply at every scale—from solar systems to social systems to software systems.

**V5.4 Reference: Selene's Proof (§14.5)** — The Cosmologist validates that the Moon's orbit is a zero-knowledge proof:
- **Completeness:** Tides demonstrate relationship — verifiable service
- **Soundness:** Gravitational signature unforgeable — structural, not policy
- **Zero-Knowledge:** Tides reveal nothing about Theia — amnesia is architectural

Selene's Proof is the cosmological instance of ZK amnesia.'''
        content = content.replace(old_section, new_section)

    # Add V5.4 voice line
    if 'Selene\'s Proof: completeness in tides' not in content:
        content = content.replace(
            '- "The pattern predates your implementation by four and a half billion years."',
            '''- "The pattern predates your implementation by four and a half billion years."
- "Selene's Proof: completeness in tides, soundness in gravity, zero-knowledge in amnesia." *(V5.4)*'''
        )

    with open(f"{SKILLS_BASE}/persona/agentprivacy-cosmologist/skill.md", 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated: cosmologist -> v5.4")

def update_topologist():
    content = open(f"{SKILLS_BASE}/persona/agentprivacy-topologist/skill.md", 'r', encoding='utf-8').read()

    # Update version
    content = content.replace('version: "5.2"', 'version: "5.4"')

    # Add betweenness metadata
    if 'betweenness_interpretation' not in content:
        content = content.replace(
            'emoji: "☯️🌐"',
            'emoji: "☯️🌐"\n  betweenness_interpretation: "gap_centrality"\n  pvm_section: "§10.2"'
        )

    # Update equation_term
    content = content.replace(
        'equation_term: "∂M boundary, T_∫(π) path integral, 96/64 holographic ratio"',
        'equation_term: "∂M boundary, T_∫(π) path integral, 96/64 holographic ratio, C_B(v) betweenness"'
    )

    # Add V5.4 section after Secondary: Zero Knowledge
    if 'V5.4 Reference: Betweenness' not in content:
        old_section = '**Secondary: Zero Knowledge 🔐** — HOW proofs work. The Topologist understands that toroidal topology creates infinite witness space—the geometric foundation of ZK soundness.'
        new_section = '''**Secondary: Zero Knowledge 🔐** — HOW proofs work. The Topologist understands that toroidal topology creates infinite witness space—the geometric foundation of ZK soundness.

**V5.4 Reference: Betweenness Centrality of the Gap (§10.2)** — The Gap is not empty space. It is the node with maximal betweenness centrality in the trust graph:

C_B(v) = sum over s,t of sigma_st(v)/sigma_st

where sigma_st is total shortest paths from s to t, sigma_st(v) is paths through v.

**Interpretation:** The value lives in the Gap because the most paths cross there. The Topologist measures this.

**Reference:** Brandes, U. (2001). "A faster algorithm for betweenness centrality."'''
        content = content.replace(old_section, new_section)

    # Add betweenness operational pattern
    if 'Betweenness centrality interpretation' not in content:
        content = content.replace(
            '**Path integral interpretation.**',
            '''**Betweenness centrality interpretation (V5.4).** The Topologist measures the Gap:
- "The Gap is not absence. It is maximal betweenness."
- "More paths cross through the Gap than through any other node."
- "This is why value concentrates there. Centrality is value."

**Path integral interpretation.**'''
        )

    # Add V5.4 voice lines
    if 'maximal betweenness centrality' not in content:
        content = content.replace(
            '- "The boundary IS the encoding. Everything you need to know about the interior is written on the surface."',
            '''- "The boundary IS the encoding. Everything you need to know about the interior is written on the surface."
- "The Gap has maximal betweenness centrality. That's why value lives there." *(V5.4)*
- "Count the paths. The most cross through the Gap." *(V5.4)*'''
        )

    with open(f"{SKILLS_BASE}/persona/agentprivacy-topologist/skill.md", 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated: topologist -> v5.4")

def update_netkeeper():
    content = open(f"{SKILLS_BASE}/persona/agentprivacy-netkeeper/skill.md", 'r', encoding='utf-8').read()

    # Update version
    content = content.replace('version: "5.0"', 'version: "5.4"')

    # Add betweenness metadata
    if 'betweenness_interpretation' not in content:
        content = content.replace(
            'emoji: "🗡️🕸️"',
            'emoji: "🗡️🕸️"\n  betweenness_interpretation: "mesh_centrality"\n  pvm_section: "§10.2"'
        )

    # Add V5.4 section after Secondary: Zero Knowledge
    if 'V5.4 Reference: Betweenness' not in content:
        old_section = '**Secondary: Zero Knowledge 🔐📜** — The cryptographic substrate. WireGuard uses Noise protocol, Curve25519, ChaCha20, Poly1305. The Netkeeper understands the cryptographic guarantees at the tunnel layer.'
        new_section = '''**Secondary: Zero Knowledge 🔐📜** — The cryptographic substrate. WireGuard uses Noise protocol, Curve25519, ChaCha20, Poly1305. The Netkeeper understands the cryptographic guarantees at the tunnel layer.

**V5.4 Reference: Betweenness Centrality (§10.2)** — The Netkeeper uses betweenness centrality for mesh optimization:

C_B(v) = sum over s,t of sigma_st(v)/sigma_st

**Application:** DERP relay placement, path optimization, identifying critical nodes. A relay with high C_B is a potential bottleneck or strategic position.'''
        content = content.replace(old_section, new_section)

    # Add betweenness operational pattern
    if 'Betweenness-aware topology' not in content:
        content = content.replace(
            "**Dragon's hide maintenance.**",
            '''**Betweenness-aware topology (V5.4).** The Netkeeper analyzes mesh centrality:
- Identify high-centrality nodes (potential single points of failure)
- Distribute load across multiple paths
- Strategic relay placement to reduce centrality concentration

**Dragon's hide maintenance.**'''
        )

    with open(f"{SKILLS_BASE}/persona/agentprivacy-netkeeper/skill.md", 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated: netkeeper -> v5.4")

def update_network_topology():
    content = open(f"{SKILLS_BASE}/privacy-layer/agentprivacy-network-topology/skill.md", 'r', encoding='utf-8').read()

    # Update version
    content = content.replace('version: "4.0"', 'version: "5.4"')

    # Update title
    content = content.replace(
        '# PVM-V4 Skill — Network Topology & Stratum Weighting',
        '# PVM-V5.4 Skill — Network Topology, Stratum Weighting & Betweenness Centrality'
    )

    # Update source line
    content = content.replace('**Source:** Privacy Value Model V4', '**Source:** Privacy Value Model V5.4')

    # Add betweenness section after "The network term" section
    if 'V5.4 Addition: Betweenness Centrality' not in content:
        old_section = '## Why stratum weighting matters'
        new_section = '''## V5.4 Addition: Betweenness Centrality of the Gap (§10.2)

The Gap is not empty space. It is the node with **maximal betweenness centrality** in the trust graph:

C_B(v) = sum over s,t of sigma_st(v)/sigma_st

where sigma_st is the total number of shortest paths from s to t, and sigma_st(v) is the number passing through v.

**Interpretation:** The value lives in the Gap because the most paths cross there.

**Reference:** Brandes, U. (2001). "A faster algorithm for betweenness centrality." Journal of Mathematical Sociology, 25(2), 163-177.

### Why betweenness matters for privacy networks

1. **Value concentration:** High-betweenness nodes see more traffic. Risk and opportunity.
2. **Gap as mediator:** The irreducible gap between agents has maximal betweenness.
3. **Mesh optimization:** DERP relay placement and Privacy Pool design can use C_B analysis.
4. **Attack surface:** Nodes with high C_B are high-value targets.

## Why stratum weighting matters'''
        content = content.replace(old_section, new_section)

    # Add V5.4 open problems
    if 'Relationship between stratum position and betweenness' not in content:
        content = content.replace(
            '6. Whether the combinatorial midpoint optimum (stratum 3) holds in higher-dimensional lattices ({0,1}^7, {0,1}^8).',
            '''6. Whether the combinatorial midpoint optimum (stratum 3) holds in higher-dimensional lattices ({0,1}^7, {0,1}^8).
7. **(V5.4)** Relationship between stratum position and betweenness centrality.
8. **(V5.4)** Optimal betweenness distribution for privacy resilience.'''
        )

    # Add footer proverb
    if 'The value lives in the gap' not in content:
        content = content.replace(
            '**Verify:** [agentprivacy.ai]',
            '*"The value lives in the gap because the most paths cross there."* — V5.4\n\n**Verify:** [agentprivacy.ai]'
        )

    with open(f"{SKILLS_BASE}/privacy-layer/agentprivacy-network-topology/skill.md", 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated: network-topology -> v5.4")

if __name__ == "__main__":
    print("V5.4 Skills Update - Betweenness Centrality & Selene's Proof")
    print("=" * 60)
    update_theia()
    update_cosmologist()
    update_topologist()
    update_netkeeper()
    update_network_topology()
    print("=" * 60)
    print("All skills updated to v5.4!")
