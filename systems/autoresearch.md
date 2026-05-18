# Autoresearch

Karpathy's autoresearch is a compact autonomous ML-research harness: an agent repeatedly edits one training file, runs a fixed-budget experiment, evaluates a single metric, keeps improvements, and reverts failures.

The important design move is narrowing the research environment until autonomous iteration is inspectable: one modifiable file, one immutable preparation/evaluation harness, one scalar metric, and a `program.md` file that encodes the research loop.

## Design Pattern

- Minimize the action surface until the agent can safely iterate.
- Make the experimental objective observable as one scalar metric.
- Separate editable research code from fixed evaluation code.
- Treat the research loop itself as an artifact that can be read, modified, and audited.

## Related

- [[methods/agentic workflow search]]
- [[concepts/long-horizon agents]]
- [[methods/runtime routing]]

## Related Sources

- [[sources/Karpathy Autoresearch|autoresearch]]
