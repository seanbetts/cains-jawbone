#!/usr/bin/env python3
from __future__ import annotations

import argparse
import difflib
import hashlib
import re
import sys
import unicodedata
from pathlib import Path


SEP_RE = re.compile(r"^_{4,}\s*$")
NOTES_RE = re.compile(r"(?m)^##\s+Notes\s*$")


def _normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def _strip_utf8_bom(text: str) -> str:
    return text[1:] if text.startswith("\ufeff") else text


def _trim_outer_blank_lines(lines: list[str]) -> list[str]:
    while lines and lines[0].strip() == "":
        lines.pop(0)
    while lines and lines[-1].strip() == "":
        lines.pop()
    return lines


def normalize_for_compare(text: str, *, ignore_trailing_whitespace: bool) -> str:
    text = _strip_utf8_bom(_normalize_newlines(text))
    text = unicodedata.normalize("NFC", text)
    lines = text.split("\n")
    if ignore_trailing_whitespace:
        lines = [line.rstrip(" \t") for line in lines]
    lines = _trim_outer_blank_lines(lines)
    return "\n".join(lines).rstrip("\n") + "\n"


def split_source_pages(source_text: str) -> list[str]:
    source_text = _strip_utf8_bom(_normalize_newlines(source_text))
    lines = source_text.split("\n")

    pages: list[list[str]] = [[]]
    for line in lines:
        if SEP_RE.match(line.strip()):
            pages.append([])
        else:
            pages[-1].append(line)

    while pages and all(l.strip() == "" for l in pages[-1]):
        pages.pop()

    pages = [_trim_outer_blank_lines(p) for p in pages]
    return ["\n".join(p).rstrip("\n") + "\n" for p in pages]


def md_body_before_notes(md_text: str) -> str:
    md_text = _strip_utf8_bom(_normalize_newlines(md_text))
    match = NOTES_RE.search(md_text)
    if not match:
        raise ValueError("Missing '## Notes' section")
    return md_text[: match.start()]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify that page Markdown files match the archived source, ignoring content under '## Notes'."
    )
    parser.add_argument(
        "--archive",
        type=Path,
        default=Path("Archive") / "Cain's Jawbone Unformatted.txt",
        help="Path to the archived source .txt file",
    )
    parser.add_argument(
        "--pages-dir",
        type=Path,
        default=Path("Pages"),
        help="Directory containing cains_jawbone_page_*.md files",
    )
    parser.add_argument(
        "--hash-file",
        type=Path,
        default=Path("Archive") / "hash.txt",
        help="File containing the expected hash of the archive (default: Archive/hash.txt)",
    )
    parser.add_argument(
        "--hash-alg",
        default="sha256",
        help="Hash algorithm for the archive (default: sha256)",
    )
    parser.add_argument(
        "--show-diff",
        action="store_true",
        help="Print unified diffs for mismatches",
    )
    parser.add_argument(
        "--strict-whitespace",
        action="store_true",
        help="Also treat trailing spaces/tabs as differences",
    )
    args = parser.parse_args()

    if not args.archive.exists():
        print(f"Archive file not found: {args.archive}", file=sys.stderr)
        return 2
    if not args.hash_file.exists():
        print(f"Hash file not found: {args.hash_file}", file=sys.stderr)
        return 2
    if not args.pages_dir.exists():
        print(f"Pages dir not found: {args.pages_dir}", file=sys.stderr)
        return 2

    expected_hash = args.hash_file.read_text(encoding="utf-8").strip().split()[0].lower()
    archive_bytes = args.archive.read_bytes()
    try:
        actual_hash = hashlib.new(args.hash_alg, archive_bytes).hexdigest().lower()
    except ValueError:
        print(f"Unknown hash algorithm: {args.hash_alg}", file=sys.stderr)
        return 2
    if expected_hash != actual_hash:
        print(f"Archive hash mismatch for {args.archive}", file=sys.stderr)
        print(f"Expected ({args.hash_alg}): {expected_hash}", file=sys.stderr)
        print(f"Actual   ({args.hash_alg}): {actual_hash}", file=sys.stderr)
        return 1

    source_text = args.archive.read_text(encoding="utf-8-sig")
    source_pages = split_source_pages(source_text)
    if len(source_pages) != 100:
        print(f"Expected 100 pages in archive, found {len(source_pages)}", file=sys.stderr)
        return 2

    mismatches: list[int] = []
    for i in range(1, 101):
        md_path = args.pages_dir / f"cains_jawbone_page_{i}.md"
        if not md_path.exists():
            print(f"Missing: {md_path}", file=sys.stderr)
            mismatches.append(i)
            continue

        md_text = md_path.read_text(encoding="utf-8")
        try:
            md_body = md_body_before_notes(md_text)
        except ValueError as e:
            print(f"{md_path}: {e}", file=sys.stderr)
            mismatches.append(i)
            continue

        ignore_trailing = not args.strict_whitespace
        expected = normalize_for_compare(source_pages[i - 1], ignore_trailing_whitespace=ignore_trailing)
        actual = normalize_for_compare(md_body, ignore_trailing_whitespace=ignore_trailing)

        if expected != actual:
            mismatches.append(i)
            print(f"Mismatch on page {i}: {md_path}", file=sys.stderr)
            if args.show_diff:
                diff = difflib.unified_diff(
                    expected.splitlines(keepends=True),
                    actual.splitlines(keepends=True),
                    fromfile=f"archive_page_{i}",
                    tofile=str(md_path),
                )
                sys.stderr.writelines(diff)

    if mismatches:
        print(f"\nFAILED: {len(mismatches)} page(s) differ: {', '.join(map(str, mismatches))}", file=sys.stderr)
        return 1

    print("OK: archive hash verified; all 100 pages match (Notes ignored).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
