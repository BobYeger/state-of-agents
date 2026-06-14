# AlphaEvolve

Source URL: https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/

Capture date: 2026-06-14

Capture note: partial research snapshot from Google DeepMind's AlphaEvolve announcement. See the local PDF artifact for the white paper.

## Core framing

AlphaEvolve is an evolutionary coding agent for algorithm discovery and optimization. It combines LLM-generated code changes with automated evaluators and an evolutionary program database.

## Key mechanisms

- Prompt sampler assembles prompts from prior programs and context.
- Gemini models propose new programs or code modifications.
- Evaluators run and score candidate programs.
- A program database implements the evolutionary selection loop.

## Reported applications

- Production data-center scheduling heuristic recovering roughly 0.7% of Google's worldwide compute resources.
- TPU hardware-design simplification.
- Gemini training kernel speedup and FlashAttention-related low-level GPU optimization.
- Discovery of a 4x4 complex matrix multiplication algorithm using 48 scalar multiplications.
- Progress on mathematical open problems, including the 11-dimensional kissing number lower bound.

## Harness relevance

AlphaEvolve is self-improving code in the algorithm-discovery sense: the evolving artifact is code that implements an algorithm, not necessarily the agent's own scaffold. The loop still has the same harness shape: generate code, run evaluator, select, store, and repeat.
