---
title: "Today's PHP Security Release, and How We're Strengthening PHP Security"
aliases: ["PHP Foundation October Security Release"]
tags: [sources, cybersecurity, verification]
source_type: "article"
status: "verified"
evidence_class: "maintainer-incident-account"
publication_date: "2026-10-21"
publication_date_basis: "dated_primary_page"
source_version: "page_retrieved_2026-11-09"
authors: ["The PHP Foundation"]
venue: "The PHP Foundation"
url: "https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/"
created: 2026-11-09
updated: 2026-11-09
---

# PHP Foundation October Security Release

## Evidence

PHP released fixes for CVE-2026-109618 and CVE-2026-109619 on October 21 in 8.2.35, 8.3.36, 8.4.27, and 8.5.12. The first issue's underlying out-of-memory problem was recognized in 2024, without a concrete exploitation path. Calif reported demonstrated remote code execution on August 11, 2026; other researchers supplied additional paths. October is the release date, not the discovery date.

Compatibility, performance, extension changes, scarce expertise, and a consensus decision process delayed remediation. The Foundation describes this as structural failure. AI assists reproduction and grouping reports, while humans decide and patch. Since July 1, the team had published 15 CVEs and handled over 100 invalid, duplicate, or unreproducible reports; those categories are not a measured AI false-positive rate.

## Boundaries

The release moved forward from October 22 following leaked identifiers; a demonstration video and early distributor images further disrupted coordination. This maintainer account establishes validated exploitability and shipped fixes, not the prevalence of successful attacks. Deployment conditions affect exploitability.

## Connections

- [[sources/Calif PHP2Shell Research]]
- [[sources/Wiz PHP2Shell Research]]
- [[concepts/code factories]]

[Primary account](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/).
