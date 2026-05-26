May 22, 2026

**Platform Default Settings**

Org admins can now set a default platform (Linux or Windows) for all new sessions, and individual users can star their personal preference. The default platform is honored across all session creation methods, including Slack, Linear, Jira, API, and automations.

**Slack Channel Override**

Type `!channel #channel-name` in Slack to override which channel Devin spawns its response thread in for that session.

**MCP OAuth Resource Parameter**

MCP OAuth flows now forward the RFC 8707 resource parameter, fixing authentication for MCP servers that require resource indicators (such as Snowflake and Runlayer).

**Custom RRULE Schedule Input**

Automation schedules now support pasting raw RFC 5545 recurrence rule strings directly, with validation and auto-detection, for schedules that go beyond the visual editor.

**GitLab Interactive PR Review**

GitLab repositories now support interactive PR review — Devin can post review comments and resolve threads as you — when the read-write GitLab connection is enabled.

**PR Review Status API**

A new `GET /v3/enterprise/pr-reviews` endpoint lets you poll Devin Review status programmatically, with optional commit SHA filtering.

**In-App Support Dialog**

“Contact support” now opens an in-app dialog where you can submit a ticket directly, replacing the previous email link.

**Inline Repo Permission Toggle**

You can now toggle repository permissions between “Read only” and “Read & write” directly from the permissions table, without needing to remove and re-add the repository.

**Enterprise Max Concurrent Snapshot Builds**

Enterprise admins can now set a maximum concurrent snapshot builds limit in enterprise settings, with backend enforcement to prevent build queue overload.

**GitLab OAuth Scope and Token Refresh**

GitLab user OAuth now requests the broader `api` scope for better compatibility, and tokens are automatically refreshed before they expire.

**Network Config Editor Redesign**

The network policy editor has been redesigned as an inline-editable list with multi-line paste support and duplicate detection, fixing the issue where domains typed but not submitted were silently lost on save.

**GitHub Connection No Longer Required for Automations**

GitHub-triggered automations no longer require a personal GitHub connection, allowing teams to rely on the org-level connection exclusively.

**PostHog MCP**

The PostHog MCP server is now available in the MCP marketplace, enabling product analytics integration directly from Devin sessions.

**Other Improvements**

Automation sessions now appear in a dedicated “Automations involving you” sidebar folder instead of being auto-pinned. Session @-mentions in chat are clickable links. A new Cmd+K action copies the session URL to clipboard. Archive undo now restores cascade-archived child sessions. MCP connection errors are surfaced instead of silently swallowed, and a new disconnect action removes stored OAuth tokens. Integration mappings for Linear, Slack, Teams, and Jira are validated at save time. The repo selector shows a Recent section and org labels. Tool calls in Watch Devin Work display timing. Automation-spawned sessions can be renamed by any org member. Integration page actions are permission-gated. File URLs in the timeline link to the correct git provider. GHES installations resolve bot identity per-config and scope webhook processing to the owning account.May 17, 2026

**Collapsible Session Folders**

Sessions in the left sidebar can now be organized into collapsible folders. Click the chevron to expand or collapse a folder, and your preference is persisted per organization.

**Archive All Sessions**

A new “Archive all” option in the sidebar menu lets you archive all sessions or asks at once, with a confirmation dialog and undo support. Child sessions skip the confirmation step for faster cleanup.

**Sub-Devin Session Filter**

The sessions page now includes a “Sub-Devin” filter that lets you view child sessions independently, with support for combined parent and child filtering.

**Default Member Roles**

Enterprise admins can now configure default roles that are automatically assigned to new organization members on join, with badge display in the members list and safeguards against accidental deletion of roles in use.

**GHES App Registration Restriction**

GitHub Enterprise Server app registration is now restricted to one app per account and host combination, preventing duplicate registrations with a clear error message when a conflict is detected.

**Copyable Organization ID**

Your Organization ID is now displayed with a one-click copy button on both the Settings → General and Settings → Devin API pages, making it easy to share with support or use in API calls.

**Admin-Enforced Settings Lock Icon**

Settings that have been locked by an admin now display a lock icon with an explanatory tooltip, replacing the previous banner-style callout for a cleaner interface.

**MCP OAuth Client Credentials**

When installing MCP integrations that don’t support Dynamic Client Registration (such as Salesforce), you can now supply your own OAuth client credentials directly in the configuration flow.

**Tavily MCP in Marketplace**

Tavily web search is now available in the MCP marketplace, providing AI-optimized real-time web search and content extraction capabilities for your Devin sessions.

**PR Actions & Auto-Review Settings**

The PR actions menu in Devin Review has been restored with an auto-review toggle and personal settings popover, giving you quick access to review preferences without leaving the review interface.

**Checks Tab Always Visible**

The Checks tab is now always visible in the embedded PR review experience, and the merge-status popover properly restores the checks UI so you can always see CI status at a glance.

**Improved @-Mention Search**

The @-mention search in the chat input now uses fuzzy bag-of-words matching, so queries like “setup-dev” will find “setup-windsurf-dev”. Repositories are also ranked first in the dropdown for faster access.

**Slack Improvements**

This release includes several Slack integration improvements: channel names now resolve correctly even for channels you haven’t joined, mentions display as styled blue pill badges, unmapped channel messaging is clearer, the Watch channel option appears at the top of the trigger submenu, stale channel lists are fixed, and duplicate webapp-to-Slack thread posts are suppressed.

**Slack Security Hardening**

Enterprise channel isolation for Slack thread-attach has been hardened with runtime authorization that validates channels against enterprise channel preferences, preventing cross-organization channel access.

**Video Recording Download**

You can now download session recording videos directly from the video player controls.

**Miscellaneous Improvements**

This release also includes: file re-upload fix, archived chip now clickable for non-owners with unarchive permission, network config available for finished sessions, test recording viewer close button visibility fix, settings search improvements, back buttons on MCP marketplace and knowledge detail pages, deep mode callout hidden when disabled, repo name truncation so filter stays visible, mobile agent selection single-tap fix, Devin Review file scroll and merge status fixes, skills link fix, Slack support channel in help popover, and wait tool rendered as standalone worklog event.May 13, 2026

**Snapshot Build Delete**

You can now delete snapshot builds directly from the build history menu or detail page, with a confirmation dialog to prevent accidental removal. This makes it easier to clean up old or failed builds without navigating away from your environment settings.

**MCP Multiline Environment Variables**

When configuring MCP server connections in the marketplace, you can now enter multiline values for environment variables — such as PEM private keys, JSON service account credentials, and Snowflake key passphrases — without needing to escape or flatten them first.

**Sub-Devin Sidebar Improvements**

Sub-Devin sessions spawned by automations can now be pinned and reordered independently in the sidebar, and they appear expanded by default so you can see their status at a glance without clicking to expand.

**Voice Recording While Devin Is Working**

The microphone button now appears alongside the stop button while Devin is actively working, allowing you to record and send voice follow-ups without waiting for Devin to finish its current task.

**Settings Redesign**

Settings pages have been redesigned with a hub-style layout, improved search across all settings, and a streamlined navigation structure. An announcement dialog introduces the new experience on first visit, and legacy settings URLs automatically redirect to their new locations.

**Archive Active Session Warning**

When you archive a session that is still actively working, a warning dialog now informs you that archiving will put both the session and any child sessions to sleep before proceeding.

**Share Session on Mobile**

A new “Share session” action is available in the sidebar session menu on mobile devices, making it easy to share session links directly from your phone.

**Devin Review Mobile Improvements**

On mobile, tapping “Ask Devin” on a comment now opens the chat panel directly, pull-to-refresh is available on the review scroll container, and bug/flag tap targets have been fixed so they open on the first tap and reveal the associated comment.

**V3 API Enhancements**

The V3 API now supports filtering sessions by repository name via the `repo_names` parameter, filtering by archive status via `is_archived`, specifying `devin_mode` when creating sessions, and setting `folder_id` and `is_enabled` when creating or updating knowledge notes.

**Enterprise Member Invite Acknowledgement**

When inviting new members to an enterprise organization from the admin panel, an acknowledgement modal now confirms the invitation details before it is sent.

**Rename Context to Skills & Rules**

The “Context” section in settings has been renamed to “Skills & Rules” to better describe its purpose of managing Devin’s skill definitions and behavioral rules for your organization.

**Blueprint Migration Improvements**

The blueprint migration page now displays per-repo session counts, supports filtering by repository, and shows a completed state when all migrations are finished, making it easier to track progress across large organizations.

**Miscellaneous Improvements**

This release also includes: autofocus on confirmation buttons in archive dialogs, plan artifact button polish, configurable CI status in search results, debounced enterprise snapshot builds, server-side event deduplication to prevent duplicate delivery, pinned sessions remaining visible when automations are hidden in the sidebar, removal of the misleading “Action required” label for Python sessions awaiting instructions, schedule list cap raised from 50 to 200, monitor trigger cleanup when adding new Slack triggers, repo setup status fix for Dynamic Repo Setup organizations, “Approve session” visibility in the sidebar even after all PRs are merged, inline image deduplication by URL, streaming scroll stability fix, high-resolution home screen icon for Android, beta Vite mode build fix, fast mode loading indicator reset on session switch, and sidebar hover cards on expanded non-active sections.May 8, 2026

**Devin Review API**

You can now trigger Devin Review programmatically via the REST API. Use `POST /v3/organizations/{org_id}/pr-reviews` with a service user token or PAT to initiate reviews from CI pipelines, scripts, or custom integrations.

**Mermaid Diagram Rendering**

Mermaid code blocks in session messages now render as interactive SVG diagrams with zoom and pan controls, making it easier to explore flowcharts, sequence diagrams, and architecture diagrams that Devin produces.

**Close PRs on Session Archive**

When archiving a Devin session, a dialog now appears where you can optionally close any linked GitHub pull requests, keeping your repository tidy without manual cleanup.

**Per-PR Auto-Review Toggle**

You can now enable or disable automatic Devin Review on a per-PR basis from the PR actions menu, giving you granular control over which pull requests receive automated review without changing your organization-wide settings.

**Sidebar Session Notifications**

The session sidebar now shows persistent status labels, such as “PR created,” “Awaiting instructions,” or “Approve session,” alongside timestamps so you can quickly see what each session needs. Sessions also display read/unread indicators: an orange dot marks sessions with unread updates, and the dot clears once you open the session.

**Service User Permission Management**

Enterprise administrators can now assign the `ManageAccountServiceUsers` permission in custom roles, providing granular control over who can create and manage service users and API keys within the organization.

**Ask Devin in PR Discussions**

The “Ask Devin” button is now available on discussion tab thread comments in Devin Review, making it easy to ask follow-up questions or request changes directly within review conversation threads.

**MCP Secret Scoping**

When adding secrets for custom MCP server connections, you can now choose between personal scope, visible only to you, or organization scope, shared with your team, via a new scope selector in the creation dialog.

**Clickable Diff Stats in Worklog**

Clicking the +N/-M diff stats in worklog group headers now opens a scoped diff tab showing only the file changes from that specific group, making it faster to review exactly what changed at each step.

**Repo Selector Fix**

The select-all checkbox in the repository selector now correctly toggles only the repositories matching your current search filter, rather than selecting all repositories regardless of the filter.May 6, 2026

**Slack Tool Use in Worklog**

When Devin interacts with Slack during a session (sending messages, adding reactions, reading channels), these actions now appear in the worklog and progress UI with a dedicated Slack icon and action details.

**Settings Search Improvements**

Settings pages now use a centralized item registry with keyword-driven search, delivering more accurate and comprehensive results when searching across all settings pages.

**Command Palette Search**

Fixed search ordering in the command palette so results rank correctly, and resolved a scroll view issue in the search results window.

**Review Commit Links**

Fixed commit links in Devin Review to point to the correct URL path, and improved status indicators for review progress.

**Default Branch Detection**

Fixed an issue where repository indexing could use the wrong branch as the primary branch instead of the actual GitHub or GitLab default branch, which could affect DeepWiki and search results.May 1, 2026

**Stacked Review Permissions**

Enterprise admins can now assign tiered PR Review access levels to their organization members: manual-only review, automatic review on PR creation, or automatic review on every push. This gives administrators granular control over how and when Devin Review engages with pull requests across their organization.

**Skill Slash Commands**

You can now invoke skills by typing `/name` in the prompt input, in addition to the existing @mention syntax. Skills are grouped by repository in the dropdown for easier discovery.

**Auto-Attach Large Paste**

Pasting a large block of text into the prompt input now automatically attaches it as a file instead of filling the text box, preserving any message you’ve already typed.

**Jira Project Mapping Redesign**

The Jira project mapping modal has been redesigned with a fixed header and scrollable content area, making it easier to configure mappings for organizations with many Jira projects.

**Auto-Fix Includes CI Checks**

The “Auto-fix with Devin” button on pull requests now includes failing CI check names in the prompt alongside review findings, giving Devin more context to resolve issues in a single pass.

**Linear Team Mapping Improvements**

The default organization is now optional when configuring enterprise Linear team mappings, and unmapped teams can be explicitly cleared to “None” instead of requiring a catch-all mapping.

**Session Origin in API**

The v3 API session response now includes an `origin` field indicating how the session was created (webapp, Slack, API, or CLI), making it easier for API consumers to categorize and filter sessions programmatically.

**Deleted Orgs in Enterprise Sessions API**

Enterprise session endpoints now support an `include_deleted_orgs` parameter, giving enterprise admins visibility into sessions from organizations that have been removed.

**Snapshot Revert for Declarative Setup**

Users with the ManageOrgSnapshots permission can now revert an organization from declarative environment configuration back to classic configuration, without needing the broader ManageOrgSettings permission.April 29, 2026

**Revamped Blueprint Authoring Experience**

The blueprint editor has been redesigned with a shared layout, per-section play buttons, and a bottom terminal drawer. You can now deep-link directly into a repo’s blueprint editor, making it faster to author and test environment setups.

**Enterprise Commit Email Lock**

Enterprise admins can now require all member commits to use the user’s primary email. The lock is enforced across snapshot setup, session creation, and PR digest commits, helping enterprises keep commit attribution consistent for audit and compliance.

**PR Auto-Close Removed**

Devin sessions no longer automatically close their pull requests when the session ends. Open PRs now stay open by default so you can manage their lifecycle yourself, with no surprise closures.

**Hybrid Comment Mode in Devin Review**

When Devin Review is opened alongside a Devin session, review comments now default to hybrid mode — anchored to specific lines where possible and falling back to file-level comments otherwise — instead of forcing one or the other.

**Auth-Type Badges in Git Connections**

The git connection filter dropdown on the repository permissions page now shows a PAT, App, or OAuth badge next to each connection, making it easier to disambiguate connections that share a name.

**Slack Trigger Message in Sessions List**

Sessions started from Slack now display the user’s triggering Slack message in the sessions list instead of the system prompt, making it easier to identify Slack-launched sessions at a glance.

**PR Digest List Redesign**

The PR digest list has been redesigned with a cleaner layout that matches the sessions list view, making it easier to scan and navigate through pull requests.

**Double-Click File Attachment Picker**

Double-click the plus button in the prompt input to directly open the file attachment picker, skipping the intermediate menu.April 24, 2026

**Sensitive Toggle for Secrets**

When Devin requests a secret, you can now toggle whether the value should be masked (sensitive) or visible, instead of it always defaulting to masked.

**Merged Multi-Edits in Progress Tab**

Consecutive file edits to the same file are now merged into a single entry in the progress tab, showing a combined diff from the original to the final version instead of individual per-edit diffs.

**Session Category and Subcategory in API**

The v3 API session response now includes category and subcategory fields. A new category filter is available on session list endpoints, and session exports also include these fields.

**Wide Markdown Tables in Chat**

Markdown tables in Devin’s chat messages can now extend beyond the chat column width, preventing cramped multi-column tables from being unreadable.April 22, 2026

**SSO Connection Picker**

Organizations with multiple SSO connections for the same email domain now see a picker on the login page instead of being auto-redirected to the first match, letting users choose the correct identity provider.

**MCP OAuth Token Expiry Warnings**

Invalid or expired MCP OAuth tokens are now flagged with warning banners in the integrations UI. A reconnect button lets you re-authorize without navigating away from the page.

**Repository Permissions Decoupled from Git Integrations**

Repository permissions are now managed separately from git integration settings with a view/manage split, giving admins finer-grained control over who can modify repository access versus who can manage the underlying git connection.

**View Consumption Permission**

A new ViewAccountConsumption permission separates read access to usage and consumption data from billing write access, allowing admins to grant visibility without full billing control.

**Attachments in Question Answers**

File attachments are now included when you answer Devin’s prompts. Previously, attached files were silently dropped.

**MCP Auth Status Feedback**

MCP authentication requests now show success or error status in both the webapp and Slack after completion, so you know immediately whether authorization succeeded.

**Merge Time Reduction in Review**

The Devin Review page now displays the merge time reduction percentage, showing how much faster PRs are merged with Devin Review enabled.April 17, 2026

**PR Digest for Disconnected Users**

The Review page now shows a read-only digest of PRs from your Devin sessions — including open, draft, merged, and closed PRs — even if you haven’t connected GitHub yet.

**GitHub Enterprise Server in Review**

GitHub Enterprise Server instances can now be selected in the Review page’s Link GitHub flow, and GHES organizations appear in the Devin Review org selector.

**Review Permissions Enforcement**

Repository-level review permissions are now enforced, giving admins control over which repositories Devin Review can access.

**IDP Groups Management**

Enterprise settings now include a management UI for Identity Provider (Okta) groups, letting admins map groups to roles, view group members, and detect user conflicts with existing role assignments.

**Secure Mode Description**

The Secure mode description in enterprise settings has been rewritten to more clearly explain what Secure mode does and when to use it.

**WikiGenerationItem Card**

A new card is now displayed in sessions when the generate\_wiki MCP tool is invoked, giving better visibility into wiki generation progress.

**GHES Links in Integrations**

GitHub Enterprise Server user account links have been moved to the Integrations section of your profile for easier access.

**Minor Bug Fixes and Improvements**

This release also includes a range of smaller fixes and polish: sessions now indicate which are in an “Action Required” state, fixed the playback speed dropdown not opening on click, resolved invisible text in chat inputs on light backgrounds, fixed sidebar glyph flickering, corrected the Context Growth chart x-axis to use continuous datetime, removed checkboxes from combobox options, fixed seat type dropdown clipping, improved seat invitation copy for proper singular/plural phrasing, clarified the “available full seats” invite warning, updated flex seats to show as unlimited on the members page, and hid the Connect GitHub banner for GitLab MRs and during the Review intro overlay.April 15, 2026

**Close PR or Convert to Draft in Review UI**

The PR review merge bar now includes options to close a PR or convert it to a draft directly from the review page.

**Inline Session Rename**

Sessions can now be renamed inline directly in the sidebar without opening a dialog.

**Smart Table Column Sizing**

Tables throughout the app now use content-aware column width sizing for better readability.

**Faster Sidebar Session Loading**

The sidebar now lists sessions faster and more reliably, with improved rendering performance and optimistic updates when creating new sessions.

**Datadog Remote MCP Server**

Datadog is now available in the MCP marketplace as a remote MCP server with OAuth-based authentication, so Devin can query your Datadog dashboards and metrics directly.

**ACP Summarizer**

Agent Client Protocol now supports a summarizer method for generating session summaries programmatically, useful for integrations that need a concise recap of what Devin accomplished.

**Granola MCP Server**

The Granola MCP server is now promoted out of beta, letting Devin access your Granola meeting notes during a session.

**Pagination and Search for Review Settings**

Enterprise review settings now support pagination and search for repository and user lists, making it easier to manage large configurations.

**Minor Bug Fixes and Improvements**

This release also includes a range of smaller fixes and polish, including a proper 404 error page for invalid URLs, frontend performance optimizations, and assorted stability improvements across the webapp.April 10, 2026

**Theme Selector Generally Available**

The theme selector is now generally available, with system theme as the default so Devin automatically matches your OS light or dark mode.

**Wiki Effort Level Descriptions**

When choosing a DeepWiki effort level, each option now shows its expected ACU range so you can pick the right trade-off between cost and depth with confidence.

**DeepWiki Cost Breakdown Modal**

The DeepWiki cost breakdown modal is back, giving you an ACU-level view of where a wiki generation spent its budget.

**Cancel In-Progress Snapshot Builds**

You can now cancel an in-progress snapshot build directly from the snapshot list without waiting for it to finish or fail.

**Snapshot Blueprint Ordering**

Snapshot detail rails and repository-level blueprints now respect your configured blueprint ordering, so the list you see matches the order you set.

**Scheduled Session Failure Email Rate Limiting**

Failure email notifications for scheduled sessions are now rate limited, so a scheduled run hitting the same problem repeatedly will no longer flood your inbox.

**Knowledge Search Auto-Expand**

When you search your knowledge base, any folder containing a matching note now automatically expands so you can see the result in context without hunting for it.

**Profile Integrations Filter**

Your profile page now only shows integrations that are actually connected for your organization, cutting the clutter from services you do not use.

**Browser Tool Parity Improvements**

Devin’s browser tool now handles native browser dialogs, intercepts file chooser prompts, respects navigation guards, and restores focus correctly, bringing its behavior much closer to a real user browsing the web.

**Amplitude MCP Server**

Amplitude is now available in the MCP marketplace, so Devin can pull product analytics directly into a session without a custom integration.

**One-Click MCP OAuth Install**

Installing an MCP server that uses OAuth now returns the authorization URL directly, skipping an extra click and getting you connected faster.

**Personal MCP Servers**

You can now connect personal MCP servers, which enable Devin to use MCPs with authorization provided by an individual user rather than shared across an organization.

**Richer ACP Methods and @-Mentions**

Agent Client Protocol now carries @-mentions as structured resource blocks and adds new methods for listing repositories, saving secrets, archiving sessions, approving deploys, and attaching to the interactive browser, giving ACP clients a much richer surface area to work with.

**Devin CLI Polish**

The Devin CLI now preserves streamed shell output alongside exit codes, supports a `/resume` alias, renders plan-mode exits more clearly, and uses focus pings to keep a session from sleeping while you are actively watching it.

**Reconnecting VNC Screen**

The interactive browser now shows a reconnecting screen while its VNC stream is recovering, so you get clear feedback instead of a frozen view when the connection briefly drops.

**Unlink GitHub Enterprise Server OAuth**

You can now unlink a GitHub Enterprise Server OAuth connection from your account, making it easy to rotate credentials or clean up stale integrations.

**Total ACUs Column in Usage Table**

The Users table in Usage analytics now includes a Total ACUs column, so enterprise admins can rank and compare per-user consumption at a glance.

**Bulk Repository Secrets Import**

Enterprise admins can now import multiple repository secrets at once through a new bulk import flow on the repository configuration page, replacing the old one-at-a-time workflow.

**Minor Bug Fixes and Improvements**

This release also includes a range of smaller fixes and polish across the webapp, including repository branch dropdowns that now size correctly, the DeepWiki section hidden when no branches are indexed, a fix for Linear OAuth cancellations returning errors, correct starting numbers on streamed ordered lists, a copy-message button that now copies only the selected message, and assorted other stability and layout improvements.April 8, 2026

**Auto-merge from Devin Review**

You can now enable or disable GitHub auto-merge directly from the Devin Review merge button, so approved pull requests land as soon as checks pass without an extra trip to GitHub.

**Enterprise Review Consumption by Repository**

The Reviews tab on the Enterprise Consumption page now groups Devin Review spend by repository with current-cycle vs previous-cycle columns, a search box, and CSV export, making it much easier for enterprise admins to see where their review spend is going.

**Devin Review Breakdown in v3 Consumption API**

The v3 consumption API now reports Devin Review as its own line item in the product breakdown alongside sessions and indexing.

**Categorization and Subcategories**

Session categorization and subcategories are now generally available for every workspace, giving you a consistent way to organize and filter your Devin sessions.

**Pinned Organizations Sync Across Devices**

Your pinned organizations are now stored server-side and follow you across every device and browser you sign in from.

**Session Message Permalinks**

Every message in a session now has its own shareable link, so you can point teammates directly at the exact moment you want them to see.

**Larger Attachment Uploads**

Session attachments now support files up to 75 MB, up from the previous 20 MB limit.

**Higher-Quality Wiki v2**

Wiki v2 now uses stronger reasoning, subagents, and agentic page writers to produce noticeably better documentation, and shows the ACU cost of the last generation so you can see exactly what each refresh costs.

**Guardrails V3**

Our new pattern-based guardrail prompts significantly reduce false positives while keeping the same level of protection.

**Ask Sub-mode Renamed to Q&A**

The Ask sub-mode is now simply labeled “Q&A” to better reflect what it does.

**Consolidated Session Header Menu**

Session header links are now grouped into a single hyperlink menu for a cleaner, less crowded header.

**Faster Syntax Highlighting**

Code blocks across the app now render with an incremental, worker-based syntax highlighter for noticeably faster and smoother highlighting on large files.

**Scroll Restoration**

Navigating back through the app now restores your previous scroll position so you land where you left off.

**Japanese Localization Refresh**

Japanese localization strings have been refreshed across the webapp.

**MCP Marketplace Upgrades**

The MCP marketplace now includes a Recommended section, smarter Figma discovery, and a shared interactive OAuth flow that shows connection status and errors directly in chat as you install servers.

**MCP Audit Logs**

Enterprise audit logs now cover MCP server updates and secret link and unlink events for better visibility into integration changes.

**Session ACU Hard Caps**

Enterprises can now set a hard upper limit on total ACUs per session, with an acknowledgement modal and real-time validation so users always know when a session is approaching the cap.

**Cerebras Now Enterprise-Ready**

Cerebras is now available as an enterprise-ready inference provider for organizations that want to use it for their Devin workloads.

**US Privacy Controls**

Devin now honors Global Privacy Control signals and supports CCPA and CPRA opt-out requests for customers in the United States.

**Refreshed Settings Layout**

Insights, identity provider, and several other enterprise settings pages have been migrated to the new settings layout and design system for a more consistent look and faster navigation.

**Enterprise Secrets Table Polish**

The enterprise secrets table now includes an environment variable column and a build-only toggle, with a simplified layout that removes the Name column and type selector.

**Minor Bug Fixes and Improvements**

Numerous smaller fixes and polish, including sidebar collapse state persistence, sidebar pull requests loading without a GitHub connection, better multi-PR session isolation, deduplicated Slack file forwarding, quota reset on plan upgrade, billing cycle short-month correction, snapshots sorted alphabetically, an auto-organize tooltip explaining when it is disabled, and the Category beta label and Review beta badge retired for paying organizations.April 3, 2026

**Enterprise-Scoped Secrets**

Enterprise admins can manage secrets at the enterprise level, automatically shared across all organizations. Initially only available to users of declarative environment configuration.

**Enterprise ACU Visibility Control**

Enterprise admins can control whether users see ACU usage info.

**Enterprise MCP Registry Enforcement**

Enterprise admins can enforce an MCP server allowlist across their organization.

**Enterprise Build Pinning**

Enterprise admins can pin specific Devin builds and roll back to previous versions. Initially only available to users of declarative environment configuration.

**Devin Review Auto-Fix**

When Devin Review detects bugs in a PR, a new “Auto-fix with Devin” button launches a session to fix them in one click.

**PR Review Chat CI Tools**

Check CI status and view CI job logs directly within the PR review chat.

**Pin Sessions**

Pin important sessions from the three-dot menu for quick access.

**Organization Terminology**

All “team” references updated to “organization” across the product. No functional change.

**Improved Questions UI**

Navigation between questions, inline “Something else” input, cleaner design.

**Auto-Skip Pending Questions**

Devin auto-skips pending questions when you send a new message.

**Cleaner File Paths**

Relative paths with structured format instead of full absolute paths.

**PR Review Polish**

Sticky tabs, bug navigation, copy buttons, chat CTA at end of diffs, empty state for PRs without descriptions.

**Structured Output for Child Sessions**

Child sessions can return structured JSON via schema for automated workflows.

**Smarter Codebase Search**

Recency-based repository ordering for faster, more accurate results.

**/new Slash Command**

Alias for /clear to start a fresh conversation.

**Azure DevOps Service Principal**

Connect Azure DevOps via service principal instead of personal OAuth.

**Linear Assignee Filter**

Rich picker for Linear assignee filtering in automations.

**Linear Token Refresh**

Linear connections now auto-refresh OAuth tokens, preventing disconnection on expiry.

**Minor Bug Fixes and Improvements**

GitLab PAT rotation fix, responsive mobile layouts, startup command display improvements, build log scroll-to-bottom, Ctrl+O expand hint, shell security improvements, automations UI fixes.April 1, 2026

**PR Resuming**

Devin can now take over and work on existing pull requests that weren’t created in the current session, enabling continuation of work across sessions.

**Devin Review Improvements**

Added a “lines left to review” counter in the PR review diff viewer, and significantly faster page load times via parallel queries.

**Streaming Terminals**

Terminal output in the session view now streams in real time.

**Connected Accounts Pagination**

GitHub and GitLab connected accounts pages now support pagination and search for organizations with many connections.

**GHES Improvements**

Support for org-level GitHub App registration on GitHub Enterprise Server, with pre-filled app name in the manifest flow.

**Settings Page Redesign**

Multiple settings pages (Schedules, Playbooks, Knowledge, Secrets) have been redesigned with a new unified layout, along with consolidated dialog styles across the product.

**Sticky Sidebar Headers**

Sidebar section headers now stick to the top while scrolling for easier navigation.

**Light Mode Polish**

Multiple fixes for theme-aware colors across modals, dialogs, and components.

**Add or Create Team**

New button in the account dropdown to create a team without going through the GitHub integration flow.

**Auto-open Agents Tab**

The Agents tab auto-opens when child sessions are detected.

**Tab Title Simplification**

Browser tab title simplified to “Devin” with contextual page titles.

**Slack Thread Permissions**

Users without Devin accounts are now blocked from messaging in Devin Slack threads.

**Improved PR Comment Formatting**

Devin’s PR comments now include line info and outside-diff context.

**IME Composition Fix**

Fixed an issue where pressing Enter during IME composition (e.g., Japanese input) in Safari would prematurely submit text.

**Ignore Comment Info**

More helpful information shown when Devin Review comments are ignored.

**Environment Setup Cleanup**

Clarified environment description copy and removed redundant buttons.

**Bash Syntax Highlighting**

Terminal output now has syntax highlighting for bash commands.

**Scheduled Session Pill**

Visual indicator for scheduled sessions in the sessions list.

**Minor bug fixes and improvements**

Various bug fixes, performance improvements, and visual polish across the platform.March 27, 2026

**Preview Agent Toggle**

A new “Preview upcoming features” toggle is available in the agent selector, enabling streaming thoughts and faster execution. Stability may be limited as these features are still in development.

**Inline File Previews**

HTML, PDF, and SVG attachments can now be securely rendered inline in the session sidebar, with a code/render toggle and download button in the file toolbar.

**Focus Mode**

A new focus mode hides the sidebar, header, and right panel for a distraction-free chat experience. Access it from the session menu or with the keyboard shortcut Cmd+Shift+F.

**Agents Tab for Child Sessions**

A new “Agents” tab automatically appears when a session creates child sessions, showing their status, todos, and PRs in one place.

![](https://mintcdn.com/cognitionai/RTcVGIV5Ij1tsiWg/images/release-notes/agents_tab_mar27.png?w=2500&fit=max&auto=format&n=RTcVGIV5Ij1tsiWg&q=85&s=99b54a7a265e91ec15ea86facfc9cb3d)

**Test Recording Viewer**

Devin’s test recordings now display as rich cards with pass/fail summaries, playback speed controls, and loop functionality.

**Jira Integration Enhancements**

Jira now supports direct session creation from issues, service account connections, and per-project trigger options for controlling when Devin is activated.

**Redesigned Integration Settings**

The Linear, Jira, and Slack integration settings pages have been redesigned with cleaner layouts for team mapping, playbook management, bot allowlists, and automation rules.

**Minor bug fixes and improvements**

Various bug fixes and performance improvements across the platform.March 24, 2026

**Light Mode (Beta)**

Devin now supports a light mode theme. You can switch between dark, light, and system themes from your profile settings.

![](https://mintcdn.com/cognitionai/IKMeVQNNTefx1Aj_/images/release-notes/light_mode_mar24.png?w=2500&fit=max&auto=format&n=IKMeVQNNTefx1Aj_&q=85&s=967adb4a7aefcd8e9600245a84e10ffc)

**Streaming Shell Output in Worklog**

Background shell process output now streams inline within worklog items, so you can monitor long-running processes without switching to the terminal.

**Cookie JSON Builder for Secrets**

A new tabbed interface for cookie secrets lets users paste raw JSON (auto-encoded to base64) with validation, parsed previews, and expiration warnings.

**Org-Level Metrics API**

New organization-scoped API endpoints for metrics and consumption data.

**Session Insights UI Redesign**

The session insights modal has been redesigned with a refreshed layout, improved empty states, and updated copy.

**Secrets on Initial Prompt**

Users can now attach secrets when creating a new session from the home page, matching existing functionality for follow-up messages.

**Devin Reviews Analytics**

A new Devin Reviews section has been added to the usage analytics page showing review metrics.

**Minor bug fixes and improvements**

Various bug fixes and performance improvements across the platform.March 19, 2026

**Devin Manages Devins**

Devin can now orchestrate Devins and manage your Devin setup directly from any session. This will replace the current Advanced Devin features.

Devin can delegate to a team of managed Devins that work in parallel. Each managed Devin is a full Devin with its own isolated virtual machine. The main Devin session acts as a coordinator — scoping the work, monitoring progress, resolving conflicts, and compiling the results.

New capabilities include:

- Session management – Create child sessions with structured output schemas and playbooks. Search and filter past sessions by tags, playbook, origin, or time range. Analyze past sessions with full search across shell, file, browser, git, and MCP activity.
- Knowledge management – Create, update, delete, and organize knowledge notes into folders. Review knowledge suggestions.
- Playbook management – Create, edit, and delete playbooks.
- Schedule management – Create and manage scheduled sessions including recurring or one-time runs, agent selection, and notification preferences.
![](https://mintcdn.com/cognitionai/LlJfDoruQJVIwKYo/images/release-notes/devin_manages_devins_mar19.png?w=2500&fit=max&auto=format&n=LlJfDoruQJVIwKYo&q=85&s=af5e1b5352ba27ed53b7dc553e9f9722)

**Redesigned Integration Pages**

The integration settings pages have been redesigned with a new layout including connection cards, support sections, and pagination.

**Improved Playbook Page**

The playbooks page now shows a table layout. Each playbook page now shows session count, unique users, and merged PRs per playbook, with a weekly activity chart. Playbooks now include a version history.

**Parent/Child Session Grouping**

Parent and child sessions are now grouped together in the sidebar, so child sessions stay nested under their parent regardless of sorting or filtering.

**Minor bug fixes and improvements**

Various bug fixes and performance improvements across the platform.March 13, 2026

**On-Demand Session Insights**

Session insights are now generated on demand rather than automatically. You can trigger analysis from the Session Insights button in the UI or programmatically via the new [generate insights API endpoint](https://cognitionai.mintlify.app/api-reference/v3/sessions/post-organizations-session-insights-generate).

**New Session Inputs**

- An inline voice recording button is now available for hands-free messaging.
- Devin sessions can be @ mentioned to reference them directly in another session.

**Session List Improvements**

- Important sessions can be pinned to the top of the sidebar for quick access.
- A new sidebar filter hides scheduled sessions from the session list.

**Structured Output Modal**

The structured output from sessions created with the API with this parameter set can now be viewed and downloaded from the “Structured output” option in the session menu.

**Markdown Preview**

Markdown files can now be natively displayed in the right panel.

![](https://mintcdn.com/cognitionai/6rLe9xqH8tl30kzu/images/release-notes/markdown_preview_mar13.png?w=2500&fit=max&auto=format&n=6rLe9xqH8tl30kzu&q=85&s=e4f0527c7bbfbf1257b3e56719115676)March 11, 2026

**Datadog MCP Integration**

Datadog is now available as an official integration in the MCP marketplace.

**Default Branch Management**

Users can set and manage the default branch for repository indexing from the repositories management page.

**Schedule: Run as User**

Schedules can now be reassigned to run as the current user via a “Run as me” button in the schedule detail view, also available via the v3 API.

**IdP Groups in Enterprise Settings**

The enterprise members table now shows IdP group memberships for each user.

**Minor bug fixes and improvements**

Various bug fixes, performance improvements, and visual polish across the platform.March 7, 2026

**Install Devin as an App**

Devin can now be installed as a Progressive Web App on desktop and mobile. On Chrome or Edge, open app.devin.ai and click the install icon in the address bar (or Menu → Install Devin); on iOS Safari, tap Share → Add to Home Screen. Once installed, Devin links open directly in the app.

![](https://mintcdn.com/cognitionai/KW9HnR-CzYk_OnFB/images/release-notes/pwa_install_mar7.png?w=2500&fit=max&auto=format&n=KW9HnR-CzYk_OnFB&q=85&s=0a2dc244684ec95671521862a8778407)

**Session Status in Browser Tab**

The browser tab favicon now shows a colored status dot on session pages (green when Devin is working, orange when it’s waiting for you) so you can spot sessions that need attention without switching tabs.

**Minor bug fixes and improvements**

Various bug fixes, performance improvements, and visual polish across the platform.February 27, 2026

**AskDevin Upgrade**

Expanded to support Ask and Plan modes. Now has more advanced code search capabilities which produce more detailed and accurate answers. The status of Devin sessions created from AskDevin can now be seen in the conversation.

![](https://mintcdn.com/cognitionai/_dRQes3XKFhFT5iT/images/release-notes/askdevin_modes_feb27.png?w=2500&fit=max&auto=format&n=_dRQes3XKFhFT5iT&q=85&s=70d1743afb59995ece548b71162b9001)

**Devin Review: GitHub Commit Status Checks**

Status checks now displayed directly on pull request commits, giving visibility into review progress without leaving GitHub. The status links to the full Devin Review analysis.

To enable this, the Devin GitHub App will request the Commit Statuses and Checks permissions. If these permissions are not granted, all existing functionality is unaffected.

**Repository Selection for Schedules**

Schedules can now be configured with specific repositories that the session will be run with each time the schedule executes.February 24, 2026

**Devin 2.2 Launch**

Devin 2.2 is the culmination of hundreds of improvements both big and small over the last few weeks including:

- 3x faster startup time to immediately see Devin’s output and build trust that it’s on the right track
- A new UI that connects every step of the dev lifecycle: start sessions from anywhere, review agent output directly in Devin, and jump back into sessions from code review.
- Smoother and faster Slack and Linear integrations to start sessions without having to switch context

See past release notes for the full list of the improvements.

**Full Desktop Testing**

Devin now supports end-to-end testing using computer use and can test any desktop app that can run on Linux. Devin will request to QA its PR, if you approve it, it will run your app, use its desktop to click around, and send you an edited recording of the testing for your review.

Existing users can enable Desktop mode in [Settings > Customization](https://app.devin.ai/customization).

<video controls="" src="https://mintcdn.com/cognitionai/h8qwUI43QqmV5C_j/images/release-notes/desktop_testing_feb25.mp4?fit=max&amp;auto=format&amp;n=h8qwUI43QqmV5C_j&amp;q=85&amp;s=d1b61b1bbc16fe6d9777a5cb5e1d48e8"></video>February 20, 2026

**Devin v3 API Officially Released**

The v3 API is coming out of beta and is now the primary API for all Devin functionality. The new API provides all of the legacy API functionality and additionally provides role-based access control, session attribution, and new capabilities.

The legacy APIs (v1 and v2) will be deprecated in the future. The exact date will be announced in the product and in release notes. We commit to providing at least 30 days notice. During the deprecation period, the legacy APIs will continue to work but all new features will only be available in the v3 API.

**Sessions List Redesign**

The sessions list page has been redesigned with an updated layout featuring inline PR previews, message snippets, and status indicators. Sessions can now also be sorted by creation date.

![](https://mintcdn.com/cognitionai/giTocETit1KrE1tc/images/release-notes/sessions_list_redesign_feb20.png?w=2500&fit=max&auto=format&n=giTocETit1KrE1tc&q=85&s=e1b02cc937083050d117e87d9cf1dff2)

**Merge Conflict Detection**

Devin will automatically notify users when a PR created in a Devin session has merge conflicts. Available on GitHub.com only.

**New Devin Scheduling Options**

Scheduled Devins can now be created as a one-time scheduled event, and existing schedules can be triggered on demand with the “Run now” button.

**Devin Review for GitHub Enterprise Server**

Devin Review now supports GitHub Enterprise Server (GHES) repositories. You can view PR diffs, run analysis, and use the Devin Review chat agent to propose and apply code changes. Some interactions with GitHub such as posting comments, submitting reviews, and merging are not yet supported on GHES.

**Repo Selector Enhancements**

The repository selector now features an “Only” button to quickly isolate a single repository and displays setup and indexed repo counts.

![](https://mintcdn.com/cognitionai/giTocETit1KrE1tc/images/release-notes/repo_selector_feb20.png?w=2500&fit=max&auto=format&n=giTocETit1KrE1tc&q=85&s=bb53d8925ff53ee4e62a57adfaa7cd56)

**Session Messages API**

A new `GET /messages` endpoint allows programmatic access to session message history.

**Minor bug fixes and improvements**

Various bug fixes and performance improvements across the platform.February 13, 2026

**Visual Refresh and Polish**

The overall design has been improved and polished across the product. Some button locations have been minorly adjusted, but these changes do not impact the product functionality.

![](https://mintcdn.com/cognitionai/eb79m3k_19Q1Z7JT/images/release-notes/visual_refresh_feb13.png?w=2500&fit=max&auto=format&n=eb79m3k_19Q1Z7JT&q=85&s=47f5bfedee70dc389d2910d93b483006)

**Devin Fast Mode**

A new “Fast Mode” option is now available in the agent picker, delivering ~2x faster responses with the same intelligence at 4x ACU per session.

**Devin Review: Batch Comments**

When replying to PR review threads, you can now check “Start a review” to batch multiple review comments before submitting them all at once.

**Devin Review: Code Changes from Chat**

The Devin Review chat agent can now propose code edits directly in the conversation. You can review the suggested changes, then apply them as a commit to the PR branch without leaving Devin Review.

![](https://mintcdn.com/cognitionai/eb79m3k_19Q1Z7JT/images/release-notes/devin_review_code_changes_feb13.png?w=2500&fit=max&auto=format&n=eb79m3k_19Q1Z7JT&q=85&s=1968a55c660c15e2a501d271e62f0175)

**Secure Mode for All Organizations**

Secure mode is now available for non-enterprise organizations. When enabled, Devin loses native internet deployment capabilities. You can find this setting under “Security settings” on the Customization page.

**Skills Support**

Devin now recognizes and uses skills defined in your codebase. Skills provide reusable instructions that Devin can activate, search, and invoke during sessions to follow your team’s preferred workflows.

**Settings Search**

A search bar has been added to the settings sidebar, making it easy to quickly find any settings page by name or keyword.

**Minor bug fixes and improvements**

Various bug fixes and performance improvements across the platform.February 6, 2026

**Schedule from the Input Box**

You can now quickly create a scheduled Devin session directly from the input box. Use the “Schedule Devin” option in the context menu or switch to the “Create schedule” tab in Advanced mode to set up recurring sessions without leaving the home page.

![](https://mintcdn.com/cognitionai/5kC7KOFG99QiDpzy/images/release-notes/schedule_tab_feb6.png?w=2500&fit=max&auto=format&n=5kC7KOFG99QiDpzy&q=85&s=878e1e9b0985826941dae3c252b88702)

**Enterprise Organization Selection**

The enterprise landing page has been redesigned with a cleaner organization list, member counts, and sorting options for easier navigation across your enterprise.

**Devin Review: Auto-Review Settings**

Auto-review configuration is now accessible as a settings popover directly in the PR header, making it faster to enable or disable auto-reviews per repository.

**Devin Review: Hide Comment Highlights**

A new setting in the code diff viewer lets you hide comment highlight boxes for a cleaner reading experience when reviewing code.

**Git Permissions Update**

Removed the ability to index repos in the primary organization for enterprises.

**Minor bug fixes and improvements**

Various bug fixes and performance improvements across the platform.

---

## All Release Notes

- [2026 Release Notes](https://cognitionai.mintlify.app/release-notes/2026)
- [2025 Release Notes](https://cognitionai.mintlify.app/release-notes/2025)
- [2024 Release Notes](https://cognitionai.mintlify.app/release-notes/2024)

[2026](https://cognitionai.mintlify.app/release-notes/2026)