Title: Getting started

URL Source: https://jules.google/docs/

Markdown Content:
Jules is an experimental coding agent that helps you fix bugs, add documentation, and build new features. It integrates with GitHub, understands your codebase, and works **autonomously** — so you can move on while it handles the task.

This guide will walk you through setting up Jules and running your first task.

1.   Visit [jules.google.com](https://jules.google.com/)
2.   Sign in with your Google account.
3.   Accept the privacy notice (one‑time).

Jules needs access to your repositories in order to work.

1.   Click **Connect to GitHub account.**
2.   Complete the login flow.
3.   Choose _all_ or specific repos that you want to connect to Jules.
4.   You will be redirected back to Jules. If not, try refreshing the page.

Once connected, you’ll see a **repo selector** where you can select the repo you want Jules to work with, and a prompt input box.

## Starting your first task

[Section titled “Starting your first task”](https://jules.google/docs/#starting-your-first-task)

Jules runs in a virtual machine where it clones your code, installs dependencies, and modifies files.

1.   Pick a repository from the repo selector.
2.   Choose the branch you want Jules to work on. The default branch will be selected already. You do not have to modify this unless you want Jules to work on a specific branch.
3.   Write a clear, specific prompt. For example, `Add a test for "parseQueryString` function in utils.js
4.   (Optional) Add environment setup scripts.
5.   Click **Give me a plan**

Once you submit a task, Jules will generate a plan. You can review and approve it before any code changes are made.


## Include AGENTS.md file

[Section titled “Include AGENTS.md file”](https://jules.google/docs/#include-agentsmd-file)

Jules now automatically looks for a file named AGENTS.md in the root of your repository. This file can describe the agents or tools in your codebase, such as what they do, how to interact with them, or any input and output conventions. Jules uses this file to better understand your code and generate more relevant plans and completions.

**Tip:** Keep AGENTS.md up to date. It helps Jules and your teammates work with your repo more effectively.

## Enabling notifications

[Section titled “Enabling notifications”](https://jules.google/docs/#enabling-notifications)

You are free to leave Jules while it is running. To stay informed:

1.   When prompted, enable browser notifications.
2.   Go to **Settings —> notifications** at any time to enable or disable notifications.

You’ll be notified when the task completes or needs your input.


*   [Running a task with Jules](https://jules.google/docs/running-tasks/) - Full walkthrough
*   [Environment setup](https://jules.google/docs/environment/) - Make Jules smarter about your project
*   [Reviewing plans & feedback](https://jules.google/docs/review-plan/) - how to approve and integrates

Want to dive into real-world use cases? Check out the [Jules Awesome Prompts repo](https://github.com/google-labs-code/jules-awesome-list).
