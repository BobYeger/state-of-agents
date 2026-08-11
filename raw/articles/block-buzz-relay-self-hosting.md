# Run your own Buzz relay — structured capture

- Canonical URL: https://engineering.block.xyz/blog/run-your-own-buzz-relay
- Author: Kalvin Chau
- Publisher: Block Engineering
- Publication date: 2026-07-31
- Captured: 2026-08-02
- Extraction: Defuddle CLI with Markdown output
- Capture mode: metadata, structure, and operational facts; not a verbatim republication

## Deployment Shape

- One Rust process serves the WebSocket relay, REST API, and web UI.
- PostgreSQL, Redis, and an S3-compatible object store are required dependencies.
- The published paths include Docker Compose, a Railway template, and a generic VPS deployment with optional Caddy termination.

## Identity and Migration Consequences

- The relay identity and owner identity are Nostr keypairs, not ordinary passwords.
- Rotating the relay signing key changes the identity clients pin and means earlier relay-signed material no longer verifies against the new advertised key.
- Community selection is host-derived, including any explicit port. Changing the host or port can therefore select a new empty community rather than migrate the old one.
- Exact scheme/host/port matching is separately required for NIP-98 authentication, so a scheme mismatch can fail authentication even when it does not select another community.
- The backup set includes the relay key, owner key, PostgreSQL, object storage, and the Git volume.

## Operational Boundary

- Self-hostable does not mean peer-to-peer or dependency-free. The current community runtime is a centrally administered relay backed by conventional stateful services.
- Relay-key rotation and host/scheme/port changes have distinct identity, authentication, and migration consequences that must be planned before onboarding members or durable data.
- Hosted deployment may place the relay key in a provider variable store; operators must copy and protect it themselves.
