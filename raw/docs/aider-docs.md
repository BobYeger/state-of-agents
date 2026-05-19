Title: Aider Documentation

URL Source: https://aider.chat/docs/

Published Time: Sat, 25 Apr 2026 16:45:23 GMT

Markdown Content:
Aider is AI pair programming in your terminal. This documentation will help you get the most out of aider.

*   [Installation](https://aider.chat/docs/install.html)— How to install and get started pair programming with aider.
    *   [Optional steps](https://aider.chat/docs/install/optional.html)
    *   [Aider with docker](https://aider.chat/docs/install/docker.html)
    *   [GitHub Codespaces](https://aider.chat/docs/install/codespaces.html)
    *   [Replit](https://aider.chat/docs/install/replit.html)

*   [Usage](https://aider.chat/docs/usage.html)— How to use aider to pair program with AI and edit code in your local git repo.
    *   [Tips](https://aider.chat/docs/usage/tips.html)— Tips for AI pair programming with aider.
    *   [In-chat commands](https://aider.chat/docs/usage/commands.html)— Control aider with in-chat commands like /add, /model, etc.
    *   [Chat modes](https://aider.chat/docs/usage/modes.html)— Using the code, architect, ask and help chat modes.
    *   [Tutorial videos](https://aider.chat/docs/usage/tutorials.html)— Intro and tutorial videos made by aider users.
    *   [Voice-to-code with aider](https://aider.chat/docs/usage/voice.html)— Speak with aider about your code!
    *   [Images & web pages](https://aider.chat/docs/usage/images-urls.html)— Add images and web pages to the aider coding chat.
    *   [Prompt caching](https://aider.chat/docs/usage/caching.html)— Aider supports prompt caching for cost savings and faster coding.
    *   [Aider in your IDE](https://aider.chat/docs/usage/watch.html)— Aider can watch your files and respond to AI comments you add in your favorite IDE or text editor.
    *   [Notifications](https://aider.chat/docs/usage/notifications.html)— Aider can notify you when it's waiting for your input.
    *   [Aider in your browser](https://aider.chat/docs/usage/browser.html)— Aider can run in your browser, not just on the command line.
    *   [Specifying coding conventions](https://aider.chat/docs/usage/conventions.html)— Tell aider to follow your coding conventions when it works on your code.
    *   [Copy/paste with web chat](https://aider.chat/docs/usage/copypaste.html)— Aider works with LLM web chat UIs
    *   [Linting and testing](https://aider.chat/docs/usage/lint-test.html)— Automatically fix linting and testing errors.
    *   [Editing config & text files](https://aider.chat/docs/usage/not-code.html)— Use aider to edit configuration files, documentation, and other text-based formats.

*   [Connecting to LLMs](https://aider.chat/docs/llms.html)— Aider can connect to most LLMs for AI pair programming.
    *   [OpenAI](https://aider.chat/docs/llms/openai.html)
    *   [Anthropic](https://aider.chat/docs/llms/anthropic.html)
    *   [Gemini](https://aider.chat/docs/llms/gemini.html)
    *   [GROQ](https://aider.chat/docs/llms/groq.html)
    *   [LM Studio](https://aider.chat/docs/llms/lm-studio.html)
    *   [xAI](https://aider.chat/docs/llms/xai.html)
    *   [Azure](https://aider.chat/docs/llms/azure.html)
    *   [Cohere](https://aider.chat/docs/llms/cohere.html)
    *   [DeepSeek](https://aider.chat/docs/llms/deepseek.html)
    *   [Ollama](https://aider.chat/docs/llms/ollama.html)
    *   [OpenAI compatible APIs](https://aider.chat/docs/llms/openai-compat.html)
    *   [OpenRouter](https://aider.chat/docs/llms/openrouter.html)
    *   [GitHub Copilot](https://aider.chat/docs/llms/github.html)
    *   [Vertex AI](https://aider.chat/docs/llms/vertex.html)
    *   [Amazon Bedrock](https://aider.chat/docs/llms/bedrock.html)
    *   [Other LLMs](https://aider.chat/docs/llms/other.html)
    *   [Model warnings](https://aider.chat/docs/llms/warnings.html)

*   [Configuration](https://aider.chat/docs/config.html)— Information on all of aider's settings and how to use them.
    *   [API Keys](https://aider.chat/docs/config/api-keys.html)— Setting API keys for API providers.
    *   [Options reference](https://aider.chat/docs/config/options.html)— Details about all of aider's settings.
    *   [YAML config file](https://aider.chat/docs/config/aider_conf.html)— How to configure aider with a YAML config file.
    *   [Config with .env](https://aider.chat/docs/config/dotenv.html)— Using a .env file to store LLM API keys for aider.
    *   [Editor configuration](https://aider.chat/docs/config/editor.html)— How to configure a custom editor for aider's /editor command
    *   [Reasoning models](https://aider.chat/docs/config/reasoning.html)— How to configure reasoning model settings from secondary providers.
    *   [Advanced model settings](https://aider.chat/docs/config/adv-model-settings.html)— Configuring advanced settings for LLMs.
    *   [Model Aliases](https://aider.chat/docs/config/model-aliases.html)— Assign convenient short names to models.

*   [Troubleshooting](https://aider.chat/docs/troubleshooting.html)— How to troubleshoot problems with aider and get help.
    *   [File editing problems](https://aider.chat/docs/troubleshooting/edit-errors.html)
    *   [Model warnings](https://aider.chat/docs/troubleshooting/warnings.html)
    *   [Token limits](https://aider.chat/docs/troubleshooting/token-limits.html)
    *   [Aider not found](https://aider.chat/docs/troubleshooting/aider-not-found.html)
    *   [Dependency versions](https://aider.chat/docs/troubleshooting/imports.html)
    *   [Models and API keys](https://aider.chat/docs/troubleshooting/models-and-keys.html)
    *   [Using /help](https://aider.chat/docs/troubleshooting/support.html)

*   [Screen recordings](https://aider.chat/docs/recordings/)— Screen recordings of aider building aider.
    *   [Add language support via tree-sitter-language-pack](https://aider.chat/docs/recordings/tree-sitter-language-pack.html)— Watch how aider adds support for tons of new programming languages by integrating with tree-sitter-language-pack. Demonstrates using aider to script downloading a collection of files, and using ad-hoc bash scripts to have aider modify a collection of files.
    *   [Add –auto-accept-architect feature](https://aider.chat/docs/recordings/auto-accept-architect.html)— See how a new command-line option is added to automatically accept edits proposed by the architect model, with implementation. Aider also updates the project's HISTORY file.
    *   [Don’t /drop read-only files added at launch](https://aider.chat/docs/recordings/dont-drop-original-read-files.html)— Follow along as aider is modified to preserve read-only files specified at launch when using the /drop command. Aider does this implementation and adds test coverage.
    *   [Warn when users apply unsupported reasoning settings](https://aider.chat/docs/recordings/model-accepts-settings.html)— Watch the implementation of a warning system that alerts users when they try to apply reasoning settings to models that don't support them. Includes adding model metadata, confirmation dialogs, refactoring, and comprehensive test coverage.

*   [Example chat transcripts](https://aider.chat/examples/README.html)
    *   [Editing an asciinema cast file with aider](https://aider.chat/examples/asciinema.html)
    *   [Download, analyze and plot US Census data](https://aider.chat/examples/census.html)
    *   [Improve css styling of chat transcripts](https://aider.chat/examples/chat-transcript-css.html)
    *   [Complete a css exercise with aider](https://aider.chat/examples/css-exercises.html)
    *   [Hello aider!](https://aider.chat/examples/hello.html)
    *   [Honor the NO_COLOR environment variable](https://aider.chat/examples/no-color.html)
    *   [Build pong with aider and pygame.](https://aider.chat/examples/pong.html)
    *   [Semantic search & replace code with aider](https://aider.chat/examples/semantic-search-replace.html)
    *   [Automatically update docs with aider](https://aider.chat/examples/update-docs.html)
    *   [Create a simple flask app with aider](https://aider.chat/examples/hello-world-flask.html)
    *   [Modify an open source 2048 game with aider](https://aider.chat/examples/2048-game.html)
    *   [A complex multi-file change, with debugging](https://aider.chat/examples/complex-change.html)
    *   [Create a “black box” test case](https://aider.chat/examples/add-test.html)

*   [More info](https://aider.chat/docs/more-info.html)
    *   [Git integration](https://aider.chat/docs/git.html)— Aider is tightly integrated with git.
    *   [Supported languages](https://aider.chat/docs/languages.html)— Aider supports pretty much all popular coding languages.
    *   [Repository map](https://aider.chat/docs/repomap.html)— Aider uses a map of your git repository to provide code context to LLMs.
    *   [Scripting aider](https://aider.chat/docs/scripting.html)— You can script aider via the command line or python.
    *   [Infinite output](https://aider.chat/docs/more/infinite-output.html)— Aider can handle "infinite output" from models that support prefill.
    *   [Edit formats](https://aider.chat/docs/more/edit-formats.html)— Aider uses various "edit formats" to let LLMs edit source files.
    *   [Analytics](https://aider.chat/docs/more/analytics.html)— Opt-in, anonymous, no personal info.
    *   [Privacy policy](https://aider.chat/docs/legal/privacy.html)

*   [FAQ](https://aider.chat/docs/faq.html)— Frequently asked questions about aider.
*   [Release history](https://aider.chat/HISTORY.html)— Release notes and stats on aider writing its own code.
*   [Aider LLM Leaderboards](https://aider.chat/docs/leaderboards/)— Quantitative benchmarks of LLM code editing skill.
    *   [Code editing leaderboard](https://aider.chat/docs/leaderboards/edit.html)— Quantitative benchmark of basic LLM code editing skill.
    *   [Refactoring leaderboard](https://aider.chat/docs/leaderboards/refactor.html)— Quantitative benchmark of LLM code refactoring skill.
    *   [Scores by release date](https://aider.chat/docs/leaderboards/by-release-date.html)
    *   [Benchmark notes](https://aider.chat/docs/leaderboards/notes.html)
    *   [Contributing results](https://aider.chat/docs/leaderboards/contrib.html)

*   [Aider blog](https://aider.chat/blog/)
