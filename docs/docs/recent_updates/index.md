# Recent Updates and Future Roadmap

`Page last updated: 2025-06-01`

This page summarizes recent enhancements to Qodo Merge (last three months).

It also outlines our development roadmap for the upcoming three months. Please note that the roadmap is subject to change, and features may be adjusted, added, or reprioritized.

=== "Recent Updates"
    - **Simplified Free Tier**: Qodo Merge now offers a simplified free tier with a monthly limit of 75 PR reviews per organization, replacing the previous two-week trial. ([Learn more](https://qodo-merge-docs.qodo.ai/installation/qodo_merge/#cloud-users))
    - **Linear tickets support**: Qodo Merge now supports Linear tickets. ([Learn more](https://qodo-merge-docs.qodo.ai/core-abilities/fetching_ticket_context/#linear-integration))
    - **Smart Update**: Upon PR updates, Qodo Merge will offer tailored code suggestions, addressing both the entire PR and the specific incremental changes since the last feedback  ([Learn more](https://qodo-merge-docs.qodo.ai/core-abilities/incremental_update//))
    - **Qodo Merge Pull Request Benchmark** - evaluating the performance of LLMs in analyzing pull request code ([Learn more](https://qodo-merge-docs.qodo.ai/pr_benchmark/))
    - **Chat on Suggestions**:  Users can now chat with code suggestions ([Learn more](https://qodo-merge-docs.qodo.ai/tools/improve/#chat-on-code-suggestions))
    - **Scan Repo Discussions Tool**: A new tool that analyzes past code discussions to generate a `best_practices.md` file, distilling key insights and recommendations. ([Learn more](https://qodo-merge-docs.qodo.ai/tools/scan_repo_discussions/))


=== "Future Roadmap"
    - **Best Practices Hierarchy**: Introducing support for structured best practices, such as for folders in monorepos or a unified best practice file for a group of repositories.
    - **Enhanced `review` tool**: Enhancing the `review` tool validate compliance across multiple categories including security, tickets, and custom best practices.
    - **Smarter context retrieval**: Leverage AST and LSP analysis to gather relevant context from across the entire repository.
    - **Enhanced portal experience**: Improved user experience in the Qodo Merge portal with new options and capabilities.
