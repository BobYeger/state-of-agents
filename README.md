# State of AI Agents

Public Obsidian vault for tracking the state of AI agents: papers, articles, protocols, harnesses, frameworks, deployed products, benchmarks, safety work, and source archives.

## How To Read

Open `index.md` first, then use the maps:

- `maps/Research Map.md`
- `maps/Systems Map.md`
- `maps/Claims Map.md`
- `maps/Frontier Reading Queue.md`

For design work, two playbooks are the goal-scoped entry points:

- `maps/Harness Design Playbook.md` — designing an agent harness or multi-agent system
- `maps/Code Factory Playbook.md` — designing self-improving, self-healing development loops (with `maps/Self-Improving Systems Map.md` as the evidence map)

The vault is organized around durable synthesis notes. `sources/` contains compact evidence cards with dates, citations, summaries, and links into the conceptual graph. `raw/` contains downloaded source material and is intentionally excluded from graph exploration.

## Local Obsidian Use

Open this folder as an Obsidian vault:

```bash
open -a Obsidian .
```

The vault includes local graph color groups in `.obsidian/graph.json` and Publish styling in `publish.css`.

## Obsidian CLI

Obsidian must be running and CLI access must be enabled in Obsidian: Settings -> General -> Advanced -> Command line interface. After the `obsidian` command is on your shell path, run:

```bash
obsidian help
```

## Vault Health

Check Obsidian wikilinks before publishing or after a large source import:

```bash
python3 scripts/check_wikilinks.py
```

The checker resolves both note-name links such as `[[Codex]]` and path links such as `[[sources/OpenAI Codex Agent Loop]]`. It ignores `talk/` by default because talk materials are local working artifacts.

## Publish Notes

`publish.css` provides the public site theme. Obsidian Publish does not expose the same full local graph configuration surface as the desktop app, so graph color groups remain canonical in `.obsidian/graph.json`; the public CSS adds matching folder/topic color cues where Publish supports them.

The headless Publish CLI uses the `ob` command:

```bash
ob login
ob publish-list-sites
ob publish-setup --path .
ob publish --dry-run
ob publish
```

Use the interactive login prompt rather than putting account passwords in shell commands.

## Inclusion Rule

Include sources that expose useful agent-system knowledge: architecture, harnesses, protocols, multi-agent coordination, tool use, memory, skills, evaluation, safety, security, operations, or frontier research.

Avoid product-only or promotional pages unless they provide concrete technical evidence.
