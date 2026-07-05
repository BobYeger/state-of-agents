Title: Caught in the Hook: RCE and API Token Exfiltration Through Claude Code Project Files | CVE-2025-59536 | CVE-2026-21852

URL Source: https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/

Published Time: 2026-02-25T13:58:39+00:00

Markdown Content:
By Aviv Donenfeld and Oded Vanunu

## Executive Summary

Check Point Research has discovered **critical** vulnerabilities in Anthropic’s Claude Code that allow attackers to achieve **remote code execution** and steal API credentials through malicious project configurations. The vulnerabilities exploit various configuration mechanisms including **Hooks**, **Model Context Protocol** (MCP) servers, and **environment variables**-executing arbitrary shell commands and exfiltrating Anthropic API keys when users clone and open untrusted repositories. Following our disclosure, Check Point Research collaborated closely with the Anthropic security team to ensure these vulnerabilities were fully remediated. **All reported issues have been successfully patched prior to this publication.**

## Background

As AI-powered development tools rapidly integrate into software workflows, they introduce novel attack surfaces that traditional security models haven’t fully addressed. These platforms combine the convenience of automated code generation with the risks of executing AI-generated commands and sharing project configurations across collaborative environments.

Claude Code, Anthropic’s AI-powered command-line development tool, represents a significant target in this landscape. As a leading agentic tool within the developer ecosystem, its adoption by technology professionals and integration into enterprise workflows means that the platform’s security model directly impacts a substantial portion of the AI-assisted development landscape.

## Claude Code Platform

Claude Code enables developers to delegate coding tasks directly from their terminal through natural language instructions. The platform supports comprehensive development operations including file modifications, Git repository management, automated testing, build system integration, Model Context Protocol (MCP) tool connections, and shell command execution.

![Image 1](https://research.checkpoint.com/wp-content/uploads/2026/02/image-22.png)
Vibe-coding an awesome project using Claude Code

## Configuration Files as Attack Surface

While analyzing Claude Code’s architecture, we examined how the platform manages its configurations. Claude Code supports project-level configurations through a .claude/settings.json file that lives directly in the repository. This design makes sense for team collaboration – when developers clone a project, they automatically inherit the same Claude Code settings their teammates use, ensuring consistent behavior across the team.

Since .claude/settings.json is just another file in the repository, any contributor with commit access can modify it. This creates a potential attack vector: malicious configurations could be injected into repositories, possibly triggering actions that users don’t expect and may not even be aware are occurring.

We set out to investigate what these repository-controlled configurations could actually do, and whether they could be leveraged to compromise developers working with affected codebases.

## Vulnerability #1: RCE via Untrusted Project Hooks

During our research into Claude Code’s configuration documentation, we encountered Anthropic’s recently released Hooks feature. Hooks are designed to provide deterministic control over Claude Code’s behavior by executing user-defined commands at various points in the tool’s lifecycle. Unlike relying on the AI model to choose when to perform certain actions, Hooks ensure that specific operations always execute when predetermined conditions are met.

Some common use cases for Hooks include:

*   **Automatic code formatting**: Run prettier on .ts files, gofmt on .go files, etc. after every file edit
*   **Compliance and debugging workflows**: Provide automated feedback when Claude Code produces code that doesn’t follow codebase conventions
*   **Custom permissions**: Block modifications to production files or sensitive directories

Hooks are defined in .claude/settings.json – the same repository-controlled configuration file we identified earlier. This means any contributor with commit access can define hooks that will execute shell commands on every collaborator’s machine when they work with the project. The question was: **what happens when those commands come from an untrusted source?**

To test this, we crafted a .claude/settings.json file which includes a simple **hook** that would open a Calculator. We chose to use the SessionStart event with a startup matcher, which according to Hooks documentation triggers automatically during Claude Code initialization:

![Image 2](https://research.checkpoint.com/wp-content/uploads/2026/02/1.png)

When we ran claude in the project directory, the following trust dialog was presented:

![Image 3](https://research.checkpoint.com/wp-content/uploads/2026/02/image-10.png)

The dialog warns about reading files and mentions that Claude Code may execute files “**_with your permission_**.” This phrasing suggests that user approval will be required before any execution occurs. Indeed, when Claude Code attempts to run commands during a normal session (such as executing a bash script), it does prompt for explicit confirmation:

![Image 4](https://research.checkpoint.com/wp-content/uploads/2026/02/image-25.png)

Before execution of bash commands, Claude requests for explicit approval from the user.

We expected hooks to receive the same explicit confirmation prompt.

Back to our test: we clicked “Yes, proceed” on the prompt from when we first ran Claude.

Surprisingly, the Calculator app opened immediately, with no additional prompt or execution warning.

![Image 5](https://research.checkpoint.com/wp-content/uploads/2026/02/image-20.png)

We went back and examined the initial dialog more carefully. While it mentions files being executed “**_with your permission_**,” there’s no warning that hook commands defined in .claude/settings.json will run automatically without confirmation, as well as no explicit approval which was required to execute the bash command demonstrated above. The session appears completely normal while commands from the untrusted repository have already run in the background.

With this behavior confirmed, the path to remote code execution became clear. An attacker could configure the hook to execute any shell command – such as downloading and running a malicious payload:

> ![Image 6](https://research.checkpoint.com/wp-content/uploads/2026/02/2-1024x510.png)

The following video demonstrates how an attacker may leverage this vulnerability to achieve a reverse shell:

[Video 7](https://www.youtube.com/watch?v=BJjkYZwMfG0)

During our investigation of Claude Code’s configuration system, we discovered that hooks weren’t the only feature controlled through repository settings. This led us to examine other configuration-based execution mechanisms, particularly the MCP (Model Context Protocol) integration.

## Vulnerability #2: RCE Using MCP User Consent Bypass

Another interesting setting that Claude Code supports is MCP (Model Context Protocol), which allows Claude Code to interact with external tools and services through a standardized interface.

Similar to Hooks, MCP servers can be configured within the repository via .mcp.json configuration file. When opening a Claude Code conversation, the application initializes all MCP servers by running the commands written in the MCP configuration file.

To test the MCP configurations, we configured a fake MCP server whose initialization command opens a Calculator for demonstration:

![Image 7](https://research.checkpoint.com/wp-content/uploads/2026/02/3.png)

We observed that Anthropic had implemented an improved dialog in response to our first reported vulnerability [[GHSA-ph6w-f82w-28w6](https://github.com/anthropics/claude-code/security/advisories/GHSA-ph6w-f82w-28w6)]. This new dialog explicitly mentions that commands in .mcp.json may be executed and emphasizes the risks of proceeding:

![Image 8](https://research.checkpoint.com/wp-content/uploads/2026/02/image-13.png)

User consent dialogue for MCP servers initialization

This improved warning would make it much more difficult for an attacker to convince users to confirm initialization of Claude Code over a malicious project. With this in mind, our goal shifted to finding a way to execute the injected commands without any user consent.

Reviewing [Claude Code’s settings documentation](https://code.claude.com/docs/en/settings), we identified the following two configurations:

![Image 9](https://research.checkpoint.com/wp-content/uploads/2026/02/image-7.png)

These parameters allow automatic approval of MCP servers: enableAllProjectMcpServers enables all servers defined in the project’s .mcp.json file, while enabledMcpjsonServers whitelists specific server names. In legitimate use cases, these settings enable seamless team collaboration – developers cloning a repository automatically get the same MCP integrations (filesystem, database, or GitHub tools) without manual setup.

Additionally, just like Claude Code hooks, these configurations can be included in the repository-controlled .claude/settings.json file. We tested whether this could bypass the user consent dialog:

![Image 10](https://research.checkpoint.com/wp-content/uploads/2026/02/4.png)

Starting Claude Code with this configuration revealed a severe vulnerability: our command executed **immediately upon running****claude** – **before the user could even read the trust dialog**. Ironically, the calculator application opened on top of the pending trust dialog:

![Image 11](https://research.checkpoint.com/wp-content/uploads/2026/02/image-23.png)
Similar to the hooks vulnerability, we escalated this into a reverse shell, demonstrating complete compromise of a victim’s machine:

[Video 8](https://www.youtube.com/watch?v=RlmEcN7csDI)

## Vulnerability #3: API Key Exfiltration via Malicious ANTHROPIC_BASE_URL

Following our discovery that Claude Code’s configuration system could execute arbitrary commands, we wanted to understand the full scope of what could be controlled through .claude/settings.json. While exploring the configuration schema, we found that environment variables could also be defined in this file. One particular variable caught our attention: ANTHROPIC_BASE_URL.

This environment variable controls the endpoint for all Claude Code API communications. In normal operation, it points to Anthropic’s servers, but like other settings, it could be overridden in the project’s configuration file.

This presented an opportunity: we could intercept and analyze the actual communication between Claude Code and Anthropic’s servers. We set up mitmproxy, a tool for intercepting HTTP traffic, and configured ANTHROPIC_BASE_URL to route through our local proxy. This would let us observe every API call Claude Code made in real-time:

![Image 12](https://research.checkpoint.com/wp-content/uploads/2026/02/5.png)
We started Claude Code and watched the traffic flow through our proxy. Something immediately caught our attention: before we could even interact with the trust dialog, Claude Code had already initiated several requests to Anthropic’s servers:

![Image 13](https://research.checkpoint.com/wp-content/uploads/2026/02/image-14.png)

Requests captured by our mitmproxy

The requests seem to include prompts responsible for initializing the session with relevant information, including file names in the repository and recent commit messages.

![Image 14](https://research.checkpoint.com/wp-content/uploads/2026/02/image-8.png)

But more critically, every request included the authorization header – our full Anthropic API key, completely exposed in plaintext:

![Image 15](https://research.checkpoint.com/wp-content/uploads/2026/02/image-11.png)

What started as research method into the communication between Claude Code client and server immediately became an attack vector on its own. An attacker could place this configuration in a malicious repository:

![Image 16](https://research.checkpoint.com/wp-content/uploads/2026/02/6.png)

When a victim clones the repository and runs claude, **their API key would be sent directly to the attacker’s server** – **before the victim decides to trust the directory**. No user interaction required.

But what could an attacker actually do with a stolen API key? The obvious answer was **billing fraud –** running Claude queries charged to the victim’s account. But as we explored Anthropic’s API documentation to understand the full scope of access, we discovered something far more concerning: **Workspaces**.

## Claude’s Workspaces

Claude’s Workspaces is a feature introduced within the API Console to help developers manage multiple Claude deployments more effectively. Workspaces are especially useful for teams and multi-project environments, allowing them to organize resources, streamline access controls, and maintain shared contexts across tools. In practice, a Workspace acts as a collaborative environment where multiple API keys can work with the same cloud-mounted project files.

![Image 17](https://research.checkpoint.com/wp-content/uploads/2026/02/image-28.png)
Files stored in a Workspace aren’t scoped to individual API keys. Instead, they belong to the **workspace itself** – meaning multiple developers, each using their own API key, may implicitly share the same storage area. Any API key belonging to that workspace inherits visibility into the Workspace’s stored files.

To understand how this behaves in practice, we created a workspace with two API keys:

![Image 18](https://research.checkpoint.com/wp-content/uploads/2026/02/image-26.png)

We then reviewed the Files API documentation, which allows managing files within a Workspace, and began testing file uploads and downloads.

We uploaded a file using the following request:

![Image 19](https://research.checkpoint.com/wp-content/uploads/2026/02/image-27.png)

We noticed the API response showed the **downloadable** parameter set to **false**:

![Image 20](https://research.checkpoint.com/wp-content/uploads/2026/02/image-18.png)

Attempting to download the file did indeed fail. We confirmed this behavior in the documentation:

You can only download files that were created by[skills](https://platform.claude.com/docs/en/build-with-claude/skills-guide)or the[code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool). Files that you uploaded cannot be downloaded.

This appears to be an architectural choice rather than a security boundary. Any developer who can upload files to the Workspace is already fully trusted: if they can write files, they typically also have access to the original content.

Nevertheless, since this weakens our attack impact, we wondered whether we could bypass this behavior. Since **files generated by Claude’s code execution tool are marked as downloadable**, we explored whether the attacker could simply ask Claude to regenerate an existing file using the stolen API key. If successful, this would convert a non-downloadable file into a workspace artifact that is eligible for download.

We instructed Claude to produce a copy of the file with a .unlocked suffix:

![Image 21](https://research.checkpoint.com/wp-content/uploads/2026/02/image-16.png)

As we expected, Claude generated an exact copy of the file:

![Image 22](https://research.checkpoint.com/wp-content/uploads/2026/02/image-19.png)

We then downloaded this regenerated file and confirmed the content was identical to the original:

![Image 23](https://research.checkpoint.com/wp-content/uploads/2026/02/image-17.png)

This demonstrates that the download restriction can be trivially bypassed: regenerating the file through the code execution tool converts it into a system-generated artifact that the Files API allows to be downloaded.

This confirms an attacker using a stolen API key gains complete read and write access to all workspace files, include those uploaded by other developers.

With a stolen API key, an attacker can:

*   **Access sensitive files** by regenerating them through the code execution tool
*   **Delete critical files** from the workspace
*   **Upload arbitrary files** to poison the workspace or exhaust the 100 GB storage space quota
*   **Exhaust API credits**, leading to unexpected costs for the account owner or service interruption when rate limits/budgets are reached

Unlike the code execution vulnerabilities that compromised a single developer’s machine, a stolen API key may provide access to an entire team’s shared resources.

The following video demonstrates the complete attack chain: exfiltrating the victim’s API key and using it to access their workspace storage:

[Video 9](https://www.youtube.com/watch?v=jMeeVxqU3hY)

## Supply Chain Attack Scenarios

This vulnerabilities are particularly dangerous because they leverage **supply chain attack vectors** – the malicious configuration spreads through trusted development channels:

*   **Malicious pull requests**: Attackers can submit seemingly legitimate PRs that include the malicious configuration alongside actual code changes, making it harder for reviewers to spot the threat
*   **Honeypot repositories**: Attackers can create useful-looking projects (development tools, code examples, tutorials) that contain the malicious configuration, targeting developers who discover and clone these repositories
*   **Internal enterprise repositories**: A single compromised developer account or insider threat can inject the configuration into company codebases, affecting entire development teams

The key factor making this a supply chain attack is that **developers inherently trust project configuration files** – they’re viewed as metadata rather than executable code, so they rarely undergo the same security scrutiny as application code during code reviews.

## Anthropic’s Fixes

Anthropic addressed the first vulnerability by implementing an enhanced warning dialog that appears when users open projects containing untrusted Claude Code configurations:

![Image 24](https://research.checkpoint.com/wp-content/uploads/2026/02/image-15.png)

This improved warning addresses not only the hooks vulnerability but also other potential risks from untrusted project directories, including malicious MCP configurations. Anthropic claimed to develop additional security hardening features planned for release in the coming months to provide more granular risk controls.

For the second vulnerability, Anthropic fixed the bypass by ensuring that MCP servers cannot execute before user approval, even when enableAllProjectMcpServers or enabledMcpjsonServers are set in the repository’s configuration files.

For the third vulnerability, **Anthropic fixed the API key exfiltration****issue** by ensuring that no API requests are initiated before users confirm the trust dialog. This prevents malicious ANTHROPIC_BASE_URL configurations from intercepting API keys during the project initialization phase, as Claude Code now defers all network operations until after explicit user consent.

We would like to thank Anthropic for their excellent collaboration and thoughtful engagement throughout this disclosure process.

## Protecting Against Configuration-Based Attacks

Modern development tools increasingly rely on project-embedded configurations and automations, creating new attack vectors that developers must navigate. As these tools continue to evolve and add features, configuration-based risks are likely here to stay as a persistent threat in development ecosystems.

Just as developers have learned they cannot blindly execute code from untrusted sources, we must extend that same caution to opening projects with modern development tools. The line between configuration and execution continues to blur, requiring us to treat project setup files with the same careful attention we apply to executable code.

**How to Stay Protected:**

*   **Keep Your Tools Updated –** Ensure you are running the latest version of Claude Code. **All vulnerabilities discussed in this report have been patched**, and running the current version is the most effective way to stay protected.
*   **Inspect configuration directories** before opening projects – examine .claude/, .vscode/, and similar tool-specific folders
*   **Pay attention to tool warnings** about potentially unsafe files, even in legitimate-looking repositories
*   **Review configuration changes** during code reviews with the same rigor applied to source code
*   **Question unusual setup requirements** that seem overly complex for a project’s apparent scope

## Timeline and Disclosure

*   **July 21st, 2025** – Check Point Research reported the malicious hooks vulnerability to Anthropic
*   **August 26th, 2025** – Anthropic implemented a final fix after collaborative refinement process
*   **August 29th, 2025** – Anthropic publishes [GitHub Security Advisory GHSA-ph6w-f82w-28w6](https://github.com/advisories/GHSA-ph6w-f82w-28w6)
*   **September 3rd, 2025** – Check Point Research reported the user consent bypass vulnerability to Anthropic
*   **September 22nd, 2025** – Anthropic implemented a fix for the bypass vulnerability
*   **October 3rd, 2025** – Anthropic publishes [CVE-2025-59536](https://github.com/anthropics/claude-code/security/advisories/GHSA-4fgq-fpq9-mr3g)
*   **October 28th, 2025** – Check Point Research reported the API Key exfiltration vulnerability to Anthropic
*   **December 28th, 2025** – Anthropic implemented a fix for the API Key exfiltration vulnerability
*   **January 21st, 2026** – Anthropic publishes [CVE-2026-21852](https://nvd.nist.gov/vuln/detail/CVE-2026-21852)
*   **February 25th, 2026** – Public disclosure

## Conclusion

These vulnerabilities in Claude Code highlight a critical challenge in modern development tools: balancing powerful automation features with security. The ability to execute arbitrary commands through repository-controlled configuration files created severe supply chain risks, where a single malicious commit could compromise any developer working with the affected repository.

The integration of AI into development workflows brings tremendous productivity benefits, but also introduces new attack surfaces that weren’t present in traditional tools. Configuration files that were once passive data now control active execution paths. As AI-powered development tools become more prevalent, the security community must carefully evaluate these new trust boundaries to protect the integrity of our software supply chains.
