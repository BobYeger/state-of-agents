Title: Separating signal from noise in coding evaluations

URL Source: http://openai.com/index/separating-signal-from-noise-coding-evaluations/

Markdown Content:
Accurately measuring our models’ capabilities is important for sound deployment and safety decisions, including decisions under OpenAI’s [Preparedness Framework⁠(opens in a new window)](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf). With each model release, we report results for a variety of external and internal benchmarks to track model progress. When evaluations have flaws that affect results, they can give a false understanding of capabilities, misrepresenting safety cases and affecting research priorities.

We [recently investigated](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) how one of the most widely used coding benchmarks, SWE-bench Verified, had fundamental design and contamination issues, and found that the eval no longer provided meaningful signal on software development capabilities. At the time, we encouraged the wider community to switch to SWE-Bench Pro.

[SWE-Bench Pro⁠(opens in a new window)](https://scale.com/blog/swe-bench-pro) was designed to improve on SWE-bench Verified by testing models on longer horizons and more realistic coding tasks to better track agentic coding capabilities. As in SWE-bench Verified, tasks are sourced programmatically from the history of feature changes in a set of public and private repositories. Models are required to implement a solution that passes new tests for a feature, without breaking existing functionality. On the 731-task public split, frontier models improved from a pass rate of 23.3% to 80.3% in eight months.

We’ve since performed a similar audit on SWE-Bench Pro, reviewing the dataset using a datapoint analysis pipeline. The pipeline reviewed model attempts at the task, task metadata, and failure traces to flag likely evaluation flaws. Each flagged task was then assessed through multiple investigator-agent passes and independently reviewed by five experienced software engineers, with disagreements escalated for further investigation.

We find evidence of breaking issues in a significant portion of the dataset. Our datapoint analysis pipeline flagged 200 (27.4%) broken tasks, while the human annotation campaign identified 249 (34.1%).

The issues primarily fell into four categories:

*   _Overly strict tests_[1](http://openai.com/index/separating-signal-from-noise-coding-evaluations/#citation-bottom-1) enforce specific implementation details not specified in the prompt, invalidating many functionally correct submissions.
*   _Underspecified prompts_[2](http://openai.com/index/separating-signal-from-noise-coding-evaluations/#citation-bottom-2) omit requirements that hidden tests enforce and that are not reasonably inferable.
*   _Low-coverage tests_ under check the requested feature, so incomplete fixes can pass.
*   A _misleading prompt_ points models toward the wrong behavior or contradicts what tests require.

Our findings point to the difficulty of curating hard but fair benchmarks and the growing utility of agents for scalable data quality checks. In light of these results, we estimate that ~30% of SWE-bench Pro tasks are broken, and advise that model developers carefully examine results.

## Methodology

Our aim is to ensure that task failures reflect genuine model limitations, and task successes reflect complete and valid solutions to the prompt requirements. To check the quality of the data used in the evaluation, we created a quality assurance pipeline to assess whether each datapoint accurately reflects model capabilities.

An initial data quality pipeline flags problems for review. We validate with a deeper agent-assisted audit of flagged tasks and a human annotation campaign working with experienced engineers.

An initial automated filter reviews the instructions given to the model, attempts by the model to solve the task, and the tests used to grade these attempts to flag likely broken or problematic examples. This filter flagged 286 potentially broken tasks. We then conducted a deeper review of that subset in two ways: a human-supervised agent review, which conducts extensive checks with investigator agents and a final human judgment; and a human annotation campaign working with experienced software developers.

## Human-supervised agent review

Each flagged problem is audited with Codex-based investigator agents that were given access to the task repository and environment. This helps them distinguish reasonable task ambiguity, which can often be resolved by studying nearby code and repository conventions, from true underspecification. The agent can run tests, inspect files in the repo, and investigate model attempts and their common failure modes on the task. After several independent repeats of these deeper audits, a researcher reviewed the summaries, made a final judgment, and labeled the likely issues.

## Human annotation campaign

In parallel, we ran a human annotation campaign over the flagged subset. We worked with experienced software engineers who were trained on the benchmark goals, issue taxonomy, and edge cases before reviewing tasks. Each task was reviewed by five engineers.

Reviewers formed an independent judgment from the visible problem statement, test cases, and the ground-truth reference solution (known as the gold patch) before using the pipeline analysis or transcript as supporting context. The reviewers then assigned a label and severity rating based on concrete evidence, and escalated disagreements or low-confidence cases for further review.

Human reviewers were more likely than the investigator agents to mark tasks as broken. There was also some disagreement on categories between the two review paths, but in no flagged task was “not broken” the most common human label. Of the categories the agent pipeline flagged, reviewers’ judgments overlapped in 74% of cases.

Compared with the agent pipeline, the human reviewers were also more likely to select multiple labels for a task, indicating that they found tasks to be broken in multiple ways or did not fit cleanly into a single category. This suggests the agent-plus-reviewer pipeline resulted in conservative labeling: it captured the same broad failure modes humans identified, while undercounting cases where reviewers saw additional or overlapping issues. The largest difference was in low-coverage tests, which humans selected as the most common issue for 9.4% of the benchmark compared with 4.1% from the agent pipeline.

### Failure modes

In several cases the task prompt prescribed a specific implementation, but the hidden test cases expected different behavior.

## Discussion

The issues we have identified, coupled with similar cases in [SWE-bench Verified](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/), highlight the importance of rigorously checking benchmarks. Issues and pull requests from open-source repositories were originally created for human collaboration, often through long back-and-forths between maintainers and contributors. As a result, problem descriptions, merged code, and unit tests do not always line up to form clean, isolated tasks for evaluating models reliably. In particular, tests included in pull requests can be overly strict because they are written to validate a specific change, rather than to define an implementation-agnostic standard for solving the task.

At the same time, evaluation flaws are easier to detect now than they would have been even a short time ago. As model capabilities improve, we can use those models to inspect prompts, tests, patches, traces, and edge cases with much greater depth and consistency, helping surface benchmark issues that were previously costly or impractical to find at scale.

We hope the wider evaluation community will develop new benchmarks built by experienced software developers specifically to test model capabilities. That approach can preserve the high bar and realism we want to measure model capabilities, and allows for better human oversight throughout the process. Given the issues uncovered in this analysis, we retract our earlier recommendation to adopt SWE-Bench Pro.

Ultimately, an eval should provide meaningful signal through benchmarks that are hard to game, easy to trust, and genuinely reflective of model capability or alignment. Because these results inform OpenAI’s deployment and safety decisions, the evals we track need to be valid and informative.
