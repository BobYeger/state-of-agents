# Observation Masking

Observation masking hides older environment observations from an agent while preserving the structure of the trajectory.

It is especially relevant for software-engineering agents because old command outputs, file reads, and test logs can dominate context while often remaining re-fetchable. The key tradeoff is that masking can be cheap and effective, but the window size and masking policy depend on the agent scaffold and task.

## Related

- [[concepts/context compaction]]
- [[concepts/tool-result clearing]]
- [[operations/cost control]]
- [[operations/agent harnesses]]
- [[maps/Context Management Map]]

## Related Sources

- [[sources/The Complexity Trap]]
- [[sources/JetBrains Cutting Through the Noise]]
