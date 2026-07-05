Title: An important update: Transitioning Gemini CLI to Antigravity CLI

URL Source: https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/

Published Time: 2026-05-19

Markdown Content:
MAY 19, 2026

When we shipped Gemini CLI last year, our goal was to bring the magic of Gemini directly into your terminal. Along the way, we’ve learned a lot from our community of millions of users, with over 100,000 GitHub stars, 6,000 merged pull requests, and hundreds of contributors, including: you love a good terminal UI, you appreciate that we ship weekly releases, and your workflows have simply outgrown those early days of 2025.

Gemini CLI proved the terminal could be an incredible interface for agentic tasks, but your needs shifted. You now require multiple agents communicating with each other to split up the work and solve complex problems. This means your terminal tools need to share a unified backend with the rest of your workflow.

Listening to your feedback made one thing clear: we can serve you best by pouring our energy into a single product built for today's multi-agent reality. To deliver the single platform you need to build the future, we're unifying our efforts into [Google Antigravity](http://antigravity.google/blog/introducing-google-antigravity-2-0), our premier agent-first development platform, which includes a powerful server-side harness and a brand-new terminal experience: [Antigravity CLI](http://antigravity.google/blog/introducing-google-antigravity-cli).

While there won't be 1:1 feature parity right out of the gate, we made sure Antigravity CLI keeps the most critical features of Gemini CLI: Agent Skills, Hooks, Subagents, and Extensions (now as Antigravity plugins). Whether you use Gemini CLI to get quick, grounded answers, scaffold and build out a new coding project, or help provision your cloud infrastructure, you can still do all of that right in Antigravity CLI. And to make your experience better, we focused on the things that matter most to you, like:

*   Faster execution: Built in Go, Antigravity CLI is snappier and more responsive.
*   Asynchronous workflows: Antigravity CLI orchestrates multiple agents for complex tasks in the background, letting you run large-scale refactors or research several topics without locking up your terminal session.
*   Unified architecture: Antigravity CLI shares the same agent harness as [Antigravity 2.0](https://antigravity.google/blog/introducing-google-antigravity-2-0), the new Antigravity desktop application, ensuring that all future improvements to core agents are automatically applied wherever you use them.

### **Important timeline for Consumers**

Starting today, [Antigravity CLI](https://antigravity.google/download) is available to everyone.

On June 18, 2026, Gemini CLI and Gemini Code Assist IDE extensions will stop serving requests for Google AI Pro and Ultra, as well as those using it free of charge using [Gemini Code Assist for individuals](https://developers.google.com/gemini-code-assist/docs/overview#supported-features-gca).

We are here to help make the transition to Antigravity CLI and Antigravity 2.0 as smooth as possible. You can get started now with our [technical documentation](http://antigravity.google/docs/gcli-migration), and we will be releasing video walkthroughs in the coming weeks.

For [Gemini Code Assist for GitHub](https://developers.google.com/gemini-code-assist/docs/review-repo-code), this change will also apply and on June 18, 2026, there will be no new installations on Github organizations and requests in the following weeks will stop being served.

### **For enterprise customers**

If your organization uses Gemini CLI or our IDE extensions via a Gemini Code Assist Standard or Enterprise license, or if your organization uses Gemini Code Assist for GitHub through Google Cloud, your access remains unchanged. We’ll continue to support Gemini CLI and Gemini Code Assist with access to the latest Gemini models and other updates. Gemini CLI will remain accessible via paid Gemini and Gemini Enterprise Agent Platform API keys. And if you’re excited to try Antigravity CLI, you can use it now with your [Google Cloud projects](http://antigravity.google/blog/google-antigravity-for-enterprises).

We welcome your feedback in the Antigravity CLI [community forum](https://github.com/google-antigravity/antigravity-cli), especially if there is a feature you’d like to request during this transition. We look forward to seeing what you build next with Antigravity 2.0 and Antigravity CLI.

Explore this announcement and all Google I/O 2026 updates on [io.google](https://io.google/2026/?utm_source=blogpost&utm_medium=pr&utm_campaign=devblogs&utm_content=).

[](https://developers.googleblog.com/blazing-fast-on-device-genai-with-litert-lm/)
Previous

Next

[](https://developers.googleblog.com/one-year-of-innovation-celebrating-100k-members-in-the-google-cloud-x-nvidia-developer-community/)
