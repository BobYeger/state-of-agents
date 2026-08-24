# State of AI Agents

Public Obsidian vault for tracking the state of AI agents: papers, articles, protocols, harnesses, frameworks, deployed products, benchmarks, safety work, and source archives.

## How To Read

Start with [the vault index](index.md), then use the broad navigation maps:

- [Research Map](maps/Research%20Map.md)
- [Systems Map](maps/Systems%20Map.md)
- [Claims Map](maps/Claims%20Map.md)
- [Frontier Reading Queue](maps/Frontier%20Reading%20Queue.md)

For design work and deeper synthesis, use the goal-scoped paths:

- **Harnesses:** [Harness Design Playbook](maps/Harness%20Design%20Playbook.md), [Harness Tracker](maps/Harness%20Tracker.md), and [Harness Engineering Report](reports/Harness%20Engineering%20Report.md)
- **Multi-agent systems and cross-session communication:** [MAS Orchestration and Architecture](maps/MAS%20Orchestration%20and%20Architecture.md), [Agent Teams and Workforces Map](maps/Agent%20Teams%20and%20Workforces%20Map.md), and [Multi Agent Report](reports/Multi%20Agent%20Report.md)
- **Memory and context:** [Context Management Map](maps/Context%20Management%20Map.md), [Agent Memory Report](reports/Agent%20Memory%20Report.md), and [Agent Memory Technical Brief](reports/Agent%20Memory%20Technical%20Brief.md)
- **Self-improving systems:** [Self-Improving Systems Map](maps/Self-Improving%20Systems%20Map.md), [Code Factory Playbook](maps/Code%20Factory%20Playbook.md), and [Self-Improving Systems Report](reports/Self-Improving%20Systems%20Report.md)

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
python3 scripts/check_talk_sources.py
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

## Talk and Video Sources

Use `source_type: "talk"` for conference talks, workshops, interviews, and other substantive recorded presentations. YouTube is the distribution platform, not the epistemic source type.

Before transcribing a recording, look for an official written version, architecture note, system card, or paper. Use that written artifact as the primary source for stable architecture and exact metrics; keep the talk as a supplemental source for demonstrations, oral qualifications, and operator commentary.

Talk cards should separate event metadata, distribution metadata, source verification, and transcript review:

```yaml
source_type: "talk"
medium: "video"
platform: "youtube"
video_id: "..."
event_date: 2026-01-01 # null when unverified
youtube_upload_date: 2026-01-02
duration_seconds: 0
language: "en"
transcript_status: "captured"
transcript_type: "youtube-auto-captions" # or local-asr-lightly-normalized
transcript_language: "en"
transcript_review_status: "claim-ranges-spot-checked" # not-reviewed, claim-ranges-spot-checked, or proofread
transcript_storage: "local-only"
transcript_locator: ".private/talk-transcripts/Title - transcript.md"
transcript_sha256: "..."
evidence_class: "official-conference-workshop" # or vendor-operator-report, interview, etc.
metrics_status: "speaker-reported"
```

`status: "verified"` verifies the source identity and metadata; it does not mean that an automatic transcript was proofread. Keep those states separate.

Full third-party transcripts are local-only by default under `.private/talk-transcripts/`, which is excluded from Git and Obsidian Publish. Publish a full transcript only when its license or rights-holder permission permits redistribution. Public source cards should carry a timestamped claim index, paraphrased synthesis, canonical URL, capture method, review status, and hash of the local capture.

The default talk checker is portable to public clones where private transcripts are absent. On the capture workstation, run `python3 scripts/check_talk_sources.py --require-local` to require each local artifact and verify its hash.

For platform captions, retain the original VTT or JSON3 file locally alongside any normalized Markdown. For local speech recognition, record the source-media hash, transcription tool and version, model, exact command, timestamp-generation method, and a correction log. If an older capture omitted any field, mark it `not-recorded` rather than reconstructing it. Never silently upgrade speaker or vendor claims into independent evidence, and do not commit video or audio binaries by default.
