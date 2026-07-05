Title: Why SWE-bench Verified no longer measures frontier coding capabilities

URL Source: https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/

Markdown Content:
Since we first published [SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/) in August 2024, the industry has widely used it to measure the progress of models on autonomous software engineering tasks. After its release, SWE-bench Verified provided a strong signal of capability progress and became a standard metric reported in frontier model releases. Tracking and forecasting progress of these capabilities is also an important part of OpenAI’s [Preparedness Framework](https://openai.com/index/updating-our-preparedness-framework/). When we created the Verified benchmark initially, we attempted to solve issues in the original evaluation that made certain tasks impossible to accomplish in the [SWE-bench dataset⁠(opens in a new window)](https://arxiv.org/abs/2310.06770).

After initial leaps, state-of-the-art progress on SWE-bench Verified has slowed, [improving⁠(opens in a new window)](https://llm-stats.com/benchmarks/swe-bench-verified) from 74.9% to 80.9% in the last 6 months. This raises the question: do the remaining failures reflect model limitations or properties of the dataset itself?

In a new analysis, we found two major issues with the Verified set that indicate the benchmark is no longer suitable for measuring progress on autonomous software engineering capabilities for frontier launches at today’s performance levels:

1.   **Tests reject correct solutions:**We audited a 27.6% subset of the dataset that models often failed to solve and found that at least 59.4% of the audited problems have flawed test cases that reject functionally correct submissions, despite our best efforts in improving on this in the initial creation of SWE-bench Verified.
2.   **Training on solutions:** Because large frontier models can learn information from their training, it is important that they are never trained on problems and solutions they are evaluated on. This is akin to sharing problems and solutions for an upcoming test with students before the test - they may not memorize the answer but students who have seen the answers before will certainly do better than those without. SWE-bench problems are sourced from open-source repositories many model providers use for training purposes. In our analysis we found that all frontier models we tested were able to reproduce the original, human-written bug fix used as the ground-truth reference, known as the gold patch, or verbatim problem statement specifics for certain tasks, indicating that all of them have seen at least some of the problems and solutions during training.

**We also found evidence that models that have seen the problems during training are more likely to succeed, because they have additional information needed to pass the underspecified tests.**

This means that improvements on SWE-bench Verified no longer reflect meaningful improvements in models’ real-world software development abilities. Instead, they increasingly reflect how much the model was exposed to the benchmark at training time. This is why we have stopped reporting SWE-bench Verified scores, and we recommend that other model developers do so too.

We’re building new, uncontaminated evaluations to better track coding capabilities, and we think this is an important area to focus on for the wider research community. Until we have those, OpenAI recommends reporting results for SWE-bench Pro.

## Background

The original [SWE-bench⁠(opens in a new window)](https://arxiv.org/abs/2310.06770) evaluation was released in 2023. Each problem is sourced from a resolved GitHub issue in one of 12 open-source Python repositories and paired with the corresponding pull request (PR). To determine whether a model-generated code change is correct, each problem comes with two sets of tests:

*   Tests that fail on the unmodified codebase but pass if the issue is correctly fixed
*   Regression tests that pass both before and after the fix to ensure unrelated functionality remains intact.

The model does not see the tests. It has to produce a code change given only the original issue text and the state of the repository before the fix. It passes a problem only if all tests pass after the code change is applied.

We found many issues with that evaluation that could lead to underreporting the capability of models.

*   Some unit tests were overly specific or misaligned with the task so correct fixes could be rejected.
*   Many task statements were underspecified, which could lead to multiple valid interpretations - while the tests only covered a specific one.
*   Depending on setup of the environment (for example Linux vs Windows, or the python version), some tests could spuriously fail

We created [SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/) in 2024 to address these issues. We worked with expert software engineers to review 1,699 SWE-bench problems and filter out problems that had these issues. Each problem was reviewed by three experts independently. This review process resulted in SWE-bench Verified, a curated set of 500 problems.

## Too narrow and too wide tests

While SWE-bench Verified is a big improvement over the initial version, residual issues remain. We conducted an audit of 138 SWE-bench Verified problems that OpenAI o3 did not consistently solve over 64 independent runs. Each case was independently reviewed by at least six experienced software engineers. If an expert flagged an issue, it was re-verified by an additional team.

We found that 59.4% of the 138 problems contained material issues in test design and/or problem description, rendering them extremely difficult or impossible even for the most capable model or human to solve.

*   35.5% of the audited tasks have strict test cases that enforce specific implementation details, invalidating many functionally correct submissions, which we call _narrow test cases._
*   18.8% of the audited tasks have tests that check for additional functionality that wasn’t specified in the problem description, which we call _wide test cases._
*   The remaining 5.1% of tasks had miscellaneous issues that were not well grouped with this taxonomy.

An illustrative example of the first failure mode is [pylint-dev__pylint-4551⁠(opens in a new window)](https://github.com/pylint-dev/pylint/pull/4551), where the PR introduces a new function `get_annotation` as part of the overall solution. This function name is not mentioned in the problem description, but is imported directly by the tests. While some models might intuit to create such a function, it’s not strictly necessary to implement a function with this specific name to correctly address the problem. Many valid solutions fail the tests on import errors.

#### Problem description

#### PR test snippet

#### PR test failures (truncated for readability)

An example of too wide test cases is [sympy__sympy-18199⁠(opens in a new window)](https://github.com/sympy/sympy/pull/18199). This task was sourced from a PR that addressed three distinct issues with the `nthroot_mod` function, specifically [#17373⁠(opens in a new window)](https://github.com/sympy/sympy/issues/17373), [#17377⁠(opens in a new window)](https://github.com/sympy/sympy/issues/17377), and [#18212⁠(opens in a new window)](https://github.com/sympy/sympy/issues/18212). The description for the SWE-bench Verified task, however, covers only the final issue [#18212⁠(opens in a new window)](https://github.com/sympy/sympy/issues/18212). This creates a mismatch: the PR tests cover all three issues, while the description details only one. In our runs, models often correctly implement the described fix and then fail tests that cover implementation for the other two issues.

#### Original PR description (from the GitHub PR)

#### Problem Description for #18212

#### Problem Description for SWE-bench Verified task (only taken from #18212):

## Contamination

SWE-bench Verified and the repositories (code bases and release notes) are both open-source and broadly used and discussed, which makes avoiding contamination difficult for model developers.

We first encountered signs of contamination in our own models. For example, when GPT‑5.2 solved 31 tasks we identified to be almost impossible to solve. In [django__django-14725⁠(opens in a new window)](https://github.com/django/django/pull/14725) the tests require a specific new parameter `edit_only` which is not explicitly required by the problem statement. While solving the problem, GPT‑5.2 shows in its chain of thought that it has information about the release notes that detail changes to the codebase, and correctly identifies that the `edit_only` parameter was introduced in Django 4.1.

#### GPT‑5.2 CoT

To assess how significant contamination is more broadly, we created an automated red-teaming setup. For each SWE-bench Verified question, we tasked GPT‑5 with probing a GPT‑5.2‑Chat, Claude Opus 4.5 and Gemini 3 Flash Preview for contamination. These models were chosen to exclude reasoning models, but we acknowledge there is likely a non-trivial capability gap between them.

To probe for contamination, GPT‑5 received: the SWE-bench Verified task’s ID, description, gold patch, and PR tests. Over 15 turns, we allowed GPT‑5 to vary the system/developer prompt, user prompt, and assistant prefill and different elicitation strategies. After each turn, a judge model labeled how much novel task-specific information appeared and each response was labeled for contamination severity from “none” to “strong.” GPT‑5 was allowed to adapt its strategy based on prior turns to iteratively recover task-specific details. For each example of strong contamination, we verified with another judge that GPT‑5 didn’t leak too much information to the target model. Finally, we then manually reviewed the “strong” examples that make up the transcripts in this post.

Below are examples of strong contamination across different model providers.

## GPT‑5.2

Given a short snippet from the task description, GPT‑5.2 outputs the exact gold patch. In particular, it knows the exact class and method name, and the new early return condition ``if username is None or password is None`` that is introduced.

#### Contamination elicitation

#### Gold patch

## Claude Opus 4.5

Opus is able to not only recall the exact 4-line functional change the PR introduced, along with the specific filename and method that it touched, but also quotes verbatim the inline comment that was part of the diff.

#### Contamination elicitation

#### Gold patch

## Gemini 3 Flash

Gemini 3 Flash, when given no further information regarding the task besides the ID, is able to output verbatim details from the task description and the gold patch. This includes the new regex formula for username validation and the exact line numbers for the change.

#### Contamination elicitation

#### Gold patch

## Discussion

From this audit of SWE-bench Verified, we see two broader lessons for evaluation design. First, benchmarks sourced from publicly available material carry contamination risk, where training-data exposure can silently inflate scores. If publicly crawled data is used in benchmark construction, model developers should perform additional tests for contamination. Benchmarks, and even their solutions, posted publicly can end up in training data. Extra care should be taken both in how datasets are posted (i.e. password protected) and training data filtering (i.e. strict adherence to canary strings).

Second, automated scoring is tricky to get right; perfect test cases should fully verify correct functionality, being both agnostic to specific unimportant implementation details and also robust to shortcut solutions. These problems are inherently complex and difficult to solve. Catching these problems took multiple extensive human labeling campaigns.

We have incorporated these findings into our recent evaluation efforts. In the last months we’ve chosen to report results from the public split of SWE-Bench Pro. We recommend other model developers do the same. SWE-bench Pro is not perfect, but empirically seems to suffer less from contamination issues. Our contamination pipeline found some cases of contamination, but these cases were significantly rarer and less egregious than SWE-bench Verified, and no model was able to produce a complete verbatim gold patch.

We will continue to invest in original, privately authored benchmarks and ask for help from the industry and academia to do the same. In [GDPVal⁠](https://openai.com/index/gdpval/), tasks are privately authored by domain experts, reducing exposure risk, and solutions are graded holistically by trained reviewers. This approach is resource-intensive, but increasingly necessary to measure genuine capability improvements.
