# State of AI Agents — Talk Outline

> Draft v2 · slide-by-slide. Structure: **every content slide is split into two parallel tracks** — **Left = Multi-Agent Systems (MAS)**, **Right = Harnesses / coding agents**. Halves run as independent threads and don't need to pair up 1:1; they happen to rhyme at the structural level. Title + the reused "Journey" recap + closing are the full-width exceptions. Field-only (no DreamGroup content yet). No visual theme applied yet.

## Talk meta

- **Audience:** internal team (technical)
- **Length:** ~20–30 min · **15 slides**
- **Two spines:**
  - **MAS (left):** "more agents" → **division of labor** — what to parallelize vs. serialize, hand off vs. do together → real **code factories**.
  - **Harness (right):** prompt → context → **harness engineering** — we stopped tuning the input and started engineering the whole state.
- **Through-line:** *stop tuning the input; engineer the system around the model.* Both spines are the same move.
- **Sourcing rule:** most-meaningful sources only, cited and quoted. Wikilinks resolve inside the vault.

---

## Slide 1 — Title (full width)

**The State of AI Agents — 2026**
*The next two chapters: dividing the work (MAS) · engineering the harness.*

- One line: "Two lenses on one year. We'll run them side by side."

## Slide 2 — The Journey: from Prediction to Agency (full width · reused)

*Your closing slide from last year's talk — reused as the on-ramp.* 2022 next-token → CoT → function calling → structured outputs → ReAct (tool use + loops) → reasoning models → MCP → **2025: context engineering**.

- Main point: last year ended at *"managing what goes into context."* **This talk continues the timeline** — and adds the second track we didn't draw: coordination.
- *Visual:* extend the timeline one notch on each side → **2026: harness engineering** (right) and **2026: division of labor / code factories** (left).

## Slide 3 — Where this picks up: the thesis

- **L · MAS:** the hidden second track was **coordination**. "More agents" is giving way to **division of labor** — deciding what to parallelize, serialize, hand off, or do together.
- **R · Harness:** context engineering was a waypoint, not the destination. The frontier moved to managing the **entire state** — loop, tools, memory, sandbox, approvals — i.e. the **harness**.
- **Most meaningful source (R):** *Effective context engineering for AI agents* — Anthropic Eng., Sep 2025: "we view context engineering as the **natural progression of prompt engineering**… as we move towards engineering more capable agents… we need strategies for **managing the entire context state**." [[sources/Anthropic Effective Context Engineering]]
- **Most meaningful source (L):** *How we built our multi-agent research system* — Anthropic Eng., Jun 2025: "A multi-agent system consists of multiple agents (LLMs autonomously using tools in a loop) working together." [[sources/Anthropic Multi-Agent Research System]]
- *Bridge:* both halves = **stop tuning the input; engineer the system.**

## Slide 4 — The unit of design

- **L · MAS:** a MAS is a **coordination structure** — roles, topology, communication, shared vs. private memory, central vs. decentralized control, runtime routing. Not "a pile of agents." [[concepts/multi-agent systems]]
- **R · Harness:** a harness is the **runtime layer** — the loop, context, tool dispatch, memory, approvals, traces, compaction, resumption. *"A framework defines agent structure; a harness executes the agent loop in a concrete environment."* [[operations/agent harnesses]] · [[maps/Harness Tracker]]

## Slide 5 — Why the naive version underperforms

- **L · MAS:** more agents ≠ better — the same system that wins on breadth is also the costly one. *Anthropic multi-agent research* (Jun 2025): wins on breadth-first work, **but** "multi-agent systems use about **15× more tokens** than chats," and "most coding tasks involve **fewer truly parallelizable tasks** than research, and LLM agents are not yet great at coordinating and delegating… in real time." [[sources/Anthropic Multi-Agent Research System]] · [[claims/Claim - More agents are not automatically better]]
- **R · Harness:** a bigger context window isn't the fix. *Anthropic context engineering* (Sep 2025): "Context… must be treated as a **finite resource with diminishing marginal returns**" — the "attention budget" and **context rot**. [[sources/Anthropic Effective Context Engineering]]

## Slide 6 — Failure has a taxonomy

- **L · MAS:** *Why Do Multi-Agent LLM Systems Fail?* — Cemri et al., NeurIPS 2025 (arXiv 2503.13657). The **MAST** taxonomy groups failures into **specification/design, inter-agent misalignment, and verification/termination.** [[sources/Why Do Multi-Agent LLM Systems Fail]]
- **R · Harness:** the failure surface is the **context trajectory** — overflow, lost state, stale tool results. *Cursor, Continually improving our agent harness* (Apr 2026): tool errors "remain in context, wasting tokens and causing **'context rot'**." Fixes: compaction, masking, tool-result clearing, handoff, retrieval. [[maps/Context Management Map]] · [[sources/Cursor Improving Agent Harness]]

## Slide 7 — The winning shapes *(anchor — harness-in-practice on the right)*

- **L · MAS:** the structures that actually pay off — **orchestrator-worker** (lead plans, subagents explore in parallel; **+90.2%** over single-agent on Anthropic's research eval), **leader/worker/verifier** (MiniMax), and **owned-scope teams** with a shared task list and a definition of done. [[sources/Anthropic Multi-Agent Research System]] · [[sources/MiniMax Agent Team]] · [[maps/Agent Teams and Workforces Map]]
- **R · Harness — *harness engineering in practice*** (adapts your 4-column ONA slide): **docs & context** (Skills, AGENTS.md) · **guardrails** (linters, hooks, CI gates) · **testing & feedback** (evals, golden files) · **environment & tooling** (MCP, sandboxes, devcontainers). *Anthropic, Effective harnesses* (Nov 2025): "**Inspiration for these practices came from knowing what effective software engineers do every day.**" [[operations/agent harnesses]] · [[concepts/agent skills]]

## Slide 8 — Tools & the surface area of action

- **L · MAS:** coordination state lives **outside the model** — shared task list, issue tracker, event log, **handoff packages**; **protocols (MCP, A2A)** are the wire between agents. [[concepts/handoff over compaction]] · [[protocols/MCP]] · [[protocols/A2A]]
- **R · Harness:** get tools **out of the prompt**. *Agent operating surfaces*: "Large tool lists consume context and encourage **shallow one-call-at-a-time behavior**" → dynamic discovery + **code mode** ("an entire API in ~1,000 tokens"). [[concepts/agent operating surfaces]] · [[concepts/programmatic tool calling]]

## Slide 9 — Production reality: code factories *(the high beat)*

- **L · MAS:** multi-agent software production is **real now**. *Building a C compiler with a team of parallel Claudes* — Carlini/Anthropic, Feb 2026: "I tasked **16 agents** with writing a Rust-based C compiler… Over nearly **2,000 Claude Code sessions** and **$20,000** in API costs, the agent team produced a **100,000-line compiler that can build Linux 6.9** on x86, ARM, and RISC-V." Plus Devin managing Devins in isolated VMs and Symphony turning Linear tickets into agent runs. [[sources/Anthropic Parallel Claudes C Compiler]] · [[sources/Devin Manages Devins]] · [[sources/OpenAI Symphony]]
- **R · Harness:** what makes that possible is the **long-running harness**. *Anthropic, Effective harnesses* (Nov 2025): "each new session begins with **no memory of what came before**" → an **initializer + coding agent** that leave artifacts (`claude-progress.txt` + git history). Blunt finding: "**compaction isn't sufficient.**" [[sources/Anthropic Effective Harnesses for Long-Running Agents]] · [[methods/ralph loop]]

## Slide 10 — Always-on agents *(anchor — background-agent taxonomy on the left)*

- **L · MAS — *background-agent taxonomy*** (adapts your ONA "Background Agents" slide): **swarms** (converge on one result from many angles) · **fleets** (independent parallel work across repos) · **event-driven** (PR events, CI failures, webhooks) · **scheduled** (cron — nightly updates, weekly audits, daily triage). [[sources/Cursor 3 Agents Window]] · [[sources/OpenAI Symphony]]
- **R · Harness:** the enabling pattern is the **durable dormant agent** — pause when blocked, persist explicit state, wake on events; **durable sessions** keep events/artifacts outside the context window. [[concepts/durable dormant agents]] · [[operations/durable sessions]]

## Slide 11 — Runtime & isolation *(anchor — runtime-approaches table)*

- **L · MAS:** isolating a **fleet** — a **worktree/branch per agent** so parallel edits don't collide; compare best-of-N; coordinate through a tracker or lead. [[operations/worktree isolation]]
- **R · Harness:** **a worktree is *not* a sandbox.** *Worktree isolation* note: "This is **not a security sandbox**." Fleets still need process/network/secret isolation → **containers / microVMs / dev-environments**. [[operations/sandboxes]] · [[operations/permissions]]
- *Visual (shared):* your **Runtime approaches** table — Threads / Worktrees / Containers·microVMs / Dev-environments × isolation · tooling · secrets · IDE access · coordination · lifecycle.

## Slide 12 — Did it actually work? (eval & observability)

- **L · MAS:** measure **coordination quality**, not just task success — treat architecture as an experimental variable (cost, latency, failure modes). [[benchmarks/multi-agent benchmarks]] · [[sources/Why Do Multi-Agent LLM Systems Fail]]
- **R · Harness:** honest eval is harness work. *Cursor* (Apr 2026): public benchmarks + CursorBench + online A/B, plus a **"Keep Rate"** (what fraction of agent edits survive in the user's codebase). Long-horizon & context benchmarks (ContextBench), plus traces / event streams / replay. [[benchmarks/long-horizon benchmarks]] · [[sources/ContextBench]] · [[operations/agent observability]]

## Slide 13 — The tax on autonomy (safety & security)

- **L · MAS:** more agents + more connectivity = a **bigger attack surface** — protocol security, inter-agent trust, collective misalignment. [[safety/protocol security]] · [[safety/agentic misalignment risk]]
- **R · Harness:** *Sandboxes* note: the risk isn't only a classic escape — "A model can also be tricked into **reading credentials, exfiltrating logs**… or **using one tool's authority to affect another system**." Defenses: prompt-injection hardening, sandboxing, permission/path/network policy. [[safety/prompt injection]] · [[safety/sandbox escape and credential exposure]] · [[operations/permissions]]

## Slide 14 — Convergence: the new stack *(climax)*

- **L · MAS:** the structure questions — parallelize/serialize, teams, routing, verification…
- **R · Harness:** …become **layers of one operating substrate** — versioned context + skills + dynamic tools + memory consolidation + evaluators + durable runtime + subagents + observability + governance.
- *Bridge:* **old stack = prompt + tools + loop → new stack = the operating substrate.** Both spines were describing the same thing. [[maps/Recent Agent Operating Concepts]] · [[maps/What Makes Agent Systems Better]]

## Slide 15 — Takeaways + go deeper (closing · split)

- **L · MAS:** more agents ≠ better · structure must match the task · runtime control & verification beat a longer chain.
- **R · Harness:** harness, tools, and context are the levers · **engineer the state, not the prompt** · memory & skills compound.
- *Pointer:* the vault's first reading path for anyone going deeper. [[maps/Claims Map]] · [[maps/What Makes Agent Systems Better]]

---

## Open decisions for you

1. **Left/right orientation** — I put **MAS left, Harness right** (matches "topic 1 = MAS"). Trivially flippable; say the word.
2. **Ending** — currently converges on "the new stack," with code-factories (slide 9) as the high-energy beat just before. Good, or end somewhere else?
3. **Length** — 15 slides. To hit ~12: fold slide 6 into 5 and 12 into 13. To expand: give context-management (currently inside 5/6) its own slide and split slide 9's evidence across two.
4. **Quotes** — I pulled verbatim lines for the pivotal slides. Want me to source an exact pull-quote for *every* slide, or keep quotes only where they punch?

## Next steps once you sign off

- Lock the spine → I expand each half into final on-slide copy (tighten with **`design:ux-copy`**).
- Then build the `.pptx` and run a layout pass (**`design:design-critique`**) once you pick a visual direction.
