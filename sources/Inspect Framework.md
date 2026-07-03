---
title: "Inspect: A framework for frontier AI evaluations"
aliases:
  - "Inspect"
  - "Inspect AI"
source_type: "docs"
kind: "eval-framework"
status: "verified"
year: 2024
publication_date: "2024-05"
publication_date_basis: "first_release_month"
authors:
  - "UK AI Security Institute"
  - "Meridian Labs"
venue: "inspect.aisi.org.uk"
url: "https://inspect.aisi.org.uk/"
created: 2026-07-03
updated: 2026-07-03
---

# Inspect Framework

## Summary

- Evals are composed from three parts: datasets (samples with input and target), solvers (from single model calls up to multi-turn agents with tools, a built-in ReAct agent, and multi-agent primitives), and scorers (text comparison, model grading, custom).
- Embodies the transcript-as-first-class-artifact pattern: every run emits an eval log containing the full transcript — model reasoning, tool interactions, and scores — and scorers can grade the whole trajectory rather than only the final answer.
- Logs are viewable in the Inspect View web viewer and a VS Code extension, and export to data frames and transcript-scanning analysis tools.
- 200+ prebuilt evaluations (inspect_evals); sandboxing backends for untrusted agent code include Docker, Kubernetes, Modal, and Proxmox, with tool-approval mechanisms for human-in-the-loop control; 20+ model providers supported.
- Agent bridges run external harnesses — Claude Code, Codex CLI, and Gemini CLI — inside evaluations, with checkpointing and intervention primitives.
- Open-sourced May 2024 by the UK AI Security Institute; 50+ contributors including other national safety institutes and frontier labs.

## Connections

- [[operations/agent evals]]
- [[operations/agent observability]]
- [[operations/sandboxes]]
- [[benchmarks/agent evaluation]]
- [[sources/Anthropic Demystifying Agent Evals]]

## Notes

- Canonical URL: https://inspect.aisi.org.uk/
- Covers offline, transcript-scored evaluation only; it has no online/production half (telemetry sampling, A/B gating), so it is a pattern library for the offline side of a promotion pipeline.
- Living documentation for an actively developed framework; feature counts (200+ evals, provider list) drift.
