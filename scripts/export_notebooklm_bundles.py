#!/usr/bin/env python3
"""Create small NotebookLM-ready source bundles from curated vault topics."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - dependency guard
    raise SystemExit("PyYAML is required. Install with: python3 -m pip install pyyaml") from exc


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TOPICS = ROOT / "notebooklm" / "topics.yml"
DEFAULT_OUT = ROOT / "exports" / "notebooklm"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = read_text(path)
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 5 :]
    data = yaml.safe_load(raw) or {}
    if not isinstance(data, dict):
        data = {}
    return data, body


def first_heading(body: str) -> str | None:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def slugify(value: str, max_len: int = 96) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9._ -]+", "", value)
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:max_len].strip("-") or "source"


def wikilink(path: str) -> str:
    p = Path(path)
    if p.suffix == ".md":
        return f"[[{p.with_suffix('').as_posix()}]]"
    return p.as_posix()


def copy_or_link(src: Path, dst: Path, mode: str) -> str:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        dst.unlink()
    if mode == "copy":
        shutil.copy2(src, dst)
        return "copied"
    try:
        os.link(src, dst)
        return "hardlinked"
    except OSError:
        shutil.copy2(src, dst)
        return "copied"


def load_topics(path: Path) -> list[dict[str, Any]]:
    data = yaml.safe_load(read_text(path)) or {}
    topics = data.get("topics", [])
    if not isinstance(topics, list):
        raise ValueError(f"{path} must contain a top-level topics list")
    return topics


def resolve_source(note_path: str) -> dict[str, Any]:
    note = ROOT / note_path
    if not note.exists():
        raise FileNotFoundError(f"Missing source note: {note_path}")
    frontmatter, body = parse_frontmatter(note)
    title = frontmatter.get("title") or first_heading(body) or note.stem
    artifacts = frontmatter.get("artifacts") or []
    if not isinstance(artifacts, list):
        artifacts = []
    return {
        "note": note_path,
        "title": title,
        "source_type": frontmatter.get("source_type"),
        "kind": frontmatter.get("kind"),
        "status": frontmatter.get("status"),
        "publication_date": frontmatter.get("publication_date"),
        "year": frontmatter.get("year"),
        "citation_count": frontmatter.get("citation_count"),
        "citation_source": frontmatter.get("citation_source"),
        "url": frontmatter.get("url"),
        "pdf_url": frontmatter.get("pdf_url"),
        "artifacts": artifacts,
    }


def make_guide(topic: dict[str, Any], resolved: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    lines.append(f"# {topic['title']}")
    lines.append("")
    lines.append("This is a curated NotebookLM guide generated from the State of Agents vault.")
    lines.append("")
    lines.append("## Focus")
    lines.append("")
    lines.append(topic.get("focus", ""))
    lines.append("")
    if topic.get("questions"):
        lines.append("## Questions")
        lines.append("")
        for question in topic["questions"]:
            lines.append(f"- {question}")
        lines.append("")
    lines.append("## Reading Order")
    lines.append("")
    for index, source in enumerate(topic.get("sources", []), 1):
        item = resolved[index - 1]
        date = item.get("publication_date") or item.get("year") or "n.d."
        citation = item.get("citation_count")
        citation_text = f"; citations: {citation}" if citation not in (None, "") else ""
        lines.append(f"{index}. **{item['title']}** ({date}{citation_text})")
        lines.append(f"   - Vault note: {wikilink(item['note'])}")
        if source.get("why"):
            lines.append(f"   - Why included: {source['why']}")
        if item.get("url"):
            lines.append(f"   - URL: {item['url']}")
        lines.append("")
    lines.append("## Audio Overview Direction")
    lines.append("")
    lines.append(topic.get("podcast_angle", "Explain the key ideas, disagreements, and practical implications."))
    lines.append("")
    lines.append("Avoid treating every source as equally important. Prefer the sources marked as architecture, survey, benchmark, or original method anchors.")
    lines.append("")
    return "\n".join(lines)


def make_prompt(topic: dict[str, Any], resolved: list[dict[str, Any]]) -> str:
    titles = "\n".join(f"- {item['title']}" for item in resolved)
    questions = "\n".join(f"- {q}" for q in topic.get("questions", []))
    return f"""Create a focused Audio Overview for: {topic['title']}.

Focus:
{topic.get('focus', '')}

Angle:
{topic.get('podcast_angle', '')}

Core questions:
{questions}

Sources in this notebook:
{titles}

Style:
- Treat this as an expert learning conversation, not marketing.
- Preserve disagreement and negative results where present.
- Call out which ideas are well-supported versus speculative.
- Prefer architecture, mechanism, evaluation, and failure modes over vendor feature lists.
- End with concrete takeaways for building or evaluating agent systems.
"""


def export_topic(topic: dict[str, Any], out_root: Path, mode: str, clean: bool) -> dict[str, Any]:
    topic_id = topic["id"]
    out_dir = out_root / topic_id
    if clean and out_dir.exists():
        shutil.rmtree(out_dir)
    (out_dir / "sources").mkdir(parents=True, exist_ok=True)

    resolved = [resolve_source(item["note"]) for item in topic.get("sources", [])]

    copied_sources: list[dict[str, Any]] = []
    for source_index, item in enumerate(resolved, 1):
        source_entry = dict(item)
        artifact_entries = []
        artifacts = item.get("artifacts") or []
        if artifacts:
            for artifact_index, artifact in enumerate(artifacts, 1):
                artifact_path = ROOT / artifact
                entry: dict[str, Any] = {"path": artifact, "exists": artifact_path.exists()}
                if artifact_path.exists():
                    suffix = artifact_path.suffix
                    name = f"{source_index:02d}-{artifact_index:02d}-{slugify(item['title'])}{suffix}"
                    dst = out_dir / "sources" / name
                    action = copy_or_link(artifact_path, dst, mode)
                    entry.update({"exported_as": str(dst.relative_to(out_dir)), "action": action})
                artifact_entries.append(entry)
        else:
            note_path = ROOT / item["note"]
            name = f"{source_index:02d}-00-{slugify(item['title'])}.md"
            dst = out_dir / "sources" / name
            action = copy_or_link(note_path, dst, mode)
            artifact_entries.append(
                {
                    "path": item["note"],
                    "exists": True,
                    "exported_as": str(dst.relative_to(out_dir)),
                    "action": action,
                    "fallback": "source_note_no_raw_artifact",
                }
            )
        source_entry["exported_artifacts"] = artifact_entries
        copied_sources.append(source_entry)

    (out_dir / "00-guide.md").write_text(make_guide(topic, resolved), encoding="utf-8")
    (out_dir / "podcast_prompt.md").write_text(make_prompt(topic, resolved), encoding="utf-8")
    manifest = {
        "id": topic_id,
        "title": topic["title"],
        "focus": topic.get("focus"),
        "podcast_angle": topic.get("podcast_angle"),
        "source_count": len(copied_sources),
        "sources": copied_sources,
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topics", type=Path, default=DEFAULT_TOPICS)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--mode", choices=["hardlink", "copy"], default="hardlink")
    parser.add_argument("--no-clean", action="store_true", help="Do not delete existing topic export directories before writing")
    parser.add_argument("--dry-run", action="store_true", help="Validate topics and print what would be exported")
    args = parser.parse_args()

    topics = load_topics(args.topics)
    args.out.mkdir(parents=True, exist_ok=True)

    failures = 0
    summaries = []
    for topic in topics:
        try:
            if args.dry_run:
                resolved = [resolve_source(item["note"]) for item in topic.get("sources", [])]
                summaries.append({"id": topic["id"], "title": topic["title"], "source_count": len(resolved)})
            else:
                summaries.append(export_topic(topic, args.out, args.mode, clean=not args.no_clean))
        except Exception as exc:  # noqa: BLE001 - command-line validation should report all failures simply
            failures += 1
            print(f"ERROR {topic.get('id', '<missing-id>')}: {exc}", file=sys.stderr)

    for summary in summaries:
        print(f"{summary['id']}: {summary['source_count']} sources")
    if failures:
        return 1
    if args.dry_run:
        print(f"Validated {len(summaries)} NotebookLM bundle definitions")
    else:
        print(f"Exported {len(summaries)} NotebookLM bundles to {args.out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
