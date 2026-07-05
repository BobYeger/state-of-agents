Title: Seer, Sentry’s AI Debugger, is Generally Available

URL Source: https://blog.sentry.io/seer-sentrys-ai-debugger-is-generally-available/

Published Time: 2025-06-17T00:00

Markdown Content:
Tired of trying to guess if that half-baked LLM suggestion is really going to fix the issue with your code? Meet [Seer](https://docs.sentry.io/product/ai-in-sentry/seer/)—our new AI agent that taps into _all_ the issue context from Sentry _and_ your codebase to not just _guess_, but root cause gnarly issues and propose merge-ready fixes specific to your application.

Code gen tools are great fun—and useful. But even a recent Microsoft [study](https://www.microsoft.com/en-us/research/blog/debug-gym-an-environment-for-ai-coding-tools-to-learn-how-to-debug-code-like-programmers/) confirmed what you already know: AI struggles with debugging. And as reported [here](https://venturebeat.com/ai/ai-can-fix-bugs-but-cant-find-them-openais-study-highlights-limits-of-llms-in-software-engineering/) (before Seer GA’d, of course), “Agents excel at localizing, but fail to root cause, resulting in partial or flawed solutions.”

### That’s where Seer is different.

[Debugging needs deep context](https://blog.sentry.io/want-ai-to-be-better-at-debugging-its-all-about-context/). Seer gets it—from the stack trace, the commit history, the traces and spans, and even that haunted line of code someone pushed six months ago. It’s not a hallucinating solution. It’s _diagnosing the problem with precision_.

Since its beta (you might remember it as Autofix), Seer has:

*   Analyzed 38,000+ issues
*   Identified root causes with 94.5% accuracy
*   Saved devs over 2 years of collective time

### The TL;DR?

It’s the debugger you’ve always wished would just show up, figure out what broke and why, tell you how to fix it, and shut the laptop for you.

![Image 1: Tweet by Aiden Bai (@aidenybai) says Sentry Autofix worked surprisingly well, fixing a bug instantly that took him 2 hours to debug. Screenshot shows Sentry Autofix (beta) identifying a root cause: mouse events after page closure caused a TargetCloseError due to unsynchronized page and socket operations.](https://blog.sentry.io/_vercel/image?url=_astro%2Finline-0.CyzU3r49.png&w=1200&q=100)

## How does Seer work?

Seer pulls together everything Sentry knows about an issue—stack traces, environment info (browser, OS, etc.), spans, commits, logs ([now in beta](https://blog.sentry.io/logs-in-sentry-open-beta/)), and profiling data. It is able to access this context in an agentic fashion - this means we’re not just copy-pasting a bunch of Sentry context, we’re exposing it to Seer as a resource just like code search.

Also, Seer doesn’t just leverage context from all the exceptions Sentry captures — it also taps into your codebase to:

*   Execute grep-like searches across your files
*   Parse and interpret documentation
*   Trace and analyze commit history
*   Examine multiple repositories to catch potential breaking changes before they happen
*   Modify files directly when needed

[Video 3](https://vimeo.com/1093596425)

Think uncaught JavaScript exceptions, Rust backend crashes, or slow N+1 queries. That `TypeError` in a React component? Sentry shows you the error and the commit—Seer takes it further. It analyzes the code, recent changes, and runtime context to root-cause the issue. Maybe it’s an undefined prop or a missing null check—Seer figures it out, suggests a fix, and opens a pull request. No guesswork, no context-switching.

### **Oh, and one more thing: Seer doesn’t just _suggest_ fixes—it can now fix things for you. Automatically.**

Yep. With automated issue scans, Seer keeps an eye on all your incoming issues and highlights the ones that are most actionable—giving you tighter Slack alerts and less noise.

![Image 2: Screenshot of the “New and Actionable” issues view in Sentry’s dashboard. A search filter is applied: unresolved issues with issue.seer_actionability set to super_high. The list shows several “SubscriptionError” issues with tags like se is not a tag in the metrics dataset and http.url is not a tag in the metrics dataset. Each issue displays status info such as age, last seen, event count, users affected, priority, and assignee. A tooltip is visible over one issue that says: “Seer has a potential quick fix for this issue.”](https://blog.sentry.io/_vercel/image?url=_astro%2Finline-1.CfrLrS0n.png&w=2048&q=100)

Flip on Automated Fixes, and Seer will go _even_ further: it’ll root cause the issue _and_ draft a solution without you lifting a finger. You stay in control—nothing gets merged without your approval.

**No triage. No toil. No wasted cycles. Just real fixes.**

## What can Seer _really_ fix for me?

Seer can act like your robovac. It will pick up all the scraps and fix basic issues for you while you mow through new feature tickets. Seer’s also really good at figuring out tricky problems that involve a bunch of different services talking to each other, because it sees so much data.

### Type errors, null dereferences, missing keys — solving simple issues, fast

For routine bugs and performance issues—like unhandled type exceptions (“`foo`” where an `int` was expected)—Seer helps clear the backlog fast.

Instead of opening your IDE, creating a new branch, tracking down the relevant code, and writing a fix, Seer can run automatically the moment the error hits Sentry. By the time you see the alert, it’s already proposed a fix. The PR is two clicks away.

> “It’s no longer one dev, one PR. I’m running Seer across all our issues in parallel. If a fix is off, no big deal—reject it, give more context, try again. Iteration is cheap, and it’s saving my team days.”

_-Neil Wang, Engineering Manager at Curai_

We’ve seen it ourselves too. In one case, Seer opened [a PR](https://github.com/getsentry/sentry/pull/91809) in the Sentry repo (yes, it’s fixing itself) to resolve an exception caused by unhandled `None` values. All our team had to do was review the diff and hit merge.

![Image 3: Screenshot of a merged GitHub pull request titled: “fix(seer): Ensure count is a valid float in TimeSeriesPoint (#91809)” The PR was merged into the master branch from autofix/fix-seer-float-count. A comment from the seer-by-sentry bot states the PR was auto-generated by Autofix and triggered by Rohan Agarwal. It fixes an issue where format_crash_free_data passed None values as TimeSeriesPoint.value, which failed float validation. Fix summary: Ensures count is always a valid float. Converts None to 0.0 for count. Reviewers include user ceorourke under the "Machine Learning & AI" team. Labels show: Scope: Backend and Trigger: getsentry tests.](https://blog.sentry.io/_vercel/image?url=_astro%2Finline-2.HnSffVLf.png&w=2048&q=100)

### Flaky jobs, lost responses, invisible failures — debug complex issues

Seer is like a pair programmer that’s spent 10+ hours reviewing all of the relevant Sentry telemetry data. For example, it uses spans/trace data to infer relationships across repos and projects in complex, distributed systems. And everything from its prompts to its tools is purpose-built and rigorously tested to turn that context into answers—more reliably than any generic AI.

Take Curai Health, an AI-powered healthcare startup with a React Native codebase and a product surface spanning web and mobile. After introducing animated to-dos, a subtle bug slipped past QA — Android expected a `gap` property in the reordered array, but web didn’t care. Seer read the breadcrumbs, traced the root cause, and surfaced a fix in minutes — something that would’ve taken a developer a full day to track down.

> Seer provided insights that led us to a fix within 30 minutes, for a bug that would have taken an engineer at least a day otherwise.

_- Neil Wang, engineering manager at Curai Health_

In one case, Seer [refactored](https://github.com/getsentry/sentry/pull/83888) the `create_issue` method in `issues.py` to improve clarity and efficiency—grouping required fields into a dictionary, conditionally adding optional fields, and cleaning up formatting. The result? Less redundancy, cleaner diffs, and a more maintainable implementation.

![Image 4: Screenshot of a merged GitHub pull request titled: “🤖 Refactor GitHub Issue Creation Code for Clarity and Efficiency (#83888)” User cleptric merged 2 commits into the master branch from autofix/refactor-github-issue-creation-code-for-clarity-and-efficiency on January 24. A comment by the seer-by-sentry bot notes the PR was automatically generated by Autofix and triggered by Michi Hoffmann. It fixes issue SENTRY-3GEH by refactoring the create_issue method in issues.py to use an issue_data dictionary for better clarity and efficiency. Reviewers include cleptric, and teams: Product Owners: Settings - Integrations and Ecosystem. Label changes show +13 additions and -11 deletions.](https://blog.sentry.io/_vercel/image?url=_astro%2Finline-3.D82i7JL6.png&w=2048&q=100)

Troubleshoot issues in distributed systems

Seer can also work across distributed systems in multiple codebases.

In one of our sample apps, Sentry logged a `TypeError` on the React frontend: “Failed to fetch”. Seer [traced](https://docs.sentry.io/concepts/key-terms/tracing/) it through the stack to an ASP.NET backend, where a recent change had broken the API response. The frontend wasn’t handling the null value—because no one told it to.

Seer identified the backend commit, explained the root cause, suggested a fix, and opened a pull request—on the right service.

![Image 5: Screenshot of a Sentry error issue page (ID: REACT-5XK) and its AI-powered Seer panel. The error is: “Checkout failed: TypeError: Failed to fetch (aspnetcore.empower-plant.com)” The issue is labeled new and occurred on the /checkout endpoint, with 2.4k events and 2.2k users affected. In the Seer panel (beta), Seer analyzes the issue and highlights the problem: “The backend Checkout method is hardcoded to throw a 'Not enough inventory' exception.” It provides a solution: “Remove hardcoded exception in backend checkout controller.” Suggested code changes show an edit in aspnetcore/Controllers/CheckoutController.cs to return a 204 No Content status instead of throwing an exception. Options shown include “Code It Up,” “Check Out Locally,” and “Draft PR.”](https://blog.sentry.io/_vercel/image?url=_astro%2Finline-4.BgEwDVPQ.png&w=2048&q=100)

## What do developers think so far?

We’re not usually ones to brag, so we’ll let a few developers do it for us

Even though today’s experience with Seer is already good—like any AI tool, it’s only getting better. We built it to flexibly adopt the best frontier models from OpenAI, Anthropic, Google, and others. As new LLMs become available, we evaluate and integrate them if they improve results.

> I’ve been using Seer firsthand over the past few days, and I must say — the tool looks very promising. The root cause analysis is spot-on, and it’s truly impressive work from Sentry to empower developers with such deep insights.

_-Bharath Manjunath, Sr. Software Engineer at Sky Network TV_

We’re also expanding what Seer can access inside Sentry. Since the start of the year, we added support for traces, profiles, and logs—session replays are coming soon. We recently shared more about [our approach](https://blog.sentry.io/sentry-ai-debugger-autofix-superpower-traces/) on the blog.

## Puts your privacy first

We built Seer with privacy and security front and center. Here’s the short version:

*   Seer doesn’t use your data to train generative AI models without your explicit consent (it’s off by default).
*   Your inputs and responses stay private—visible only to you and other authorized users in your Sentry organization.

You can dig into the full details in our [AI privacy and security](https://docs.sentry.io/product/ai-in-sentry/ai-privacy-and-security/)docs.

## How can I try Seer?

Seer is available to all Sentry users on a paid plan (Team, Business, or Enterprise). You can try it free for 14 days—no separate setup required.

After the trial, Seer can be added to your subscription for $20/month, which includes $25/month in credits for issue fixes ($1/run) and scans ($0.003/issue).

To get started, just go into any issue and click ‘Find Root Cause’ where you will be prompted to start your free trial. You can connect your [GitHub](https://docs.sentry.io/organization/integrations/source-code-mgmt/github/) repo to, bring in more insights, unlock automated fixes, and configure your project settings.

Got feedback, feature requests, or a “Seer saved my day” story? We’d love to hear it—email us at [seer@sentry.io](mailto:seer@sentry.io)or come hang out on [Discord](https://discord.com/invite/ez5KZN7).
