# SkillOpt project page

Source URL: https://microsoft.github.io/SkillOpt/

Capture date: 2026-06-16

Capture note: readable local markdown snapshot generated from the public Microsoft Research project page with Defuddle. The extraction starts at the first content section; source metadata and title are added here.

## SkillOpt in motion.

A short visual overview of how SkillOpt treats natural-language skills as trainable artifacts: roll out, reflect, edit, validate, and export.

![](https://www.youtube.com/watch?v=JUBMDTCiM0M)

Promotional video for the SkillOpt project page. The static paper teaser is shown below for high-resolution inspection.

Paper Teaser

## The core loop at a glance.

The teaser summarizes the SkillOpt training loop: rollout evidence, optimizer-side reflection, bounded skill edits, validation gating, and the exported reusable skill.

![SkillOpt teaser figure showing the target model, optimizer model, bounded edits, validation gate, and exported best skill.](https://microsoft.github.io/SkillOpt/skillopt-assets/teaser-1.png)

SkillOpt teaser figure showing the target model, optimizer model, bounded edits, validation gate, and exported best skill.

Figure from the SkillOpt paper. On small screens, the figure area scrolls horizontally to preserve the original details.

## Train the procedure, not the weights.

SkillOpt makes the skill document itself the optimization target. The target model, backend, and harness stay fixed; the procedure that guides evidence gathering, tool use, verification, and output formatting evolves.

### A skill is external state for an agent.

Instead of fine-tuning a model or hand-maintaining prompts, SkillOpt runs the frozen agent on scored batches, asks a separate optimizer model to propose structured edits, and accepts a candidate only when validation performance improves.

Frozen target model Optimizer model Add / delete / replace edits Held-out gate

**Rollout**

The target model executes tasks with the current skill and records scored trajectories.

**Reflect**

The optimizer analyzes success and failure minibatches to find reusable procedures.

**Edit**

Candidate add, delete, and replace operations are merged and ranked under a budget.

**Gate**

The candidate skill is kept only if it improves held-out selection performance.

## A training loop for natural-language skills.

The loop deliberately mirrors a learning algorithm: rollout evidence acts like a forward pass, reflection acts like a language-level backward pass, and the textual learning rate bounds how far the skill can move.

### Evidence

Rollout batches capture messages, tool calls, verifier feedback, task metadata, and final scores.

### Minibatches

Failures and successes are reflected separately so edits correct recurring errors while preserving working behavior.

### Bounded Edits

An edit budget functions as a textual learning rate, preventing useful rules from being overwritten by broad rewrites.

### Memory

Rejected edits, slow update, and optimizer-side meta skill provide longer-horizon feedback without bloating deployment.

![SkillOpt pipeline showing rollout, reflection, bounded edits, validation gate, slow update, and meta skill.](https://microsoft.github.io/SkillOpt/skillopt-assets/pipeline-1.png)

SkillOpt pipeline from the paper. The frozen target model executes with the current skill; the optimizer model proposes bounded edits; held-out validation decides whether the candidate becomes the new current skill.

## SkillOpt improves GPT and Qwen target models.

The table reports main-result gains across target models and execution harnesses, comparing no-skill execution with the final SkillOpt skill on held-out test splits.

| Target model | Harness | SearchQA | Sheet | Office | DocVQA | LiveMath | ALFWorld | Avg gain |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![OpenAI logo](https://microsoft.github.io/SkillOpt/skillopt-assets/openai.png)  OpenAI logo | Direct chat | +9.6 | +38.9 | +39.0 | +12.4 | +29.3 | +11.9 | +23.5 |
| ![OpenAI logo](https://microsoft.github.io/SkillOpt/skillopt-assets/openai.png)  OpenAI logo | Direct chat | +6.2 | +21.1 | +12.8 | +13.6 | +7.2 | +15.6 | +12.8 |
| ![OpenAI logo](https://microsoft.github.io/SkillOpt/skillopt-assets/openai.png)  OpenAI logo | Direct chat | +4.3 | +11.4 | +26.7 | +16.5 | +4.8 | +12.7 | +12.7 |
| ![OpenAI logo](https://microsoft.github.io/SkillOpt/skillopt-assets/openai.png)  OpenAI logo | Direct chat | +19.0 | +8.2 | +33.7 | +49.4 | +4.0 | +35.1 | +24.9 |
| ![OpenAI logo](https://microsoft.github.io/SkillOpt/skillopt-assets/openai.png)  OpenAI logo | Direct chat | +11.2 | +18.9 | +21.5 | +16.5 | +15.2 | +16.4 | +16.6 |
| ![Qwen logo](https://microsoft.github.io/SkillOpt/skillopt-assets/qwen-color.png) | Direct chat | +3.1 | +14.6 | +15.2 | +2.1 | +29.6 | +50.7 | +19.2 |
| ![Qwen logo](https://microsoft.github.io/SkillOpt/skillopt-assets/qwen-color.png) | Direct chat | +7.6 | +9.3 | +1.2 | +3.8 | +10.4 | +22.4 | +9.1 |
| ![OpenAI logo](https://microsoft.github.io/SkillOpt/skillopt-assets/openai.png)  OpenAI logo | Codex | +5.5 | +57.5 | +12.8 | +5.0 | +28.0 | N/A | +21.8 |
| ![OpenAI logo](https://microsoft.github.io/SkillOpt/skillopt-assets/openai.png)  OpenAI logo | Claude Code | +4.0 | +58.3 | +13.9 | +3.5 | +13.3 | N/A | +18.6 |

Method comparison

### SkillOpt clears the strongest baseline on every benchmark.

## The controls are doing real work.

The paper isolates the optimizer components that keep skill learning stable: enough evidence, bounded textual updates, rejected-edit feedback, slow update, and optimizer-side memory.

| Component | Setting | SearchQA | Spreadsheet | LiveMath |
| --- | --- | --- | --- | --- |
| Learning rate | lr=4 default | **87.1** | **77.5** | **61.3** |
| Learning rate | without lr | 84.6 | 75.7 | 57.3 |
| Rejected buffer | with buffer | **87.1** | **77.5** | **61.3** |
| Rejected buffer | without buffer | 85.5 | 72.9 | 58.9 |
| Update memory | meta skill + slow update | **87.1** | **77.5** | **61.3** |
| Update memory | without both | 86.3 | 55.0 | 59.7 |

### What the ablations say

**Bounded** Textual learning rates prevent destructive rewrites while keeping enough plasticity to learn new procedures.

**Gated** Held-out selection turns reflection into propose-and-test optimization rather than unconditional self-editing.

**Buffered** Rejected edits become negative feedback, helping the optimizer avoid repeating harmful directions.

![Epoch checkpoint trends for SpreadsheetBench, SearchQA, and LiveMath.](https://microsoft.github.io/SkillOpt/skillopt-assets/epoch-trends-1.png)

Epoch checkpoint trends from the paper. Selection-best checkpoints are compared with train rollout score and unseen test performance.

## A typical run turns failures into concrete operating rules.

This ALFWorld run uses GPT-5.4-mini as the frozen target model and GPT-5.5 as the optimizer model. The plot tracks train rollout and held-out selection scores; hover or focus a point to inspect the skill edit proposed at that stage.

ALFWorld / train-sel evolution

Train rollout Selection gate

<svg viewBox="0 0 790 340" role="img" aria-labelledby="evolution-chart-title evolution-chart-desc"><title id="evolution-chart-title">ALFWorld skill evolution scores</title> <desc id="evolution-chart-desc">Selection score rises from 68.6 percent to 81.4 percent, while rejected edits are visible as downward candidate points.</desc> <line stroke-opacity="0.2" stroke="currentColor" x1="70" y1="60" x2="730" y2="60"></line><line stroke-opacity="0.2" stroke="currentColor" x1="70" y1="115" x2="730" y2="115"></line><line stroke-opacity="0.2" stroke="currentColor" x1="70" y1="170" x2="730" y2="170"></line><line stroke-opacity="0.2" stroke="currentColor" x1="70" y1="225" x2="730" y2="225"></line><line stroke-opacity="0.2" stroke="currentColor" x1="70" y1="280" x2="730" y2="280"></line><line stroke-opacity="0.2" stroke="currentColor" x1="70" y1="280" x2="730" y2="280"></line><line stroke-opacity="0.2" stroke="currentColor" x1="70" y1="60" x2="70" y2="280"></line><text fill="currentColor" x="25" y="64">85%</text> <text fill="currentColor" x="25" y="119">80%</text> <text fill="currentColor" x="25" y="174">75%</text> <text fill="currentColor" x="25" y="229">70%</text> <text fill="currentColor" x="25" y="284">65%</text> <text fill="currentColor" x="50" y="318">base</text> <text fill="currentColor" x="181" y="318">step 1</text> <text fill="currentColor" x="311" y="318">step 2</text> <text fill="currentColor" x="441" y="318">step 3</text> <text fill="currentColor" x="563" y="318">slow</text> <text fill="currentColor" x="701" y="318">step 4</text><polyline stroke-opacity="0.2" stroke="currentColor" points="70,240.7 200,201.4 330,162.1 460,232.9 590,99.3 720,146.4"></polyline><polyline stroke-opacity="0.2" stroke="currentColor" points="200,238.8 330,156.3 460,142.5 590,115 720,87.5"></polyline><g data-index="0" data-state="baseline" tabindex="0" role="button" aria-label="Baseline selection score 68.6 percent"><circle stroke="currentColor" fill="none" cx="70" cy="240.7" r="12"></circle><circle cx="70" cy="240.7" r="5"></circle></g><g data-index="1" data-state="accepted" tabindex="0" role="button" aria-label="Step 1 accepted, selection score 72.1 percent"><circle stroke="currentColor" fill="none" cx="200" cy="201.4" r="12"></circle><circle cx="200" cy="201.4" r="5"></circle><circle cx="200" cy="238.8" r="4"></circle></g><g data-index="2" data-state="accepted" tabindex="0" role="button" aria-label="Step 2 accepted, selection score 75.7 percent"><circle stroke="currentColor" fill="none" cx="330" cy="162.1" r="12"></circle><circle cx="330" cy="162.1" r="5"></circle><circle cx="330" cy="156.3" r="4"></circle></g><g data-index="3" data-state="rejected" tabindex="0" role="button" aria-label="Step 3 rejected, candidate selection score 69.3 percent"><circle stroke="currentColor" fill="none" cx="460" cy="232.9" r="12"></circle><circle cx="460" cy="232.9" r="5"></circle><circle cx="460" cy="142.5" r="4"></circle></g><g data-index="4" data-state="slow" tabindex="0" role="button" aria-label="Slow update accepted, selection score 81.4 percent"><circle stroke="currentColor" fill="none" cx="590" cy="99.3" r="12"></circle><circle cx="590" cy="99.3" r="5"></circle><circle cx="590" cy="115" r="4"></circle></g><g data-index="5" data-state="rejected" tabindex="0" role="button" aria-label="Step 4 rejected, candidate selection score 77.1 percent"><circle stroke="currentColor" fill="none" cx="720" cy="146.4" r="12"></circle><circle cx="720" cy="146.4" r="5"></circle><circle cx="720" cy="87.5" r="4"></circle></g></svg>

Accepted edits become the current skill only after held-out selection improves. Step 3 is rescued by a slow update; Step 4 trains higher but fails selection.

**Run setup** Target model: GPT-5.4-mini. Optimizer model: GPT-5.5. The skill starts from a compact ALFWorld instruction file and is edited in text space.

**Selection rule** Candidate edits are accepted only when held-out selection improves the current best score.

**Outcome** The selected skill improves final ALFWorld test hard score from 70.9% to 85.8%.

## The exported skill behaves like a reusable artifact.

SkillOpt exports a compact `best_skill.md`. The paper tests whether that artifact transfers across model sizes, execution harnesses, and nearby benchmarks without further target-side optimization.

Cross-model +15.2

GPT-5.4 LiveMath skill transferred to GPT-5.4-nano on LiveMathBench.

Cross-harness +31.8

Codex-trained SpreadsheetBench skill transferred into Claude Code.

Self-optimizer +10.4

GPT-5.4-nano used as its own optimizer improved SpreadsheetBench over baseline.

Deployment 1 file

The target model consumes only the final skill, not optimizer memory.

A stronger optimizer model gives the largest gains, but the loop is not merely distillation from a stronger model. Even matched target-as-optimizer settings can discover useful edits when the update is constrained, buffered, and validated.

## Citation.

If you find SkillOpt useful, please cite the arXiv preprint below.

```
@misc{yang2026skilloptexecutivestrategyselfevolving,
      title={SkillOpt: Executive Strategy for Self-Evolving Agent Skills},
      author={Yifan Yang and Ziyang Gong and Weiquan Huang and Qihao Yang and Ziwei Zhou and Zisu Huang and Yan Li and Xuemei Gao and Qi Dai and Bei Liu and Kai Qiu and Yuqing Yang and Dongdong Chen and Xue Yang and Chong Luo},
      year={2026},
      eprint={2605.23904},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2605.23904},
}
```
