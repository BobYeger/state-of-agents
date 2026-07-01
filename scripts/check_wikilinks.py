#!/usr/bin/env python3
"""Check Obsidian wikilinks for missing targets."""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKILINK_RE = re.compile(r"!?\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
DEFAULT_IGNORES = (".git", "node_modules", "talk")


def is_ignored(path: Path, ignored_dirs: set[str]) -> bool:
    return any(part in ignored_dirs for part in path.parts)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def iter_files(ignored_dirs: set[str]) -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file() and not is_ignored(path.relative_to(ROOT), ignored_dirs)
    )


def build_targets(files: list[Path]) -> tuple[set[str], set[str]]:
    exact: set[str] = set()
    note_names: set[str] = set()

    for path in files:
        relative = rel(path)
        exact.add(relative)
        if path.suffix == ".md":
            without_suffix = relative.removesuffix(".md")
            exact.add(without_suffix)
            note_names.add(Path(without_suffix).name)

    return exact, note_names


def target_exists(target: str, exact: set[str], note_names: set[str]) -> bool:
    if not target or target.startswith("#"):
        return True

    if "/" in target or "." in target:
        candidates = {target}
        if target.endswith(".md"):
            candidates.add(target.removesuffix(".md"))
        else:
            candidates.add(f"{target}.md")
        return any(candidate in exact for candidate in candidates)

    return target in note_names


def find_missing(markdown_files: list[Path], exact: set[str], note_names: set[str]) -> dict[str, list[str]]:
    missing: dict[str, list[str]] = defaultdict(list)

    for path in markdown_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_number, line in enumerate(text.splitlines(), 1):
            for match in WIKILINK_RE.finditer(line):
                target = match.group(1).strip()
                if not target_exists(target, exact, note_names):
                    missing[target].append(f"{rel(path)}:{line_number}")

    return dict(sorted(missing.items()))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ignore-dir",
        action="append",
        default=list(DEFAULT_IGNORES),
        help="Directory name to ignore. Can be passed more than once.",
    )
    parser.add_argument("--quiet", action="store_true", help="Only print failures.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    ignored_dirs = set(args.ignore_dir)
    files = iter_files(ignored_dirs)
    markdown_files = [path for path in files if path.suffix == ".md"]
    exact, note_names = build_targets(files)
    missing = find_missing(markdown_files, exact, note_names)

    if not missing:
        if not args.quiet:
            print(f"OK: {len(markdown_files)} markdown files checked; no missing wikilinks.")
        return 0

    print(f"Missing wikilink targets: {len(missing)}", file=sys.stderr)
    for target, locations in missing.items():
        print(f"[[{target}]]", file=sys.stderr)
        for location in locations[:12]:
            print(f"  {location}", file=sys.stderr)
        if len(locations) > 12:
            print(f"  ... {len(locations) - 12} more", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
