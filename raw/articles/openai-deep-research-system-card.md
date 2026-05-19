Title: Deep research System Card

URL Source: https://openai.com/index/deep-research-system-card/

Markdown Content:
# Deep research System Card | OpenAI

[Skip to main content](https://openai.com/index/deep-research-system-card/#main)

*   [Research](https://openai.com/research/index/)
*   Products
*   [Business](https://openai.com/business/)
*   [Developers](https://openai.com/api/)
*   [Company](https://openai.com/about/)
*   [Foundation(opens in a new window)](https://openaifoundation.org/)

Log in[Try ChatGPT(opens in a new window)](https://chatgpt.com/?openaicom-did=e2c323d9-b0ce-4eaf-a763-58ff070aaae8&openaicom_referred=true)

*   Research
*   Products
*   Business
*   Developers
*   Company
*   [Foundation(opens in a new window)](https://openaifoundation.org/)

Deep research System Card | OpenAI

February 25, 2025

[Safety](https://openai.com/news/safety-alignment/)[Publication](https://openai.com/research/index/publication/)

# Deep research System Card

This report outlines the safety work carried out prior to releasing deep research including external red teaming, frontier risk evaluations according to our Preparedness Framework, and an overview of the mitigations we built in to address key risk areas.

[Read the system card(opens in a new window)](https://deploymentsafety.openai.com/deep-research)[Contributions(opens in a new window)](https://openai.com/index/introducing-deep-research)

Share

## Deep research system card

Specific areas of risk

*   Prompt injections 
*   Disallowed content 
*   Privacy 
*   Ability to run code 
*   Bias 
*    Hallucinations 

Preparedness Scorecard

*   CBRN

Medium

*   Cybersecurity

Medium

*   Persuasion

Medium

*   Model autonomy

Medium

## Scorecard ratings

*   Low
*   Medium
*   High
*   Critical

Only models with a post-mitigation score of "medium" or below can be deployed.

Only models with a post-mitigation score of "high" or below can be developed further.

## Introduction

Deep research is a new agentic capability that conducts multi-step research on the internet for complex tasks. The deep research model is powered by an early version of OpenAI o3 that is optimized for web browsing. Deep research leverages reasoning to search, interpret, and analyze massive amounts of text, images, and PDFs on the internet, pivoting as needed in reaction to information it encounters. It can also read files provided by the user and analyze data by writing and executing python code. We believe deep research will be useful to people across a wide range of situations.

Before launching deep research and making it available to our Pro users, we conducted rigorous safety testing, Preparedness evaluations and governance reviews. We also ran additional safety testing to better understand incremental risks associated with deep research's ability to browse the web, and added new mitigations. Key areas of new work included strengthening privacy protections around personal information that is published online, and training the model to resist malicious instructions that it may come across while searching the Internet.

At the same time, our testing on deep research also surfaced opportunities to further improve our testing methods. We took the time before broadening the release of deep research to conduct further human probing and automated testing for select risks.

Building on OpenAI’s established safety practices and Preparedness Framework, this system card provides more details on how we built deep research, learned about its capabilities and risks, and improved safety prior to launch.

*   [System Cards](https://openai.com/news/?tags=system-cards)

## Authors

OpenAI

Our Research
*   [Research Index](https://openai.com/research/index/)
*   [Research Overview](https://openai.com/research/)
*   [Research Residency](https://openai.com/residency/)
*   [Economic Research](https://openai.com/signals/)

Latest Advancements
*   [GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)
*   [GPT-5.4](https://openai.com/index/introducing-gpt-5-4/)
*   [GPT-5.3 Instant](https://openai.com/index/gpt-5-3-instant/)
*   [GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-3-codex/)

Safety
*   [Safety Approach](https://openai.com/safety/)
*   [Security & Privacy](https://openai.com/security-and-privacy/)
*   [Trust & Transparency](https://openai.com/trust-and-transparency/)

ChatGPT
*   [Explore ChatGPT(opens in a new window)](https://chatgpt.com/overview?openaicom-did=e2c323d9-b0ce-4eaf-a763-58ff070aaae8&openaicom_referred=true)
*   [Business](https://chatgpt.com/business/business-plan?openaicom-did=e2c323d9-b0ce-4eaf-a763-58ff070aaae8&openaicom_referred=true)
*   [Enterprise](https://chatgpt.com/business/enterprise?openaicom-did=e2c323d9-b0ce-4eaf-a763-58ff070aaae8&openaicom_referred=true)
*   [Education](https://chatgpt.com/business/education?openaicom-did=e2c323d9-b0ce-4eaf-a763-58ff070aaae8&openaicom_referred=true)
*   [Pricing(opens in a new window)](https://chatgpt.com/pricing?openaicom-did=e2c323d9-b0ce-4eaf-a763-58ff070aaae8&openaicom_referred=true)
*   [Download(opens in a new window)](https://chatgpt.com/download?openaicom-did=e2c323d9-b0ce-4eaf-a763-58ff070aaae8&openaicom_referred=true)

API Platform
*   [Platform Overview](https://openai.com/api/)
*   [Pricing](https://openai.com/api/pricing/)
*   [API log in(opens in a new window)](https://platform.openai.com/login)
*   [Documentation(opens in a new window)](https://developers.openai.com/api/docs)
*   [Developer Forum(opens in a new window)](https://community.openai.com/)

For Business
*   [Business Overview](https://openai.com/business/)
*   [Solutions](https://openai.com/solutions/)
*   [Contact Sales](https://openai.com/contact-sales/)

Company
*   [About Us](https://openai.com/about/)
*   [Our Charter](https://openai.com/charter/)
*   [Foundation(opens in a new window)](https://openaifoundation.org/)
*   [Careers](https://openai.com/careers/)
*   [Brand](https://openai.com/brand/)

Support
*   [Help Center(opens in a new window)](https://help.openai.com/)

More
*   [News](https://openai.com/news/)
*   [Stories](https://openai.com/stories/)
*   [Academy](https://openai.com/academy/)
*   [Livestreams](https://openai.com/live/)
*   [Podcast](https://openai.com/podcast/)
*   [RSS](https://openai.com/news/rss.xml)

Terms & Policies
*   [Terms of Use](https://openai.com/policies/terms-of-use/)
*   [Privacy Policy](https://openai.com/policies/privacy-policy/)
*   [Other Policies](https://openai.com/policies/)

[(opens in a new window)](https://x.com/OpenAI)[(opens in a new window)](https://www.youtube.com/OpenAI)[(opens in a new window)](https://www.linkedin.com/company/openai)[(opens in a new window)](https://github.com/openai)[(opens in a new window)](https://www.instagram.com/openai/)[(opens in a new window)](https://www.tiktok.com/@openai)[(opens in a new window)](https://discord.gg/openai)

OpenAI © 2015–2026 Your privacy choices

English United States
