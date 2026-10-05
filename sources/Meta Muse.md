---
title: "Introducing Muse: a personal AI agent"
aliases:
  - "Muse personal agent"
source_type: "product"
kind: "persistent-personal-agent"
status: "verified"
year: 2026
publication_date: "2026-09-08"
publication_date_basis: "official_launch_post_and_engineering_post"
source_updated_date: "2026-09-30"
source_updated_date_basis: "official_launch_page_updated_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Meta"
venue: "Meta Newsroom"
url: "https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/"
pdf_url: ""
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# Meta Muse

## Summary

- Meta [launched Muse on September 8, 2026](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/), initially rolling out in the US through its own apps, the web and WhatsApp. It is a consumer personal agent for tasks and continuing goals, with a dedicated per-user cloud computer and browser. September 30 is the launch page's update date.
- The [product design account](https://introducing.muse.ai/) describes persistent conversational memory, editable memory files, concurrent tasks, schedules and event-triggered work while the app is closed. Background results pass a usefulness decision before notifying the user. Main chat, side chats, goals, activity history, artifacts and structured approvals expose different parts of ongoing work.
- The user delegates goals and controls permissions; Muse can propose follow-ups and act between conversations. This is a product example of [[concepts/persistent personal agents]], with implementation details separately captured in [[sources/Meta Muse Security Architecture]].

## Research and Evaluation Evidence

- [Muse Spark 1.3](https://research.meta.ai/blog/introducing-muse-spark-1-3), released September 2, is the model identified in the engineering account. Meta describes training across multiple harnesses for long tasks, multitasking, collaboration and consequential-action judgment. It does not disclose a specific memory or proactivity algorithm in these pages.
- The model's [evaluation methodology](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology) names OSWorld 2.0, AutomationBench, DeepSearchQA, professional-work, coding and long-context tests. These use benchmark-specific or common internal harnesses, rather than establishing consumer Muse performance. For example, OSWorld 2.0 reports mean partial credit across 108 workflows; Spark 1.2 and 1.3 use different benchmark revisions.
- These are vendor descriptions and model evaluations. They do not measure whether months of personal memory remain correct, unsolicited interventions are useful, or delegated actions remain reliable in the shipped product. The architecture's explicit practitioner citation is recorded in the linked security card; conceptual resemblance to other agent papers is not evidence of adoption.

## Connections

- [[systems/personal assistant agents]]
- [[concepts/persistent personal agents]]
- [[concepts/background agents]]
- [[concepts/event-driven agents]]
- [[operations/agent memory]]
- [[sources/Meta Muse Security Architecture]]
