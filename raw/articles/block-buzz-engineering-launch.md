# Buzz! — structured capture

- Canonical URL: https://engineering.block.xyz/blog/buzz
- Author: Tyler Longwell
- Publisher: Block Engineering
- Publication date: 2026-07-21
- Captured: 2026-08-02
- Extraction: Defuddle CLI with Markdown output
- Capture mode: metadata, structure, and claim-level facts; not a verbatim republication

## Architecture Facts

- Buzz is presented as a self-hostable workspace in which humans, agents, repositories, workflows, and decisions share a Nostr event substrate.
- Each participant has a signing key. Agent authorization is intended to preserve the agent as author rather than attributing its work to the owner.
- Claude Code, Codex, goose, and other ACP-compatible harnesses can connect without becoming the durable owner of workspace identity or history.
- Live telemetry and cancellation are described as ephemeral encrypted messages; memory and cost records are encrypted durable messages.
- Feature branches are intended to become temporary channels that collect discussion, patches, CI, review, and the merge decision in one record.

## Multi-Agent Claims

- The author describes using one frontier agent to direct cheaper workers that research, implement, test, and review through ordinary channel mentions.
- Agents reportedly recruit one another, open side channels, and hand off work without those exact behaviors being scripted.
- Shared rooms are argued to reduce human context-ferrying between private agent sessions.

These are first-person operator observations. The article publishes no task set, baseline, score, cost table, trace corpus, or controlled comparison for its swarm or productivity claims.

## Git Storage Claim

- Repositories are stored as immutable content-addressed packfiles plus one mutable manifest pointer advanced through conditional compare-and-swap.
- Block reports model-checking durability, reconstruction, and concurrent pushes in TLA+ and requiring each object-store backend to pass a conformance suite.
- The repository contains the formal specification and makes its bounded state space and storage assumptions explicit; those details are captured in [[raw/repositories/block-buzz-repository]].

## Maturity Boundary

- The post explicitly calls Buzz early and acknowledges rough edges and large gaps between the vision and current implementation.
- Claims about “human-months” of activity and better/faster teamwork are promotional or anecdotal, not empirical findings.
- Use the repository snapshot to decide what currently ships; do not infer implementation from the narrative scenarios alone.
