Title: Cursor Docs — Agent, Rules, MCP, Skills & CLI

URL Source: https://docs.cursor.com/en/background-agents

Markdown Content:
# Cursor Docs — Agent, Rules, MCP, Skills & CLI

[Skip to main content](https://docs.cursor.com/en/background-agents#main-content)

[](https://docs.cursor.com/docs)[Docs](https://docs.cursor.com/docs)[API](https://docs.cursor.com/docs/api)[Learn](https://docs.cursor.com/learn)[Help](https://docs.cursor.com/help)

Search docs...⌘K

Ask AI⌘I

[Sign in](https://cursor.com/dashboard)[Download](https://cursor.com/downloads)

## Command Palette

Search for a command to run...

## Get Started

[Welcome](https://docs.cursor.com/docs)[Quickstart](https://docs.cursor.com/docs/get-started/quickstart)

Models & Pricing

[Changelog](https://cursor.com/changelog)

## Agent

[Overview](https://docs.cursor.com/docs/agent/overview)[Agents Window](https://docs.cursor.com/docs/agent/agents-window)[Agent Review](https://docs.cursor.com/docs/agent/agent-review)[Planning](https://docs.cursor.com/docs/agent/plan-mode)[Prompting](https://docs.cursor.com/docs/agent/prompting)[Debugging](https://docs.cursor.com/docs/agent/debug-mode)

Tools

[Security](https://docs.cursor.com/docs/agent/security)

## Customizing

[Plugins](https://docs.cursor.com/docs/plugins)[Rules](https://docs.cursor.com/docs/rules)[Skills](https://docs.cursor.com/docs/skills)[Subagents](https://docs.cursor.com/docs/subagents)[Hooks](https://docs.cursor.com/docs/hooks)[MCP](https://docs.cursor.com/docs/mcp)

## Cloud Agents

[Overview](https://docs.cursor.com/docs/cloud-agent)[Setup](https://docs.cursor.com/docs/cloud-agent/setup)[Capabilities](https://docs.cursor.com/docs/cloud-agent/capabilities)[My Machines](https://docs.cursor.com/docs/cloud-agent/my-machines)[Self-Hosted Pool](https://docs.cursor.com/docs/cloud-agent/self-hosted-pool)[Google Cloud Run](https://docs.cursor.com/docs/cloud-agent/self-hosted-cloud-run)[Bugbot](https://docs.cursor.com/docs/bugbot)[Automations](https://docs.cursor.com/docs/cloud-agent/automations)[Best Practices](https://docs.cursor.com/docs/cloud-agent/best-practices)[Security Agents](https://docs.cursor.com/docs/security-agents)[Security & Network](https://docs.cursor.com/docs/cloud-agent/security-network)[Settings](https://docs.cursor.com/docs/cloud-agent/settings)[API](https://docs.cursor.com/docs/cloud-agent/api/endpoints)

## Integrations

[Slack](https://docs.cursor.com/docs/integrations/slack)[Microsoft Teams](https://docs.cursor.com/docs/integrations/microsoft-teams)[Linear](https://docs.cursor.com/docs/integrations/linear)[GitHub](https://docs.cursor.com/docs/integrations/github)[GitLab](https://docs.cursor.com/docs/integrations/gitlab)[JetBrains](https://docs.cursor.com/docs/integrations/jetbrains)[Xcode](https://docs.cursor.com/docs/integrations/xcode)[Deeplinks](https://docs.cursor.com/docs/reference/deeplinks)

## SDK

[Cursor SDK](https://docs.cursor.com/docs/sdk/typescript)

## CLI

[Overview](https://docs.cursor.com/docs/cli/overview)[Installation](https://docs.cursor.com/docs/cli/installation)[Capabilities](https://docs.cursor.com/docs/cli/using)[Shell Mode](https://docs.cursor.com/docs/cli/shell-mode)[ACP](https://docs.cursor.com/docs/cli/acp)[Headless / CI](https://docs.cursor.com/docs/cli/headless)

Reference

## Teams & Enterprise

Teams

Enterprise

Get Started

# Cursor Documentation

Cursor is an AI editor and coding agent. Use it to understand your codebase, plan and build features, fix bugs, review changes, and work with the tools you already use.

## [Start here](https://docs.cursor.com/en/background-agents#start-here)

[Get started Go from install to your first useful change in Cursor](https://docs.cursor.com/docs/get-started/quickstart)[Models & Pricing Compare models, usage pools, and plan pricing](https://docs.cursor.com/docs/models-and-pricing)[Changelog Stay up to date with the latest features and improvements](https://www.cursor.com/changelog)

## [What you can do with Cursor](https://docs.cursor.com/en/background-agents#what-you-can-do-with-cursor)

[Understand your code Trace how a repo fits together and find the right places to start](https://docs.cursor.com/learn/understanding-your-codebase)[Plan and build features Scope changes, use Plan Mode, and ship bigger work with confidence](https://docs.cursor.com/learn/creating-features)[Find and fix bugs Reproduce issues, narrow the root cause, and verify the fix](https://docs.cursor.com/learn/finding-fixing-bugs)[Review changes Inspect diffs, run checks, and catch problems before you merge](https://docs.cursor.com/learn/reviewing-testing)[Customize Cursor Use rules, skills, and prompts that match how your team works](https://docs.cursor.com/docs/rules)[Connect your workflow Work with GitHub, GitLab, JetBrains, Slack, Linear, and more](https://docs.cursor.com/docs/integrations/github)

## [Models](https://docs.cursor.com/en/background-agents#models)

See all model attributes on the [Models & Pricing](https://docs.cursor.com/docs/models-and-pricing) page.

| Name | Default Context | Max Mode | Capabilities |
| --- | --- | --- | --- |
| ![Image 3: Anthropic](https://docs.cursor.com/docs-static/images/providers/anthropic-dark.svg)![Image 4: Anthropic](https://docs.cursor.com/docs-static/images/providers/anthropic-light.svg) [Claude 4.6 Sonnet](https://docs.cursor.com/docs/models/claude-4-6-sonnet) | 200k | 1M |  |
| ![Image 5: Anthropic](https://docs.cursor.com/docs-static/images/providers/anthropic-dark.svg)![Image 6: Anthropic](https://docs.cursor.com/docs-static/images/providers/anthropic-light.svg) [Claude 4.7 Opus](https://docs.cursor.com/docs/models/claude-opus-4-7) | 200k | 1M |  |
| ![Image 7: Cursor](https://docs.cursor.com/docs-static/images/providers/cursor.svg) [Composer 2](https://docs.cursor.com/docs/models/cursor-composer-2) | 200k | - |  |
| ![Image 8: Google](https://docs.cursor.com/docs-static/images/providers/google.svg) [Gemini 3.1 Pro](https://docs.cursor.com/docs/models/gemini-3-1-pro) | 200k | 1M |  |
| ![Image 9: OpenAI](https://docs.cursor.com/docs-static/images/providers/openai-dark.svg)![Image 10: OpenAI](https://docs.cursor.com/docs-static/images/providers/openai-light.svg) [GPT-5.3 Codex](https://docs.cursor.com/docs/models/gpt-5-3-codex) | 272k | - |  |
| ![Image 11: OpenAI](https://docs.cursor.com/docs-static/images/providers/openai-dark.svg)![Image 12: OpenAI](https://docs.cursor.com/docs-static/images/providers/openai-light.svg) [GPT-5.5](https://docs.cursor.com/docs/models/gpt-5-5) | 272k | 1M |  |
| ![Image 13: xAI](https://docs.cursor.com/docs-static/images/providers/xai-dark.svg)![Image 14: xAI](https://docs.cursor.com/docs-static/images/providers/xai-light.svg) [Grok 4.3](https://docs.cursor.com/docs/models/grok-4-3) | 200k | 1M |  |

Show more models

## [More resources](https://docs.cursor.com/en/background-agents#more-resources)

[Downloads Get Cursor for your computer](https://cursor.com/downloads)[Help Find answers to common questions and troubleshooting guides](https://docs.cursor.com/help)

Support

For account and billing questions, contact our support team

English

*   English
*   简体中文
*   日本語
*   繁體中文
*   Español
*   Français
*   Português
*   한국어
*   Русский
*   Türkçe
*   Bahasa Indonesia
*   Deutsch
*   हिन्दी

*   [Start here](https://docs.cursor.com/en/background-agents#start-here)
*   [What you can do with Cursor](https://docs.cursor.com/en/background-agents#what-you-can-do-with-cursor)
*   [Models](https://docs.cursor.com/en/background-agents#models)
*   [More resources](https://docs.cursor.com/en/background-agents#more-resources)

Copy page

Share feedback

Explain more

Agent

Tokenizer Off Context: 0/200k (0%)

Open chat
