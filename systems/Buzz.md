# Buzz

Buzz is Block's open-source workspace for human-agent collaboration. Its important system contribution is a shared, signed coordination substrate around agents—not a model, training method, or autonomous swarm algorithm.

## System Shape

| Layer | Current Buzz mechanism | Design boundary |
|---|---|---|
| Workspace state | Central Nostr relay with channels, messages, workflows, repository events, search, and audit | Self-hostable and protocol-based, but current community state is not peer-replicated |
| Agent interoperability | `buzz-acp` bridges relay events to arbitrary ACP agents; the first-party `buzz-agent` can use the separate `buzz-dev-mcp` tool server | Other ACP agents need not use Buzz's MCP server; standards define seams, not orchestration quality or execution safety |
| Identity | Humans and agents use separate signing keys; owner attestation does not erase agent authorship | Attribution/authentication is not a sandbox or a complete least-privilege capability system |
| Team coordination | Mentions and channels; Harbor Orchestra adds distinct identities and orchestrator/worker/verifier persona contracts | Ordinary `buzz-acp --agents N` is a shared-identity channel pool; Orchestra's work rules are prompt-level |
| Memory and telemetry | Encrypted engrams, ephemeral observer frames, durable turn metrics | Draft Buzz NIP extensions; memory is not a self-improvement loop and metrics are not billing-grade |
| Code and workflow | Git hosting, signed events, workflow engine, branch-as-room vision | Approval persistence/resume and several forge/workflow actions remain incomplete |

## The Multi-Agent Reading

Buzz externalizes team state into a durable room where people and agents can see assignments, evidence, decisions, and failed paths. That makes it closer to a message bus plus collaboration/control plane than to Kimi's trained commander or Cursor's recursive swarm harness.

The repository contains two distinct concurrency patterns:

- `buzz-acp --agents N` partitions channels across interchangeable subprocesses sharing one identity and serializes each channel.
- Harbor Buzz Orchestra creates distinct orchestrator and worker identities over one task filesystem. Its persona prompts prohibit overlapping assignments, require evidence-bearing reports, and call for verification by a different worker; the runtime enforces process liveness and orchestrator-authored completion, not those work contracts.

The second is the reusable team-prompt design. Its manifest records useful condition data, but no public results currently show that it beats a single-agent baseline.

## Harness Reading

The cleanest design decision is protocol separation. `buzz-acp` bridges relay events to a downstream ACP agent, which owns its model loop; in the first-party path, `buzz-agent` can reach tools through `buzz-dev-mcp`. Other ACP agents need not use that MCP server. First-party sessions isolate history, context, and tool subprocesses; channel queues prevent same-channel races; and runtime controls cover cancellation, rotation, shutdown, agent-subprocess respawn, relay reconnect, output bounds, and process-tree cleanup.

Observability is split by lifecycle rather than forced into one log: encrypted live frames for supervision and cancellation, durable encrypted usage records for accounting, and persistent channels for team history. The activity-feed design then normalizes raw protocol traffic into verb, object, and outcome while retaining raw detail on demand.

## Security Reading

Buzz's key model usefully keeps the software actor visible. The mobile article simultaneously discloses that agents commonly run outside a sandbox with broad host permissions, making identity only the first boundary. Direct sender authentication does not constrain commands hidden in data, limit ambient credentials, or bound tool side effects.

The public owner-attestation protocol is also narrower than Block's separate User Identity Delegation architecture. Buzz currently provides agent authorship, owner-backed relay admission, and channel membership; it should not be described as implementing subject–actor consent intersection across downstream services.

## Evidence and Maturity

- **Implemented evidence:** relay/workspace, ACP bridge and first-party ACP/MCP path, channel worker pool, Orchestra code/prompts/manifests, engrams, observer frames, usage metrics, Git storage, and formal artifacts.
- **Method without result:** Harbor/Terminal-Bench adapter; no score, cost comparison, or single-agent baseline published.
- **Operator anecdote:** spontaneous agent recruitment, lower coordination burden, and human-months-scale activity.
- **Incomplete/vision:** durable approval resume, several workflow/forge actions, and remote-agent substrate deployment.

## Related

- [[concepts/agent teams]]
- [[operations/agent identity]]
- [[operations/permissions]]
- [[operations/sandboxes]]
- [[operations/durable sessions]]
- [[benchmarks/multi-agent benchmarks]]
- [[protocols/ACP]]

## Related Sources

- [[sources/Block Buzz]]
- [[sources/Buzz Repository]]
- [[sources/Block User Identity Delegation]]
