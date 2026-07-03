# Builder Ecosystem Map

This map tracks source material for the practical builder ecosystem around agents: frameworks, orchestration libraries, harnesses, runtimes, deployed agent products, and China-origin agent stacks.

The inclusion rule is intentionally strict: include sources with a concrete agent-system, multi-agent, harness, tool-use, memory, protocol, eval, safety, or autonomous-execution angle. Exclude generic model-release pages and generic chatbot pages unless the source explains an agent architecture or runtime.

## The 2025-2026 Vendor Consolidation

The vendor landscape reorganized around four structural shifts, each now grounded in source cards.

| Shift | What happened | Evidence |
|---|---|---|
| Platforms orchestrate rival agents | GitHub turned Copilot into a control plane that runs Anthropic, OpenAI, and other vendors' agents under one mission control | [[sources/GitHub Agent HQ]]: the announcement; [[sources/GitHub Agent HQ Claude and Codex]]: the 2026-02 GA moment; [[sources/GitHub Copilot Coding Agent]]: the underlying Actions-VM sandbox and issue-tracker control plane |
| Harness consolidation and kill-and-replace | Google retired Gemini CLI within roughly a year of open-sourcing it, folding terminal and IDE surfaces into one Antigravity harness with a dedicated agent-manager surface | [[sources/Google Antigravity]]: the two-surface Editor + Manager design; [[sources/Google Antigravity CLI Transition]]: the retirement timeline and the skills/hooks/subagents feature set carrying over as the cross-vendor baseline |
| Harness reuse across audiences | The same coding harness gets repackaged for new users rather than rebuilt: Anthropic shipped the Claude Code harness in a sandboxed desktop VM for non-technical knowledge work | [[sources/Claude Cowork Research Preview]]: harness-in-a-VM architecture, approval gates, outcome-first flow |
| Environment readiness as a product | Vendors grade the repository, not just the agent: readiness levels gate what autonomy a codebase can support | [[sources/Factory Agent Readiness]]: 8 pillars x 5 levels with Level 3 as production-ready for agents; [[sources/Factory 2.0 Software Factory]]: the surrounding software-factory framing |

Other vendor cards worth routing to directly: [[sources/OpenHands Software Agent SDK]] (open-source V1 SDK redesign argued from production failure data), [[sources/Devin Manages Devins]] (manager-of-agents product architecture in isolated VMs), [[sources/Manus Context Engineering]] (production context-engineering lessons: KV-cache hit rate, filesystem-as-context, keeping failures in context), and [[sources/OpenAI Codex App Server Docs]] (the harness exposed as a thread/turn/item control plane for building products on top).

## Route Through Hubs

- [[systems/agent frameworks and orchestration libraries]]
- [[operations/agent harnesses]]
- [[systems/deployed agent products]]
- [[maps/Harness Tracker]]
- [[maps/What Makes Agent Systems Better]]
- [[systems/china agent ecosystem]]
- [[protocols/agent protocols]]
- [[maps/Agent Skills Map]]
- [[maps/Courses and Curricula Map]]

## Related Maps

- [[maps/Production Infrastructure Map]]
- [[maps/Protocols Map]]
- [[maps/Multi-Agent Systems Map]]
- [[maps/Long-Horizon Agents Map]]
