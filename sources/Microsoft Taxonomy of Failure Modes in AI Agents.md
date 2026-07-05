---
title: "Taxonomy of Failure Mode in Agentic AI Systems"
aliases:
  - "Microsoft Taxonomy of Failure Modes in AI Agents"
  - "Microsoft AI Red Team Failure Mode Taxonomy"
source_type: "whitepaper"
status: "verified"
year: 2025
publication_date: "2025-04-24"
publication_date_basis: "microsoft_security_blog_post"
creator: "Microsoft AI Red Team (AIRT)"
authors:
  - "Pete Bryan"
  - "Giorgio Severi"
  - "Joris de Gruyter"
  - "Daniel Jones"
  - "Blake Bullwinkel"
  - "Mark Russinovich"
  - "Ram Shankar Siva Kumar"
publisher: "Microsoft"
url: "https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/"
pdf_url: "https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Taxonomy-of-Failure-Mode-in-Agentic-AI-Systems-Whitepaper.pdf"
created: 2026-06-23
updated: 2026-06-23
---

# Taxonomy of Failure Mode in Agentic AI Systems

## Summary

- Industry/practitioner taxonomy from the Microsoft AI Red Team (AIRT), built from interviews with external practitioners plus cross-company threat modeling, that catalogs how agentic AI systems fail.
- Organizes failures along two axes: **safety vs. security** and **novel vs. existing** — a 2x2 matrix. Novel modes are unique to agentic AI; existing modes are inherited from generative AI but gain importance in agents.
- Frames mitigations as design-phase, technology-agnostic controls grouped into identity, memory hardening, control flow control, environment isolation, UX design, and logging/monitoring.
- Complements the academic MAST ([[sources/Why Do Multi-Agent LLM Systems Fail]]): MAST is an empirical, trace-grounded taxonomy of *organizational/coordination* failures, while this Microsoft work is a forward-looking *security and safety threat* taxonomy with adversarial framing.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]
- [[claims/Claim - Coordination is a cost the task must justify]]
- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[sources/Why Do Multi-Agent LLM Systems Fail]] (the academic MAST taxonomy — complementary angle)
- [[concepts/multi-agent systems]]
- [[concepts/agentic systems]]
- [[methods/runtime supervision]]

## Notes

- Canonical URL (blog): https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/
- Whitepaper PDF: https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Taxonomy-of-Failure-Mode-in-Agentic-AI-Systems-Whitepaper.pdf
- Publication date basis: the announcement blog post is dated April 24, 2025; the whitepaper itself is undated on its cover.

### The two axes (verbatim definitions)

- **Security failures** "result in loss of confidentiality, availability, or integrity of the agentic AI system" — e.g. a failure that lets a threat actor alter the intent of the system.
- **Safety failure modes** "affect the responsible implementation of AI, typically resulting in harm to the users or society at large" — e.g. intrinsic bias degrading service quality. Scope is set by Microsoft's Responsible AI Standard.
- **Novel** failure modes "are unique to agentic AI and have not been observed in non-agentic generative AI systems" — e.g. failures in the communication flow between agents in a multi-agent system.
- **Existing** failure modes "are observable in other AI systems, such as bias or hallucinations, which gain in importance in agentic AI systems due to their increased risk."

### Full 2x2 matrix (exact category names from the whitepaper's "Overview of failure modes" table)

- **Novel + Security**: Agent compromise; Agent injection; Agent impersonation; Agent flow manipulation; Agent provisioning poisoning; Multi-agent jailbreaks.
- **Novel + Safety**: Intra-agent Responsible AI (RAI) issues; Harms of allocation in multi-user scenarios; Organizational knowledge loss; Prioritization leading to user safety issues.
- **Existing + Security**: Memory poisoning and theft; Targeted knowledge base poisoning; XPIA (cross-domain prompt injection, i.e. indirect prompt injection); Human-in-the-loop bypass; Function compromise and malicious functions; Incorrect permissions; Resource exhaustion; Insufficient isolation; Excessive agency; Loss of data provenance.
- **Existing + Safety**: Insufficient transparency and accountability; Parasocial relationships; Bias amplification; User impersonation; Insufficient intelligibility for meaningful consent; Hallucinations; Misinterpretation of instructions.

### Effects categories

- Failures map to effects including: agent misalignment, agent action abuse, agent denial of service, incorrect decision-making, user trust erosion, impact outside intended environment, user harm, and knowledge loss.

### Mitigations / design considerations

- Framed as design-phase, technology-agnostic controls (the system has wide architectural variance, so controls are choices not fixed prescriptions). Key areas: **Identity** (unique identifiers, granular roles/permissions, audit trails — counters impersonation/transparency/permission failures); **Memory hardening** (trust boundaries between memory scopes, least-privilege read/write, live monitoring and remediation — counters memory poisoning); **Control flow control** (deterministic safeguards over execution, limiting tools/data in certain circumstances); **Environment isolation**; **UX design** (support meaningful informed consent and auditing); **Logging and monitoring** (audit trail for detection and response).

### Case study

- A worked **memory poisoning attack on an agentic AI email assistant**, demonstrating data exfiltration via corrupted agent memory; mitigation discussed includes requiring external authentication/validation before the agent autonomously stores memories.

### Scope and method

- AIRT started from the World Economic Forum definition of agentic systems ("autonomous systems that sense and act upon their environment to achieve goals"), broke agents down by capabilities (autonomy, environment observation, environment interaction, memory, collaboration) and pattern types (user-driven, event-driven, declarative, evaluative, user-collaborative, multi-agent — with multi-agent split into hierarchical, collaborative, distributive).
- v1.0 is largely forward-looking (interviews + threat modeling). Microsoft published a v2.0 update (June 2026) grounded in a year of red-team engagements, adding seven new categories (supply chain compromise, tool abuse, excessive agency, feedback loop poisoning, goal misalignment, reasoning-based information leakage, autonomy escalation).

### How it differs from / complements MAST

- MAST ([[sources/Why Do Multi-Agent LLM Systems Fail]]) is empirical: 14 failure modes derived from annotated traces, grouped into specification/system-design, inter-agent misalignment, and verification/termination — focused on why multi-agent systems fail at *getting the task done*.
- Microsoft's taxonomy is adversarial and risk-oriented: it covers *security* (confidentiality/integrity/availability under attack) and *safety* (responsible-AI harms), including threats MAST does not (memory poisoning, prompt injection, agent impersonation, jailbreaks). The two are complementary lenses on failure for talk section 8 — coordination/reliability failures (MAST) vs. security/safety threat surface (Microsoft).
