Title: The age of agents: cryptographically recognizing agent traffic

URL Source: https://blog.cloudflare.com/signed-agents/

Published Time: 2025-08-28T14:00+00:00

Markdown Content:
2025-08-28

6 min read

![Image 1](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/5ymXU3Ub2reFnHjtEddext/c64f8f46cb0f1eaeb0fa597c1a273c6b/BLOG-2930_1.png)

On the surface, the goal of handling bot traffic is clear: keep malicious bots away, while letting through the helpful ones. Some bots are evidently malicious — such as mass price scrapers or those testing stolen credit cards. Others are helpful, like the bots that index your website. Cloudflare has segmented this second category of helpful bot traffic through our [verified bots](https://developers.cloudflare.com/bots/concepts/bot/#verified-bots) program, [vetting](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/policy/) and validating bots that are transparent about who they are and what they do.

Today, the rise of [agents](https://agents.cloudflare.com/) has transformed how we interact with the Internet, often blurring the distinctions between benign and malicious bot actors. Bots are no longer directed only by the bot owners, but also by individual end users to act on their behalf. These bots directed by end users are often working in ways that website owners want to allow, such as planning a trip, ordering food, or making a purchase.

Our customers have asked us for easier, more granular ways to ensure specific [bots](https://www.cloudflare.com/learning/bots/what-is-a-bot/), [crawlers](https://www.cloudflare.com/learning/bots/what-is-a-web-crawler/), and [agents](https://www.cloudflare.com/learning/ai/what-is-agentic-ai/) can reach their websites, while continuing to block bad actors. That’s why we’re excited to introduce **signed agents**, an extension of our verified bots program that gives a new bot classification in our security rules and in Radar. Cloudflare has long recognized agents — but we’re now endowing them with their own classification to make it even easier for our customers to set the traffic lanes they want for their website.

## The age of agents

Cloudflare has continuously expanded our verified bot categorization to include different functions as the market has evolved. For instance, we first announced our grouping of [AI crawler traffic as an official bot category](https://blog.cloudflare.com/ai-bots/) in 2023. And in 2024, when OpenAI announced a [new AI search prototype](https://openai.com/index/searchgpt-prototype/) and introduced [three different bots](https://platform.openai.com/docs/bots) with distinct purposes, we [added three new categories](https://blog.cloudflare.com/cloudflare-ai-audit-control-ai-content-crawlers/) to account for this innovation: AI Search, AI Assistant, and Archiver.

But the bot landscape is constantly evolving. Let's unpack a common type of verified AI bot — an AI crawler such as [GPTBot](https://radar.cloudflare.com/bots/directory/gptbot). Even though the bot performs an array of tasks, the bot’s ultimate purpose is a singular, repetitive task on behalf of the operator of that bot: fetch and index information. Its intelligence is applied to performing that singular job on behalf of that bot owner.

Agents, though, are different. Think about an AI agent tasked by a user to "Book the best deal for a round-trip flight to New York City next month." These agents sometimes use remote browsing products like Cloudflare's [Browser Rendering](https://developers.cloudflare.com/browser-rendering/) and similar products from companies like Browserbase and Anchor Browser. And here is the key distinction: this particular type of bot isn’t operating on behalf of a single company, like OpenAI in the prior example, but rather the end users themselves.

## Introducing signed agents

In May, we announced Web Bot Auth, a new method of [using cryptography to verify bot and agent traffic](https://blog.cloudflare.com/web-bot-auth/). HTTP message signatures allow bots to authenticate themselves and allow customer origins to identify them. This is one of the authentication methods we use today for our verified bots program.

What, exactly, is a [signed agent](https://developers.cloudflare.com/bots/concepts/bot/signed-agents/)? First, they are agents that are generally directed by an end user instead of a single company or entity. Second, the infrastructure or remote browsing platform the agents use is signing their HTTP requests via Web Both Auth, with Cloudflare validating these message signatures. And last, they comply with our [signed agent policy](https://developers.cloudflare.com/bots/concepts/bot/signed-agents/policy/).

The signed agents classification improves on our existing frameworks in a couple of ways:

1.   **Increased precision and visibility:** we’ve updated the _Cloudflare bots and agents directory to include signed agents_ in addition to verified bots. This allows us to verify the cryptographic signatures of a much wider set of automated traffic, and our customers to granularly apply their security preferences more easily. Bot operators can now _submit signed agent applications from the Cloudflare dashboard_, allowing bot owners to specify to us how they think we should segment their automated traffic.

2.   **Easier controls from security rules**: similar to how they can take action on verified bots as a group, our Enterprise customers will be able to take action on _signed agents as a group when configuring their security rules_. This new field will be available in the Cloudflare dashboard under security rules soon.

To apply to have an agent added to Cloudflare’s directory of bots and agents, customers should complete the [Bot Submission Form](https://dash.cloudflare.com/?to=/:account/configurations/bot-submission-form) in the Cloudflare dashboard. Here, they can specify whether the submission should be considered for the signed agents list or the verified bots list. All signed agents will be recognized by their cryptographic signatures through [Web Bot Auth validation](https://datatracker.ietf.org/doc/html/draft-meunier-web-bot-auth-architecture).

![Image 2: BLOG-2930 2](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/5caeGdhlmI3dO3GNZKeEUg/0dac239a94732404861b3876f6bdb8b6/BLOG-2930_2.png)
The Bot Submission Form, available in the Cloudflare dashboard for bot owners to submit both verified bot and signed agent applications.

We want to be clear: our verified bots program isn’t going anywhere. In fact, well-behaved and transparent applications that make use of signed agents can further qualify to be a verified bot, if their specific service adheres to our [policy](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/policy/). For instance,[Cloudflare Radar's URL Scanner](https://radar.cloudflare.com/scan), which relies on Browser Rendering as a service to scan URLs, is a [verified bot](https://radar.cloudflare.com/bots/directory/cloudflare-radar-url-scanner). While Browser Rendering itself does not qualify to be a verified bot, URL Scanner does, since the bot owner (in this case, Cloudflare Radar) directs the traffic sent by the bot and always identifies itself with a unique Web Bot Auth signature — distinct from [Browser Rendering’s signature](https://developers.cloudflare.com/browser-rendering/reference/automatic-request-headers/).

## From an agent’s perspective…

Since the launch of Web Bot Auth, our own Browser Rendering product has been sending signed Web Bot Auth HTTP headers, and is always given a bot score of 1 for our Bot Management customers. As of today, Browser Rendering will now show up in this new signed agent category.

![Image 3: BLOG-2930 3](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/1F8Z0E6WqJTxLf9G3PLB3a/84e80539be402066fe02ab60c431100a/BLOG-2930_3.png)
We’re also excited to announce the first cohort of agents that we’re partnering with and will be classifying as signed agents: [ChatGPT agent](https://openai.com/index/introducing-chatgpt-agent/), [Goose](https://block.xyz/inside/block-open-source-introduces-codename-goose) from Block, [Browserbase](https://docs.browserbase.com/introduction/what-is-browserbase), and [Anchor Browser](https://anchorbrowser.io/). They are perfect examples of this new classification because their remote browsers are used by their end customers, not necessarily the companies themselves. We’re thrilled to partner with these teams to take this critical step for the AI ecosystem:

> “_When we built Goose as an open source tool, we designed it to run locally with an extensible architecture that lets developers automate complex workflows. As Goose has evolved to interact with external services and third-party sites on users' behalf, Web Bot Auth enables those sites to trust Goose while preserving what makes it unique._**_This authentication breakthrough unlocks entirely new possibilities for autonomous agents_**." – **Douwe Osinga**, Staff Software Engineer, Block

> _"At Browserbase, we provide web browsing capabilities for some of the largest AI applications. We're excited to partner with Cloudflare to support the adoption of Web Bot Auth, a critical layer of identity for agents._**_For AI to thrive, agents need reliable, responsible web access._**_"_ – **Paul Klein**, CEO, Browserbase

> _“Anchor Browser has partnered with Cloudflare to let developers ship verified browser agents. This way_**_trustworthy bots get reliable access while sites stay protected_**_.”_ – **Idan Raman**, CEO, Anchor Browser

## Updated visibility on Radar

We want everyone to be in the know about our bot classifications. Cloudflare began publishing verified bots on our Radar page [back in 2022](https://radar.cloudflare.com/bots#verified-bots), meaning anyone on the Internet — Cloudflare customer or not — can see all of our [verified bots on Radar](https://radar.cloudflare.com/bots#verified-bots). We dynamically update the list of bots, but show more than just a list: we announced on [Content Independence Day](https://www.cloudflare.com/en-gb/press-releases/2025/cloudflare-just-changed-how-ai-crawlers-scrape-the-internet-at-large/) that [every verified bot would get its own page](https://blog.cloudflare.com/ai-search-crawl-refer-ratio-on-radar/#one-more-thing) in our public-facing directory on Radar, which includes the traffic patterns that we see for each bot.

Our directory has been updated to include [**both signed agents and verified bots**](https://radar.cloudflare.com/bots/directory) — we share exactly how Cloudflare classifies the bots that it recognizes, plus we surface all of the traffic that Cloudflare observes from these many recognized agents and bots. Through this updated directory, we’re not only giving better visibility to our customers, but also striving to set a higher standard for transparency of bot traffic on the Internet.

![Image 4: BLOG-2930 4](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/65QPFjmbBde3EzHTOwElSL/cccc8f23c37716c251e0c21850855265/BLOG-2930_4.png)
Cloudflare Radar’s Bots Directory, which lists verified bots and signed agents. This view is filtered to view only agent entries.

![Image 5: BLOG-2930 5](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/2wBz7UwrQQzT7rJJnXiF8C/16eed3f1afd95cac32c4bcb647c6e5e6/BLOG-2930_5.png)
Cloudflare Radar’s signed agent page for ChatGPT agent, which includes its traffic patterns for the last 7 days, from August 21, 2025 to August 27, 2025.

## What’s now, what’s next

As of today, the Cloudflare bot directory supports both bots and agents in a more clear-cut way, and customers or agent creators can submit agents to be signed and recognized [through their account dashboard](https://dash.cloudflare.com/?to=/:account/configurations/bot-submission-form). In addition, anyone can see our signed agents and their traffic patterns on Radar. Soon, customers will be able to take action on signed agents as a group within their firewall rules, the same way you can take action on our verified bots.

Agents are changing the way that humans interact with the Internet. Websites need to know what tools are interacting with them, and for the builders of those tools to be able to easily scale. Message signatures help achieve both of these goals, but this is only step one. Cloudflare will continue to make it easier for agents and websites to interact (or not!) at scale, in a seamless way.

[AI Week](https://blog.cloudflare.com/tag/ai-week/)[AI](https://blog.cloudflare.com/tag/ai/)[Bots](https://blog.cloudflare.com/tag/bots/)[AI Bots](https://blog.cloudflare.com/tag/ai-bots/)[Bot Management](https://blog.cloudflare.com/tag/bot-management/)[Security](https://blog.cloudflare.com/tag/security/)

Related posts

July 01, 2026

## [Making AI search smarter](https://blog.cloudflare.com/making-ai-search-smarter/)
Search is how we find nearly everything on the web — creators, merchants, answers. AI is rewriting the rules, leaving creators caught between staying discoverable in an agentic era and getting paid for their work. Today we're launching two initiatives to help....

By

July 01, 2026

## [Your site, your rules: new AI traffic options for all customers](https://blog.cloudflare.com/content-independence-day-ai-options/)
For our second Content Independence Day, we’re giving website owners finer options to manage AI traffic. Instead of a one-size-fits-all block, all customers can now easily distinguish and manage Search, Agent, and Training bots, alongside the new ability to protect ad-monetized pages....

By

July 01, 2026

## [Content Independence Day, one year on: building the business model for the agentic Internet](https://blog.cloudflare.com/agentic-internet-bot-report/)
One year after declaring Content Independence Day, a dynamic market for monetized content has officially emerged. In this report, we examine how the rise of autonomous AI agents is upending traditional search referrals and detail the new infrastructure required to support a sustainable web economy. ...

By

July 01, 2026

## [Announcing the Monetization Gateway: charge for any resource behind Cloudflare via x402](https://blog.cloudflare.com/monetization-gateway/)
We're opening the waitlist for our Monetization Gateway, which will allow you to charge for any web page, dataset, API, or MCP tool behind Cloudflare. The charges will settle in stablecoins over the x402 open protocol, with no payments stack of your own to build....

By
