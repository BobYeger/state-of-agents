# A Buzz on your phone — structured capture

- Canonical URL: https://engineering.block.xyz/blog/a-buzz-on-your-phone
- Author: Tom Brow
- Publisher: Block Engineering
- Publication date: 2026-07-29
- Captured: 2026-08-02
- Extraction: Defuddle CLI with Markdown output
- Capture mode: metadata, structure, and claim-level facts; not a verbatim republication

## Security-Relevant Facts

- The article says Buzz agents typically run on a human's computer, outside a sandbox, with `--dangerously-skip-permissions` enabled.
- This gives agents access to the machine's project instructions, skills, credentials, and ambient execution authority.
- Block therefore makes signed message origin the central direct-command boundary: an agent acts on messages signed by its owner's key rather than trusting the relay to identify the sender.
- The mobile client signs messages locally and connects directly to relays; it is not merely a remote-control client behind a trusted Block service.

## Privacy and Pairing

- Desktop-to-mobile pairing reuses the user's keypair through a QR-mediated flow.
- Block says the mobile clients ship without analytics SDKs at the time of publication and remove location metadata from image uploads.
- The draft NIP-PL push design separates knowledge across the relay, push gateway, and mobile push provider so no one intermediary receives the full identity/message/device mapping.
- Repository-side boundary: the checked-in NIP-PL models cover bounded lease-acceptance and gateway-authority transitions, not the not-yet-shipped relay matcher/worker or complete SQL/network behavior. Constant push payloads conceal content but not wake timing or frequency.

## Security Boundary

- Owner-signature checks address relay impersonation and unauthorized direct commands; they are not execution containment.
- They do not by themselves prevent indirect prompt injection in content the owner asks an agent to inspect, malicious instructions from an authorized but compromised endpoint, agent-key compromise, or abuse of ambient host credentials.
- The article is therefore a useful negative case: identity and input authorization cannot substitute for permissions, sandboxing, and egress controls.
- No independent mobile privacy or security audit is cited.
