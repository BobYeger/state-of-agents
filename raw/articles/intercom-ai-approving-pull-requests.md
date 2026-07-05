Title: AI is approving our pull requests: Here’s how we made it safe

URL Source: https://www.intercom.com/blog/ai-is-approving-our-pull-requests-heres-how-we-made-it-safe/

Published Time: 2026-04-21T15:36:28+00:00

Markdown Content:
At Intercom, [shipping is our heartbeat](https://www.intercom.com/blog/shipping-is-your-companys-heartbeat/). We push code to production hundreds of times a day.

Engineers, engineering managers, designers, and PMs all contribute to this, safely. The average time from merging code to it running in production is [12 minutes](https://www.intercom.com/blog/the-safety-of-speed-shipping-code-at-intercom/).

We’ve long held a belief that might sound counterintuitive: speed is not the enemy of safety. It’s a prerequisite for it. Accumulating code creates risk. Shipping small batches minimizes it. The faster you ship, the smaller each change is, and the easier it is to catch problems, and roll back when something goes wrong as the context is still fresh in your head.

Today, over 93% of our pull requests (PRs) across our two main codebases are Agent-driven. And over 19% are auto-approved with no human reviewer in the loop.

This post is about that second number, and why we think it makes us safer. Most people hear “AI is approving our pull requests” and think that’s reckless. We think the data tells a different story.

## The 2x effort

Last year, our CTO Darragh Curran set an explicit goal: [double the productivity of our entire R&D organization within 12 months](https://ideas.fin.ai/p/2). Because the faster we can build and ship, the faster our customers get the capabilities they need.

Nine months later, [we did it](https://ideas.fin.ai/p/2x-nine-months-later). The results have been significant across the board, but the number that matters most for this post: downtime from breaking code changes dropped 35%, even as our deployments doubled. Shipping faster made us safer. As we modernize how we build and ship software, we systematically surface bottlenecks and tackle them. One of the biggest we’ve found? PR review.

## The PR review problem

Humans simply don’t have the time or mental capacity to properly review the volume of AI-generated code we’re now producing.

When an AI Agent can produce a working implementation in minutes, waiting hours or days for a human to review it is an impedance mismatch. The production line is moving faster than the quality gate can keep up.

When that happens, one of two things follows: either the queue backs up and velocity drops, or, more dangerously, humans start rubber-stamping. Glancing at a diff, skimming the description, clicking approve.

Some companies are drifting into this failure mode silently. We chose to confront it head-on and built a rigorous solution.

PR review, done properly, is a genuinely complicated process. A good reviewer assesses the quality of the problem statement based on the PR description. They confirm the changeset actually matches the stated intent. They review the code against best practices, look for logical issues, apply their personal product context to validate the changes make sense, and check for performance issues, safety concerns, and more. No single human reviewer realistically has experience to properly cover every one of these dimensions on every PR, especially not under time pressure. And as we’ll see in the data, the baseline we’ve been comparing against, human review, was weaker than most of us assumed.

So we asked ourselves: what if we could do better?

## How our PR review Agent works

Our PR review Agent doesn’t treat code review as a single task. It decomposes it into separate sub-jobs, each handled by an independent sub-Agent. One assesses the quality of the problem description. Another checks whether the diff actually aligns with the stated intent. Another reviews for safety concerns. Another checks for logical correctness. Another reviews against best practices and known anti-patterns. And so on.

The result is that every PR is reviewed as if a dozen of our most tenured and knowledgeable engineers were all looking at it simultaneously, each bringing their own specialist lens. In the past, getting that breadth of review on a single PR was impossible. Now it’s the default.

A human reviewer typically focuses on the actual code changes, the diff. Our Agent goes deeper. It traces execution paths, following the implications of a change through the codebase. This is something humans rarely had time to do, even when they wanted to.

A real example:

While testing our new PR review Agent on a set of historical PRs, we found it flagging a one-line text copy change as incorrect. On the surface, it looked completely harmless, just a text update. We assumed it was a mistake, but it wasn’t. Our Agent caught that the new copy contradicted an existing validation mechanism elsewhere in the codebase. No human reviewer would have realistically found this unless they happened to have written that validation code very recently. Our Agent catches this kind of thing consistently, every time, because it’s always tracing execution.

The review isn’t generic either. It’s grounded in Intercom-specific guidance that our engineers have built and continue to refine, encoding the same context, standards, and product knowledge they’d apply if they were reviewing the PR themselves. When the Agent reviews a PR, engineers flag whether the review comments were helpful or not, and that feedback continuously sharpens the guidance. It’s a flywheel: the more our engineers invest in teaching the system how to think about our codebase, the better every subsequent review gets.

Automated approval is also never forced. Any engineer can request a human review on any change, at any time. The system is a tool, not a mandate. At Intercom, shipping code doesn’t end at merge. The engineer who ships a change is expected to watch it go live, monitor its behaviour in production, and be ready to roll back if something isn’t right. AI approval doesn’t change that. The human who ships the code remains accountable for the outcome.

![Image 1: Graph showing 19.2% of all PRs fully auto-approved by AI, 60% are evaluated by AI](https://blog.intercomassets.com/blog/wp-content/uploads/2026/04/pr-funnel-scaled.png)

## Not just faster; safer

The naive take on AI-approved PRs is that it’s just a rubber-stamp LLM call so that humans don’t have to bother. A convenience feature. That misses what’s actually happening.

Our Agent is strict. It won’t approve large PRs. If a change is too big, too complex, or too broad in scope, it flags it and requires it to be broken down. Creating a direct, positive incentive for engineers to ship smaller, more incremental, well-scoped changes.

This matters enormously for safety. Small changes are easier to review, easier to test, easier to understand, and, critically, easier to roll back when something goes wrong. This is the same principle that has always underpinned [our shipping culture](https://www.intercom.com/blog/ship-fast-safe-learn-from-production/), but now the PR review Agent actively enforces it.

It’s tempting to look at a goal like “>50% AI-approved PRs” and worry that we’re optimizing for the metric rather than the outcome. We see it differently. Our goal was to remove a bottleneck that, if left unchecked, risked pushing engineers towards rubber-stamping reviews under time pressure.

On the surface, our PR review Agent is only a solution to “humans don’t have time to review PRs.” But what it really is, at its core, is a safety mechanism. It ensures we continue shipping fast, in small increments, maintaining and increasing our heartbeat, even as the volume of AI-generated code grows.

## The data

We didn’t assume AI review would be good enough, we actively ran an experiment.

Our hypothesis was that AI review could match or outperform human review quality, measured by the outcomes that actually matter: were the changes correct? Did they cause problems in production? How quickly were they reviewed and approved?

We started with a controlled pilot of over 100 PRs through the AI approval pipeline. The results: zero reverts of AI-approved PRs, and a 6–16x improvement in time-to-approval at the 75th percentile. Since then, the system has scaled significantly. In the first four weeks of broader rollout, 497 PRs went fully autonomous, with Claude writing the code and our AI approval system reviewing, approving, and shipping to production.

![Image 2: Graph showing AI approval is 5x faster than human review](https://blog.intercomassets.com/blog/wp-content/uploads/2026/04/approval-time-scaled.png)

Beyond the approval pipeline itself, we also looked more broadly at how AI-authored code performs in production compared to human-authored code. AI-authored backend code had a revert rate of 0.53%, compared to 5.39% for human-authored. On the frontend, it was 0.22% versus 2.00%.

![Image 3: 10X lower revert rate for AI-Authored code](https://blog.intercomassets.com/blog/wp-content/uploads/2026/04/revert-rates-scaled.png)

AI-authored code, reviewed and approved through our automated pipeline, is being reverted at a fraction of the rate of human-authored, human-approved code. We don’t expect that to hold at zero forever, but the data so far tells us that the quality bar our Agent holds is at least as high as the one humans were holding, and in many cases higher.

And perhaps the most important perspective shift: those product changes that did cause outages in the past? They were all reviewed and approved by humans. Human review is not a guarantee of safety. It never was. It’s a useful heuristic, but one with real limitations that we’ve been quietly accepting for decades.

## Staying compliant while we innovate

Everything we’ve described in this post, the sub-Agent architecture, the traceability, the labelling, the data, none of it was built just to make the system fast. It was built to make the system auditable. That was a design constraint from day one.

Every AI-approved PR is labelled, logged, and queryable. The review comments, the approval decision, the test results, the merge event: all recorded. The evidence an auditor expects to see is the same whether a human or an AI approved the change. The “who” may change, but the “what” doesn’t.

We engaged our auditors, Schellman, early, before we scaled. We proactively worked with them to confirm that our automated review processes and the evidence they produce meet the requirements of our [compliance frameworks](https://trust.intercom.com/), including SOC 2, HIPAA, ISO 27001, ISO 42001, and AIUC-1, among others. We think AI-driven change management can meet and exceed the standards that human-driven processes set, and we want to help prove that.

We see this as a feature of building the system the right way, not an extra hurdle we had to clear. When you build for safety, compliance follows.

## What’s next

You can only go so far with PR review as a safety mechanism, no matter how good the reviewer is, human or AI. Only in production do you discover the unknown unknowns. The majority of Intercom’s largest outages weren’t even caused by changes to product code at all. They were infrastructure issues, unanticipated customer usage patterns, or third-party outages. PR review, whether human or AI, was never going to catch those. That’s why, in parallel, we’re also working on an Agent that proactively diagnoses issues in production. We’ll share more on this soon.

Speed has always been at the core of how we build at Intercom, not in spite of safety, but because of it. And we’re getting even faster with AI. It’s easy to assume that AI-approved PRs would lead to a drop in quality and safety but our data proves otherwise. Our heartbeat is just getting stronger.
