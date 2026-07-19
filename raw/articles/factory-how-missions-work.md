# How Missions Work — structured capture

- Canonical URL: https://factory.ai/news/missions-architecture
- Author: Theo Luan
- Publisher: Factory.ai
- Publication date: 2026-04-10
- Captured: 2026-07-14
- Extraction: Defuddle CLI with Markdown output
- Capture mode: metadata, section structure, and structured facts; not a verbatim republication

## Page Description

Factory presents the architecture behind Missions, emphasizing focused contexts, role separation, explicit validation, and multi-day autonomous software work.

## Section Structure

1. Rationale
2. Design principles
   - Separation of concerns and incentives
   - Test-driven development at worker and mission levels
   - Externalized state
   - Model specialization
3. System execution
4. Slack-clone run breakdown
5. Looking ahead

## Architecture Facts

- Roles: orchestrator, workers, and validators.
- Orchestrator responsibility: clarify the goal, define success, decompose work, and respond to validation findings.
- Worker responsibility: write tests and implement a bounded feature without holding final acceptance authority.
- Validator responsibility: inspect implementation quality or exercise behavior, then report gaps without implementing repairs.
- Validation contract: behavioral assertions are written before the feature plan.
- Shared state: validation contract, feature list, research notes, operating rules, and knowledge artifacts.
- Execution order in this snapshot: a programmatic runner starts one fresh worker per feature in order.
- Validation point: after all features in a milestone complete.
- Repair path: the orchestrator converts findings into fix features and repeats validation.
- Blocked path: control returns to the user when implementation or validation cannot proceed.

## Reported Slack-Clone Telemetry

| Measure | Value |
|---|---:|
| Runtime | 16.5 h |
| Orchestration | 0.38 h / 2.3% |
| Implementation | 9.98 h / 60.5% |
| Validation | 6.14 h / 37.2% |
| Total runs | 185 |
| Orchestrator runs | 1, plus 12 subagents |
| Worker runs | 63 |
| Validator runs | 27, plus 82 subagents |
| Total tokens | 778.5M |
| Input tokens | 30.3M |
| Cache-read tokens | 744.9M |
| Output tokens | 3.4M |
| Generated lines | 38.8K |
| Source lines | 18.5K |
| Test lines | 20.4K / 52.5% |
| Statement coverage | 89.25% |
| Round-one milestone passes | 0 / 6 |
| Round-two milestone passes | 1 / 6 |
| Round-three milestone passes | 2 / 6 |
| Round-four milestone passes | 6 / 6 |
| Original features | 40 |
| Fix features | 21 |
| Validator findings | 81 total: 65 blocking, 11 non-blocking, 5 suggestions |
| Median implementation trajectory | 51 turns; p90 123 |
| Median validation trajectory | 30 turns; p90 37 |

## Capture Boundary

- Values are transcribed from Factory's own page and remain vendor-reported.
- The page provides one detailed run rather than a controlled comparison.
- Diagrams, video, and article prose are not reproduced in this public capture.
- Factory's current product page, checked 2026-07-14, separately advertises parallel execution: https://factory.ai/product/missions
