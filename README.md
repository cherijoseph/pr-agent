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


### Jenkins Pipeline
Run PR-Agent from a Jenkins job triggered by GitHub webhooks. Configure your
pipeline to call a short Python script that invokes
`PRAgent().handle_request(<pr_url>, [<command>])` using the API endpoint and
token defined in `configuration.toml`.

Zero-setup hosted solution with advanced features and priority support
-  [Intro and Installation guide](https://qodo-merge-docs.qodo.ai/installation/qodo_merge/)
-  [Plans & Pricing](https://www.qodo.ai/pricing/)


## News and Updates

## Jun 3, 2025


## May 17, 2025

- v0.29 was [released](https://github.com/qodo-ai/pr-agent/releases)

## Apr 30, 2025


<img width="512" alt="image" src="https://codium.ai/images/pr_agent/improve_chat_on_code_suggestions_ask.png" />

Read more about it [here](https://qodo-merge-docs.qodo.ai/tools/improve/#chat-on-code-suggestions).

## Apr 16, 2025


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
## Data Privacy

### Self-hosted PR-Agent








## Contributing

To contribute to the project, get started by reading our [Contributing Guide](https://github.com/qodo-ai/pr-agent/blob/b09eec265ef7d36c232063f76553efb6b53979ff/CONTRIBUTING.md).

## Links

- Discord community: https://discord.com/invite/SgSxuQ65GF
- Blog: https://www.qodo.ai/blog/
- Troubleshooting: https://www.qodo.ai/blog/technical-faq-and-troubleshooting/
- Support: support@qodo.ai
