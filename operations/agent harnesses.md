# Agent harnesses

A harness is the runtime layer that turns a model into an acting system by managing the loop, context, tool calls, memory, execution environment, approvals, traces, compaction, and resumption.

This is separate from a framework. A framework defines agent structure; a harness executes the agent loop in a concrete environment.

## Improvement Claim

Harnesses improve agent systems by making the loop inspectable and recoverable: context, tools, observations, approvals, state, compaction, and handoff are engineered instead of left implicit.

## Tracker

- [[maps/Harness Tracker]]
- [[reports/Harness Engineering Report]]
- [[maps/Agent Teams and Workforces Map]]
- [[concepts/loop engineering]]
- [[methods/self-improving code loops]]
- [[methods/hook-based control]]
- [[methods/ralph loop]]
- [[methods/deliberative control]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Context management is an agent architecture choice]]
- [[maps/What Makes Agent Systems Better]]
- [[maps/Context Management Map]]

## Current Anchors

- [[sources/OpenAI Codex Agent Loop]]
- [[sources/OpenAI Codex Using Goals]]
- [[sources/OpenAI Unlocking Codex Harness]]
- [[sources/OpenAI Agents SDK Tools]]
- [[sources/OpenAI Codex CLI Agents SDK Cookbook]]
- [[sources/Claude Code Hooks]]
- [[sources/Anthropic Building Effective AI Agents eBook]]
- [[sources/Anthropic Effective Harnesses for Long-Running Agents]]
- [[sources/Anthropic Harness Design Long-Running Apps]]
- [[sources/Anthropic Parallel Claudes C Compiler]]
- [[sources/Claude Code Agent Teams]]
- [[sources/Claude Code Scheduled Tasks]]
- [[sources/Claude Code Workflows]]
- [[sources/Addy Osmani Loop Engineering]]
- [[sources/Meta-Harness]]
- [[sources/SkillOpt]]
- [[sources/Darwin Godel Machine]]
- [[sources/Hyperagents]]
- [[sources/Anthropic When AI Builds Itself]]
- [[sources/OpenAI Codex Subagents]]
- [[sources/Cursor 3 Agents Window]]
- [[sources/Devin Manages Devins]]
- [[sources/Anthropic Managed Agents Dreaming Outcomes]]
- [[sources/Claude Managed Agents Define Outcomes]]
- [[sources/Google ADK Durable Agents]]
- [[sources/OpenAI Symphony]]
- [[sources/Anthropic Claude Code Worktrees]]
- [[sources/OpenAI Codex App Worktrees]]
- [[sources/LangChain Deep Agents v0.6]]
- [[sources/LangChain Delta Channels]]
- [[sources/Parallel Context Compaction]]
- [[sources/Cursor Improving Agent Harness]]
- [[sources/OpenClaw Repository]]
- [[sources/OpenClaw Agent Harness Plugins]]
- [[sources/Hermes Agent Repository]]
- [[sources/Hermes Agent Docs]]
- [[sources/MiniMax Agent Lessons 2025]]
- [[sources/Cursor 3.2]]
- [[sources/OpenHarness Docs]]
- [[sources/Cloudflare Dynamic Workflows]]
- [[sources/AlphaEvolve]]
- [[sources/The AI Scientist-v2]]
- [[sources/Letta Code Memory Docs]]
- [[sources/MiniMax Agent Team]]
- [[sources/Plan-Then-Execute]]
- [[sources/Web Agents Plan-Then-Execute]]
- [[sources/Ralph Playbook]]

## Related

- [[operations/agent infrastructure]]
- [[operations/durable sessions]]
- [[operations/worktree isolation]]
- [[operations/permissions]]
- [[operations/sandboxes]]
- [[operations/agent observability]]
- [[concepts/agent operating surfaces]]
- [[concepts/context compaction]]
- [[maps/Recent Agent Operating Concepts]]
