---
title: "PHP2Shell: AI uncovers critical RCE vulnerabilities affecting 70% of the Internet"
aliases: ["Wiz PHP2Shell Research"]
tags: [sources, cybersecurity, verification]
source_type: "technical-report"
status: "verified"
evidence_class: "vendor-research-and-telemetry"
publication_date: "2026-10-21"
publication_date_basis: "dated_primary_page"
followup_date: "2026-10-27"
source_version: "pages_retrieved_2026-11-09"
authors: ["Sagi Tzadik", "Shir Tamari", "Nir Ohfeld", "Tomer Schwartz"]
venue: "Wiz Research"
url: "https://www.wiz.io/blog/php2shell-php-rce"
followup_url: "https://www.wiz.io/blog/php2shell-exploitation-so-far"
created: 2026-11-09
updated: 2026-11-09
---

# Wiz PHP2Shell Research

## Evidence

Wiz reports four exploitable bug instances grouped under two CVEs, with remote execution demonstrated on WordPress, Drupal, and Joomla test deployments, plus process-memory disclosure. Discovery began August 19; Drupal execution was confirmed August 20, WordPress August 21, and reports submitted August 24. Patches and disclosure followed October 21.

The workflow combined human researchers, Wiz Atlas, Gemini 4 Argon, and GPT-5.6 Sol. Claimed hours to adapt exploits and one researcher-week versus hypothetical team-months lack a controlled comparison, cost accounting, and model/harness ablations. The title's website-language prevalence is not a measured compromised or uniformly exploitable population.

## Subsequent Observation

The October 27 follow-up reports limited attempts with none completing in Wiz's captured telemetry. Observed exposed vulnerable machines declined approximately 67%; population/coverage changes and multiple remediation strategies prevent attributing this entirely to patching. Neither result establishes global attack prevalence or excludes successful attacks elsewhere.

## Connections

- [[sources/PHP Foundation October Security Release]]
- [[sources/Calif PHP2Shell Research]]
- [[sources/PHP2Shell Exploitation Observations]]

[Research disclosure](https://www.wiz.io/blog/php2shell-php-rce); [bounded telemetry follow-up](https://www.wiz.io/blog/php2shell-exploitation-so-far).
