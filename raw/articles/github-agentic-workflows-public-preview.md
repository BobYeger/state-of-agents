![Actions run featuring an agentic workflow created by GitHub Agentic Workflows](https://github.blog/wp-content/uploads/2026/06/605360150-74ec2653-4565-4c79-b467-a9d296725e8f.jpg?w=2064)

[GitHub Agentic Workflows](https://github.github.com/gh-aw/) is now in public preview. With agentic workflows, you can automate reasoning-based tasks like issue triage, CI failure analysis, and documentation updates by leveraging coding agents inside GitHub Actions.

Define your automation in natural language Markdown files, and GitHub Agentic Workflows compiles them into standard Actions YAML. Because these are just actions, they reuse your existing runner groups and policy constraints.

> “With GitHub Agentic Workflows, we’re able to expand how we apply agents to real engineering work at scale, including changes that span multiple repositories. The flexibility and built-in controls give us confidence to leverage agentic workflows across complex systems at Carvana.”
>
> *– Alex Devkar, senior vice president, Engineering and Analytics at [Carvana](https://www.carvana.com/)*
>
> “Our developers were losing hours every sprint to repetitive work such as triaging issues, remediating vulnerabilities, maintaining dependencies, and reviewing routine changes. With GitHub Agentic Workflows, we’ve built a catalogue of reusable workflows spanning security, quality, and delivery that our teams can adopt across any repository. What once required hours of engineering effort can now be completed autonomously in minutes, meaning our teams can spend more time focused on innovation and delivering value to customers.”
>
> *– James Hoare, CTO, Engineering at [Marks & Spencer](https://www.marksandspencer.com/)*

### Security-first by design

GitHub Agentic Workflows incorporates layered safeguards to your automation. Agents access GitHub content respecting the [integrity filter](https://github.github.io/gh-aw/reference/integrity/) rules, run with read-only permissions by default, and execute inside a sandboxed container behind the [Agent Workflow Firewall](https://github.github.com/gh-aw/introduction/architecture/#agent-workflow-firewall-awf). The outputs are validated through the [safe outputs](https://github.github.com/gh-aw/reference/safe-outputs/) process, and a dedicated [threat detection](https://github.github.com/gh-aw/reference/threat-detection/) job scans all proposed changes before they are applied.

> “Getting an agent to open a pull request was never the hard part. Trusting it enough to merge is. GitHub Agentic Workflows put agents to work across the whole SDLC, automating the checks that make sure your code won’t degrade performance or break production. With agentic workflows, we can give our customers confidence that their ‘ready to merge’ PRs are actually safe to merge.”
>
> *– May Walter, CTO at [Hud.io](https://www.hud.io/)*

### Get started

Follow the [quickstart guide](https://gh.io/gh-aw-quickstart) to install the CLI extension and trigger your first workflow in minutes. Explore prebuilt workflows in GitHub Next’s [agentics repository](https://github.com/githubnext/agentics) for ready-to-use examples covering triage, reporting, compliance, and more.

Join the conversation and share your feedback in the [community discussion](https://gh.io/aw-tp-community-feedback).[Back to top](#start-of-content)