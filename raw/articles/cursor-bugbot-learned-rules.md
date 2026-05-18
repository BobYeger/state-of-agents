Title: Bugbot now self-improves with learned rules

URL Source: https://cursor.com/blog/bugbot-learning

Published Time: 2026-04-08T12:00:00.000Z

Markdown Content:
When we [launched Bugbot](https://cursor.com/blog/bugbot-out-of-beta) out of beta in July 2025, 52% of the bugs it identified were resolved by the time the relevant PR was merged, indicating the rest were false positives.

Today, the resolution rate is nearing 80%, 15 percentage points higher than the next-closest AI code review product.

| AI code review product | Resolution rate | PRs analyzed |
| --- | --- | --- |
| Cursor Bugbot | 78.13% | 50,310 |
| Greptile | 63.49% | 11,419 |
| CodeRabbit | 48.96% | 33,487 |
| GitHub Copilot | 46.69% | 24,336 |
| Codex | 45.07% | 19,384 |
| Gemini Code Assist | 30.93% | 21,031 |

We analyzed public repositories only. For each comment produced by an AI code review product, we checked to see if it was addressed by the time it merged using an LLM judge.

Up until now, improvements have been propelled exclusively by offline experiments: We tweak Bugbot, test to see if the change improves the resolution rate, and we ship it if it does.


But a strictly offline approach leaves a lot of training potential untapped. Bugbot reviews hundreds of thousands of PRs per day, and each review is a natural experiment that Bugbot can use to self-improve based on whether the developer acted or not on its report.

To harness those real-time signals, we've now enabled Bugbot to learn from past runs, transforming feedback from the live code review process into learned rules. Rules act as additional instructions that enable greater customization of Bugbot runs, helping Bugbot focus on specific issues, business context, and more.

Since launching [learned rules](https://cursor.com/docs/bugbot#learned-rules) in beta, more than 110,000 repos have enabled learning, generating more than 44,000 learned rules.

## [](https://cursor.com/blog/bugbot-learning#how-learned-rules-work)How learned rules work

Every merged PR contains a range of signals that Bugbot can use to self-improve and codify into rules. Three important signals are:

1.   **Reactions to Bugbot comments**, where a downvote tells Bugbot the finding wasn't useful.
2.   **Replies to Bugbot comments**, in which developers explain what was wrong or how the suggestion could have been better.
3.   **Comments from human reviewers**, which flag issues that Bugbot missed.


Bugbot processes these signals into candidate rules that it continues to evaluate against incoming PRs. As signal accumulates, Bugbot can promote a candidate rule to active status where it begins influencing future reviews. Similarly, if an active rule starts generating consistent negative signal, Bugbot can disable it. You can also edit or delete rules directly in the UI.

## [](https://cursor.com/blog/bugbot-learning#get-started)Get started

We want Bugbot to catch every real bug, which requires a deep understanding of your codebase, patterns, and team's priorities. Learned rules are a big step in that direction, and they're part of our overall effort to make Bugbot continually self-improving.

Manage Bugbot learning in the [Cursor Dashboard](https://cursor.com/dashboard/bugbot/repository-rules), where you can enable learned rules and run a backfill across recent PRs, or learn more in our [docs](https://cursor.com/docs/bugbot#learned-rules).
