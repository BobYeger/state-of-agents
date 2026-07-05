---
title: "LangSmith Evaluation Concepts"
source_type: "docs"
kind: "eval-platform-docs"
status: "verified"
year: 2026
publication_date: "2026-07"
publication_date_basis: "undated_docs_page_fetch"
authors:
  - "LangChain"
venue: "docs.langchain.com"
url: "https://docs.langchain.com/langsmith/evaluation-concepts"
artifacts:
  - "raw/docs/langsmith-evaluation-concepts.md"
created: 2026-07-03
updated: 2026-07-05
---

# LangSmith Evaluation Concepts

## Summary

- Draws the offline/online split explicitly: offline evals target dataset examples with reference outputs and run as batch jobs pre-deployment; online evaluators target runs/threads from tracing projects with inputs and outputs only, configured as automated rules in the Observability tab in near real time.
- Names three triggers for sampling production traces into datasets: negative user feedback, heuristics (extended latency, errors), and LLM feedback detecting significant conversations; LLM-as-judge bootstraps initial labels, then human annotation refines them.
- Names three offline patterns a promotion pipeline needs: regression testing (compare against a baseline so new versions don't degrade), backtesting (replay a new version against historical production data), and pairwise evaluation (compare two versions when direct scoring is hard, e.g. summarization).
- Online evaluators are reference-free by design: safety checks, format validation, quality heuristics/anomaly detection, and reference-free LLM-as-judge scoring.

## Connections

- [[operations/agent evals]]
- [[operations/agent observability]]
- [[concepts/outcomes and rubric graders]]
- [[sources/LangSmith Context Hub]]
- [[sources/LangChain Agent Improvement Loop]]

## Artifacts

- [[raw/docs/langsmith-evaluation-concepts.md]]

## Notes

- Canonical URL: https://docs.langchain.com/langsmith/evaluation-concepts
- Living docs page with no publication date; content verified by fetch on 2026-07-02 and may change without notice.
- Vocabulary is LangSmith-specific but the offline/online and trace-to-dataset patterns are platform-generic.
