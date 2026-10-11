"""
batch_convert.py - Moodle to Markdown Batch Converter.
Recursively converts downloaded Moodle course directories (PDFs, Word docs,
PowerPoint presentations, Excel sheets, HTML pages, etc.) into clean,
structured Markdown notes mirroring the original tree.

Includes optional automated AI polishing with Mistral AI.

Author: Morgan Pierrefeu (@evaspace)
License: MIT
"""

import os
import sys
import time
import shutil
import argparse
from pathlib import Path
from typing import Dict, Optional
import requests
from markitdown import MarkItDown

# Attempt to load default output folder from config if available
try:
    import config
    CONFIG_DEFAULT_SOURCE = getattr(config, "OUTPUT_DIR", "moodle_notes")
    CONFIG_MISTRAL_KEY = getattr(config, "MISTRAL_API_KEY", "")
except ImportError:
    CONFIG_DEFAULT_SOURCE = "moodle_notes"
    CONFIG_MISTRAL_KEY = ""


def get_default_source() -> str:
    """Returns the most appropriate default source directory."""
    if os.path.isdir(CONFIG_DEFAULT_SOURCE):
        return CONFIG_DEFAULT_SOURCE
    if os.path.isdir("EPITA_Moodle_Notes"):
        return "EPITA_Moodle_Notes"
    return "moodle_notes"


def call_mistral_cleanup(markdown_text: str, api_key: str, model: str = "mistral-small-latest") -> str:
    """
    Cleans up conversion artifacts, table formatting, and LaTeX math equations
    using the Mistral AI API.
    """
    if not api_key or not markdown_text.strip():
        return markdown_text

    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    prompt = (
        "You are an expert academic note formatter. "
        "Your role is to clean up formatting glitches, table alignments, and LaTeX equations ($...$ and $$...$$) "
        "in the provided converted Markdown course notes. "
        "Do NOT invent or summarize information. Maintain the exact original pedagogical content. "
        "Output ONLY the cleaned Markdown text."
    )

    # Truncate content to avoid exceeding context limits during batch runs if extremely large
    content_payload = markdown_text[:14000]

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": content_payload},
        ],
        "temperature": 0.2,
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        if response.status_code == 200:
            result = response.json()
            cleaned = result["choices"][0]["message"]["content"]
            # If original was larger than payload, append the remaining unedited text
            if len(markdown_text) > 14000:
                cleaned += "\n\n" + markdown_text[14000:]
            return cleaned
        else:
            print(f"  ⚠️ Mistral API warning ({response.status_code}): {response.text[:120]}")
            return markdown_text
    except Exception as e:
        print(f"  ⚠️ Mistral API call failed: {e}")
        return markdown_text


def process_file(
    source_path: Path,
    target_path: Path,
    md_converter: MarkItDown,
    mistral_key: Optional[str] = None,
    force: bool = False,
    stats: Optional[Dict[str, int]] = None,
):
    """
    Processes a single file: copies if already markdown, or converts using MarkItDown.
    """
    ext = source_path.suffix.lower()
    supported_extensions = {".pdf", ".docx", ".pptx", ".xlsx", ".html", ".htm", ".csv", ".json", ".xml"}

    if ext == ".md":
        shutil.copy2(source_path, target_path)
        if stats:
            stats["copied"] += 1
        print(f"  📄 Copied (.md): {source_path.name}")
        return

    if ext in supported_extensions:
        target_md_path = target_path.with_suffix(".md")

        if target_md_path.exists() and not force:
            if stats:
                stats["skipped"] += 1
            print(f"  ⏩ Already converted: {target_md_path.name}")
            return

        print(f"  🔄 Converting: {source_path.name} -> {target_md_path.name}")
        try:
            result = md_converter.convert(str(source_path))
            content = result.text_content

            if mistral_key:
                print(f"     ✨ Polishing with Mistral AI...")
                content = call_mistral_cleanup(content, mistral_key)

            with open(target_md_path, "w", encoding="utf-8") as f:
                f.write(content)

            if stats:
                stats["converted"] += 1
            print(f"  ✅ Converted: {target_md_path.name}")
        except Exception as e:
            if stats:
                stats["failed"] += 1
            print(f"  ❌ Error converting {source_path.name}: {e}")
    else:
        # Ignore unsupported file formats to keep Markdown workspace clean
        if stats:
            stats["ignored"] += 1


def convert_directory(
    source_dir: str,
    target_dir: str,
    mistral_key: Optional[str] = None,
    limit: Optional[int] = None,
    force: bool = False,
):
    """
    Recursively navigates through source_dir and reproduces the directory structure
    in target_dir with all convertible files turned into Markdown.
    """
    source = Path(source_dir)
    target = Path(target_dir)

    if not source.exists():
        print(f"❌ Source folder '{source_dir}' does not exist.")
        return

    start_time = time.time()
    md_converter = MarkItDown()
    stats = {"scanned": 0, "converted": 0, "copied": 0, "skipped": 0, "failed": 0, "ignored": 0}

    print(f"\n🚀 Starting batch conversion into Markdown:")
    print(f"  📁 Source Directory : {source.resolve()}")
    print(f"  📂 Target Directory : {target.resolve()}")
    if mistral_key:
        print(f"  🤖 Mistral AI Polish : Enabled")
    if limit:
        print(f"  🧪 Limit : {limit} files")
    print("-" * 65)

    for root, _, files in os.walk(source):
        root_path = Path(root)
        rel_path = root_path.relative_to(source)
        target_root = target / rel_path
        target_root.mkdir(parents=True, exist_ok=True)

        for file in sorted(files):
            if limit and stats["scanned"] >= limit:
                print(f"\n🛑 Test limit of {limit} files reached.")
                break

            source_file = root_path / file
            target_file = target_root / file

            process_file(
                source_file=source_file,
                target_path=target_file,
                md_converter=md_converter,
                mistral_key=mistral_key,
                force=force,
                stats=stats,
            )
            stats["scanned"] += 1

        if limit and stats["scanned"] >= limit:
            break

    elapsed = round(time.time() - start_time, 2)
    print("-" * 65)
    print("🎉 Conversion Complete!")
    print(f"  ⏱️ Time elapsed      : {elapsed}s")
    print(f"  📂 Total scanned     : {stats['scanned']}")
    print(f"  ✅ Newly converted   : {stats['converted']}")
    print(f"  📄 Copied Markdown   : {stats['copied']}")
    print(f"  ⏩ Skipped (existing): {stats['skipped']}")
    print(f"  ❌ Failures          : {stats['failed']}")
    print(f"  📦 Ignored binary    : {stats['ignored']}")
    print("-" * 65)


def parse_args():
    default_src = get_default_source()
    default_tgt = f"{default_src}_MD"

    parser = argparse.ArgumentParser(
        description="Batch convert an entire Moodle course tree (PDF, DOCX, PPTX, etc.) to Markdown.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--source",
        "-s",
        default=default_src,
        help="Source directory containing downloaded Moodle courses",
    )
    parser.add_argument(
        "--target",
        "-t",
        default=default_tgt,
        help="Destination directory for parallel Markdown tree",
    )
    parser.add_argument(
        "--mistral-key",
        "-m",
        default=os.environ.get("MISTRAL_API_KEY", CONFIG_MISTRAL_KEY or None),
        help="Mistral API Key for markdown enhancement (reads MISTRAL_API_KEY env by default)",
    )
    parser.add_argument(
        "--test-limit",
        "-l",
        type=int,
        default=None,
        help="Maximum number of files to process (useful for testing)",
    )
    parser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="Force re-conversion of files even if target .md already exists",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    convert_directory(
        source_dir=args.source,
        target_dir=args.target,
        mistral_key=args.mistral_key,
        limit=args.test_limit,
        force=args.force,
    )
