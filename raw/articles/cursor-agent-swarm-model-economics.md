# Agent swarms and the new model economics — structured capture

- Canonical URL: https://cursor.com/blog/agent-swarm-model-economics
- Author: Wilson Lin
- Publisher: Cursor
- Publication date: 2026-07-20
- Captured: 2026-07-22
- Extraction: Defuddle CLI with Markdown output
- Capture mode: metadata, section structure, and structured facts; not a verbatim republication

## Page Structure

1. Motivation and old/new SQLite swarm comparison
2. Trees and leaves
3. Context efficiency and memory
4. Purpose-built version control
5. Coordination failure modes
   - Split-brain design
   - Planner contention
   - Merge conflicts
   - Megafiles
   - Ossification
6. Review lenses
7. Agent-authored shared context / Field Guide
8. SQLite experiment design
9. Results across model mixes
10. Run-level analysis
11. Model economics
12. Specs as prompts

## Experiment Facts

- Task: implement SQLite in Rust from the 835-page manual.
- Withheld from the swarm: source code, test suites, SQLite binary, and internet access.
- Evaluator: SQLite project's `sqllogictest`, containing millions of known-answer queries.
- Comparison: old and new swarms on the same task, model configurations, and time budget.
- New swarm: better than old in every tested configuration; approximately 73–85% versus 11–77% at four hours; every new run later reached 100%.
- Integrity review: Cursor manually checked for cheating, shortcuts, and uneven implementation; no raw independent audit was supplied.

## Model Mix and Cost Facts

| Configuration | Reported cost/result detail |
|---|---|
| GPT-5.5 planner + worker | Approximately $10,565 total; workers approximately $9,373 |
| Grok 4.5 planner + worker | Cost-efficient frontier comparison; old run paused before two hours |
| Opus 4.8 planner + Composer 2.5 worker | Approximately $1,339 total; workers approximately $411 |
| Fable 5 planner + Composer 2.5 worker | Similar quality; lower planner bill than Opus but more worker tokens and higher total than the Opus hybrid |

- Workers consumed at least 69% of tokens and over 90% in most runs.
- Planner tokens could still account for about two-thirds of dollars because planner models cost more per token.
- Cursor reports similar quality across mixes but does not publish an independent cost ledger or full N×N planner-worker matrix.

## Harness Facts

- Recursive tree decomposition separates frontier planners from cheaper workers.
- Cursor attributes scaling primarily to context efficiency, not parallelism alone.
- The custom VCS is reported at approximately 1,000 commits per second, compared with approximately 1,000 commits per hour in the earlier browser swarm.
- Shared design documents, compile-checked references, neutral conflict resolution, megafile decomposition, intentional-breakage comments, and stacked review lenses address distinct failure modes.
- The Field Guide is an agent-owned, line-budgeted shared context folder injected at agent start. It is a within-run successor-memory mechanism; training agents to write better successor notes is proposed future work.
- Cursor attempted GPT-5.6 Sol but reports prompt sensitivity and runaway spirals; the configuration was excluded without tuning.

## Coordination and Code-Structure Facts

| Diagnostic | Old harness | New harness |
|---|---:|---:|
| Grok 4.5 commits | 68,000 in the first two hours | Approximately 70x lower pace over the comparison window |
| Grok 4.5 merge conflicts | More than 70,000 before pause | Fewer than 1,000 over four hours |
| Hottest-file conflicts | 7,771; 1,173 agents touched the file | 47 |
| Rust crates | 54, including three SQL packages | Nine, with no later additions |
| Fable 5 engine code at full-suite completion | 64,305 lines | 9,908 lines |
| Opus-mix engine code and grade | 19,013 lines at 97% | 4,645 lines at 100% |

Cursor interprets the activity gap as old-harness thrash, contention, and split-brain design rather than useful throughput. The article does not provide a component ablation for the mechanisms bundled into the new harness.

## Capture Boundary

- All performance, cost, conflict, code-size, and model-routing values are first-party vendor reports.
- Cursor links https://github.com/cursor/minisqlite as public output from a solo Opus 4.8 run, not as the code or traces from the compared swarm runs; Cursor says its own review of that output was only preliminary.
- The raw article contains charts and diagrams; this public capture preserves their described facts without reproducing the visual assets or article prose.
- The public artifact is a structured evidence capture; use the canonical URL for the original charts and full narrative.
