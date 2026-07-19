#!/usr/bin/env python3
"""Validate talk-card metadata and local transcript integrity."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"

REQUIRED_KEYS = {
    "source_type",
    "status",
    "event_date",
    "youtube_upload_date",
    "medium",
    "platform",
    "video_id",
    "duration_seconds",
    "language",
    "transcript_status",
    "transcript_type",
    "transcript_language",
    "transcript_review_status",
    "transcript_storage",
    "evidence_class",
    "metrics_status",
}


def parse_scalar(value: str) -> str | None:
    value = value.strip()
    if value in {"", "null", "~"}:
        return None
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def frontmatter(path: Path) -> dict[str, str | None]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    match = re.search(r"\n---\n", text[4:])
    if not match:
        return {}
    block = text[4 : 4 + match.start()]
    data: dict[str, str | None] = {}
    for line in block.splitlines():
        if not line or line[0].isspace() or line.lstrip().startswith("#"):
            continue
        field = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", line)
        if field:
            data[field.group(1)] = parse_scalar(field.group(2) or "")
    return data


def validate(path: Path, data: dict[str, str | None], require_local: bool) -> list[str]:
    errors: list[str] = []
    missing = sorted(REQUIRED_KEYS - data.keys())
    if missing:
        errors.append(f"missing fields: {', '.join(missing)}")

    if data.get("platform") == "youtube" and not data.get("video_id"):
        errors.append("YouTube talk has no video_id")

    transcript_status = data.get("transcript_status")
    storage = data.get("transcript_storage")
    if transcript_status == "captured":
        for key in ("transcript_type", "transcript_language", "transcript_locator", "transcript_sha256"):
            if not data.get(key):
                errors.append(f"captured transcript has no {key}")
        if storage != "local-only":
            errors.append("captured third-party transcript must default to local-only storage")

        locator = data.get("transcript_locator")
        expected_hash = data.get("transcript_sha256")
        if locator:
            local_path = ROOT / locator
            try:
                local_path.resolve().relative_to((ROOT / ".private" / "talk-transcripts").resolve())
            except ValueError:
                errors.append("local transcript must be under .private/talk-transcripts")
            if not local_path.is_file() and require_local:
                errors.append(f"local transcript does not exist: {locator}")
            elif local_path.is_file() and expected_hash:
                actual_hash = hashlib.sha256(local_path.read_bytes()).hexdigest()
                if actual_hash != expected_hash:
                    errors.append(f"transcript hash mismatch: expected {expected_hash}, got {actual_hash}")
    elif transcript_status == "not-captured":
        if storage != "none":
            errors.append("not-captured transcript must use transcript_storage: none")
    elif transcript_status is not None:
        errors.append(f"unsupported transcript_status: {transcript_status}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--require-local",
        action="store_true",
        help="require private transcript captures and verify their hashes",
    )
    args = parser.parse_args()

    talk_count = 0
    failures: list[tuple[Path, list[str]]] = []
    for path in sorted(SOURCES.glob("*.md")):
        data = frontmatter(path)
        if data.get("source_type") != "talk":
            continue
        talk_count += 1
        errors = validate(path, data, args.require_local)
        if errors:
            failures.append((path, errors))

    if failures:
        for path, errors in failures:
            print(path.relative_to(ROOT))
            for error in errors:
                print(f"  - {error}")
        return 1

    local_mode = "required" if args.require_local else "optional"
    print(f"OK: {talk_count} talk source cards checked (local transcripts {local_mode})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
