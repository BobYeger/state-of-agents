# Who's Asking? Identity Delegation for AI Agents and Service Meshes — structured capture

- Canonical URL: https://engineering.block.xyz/blog/whos-asking-identity-delegation-for-ai-agents-and-service-meshes
- Authors: Franco Sola; Brett Caley; Cea Stapleton Cordasco
- Publisher: Block Engineering
- Publication date: 2026-07-06
- Captured: 2026-08-02
- Extraction: Defuddle CLI with Markdown output
- Capture mode: metadata, structure, and claim-level facts; not a verbatim republication

## Core Model

- Delegated requests preserve both the human subject and the software actor rather than collapsing the request into either a shared service identity or user impersonation.
- The decision vocabulary is subject, actor, capability, delegated authority, resource, and decision point.
- Four components carry the model: an edge user-identity issuer, token exchange, a consent control plane, and an authorization data plane.
- Short-lived signed user context can be exchanged for a delegated token with actor attribution for work that outlives the original request.
- The authorization data plane computes effective delegated capabilities as the intersection of the user's current grants and the capabilities the user consented to delegate to that actor.
- Consent can only narrow existing authority. It cannot create authority, and revocation is evaluated at decision time.

## Design Implications

- The downstream service remains responsible for its resource-specific authorization decision.
- Subject and actor should remain separately visible in audit records.
- Long-running agent work needs renewable, actor-bound delegation rather than a broad standing service identity.
- Resource owners may need non-delegable capabilities or stronger assurance requirements for sensitive actions.

## Evidence Boundary

- This is a first-party description of Block's internal identity-delegation architecture, not a comparative evaluation.
- The article does not establish that Buzz implements this OAuth/JWT consent plane. Buzz's public Nostr authorization protocol is a separate design with different enforcement and revocation semantics.
