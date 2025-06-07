<div align="center">

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://www.qodo.ai/wp-content/uploads/2025/02/PR-Agent-Purple-2.png">
  <source media="(prefers-color-scheme: light)" srcset="https://www.qodo.ai/wp-content/uploads/2025/02/PR-Agent-Purple-2.png">
  <img src="https://codium.ai/images/pr_agent/logo-light.png" alt="logo" width="330">

</picture>
<br/>

[Installation Guide](https://qodo-merge-docs.qodo.ai/installation/) |
[Usage Guide](https://qodo-merge-docs.qodo.ai/usage-guide/) |
[Tools Guide](https://qodo-merge-docs.qodo.ai/tools/) |
[Qodo Merge](https://qodo-merge-docs.qodo.ai/overview/pr_agent_pro/) 💎

PR-Agent aims to help efficiently review and handle pull requests, by providing AI feedback and suggestions
</div>

[![Static Badge](https://img.shields.io/badge/Chrome-Extension-violet)](https://chromewebstore.google.com/detail/qodo-merge-ai-powered-cod/ephlnjeghhogofkifjloamocljapahnl)
[![Static Badge](https://img.shields.io/badge/Pro-App-blue)](https://github.com/apps/qodo-merge-pro/)
[![Static Badge](https://img.shields.io/badge/OpenSource-App-red)](https://github.com/apps/qodo-merge-pro-for-open-source/)
[![Discord](https://badgen.net/badge/icon/discord?icon=discord&label&color=purple)](https://discord.com/invite/SgSxuQ65GF)
<a href="https://github.com/Codium-ai/pr-agent/commits/main">
<img alt="GitHub" src="https://img.shields.io/github/last-commit/Codium-ai/pr-agent/main?style=for-the-badge" height="20">
</a>
</div>

## Table of Contents

- [Getting Started](#getting-started)
- [News and Updates](#news-and-updates)
- [Overview](#overview)
- [See It in Action](#see-it-in-action)
- [Try It Now](#try-it-now)
- [Qodo Merge 💎](#qodo-merge-)
- [How It Works](#how-it-works)
- [Why Use PR-Agent?](#why-use-pr-agent)
- [Data Privacy](#data-privacy)
- [Contributing](#contributing)
- [Links](#links)

## Getting Started

### Try it Instantly
Test PR-Agent on any public GitHub repository by commenting `@CodiumAI-Agent /improve`

### GitHub Action
Add automated PR reviews to your repository with a simple workflow file using [GitHub Action setup guide](https://qodo-merge-docs.qodo.ai/installation/github/#run-as-a-github-action)


### CLI Usage
Run PR-Agent locally on your repository via command line: [Local CLI setup guide](https://qodo-merge-docs.qodo.ai/usage-guide/automations_and_usage/#local-repo-cli)

### Jenkins Pipeline
You can also run PR-Agent from a Jenkins job triggered by GitHub webhooks. Configure your pipeline to call
`python -m pr_agent.cli --pr_url <pr_url> <command>` using the API endpoint and token defined in `configuration.toml`.

### Discover Qodo Merge 💎 
Zero-setup hosted solution with advanced features and priority support
-  [Intro and Installation guide](https://qodo-merge-docs.qodo.ai/installation/qodo_merge/)
-  [Plans & Pricing](https://www.qodo.ai/pricing/)


## News and Updates

## Jun 3, 2025

Qodo Merge now offers a simplified free tier 💎.
Organizations can use Qodo Merge at no cost, with a [monthly limit](https://qodo-merge-docs.qodo.ai/installation/qodo_merge/#cloud-users) of 75 PR reviews per organization.

## May 17, 2025

- v0.29 was [released](https://github.com/qodo-ai/pr-agent/releases)
- `Qodo Merge Pull Request Benchmark` was [released](https://qodo-merge-docs.qodo.ai/pr_benchmark/). This benchmark  evaluates and compares the performance of LLMs in analyzing pull request code.
- `Recent Updates and Future Roadmap` page was added to the [Qodo Merge Docs](https://qodo-merge-docs.qodo.ai/recent_updates/)

## Apr 30, 2025

A new feature is now available in the `/improve` tool for Qodo Merge 💎 - Chat on code suggestions.

<img width="512" alt="image" src="https://codium.ai/images/pr_agent/improve_chat_on_code_suggestions_ask.png" />

Read more about it [here](https://qodo-merge-docs.qodo.ai/tools/improve/#chat-on-code-suggestions).

## Apr 16, 2025

New tool for Qodo Merge 💎 - `/scan_repo_discussions`.

<img width="635" alt="image" src="https://codium.ai/images/pr_agent/scan_repo_discussions_2.png" />

Read more about it [here](https://qodo-merge-docs.qodo.ai/tools/scan_repo_discussions/).

## Overview


## See It in Action

<h4><a href="https://github.com/Codium-ai/pr-agent/pull/530">/describe</a></h4>
<div align="center">
<p float="center">
<img src="https://www.codium.ai/images/pr_agent/describe_new_short_main.png" width="512">
</p>
</div>
<hr>

<h4><a href="https://github.com/Codium-ai/pr-agent/pull/732#issuecomment-1975099151">/review</a></h4>
<div align="center">
<p float="center">
<kbd>
<img src="https://www.codium.ai/images/pr_agent/review_new_short_main.png" width="512">
</kbd>
</p>
</div>
<hr>

<h4><a href="https://github.com/Codium-ai/pr-agent/pull/732#issuecomment-1975099159">/improve</a></h4>
<div align="center">
<p float="center">
<kbd>
<img src="https://www.codium.ai/images/pr_agent/improve_new_short_main.png" width="512">
</kbd>
</p>
</div>

<div align="left">

</div>
<hr>

## Try It Now

Try the Claude Sonnet powered PR-Agent instantly on _your public GitHub repository_. Just mention `@CodiumAI-Agent` and add the desired command in any PR comment. The agent will generate a response based on your command.
For example, add a comment to any pull request with the following text:

```
@CodiumAI-Agent /review
```

and the agent will respond with a review of your PR.

Note that this is a promotional bot, suitable only for initial experimentation.
It does not have 'edit' access to your repo, for example, so it cannot update the PR description or add labels (`@CodiumAI-Agent /describe` will publish PR description as a comment). In addition, the bot cannot be used on private repositories, as it does not have access to the files there.

---

## Qodo Merge 💎

[Qodo Merge](https://www.qodo.ai/pricing/) is a hosted version of PR-Agent, provided by Qodo. It is available for a monthly fee, and provides the following benefits:

1. **Fully managed** - We take care of everything for you - hosting, models, regular updates, and more. Installation is as simple as signing up and adding the Qodo Merge app to your GitHub repo.
2. **Improved privacy** - No data will be stored or used to train models. Qodo Merge will employ zero data retention, and will use an OpenAI account with zero data retention.
3. **Improved support** - Qodo Merge users will receive priority support, and will be able to request new features and capabilities.
4. **Extra features** - In addition to the benefits listed above, Qodo Merge will emphasize more customization, and the usage of static code analysis, in addition to LLM logic, to improve results.
See [here](https://qodo-merge-docs.qodo.ai/overview/pr_agent_pro/) for a list of features available in Qodo Merge.

## How It Works

The following diagram illustrates PR-Agent tools and their flow:

![PR-Agent Tools](https://www.qodo.ai/images/pr_agent/diagram-v0.9.png)

Check out the [PR Compression strategy](https://qodo-merge-docs.qodo.ai/core-abilities/#pr-compression-strategy) page for more details on how we convert a code diff to a manageable LLM prompt

## Why Use PR-Agent?

A reasonable question that can be asked is: `"Why use PR-Agent? What makes it stand out from existing tools?"`

Here are some advantages of PR-Agent:

- We emphasize **real-life practical usage**. Each tool (review, improve, ask, ...) has a single LLM call, no more. We feel that this is critical for realistic team usage - obtaining an answer quickly (~30 seconds) and affordably.
- Our [PR Compression strategy](https://qodo-merge-docs.qodo.ai/core-abilities/#pr-compression-strategy)  is a core ability that enables to effectively tackle both short and long PRs.
- Our JSON prompting strategy enables us to have **modular, customizable tools**. For example, the '/review' tool categories can be controlled via the [configuration](pr_agent/settings/configuration.toml) file. Adding additional categories is easy and accessible.
- We support multiple ways to use the tool (CLI, GitHub Action, GitHub App, Docker, ...) and multiple models (GPT, Claude, Deepseek, ...)

## Data Privacy

### Self-hosted PR-Agent

- If you host PR-Agent with your OpenAI API key, it is between you and OpenAI. You can read their API data privacy policy here:
https://openai.com/enterprise-privacy

### Qodo-hosted Qodo Merge 💎

- When using Qodo Merge 💎, hosted by Qodo, we will not store any of your data, nor will we use it for training. You will also benefit from an OpenAI account with zero data retention.

- For certain clients, Qodo-hosted Qodo Merge will use Qodo’s proprietary models — if this is the case, you will be notified.

- No passive collection of Code and Pull Requests’ data — Qodo Merge will be active only when you invoke it, and it will then extract and analyze only data relevant to the executed command and queried pull request.

### Qodo Merge Chrome extension

- The [Qodo Merge Chrome extension](https://chromewebstore.google.com/detail/qodo-merge-ai-powered-cod/ephlnjeghhogofkifjloamocljapahnl) serves solely to modify the visual appearance of a GitHub PR screen. It does not transmit any user's repo or pull request code. Code is only sent for processing when a user submits a GitHub comment that activates a PR-Agent tool, in accordance with the standard privacy policy of Qodo-Merge.

## Contributing

To contribute to the project, get started by reading our [Contributing Guide](https://github.com/qodo-ai/pr-agent/blob/b09eec265ef7d36c232063f76553efb6b53979ff/CONTRIBUTING.md).

## Links

- Discord community: https://discord.com/invite/SgSxuQ65GF
- Qodo site: https://www.qodo.ai/
- Blog: https://www.qodo.ai/blog/
- Troubleshooting: https://www.qodo.ai/blog/technical-faq-and-troubleshooting/
- Support: support@qodo.ai
