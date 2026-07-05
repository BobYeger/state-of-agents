Title: Inspect

URL Source: https://inspect.aisi.org.uk/

Published Time: Wed, 01 Jul 2026 17:47:07 GMT

Markdown Content:
## Welcome

Inspect is a framework for frontier AI evaluations developed by the [UK AI Security Institute](https://aisi.gov.uk/) and [Meridian Labs](https://meridianlabs.ai/). Inspect can be used for a broad range of evaluations that measure coding, agentic tasks, reasoning, knowledge, behavior, and multi-modal understanding. Core features of Inspect include:

*   Composable building blocks—datasets, agents, tools, and scorers—that make evaluations easy to write and reuse.
*   A collection of over 200 pre-built evaluations ready to run on any model.
*   Extensive tooling, including a web-based Inspect View tool for monitoring and visualizing evaluations and a VS Code Extension that assists with authoring and debugging.
*   Flexible support for tool calling—custom and MCP tools, as well as built-in bash, python, text editing, web search, web browsing, and computer tools.
*   Support for agent evaluations, including flexible built-in agents, multi-agent primitives, and the ability to run arbitrary external agents like Claude Code, Codex CLI, and Gemini CLI.
*   A sandboxing system that supports running untrusted model code in Docker, Kubernetes, Modal, Proxmox, and other systems via an extension API.

We’ll walk through two short “Hello, Inspect” examples below. Read on to learn the basics, then read the documentation on [Datasets](https://inspect.aisi.org.uk/datasets.html), [Solvers](https://inspect.aisi.org.uk/solvers.html), [Scorers](https://inspect.aisi.org.uk/scorers.html), [Tools](https://inspect.aisi.org.uk/tools.html), and [Agents](https://inspect.aisi.org.uk/agents.html) to learn how to create more advanced evaluations.

If you are primarily interested in running evaluations rather than developing new ones, see the [Evals](https://inspect.aisi.org.uk/evals/index.html) listing where you’ll find implementations for over 200 popular benchmarks.

## Getting Started

To get started using Inspect:

1.   Install Inspect from PyPI with:

`pip install inspect-ai` 
2.   If you are using VS Code, install the [Inspect VS Code Extension](https://inspect.aisi.org.uk/vscode.html) (not required but highly recommended).

To develop and run evaluations, you’ll also need access to a model, which typically requires installation of a Python package as well as ensuring that the appropriate API key is available in the environment. For example:

*   [OpenAI](https://inspect.aisi.org.uk/)
*   [Anthropic](https://inspect.aisi.org.uk/)
*   [Google](https://inspect.aisi.org.uk/)
*   [HF](https://inspect.aisi.org.uk/)

```
pip install openai
export OPENAI_API_KEY=your-openai-api-key
inspect eval simpleqa.py --model openai/gpt-4o
```

```
pip install anthropic
export ANTHROPIC_API_KEY=your-anthropic-api-key
inspect eval simpleqa.py --model anthropic/claude-sonnet-4-0
```

```
pip install google-genai
export GOOGLE_API_KEY=your-google-api-key
inspect eval simpleqa.py --model google/gemini-2.5-pro
```

```
pip install torch transformers
export HF_TOKEN=your-hf-token
inspect eval simpleqa.py --model hf/meta-llama/Llama-2-7b-chat-hf
```

Inspect has built-in support for over 20 model providers as well as support for local inference with HuggingFace, vLLM, and SGLang. See the documentation on [Model Providers](https://inspect.aisi.org.uk/providers.html) for details on all supported providers.

## Hello, Inspect

An Inspect evaluation is a [Task](https://inspect.aisi.org.uk/tasks.html) that brings together three things:

1.   [Dataset](https://inspect.aisi.org.uk/datasets.html) that provides labelled samples—typically a table with `input` and `target` columns, where `input` is the prompt and `target` is the ideal answer or grading guidance.

2.   [Solver](https://inspect.aisi.org.uk/solvers.html) that produces an answer for each sample. This can be as simple as a single [generate()](https://inspect.aisi.org.uk/reference/inspect_ai.solver.html#generate) call to the model, or as sophisticated as a full agent that uses tools over many turns.

3.   [Scorer](https://inspect.aisi.org.uk/scorers.html) that evaluates the output—using text comparisons, model grading, or other custom schemes.

Let’s look at two short examples: a question-answering benchmark and a capture the flag challenge.

### Benchmark: SimpleQA

This task evaluates a model on [SimpleQA](https://openai.com/index/introducing-simpleqa/), a benchmark of short, fact-seeking questions(click on the numbers at right for further explanation):

**simpleqa.py**

```
from inspect_ai import Task, task
from inspect_ai.dataset import FieldSpec, hf_dataset
from inspect_ai.scorer import model_graded_qa
from inspect_ai.solver import generate

@task
def simpleqa():
    return Task(
        dataset=hf_dataset(
            "codelion/SimpleQA-Verified",
            split="train",
            sample_fields=FieldSpec(
                input="problem",
                target="answer",
            ),
        ),
        solver=generate(),
        scorer=model_graded_qa(),
    )
```

1 The `@task` decorator registers the function with Inspect so that `inspect eval` can discover and run it by name.2[hf_dataset()](https://inspect.aisi.org.uk/reference/inspect_ai.dataset.html#hf_dataset) loads samples directly from Hugging Face. Inspect also reads CSV, JSON, and in-memory datasets.3[FieldSpec](https://inspect.aisi.org.uk/reference/inspect_ai.dataset.html#fieldspec) declaratively maps the dataset’s `problem` and `answer` columns onto the sample’s `input` and `target`—no custom conversion function required.4 The [generate()](https://inspect.aisi.org.uk/reference/inspect_ai.solver.html#generate) solver simply sends each `input` to the model and collects its response.5 Because the answers are free-form text, [model_graded_qa()](https://inspect.aisi.org.uk/reference/inspect_ai.scorer.html#model_graded_qa) uses a model to grade each response against the `target`.
Run it from the command line with `inspect eval`, choosing a model with `--model`:

`inspect eval simpleqa.py --model openai/gpt-5`

Use `inspect view` to view the results:

`inspect view`

[![Image 1](https://inspect.aisi.org.uk/images/log-viewer-simpleqa.png)](https://inspect.aisi.org.uk/images/log-viewer-simpleqa.png)

### Agent: CTF Challenge

Agent evaluations require the model take actions rather than just answer a question. Here’s a Capture the Flag (CTF) task where the [react()](https://inspect.aisi.org.uk/agents.html) agent explores a sandboxed system using [bash()](https://inspect.aisi.org.uk/reference/inspect_ai.tool.html#bash) and [todo_write()](https://inspect.aisi.org.uk/reference/inspect_ai.tool.html#todo_write) tools to find a hidden flag:

**ctf.py**

```
from inspect_ai import Task, task
from inspect_ai.agent import react
from inspect_ai.dataset import json_dataset
from inspect_ai.scorer import includes
from inspect_ai.tool import bash, todo_write

@task
def ctf():
    return Task(
        dataset=json_dataset("challenges.json"),
        solver=react(
            prompt=(
                "You are a Capture the Flag player.
                Explore the system and find the flag."
            ),
            tools=[bash(), todo_write()],
            attempts=3,
        ),
        scorer=includes(),
        sandbox="docker",
    )
```

1[react()](https://inspect.aisi.org.uk/reference/inspect_ai.agent.html#react) is a built-in agent that runs a reason-act-observe loop, giving the model the supplied `tools` until it submits an answer (here allowing up to 3 attempts).2 The [includes()](https://inspect.aisi.org.uk/reference/inspect_ai.scorer.html#includes) scorer passes if the target flag appears in the agent’s submitted answer.3`sandbox="docker"` runs all tool calls inside an isolated Docker container (configured by a `Dockerfile` or `compose.yaml` alongside the task).
Use `inspect view` to view the results and look more carefully at individual transcripts:

[![Image 2](https://inspect.aisi.org.uk/images/log-viewer-ctf.png)](https://inspect.aisi.org.uk/images/log-viewer-ctf.png)

See the [Tutorial](https://inspect.aisi.org.uk/tutorial.html) to explore more in-depth examples that demonstrate additional Inspect features and techniques.

## Python API

Above we demonstrated using `inspect eval` from CLI to run evaluations—you can perform all of the same operations from directly within Python using the [eval()](https://inspect.aisi.org.uk/reference/inspect_ai.html#eval) function. For example:

```
from inspect_ai import eval
from simpleqa import simpleqa

eval(simpleqa(), model="openai/gpt-5")
```

## LLM Assistance

As you learn and use Inspect we recommend you provide an LLM with the documentation required for it to assist. There are two versions of LLM friendly markdown documentation available:

*   [llms.txt](https://inspect.aisi.org.uk/llms.txt): Documentation index, articles fetched as required (~2k tokens).

*   [llms-guide.txt](https://inspect.aisi.org.uk/llms-guide.txt): Full contents of all documentation (~185k tokens).

There is also a **Copy Page** button at the top of every page that provides a markdown version of the page.

## Learning More

To learn more about using Inspect see the following documentation sections:

*   [Tutorial](https://inspect.aisi.org.uk/tutorial.html) includes several annotated examples demonstrating various features an capabilities.

*   [Components](https://inspect.aisi.org.uk/tasks.html) are the building blocks of an evaluation: tasks, datasets, solvers, and scorers.

*   [Models](https://inspect.aisi.org.uk/models.html) covers specifying models and providers, along with caching, multimodal input, reasoning, batch mode, and concurrency.

*   [Agents](https://inspect.aisi.org.uk/agents.html) combine planning, memory, and tool use for longer-horizon tasks, including the built-in ReAct agent, multi-agent architectures, and bridges to external frameworks.

*   [Tools](https://inspect.aisi.org.uk/tools.html) extend models with custom and built-in tools, MCP integrations, sandboxing, and tool-call approval.

*   [Running](https://inspect.aisi.org.uk/running.html) covers running larger eval sets, with error handling, limits, parallelism, and early stopping.

*   [Analysis](https://inspect.aisi.org.uk/analysis.html) explains how to read eval logs, extract data frames, and scan transcripts for issues.

*   [Extensions](https://inspect.aisi.org.uk/extensions.html) shows how to extend Inspect with new model APIs, components, sandboxes, approvers, hooks, and filesystems.

You may also want to explore the [Evals](https://inspect.aisi.org.uk/evals/index.html) listing of ready-to-run benchmark implementations, the [Extensions](https://inspect.aisi.org.uk/extensions/index.html) gallery of community packages, and the [Reference](https://inspect.aisi.org.uk/reference/index.html) for the complete Python and CLI API.

## Citation

BibTeX citation:

```
@software{UK_AI_Security_Institute_Inspect_AI_Framework_2024,
  author = {AI Security Institute, UK},
  title = {Inspect {AI:} {Framework} for {Large} {Language} {Model}
    {Evaluations}},
  date = {2024-05},
  url = {https://github.com/UKGovernmentBEIS/inspect_ai},
  langid = {en}
}
```

For attribution, please cite this work as:

AI Security Institute, UK. 2024. _Inspect AI: Framework for Large Language Model Evaluations_. Released May. [https://github.com/UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai).
