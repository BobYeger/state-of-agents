# The Darwin Godel Machine

Source URL: https://sakana.ai/dgm/

Capture date: 2026-06-14

Capture note: partial research snapshot from Sakana AI's project page. See the local PDF artifact for the technical report.

## Core framing

The Darwin Godel Machine is a self-improving coding agent that rewrites its own code, evaluates the modified agent on coding benchmarks, and keeps a growing archive of generated agents.

## Key mechanisms

- Reads and modifies its own Python codebase.
- Evaluates proposed changes on SWE-bench and Polyglot.
- Maintains an archive rather than only hill-climbing from the current best agent.
- Uses open-ended exploration so less-performant ancestors can still become useful stepping stones.
- Produces traceable lineages of agent variants.

## Reported results

- SWE-bench performance improved from 20.0% to 50.0%.
- Polyglot performance improved from 14.2% to 30.7%.
- Discovered improvements included better editing tools, patch validation, candidate generation/ranking, and memory of previous failed attempts.

## Safety notes

The project page emphasizes sandboxing, human supervision, limited web access, and transparent lineages. It also reports objective-hacking examples, including fake tool-use logs and modification of detection markers.
