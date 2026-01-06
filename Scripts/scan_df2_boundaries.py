#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
NOTES_RE = re.compile(r"(?m)^##\s+Notes\s*$")
PROPOSED_ORDER_RE = re.compile(r"^###\s+Proposed order\b.*\b(?P<version>v\d+\.\d+)\b", re.IGNORECASE)
PAGE_RE = re.compile(r"cains_jawbone_page_(\d+)\.md")
WORD_RE = re.compile(r"[a-z]+(?:'[a-z]+)?")


def md_body_before_notes(md_text: str) -> str:
    match = NOTES_RE.search(md_text)
    if not match:
        raise ValueError("Missing '## Notes' section")
    return md_text[: match.start()]


def tokenize(text: str) -> list[str]:
    return WORD_RE.findall(text.lower())


def ngram_set(tokens: list[str], n: int) -> set[str]:
    if n <= 0:
        raise ValueError(f"n must be >= 1, got {n}")
    if len(tokens) < n:
        return set()
    return {" ".join(tokens[i : i + n]) for i in range(0, len(tokens) - n + 1)}


@dataclass(frozen=True)
class Block:
    label: str
    pages: list[int]


def _short_block_label(label: str) -> str:
    match = re.match(r"Block\s+[A-Za-z0-9]+", label)
    return match.group(0) if match else label


def _extract_block_label(line: str) -> str:
    line = line.strip()
    match = re.match(r"^- \*\*(Block[^*]+):\*\*", line)
    if not match:
        raise ValueError(f"Could not parse block label from line: {line}")
    return match.group(1).strip()


def parse_proposed_order(hypotheses_text: str, *, version: str) -> list[Block]:
    lines = hypotheses_text.splitlines()

    start_idx: int | None = None
    version_lower = version.lower()
    for i, line in enumerate(lines):
        if not line.startswith("###"):
            continue
        match = PROPOSED_ORDER_RE.match(line)
        if not match:
            continue
        if match.group("version").lower() == version_lower:
            start_idx = i
            break

    if start_idx is None:
        raise ValueError(f"Could not find a '### Proposed order ...; {version}' section in hypotheses.")

    end_idx = len(lines)
    for i in range(start_idx + 1, len(lines)):
        if lines[i].startswith("### "):
            end_idx = i
            break

    section_lines = lines[start_idx + 1 : end_idx]

    blocks: list[Block] = []
    i = 0
    while i < len(section_lines):
        line = section_lines[i]
        if not line.startswith("- **Block"):
            i += 1
            continue

        bullet_lines = [line]
        i += 1
        while i < len(section_lines):
            cont = section_lines[i]
            if cont.startswith("  ") or cont.startswith("\t"):
                bullet_lines.append(cont)
                i += 1
                continue
            break

        bullet_text = " ".join(l.strip() for l in bullet_lines)
        pages = [int(p) for p in PAGE_RE.findall(bullet_text)]
        if not pages:
            raise ValueError(f"Block bullet had no page references: {bullet_text}")
        label = _extract_block_label(bullet_lines[0])
        blocks.append(Block(label=label, pages=pages))

    if not blocks:
        raise ValueError(f"Found {version} section but no '- **Block …**' bullets to parse.")

    order = [p for block in blocks for p in block.pages]
    unique = set(order)
    if len(order) != 100 or len(unique) != 100:
        missing = [p for p in range(1, 101) if p not in unique]
        dupes = [p for p, c in Counter(order).items() if c > 1]
        raise ValueError(
            f"Parsed {len(order)} page refs ({len(unique)} unique), expected 100 unique.\n"
            f"Missing: {missing}\n"
            f"Duplicates: {sorted(dupes)}"
        )
    if min(order) < 1 or max(order) > 100:
        raise ValueError(f"Parsed page numbers outside 1..100: min={min(order)}, max={max(order)}")

    return blocks


@dataclass(frozen=True)
class Boundary:
    a: int
    b: int
    left_block: str | None = None
    right_block: str | None = None

    def label(self) -> str:
        if self.left_block and self.right_block:
            return f"p{self.a}→p{self.b} ({self.left_block}→{self.right_block})"
        return f"p{self.a}→p{self.b}"


@dataclass(frozen=True)
class AnchorStats:
    df2_tokens: list[str]
    df2_ngrams: dict[int, list[str]]

    def token_count(self) -> int:
        return len(self.df2_tokens)

    def ngram_count(self) -> int:
        return sum(len(v) for v in self.df2_ngrams.values())

    def anchor_count(self) -> int:
        return self.token_count() + self.ngram_count()


def build_df_indexes(
    *,
    pages_dir: Path,
    min_n: int,
    max_n: int,
) -> tuple[dict[int, set[str]], dict[int, dict[int, set[str]]], Counter[str], dict[int, Counter[str]]]:
    token_sets: dict[int, set[str]] = {}
    ngram_sets: dict[int, dict[int, set[str]]] = {}

    token_df: Counter[str] = Counter()
    ngram_df: dict[int, Counter[str]] = {n: Counter() for n in range(min_n, max_n + 1)}

    for page_num in range(1, 101):
        md_path = pages_dir / f"cains_jawbone_page_{page_num}.md"
        md_text = md_path.read_text(encoding="utf-8")
        body = md_body_before_notes(md_text)

        tokens = tokenize(body)
        token_set = set(tokens)
        token_sets[page_num] = token_set
        token_df.update(token_set)

        page_ngrams: dict[int, set[str]] = {}
        for n in range(min_n, max_n + 1):
            grams = ngram_set(tokens, n)
            page_ngrams[n] = grams
            ngram_df[n].update(grams)
        ngram_sets[page_num] = page_ngrams

    return token_sets, ngram_sets, token_df, ngram_df


def boundary_stats(
    boundary: Boundary,
    *,
    token_sets: dict[int, set[str]],
    ngram_sets: dict[int, dict[int, set[str]]],
    token_df: Counter[str],
    ngram_df: dict[int, Counter[str]],
    min_n: int,
    max_n: int,
) -> AnchorStats:
    a_tokens = token_sets[boundary.a]
    b_tokens = token_sets[boundary.b]
    df2_tokens = sorted(t for t in (a_tokens & b_tokens) if token_df[t] == 2)

    df2_ngrams: dict[int, list[str]] = {}
    for n in range(min_n, max_n + 1):
        a_grams = ngram_sets[boundary.a][n]
        b_grams = ngram_sets[boundary.b][n]
        overlap = sorted(g for g in (a_grams & b_grams) if ngram_df[n][g] == 2)
        if overlap:
            df2_ngrams[n] = overlap

    return AnchorStats(df2_tokens=df2_tokens, df2_ngrams=df2_ngrams)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan a proposed order for boundaries with no shared df==2 token anchors and no shared df==2 n-gram anchors."
    )
    parser.add_argument(
        "--hypotheses",
        type=Path,
        default=REPO_ROOT / "Order" / "hypotheses.md",
        help="Path to Order/hypotheses.md",
    )
    parser.add_argument(
        "--pages-dir",
        type=Path,
        default=REPO_ROOT / "Pages",
        help="Directory containing cains_jawbone_page_*.md files",
    )
    parser.add_argument(
        "--version",
        default="v2.36",
        help="Which '### Proposed order ...; vX.Y' section to parse (default: v2.36)",
    )
    parser.add_argument(
        "--mode",
        choices=["block", "all"],
        default="block",
        help="Scan only block boundaries (block) or all adjacent page boundaries (all).",
    )
    parser.add_argument(
        "--min-n",
        type=int,
        default=2,
        help="Minimum n for n-gram anchors (default: 2)",
    )
    parser.add_argument(
        "--max-n",
        type=int,
        default=6,
        help="Maximum n for n-gram anchors (default: 6)",
    )
    parser.add_argument(
        "--list",
        choices=["zero", "weak", "all", "none"],
        default="zero",
        help="Which boundaries to print (default: zero).",
    )
    parser.add_argument(
        "--weak-threshold",
        type=int,
        default=1,
        help="When --list=weak, print boundaries with <= this many df==2 anchors (default: 1).",
    )
    parser.add_argument(
        "--show-anchors",
        action="store_true",
        help="Include the actual df==2 token/ngram overlaps for printed boundaries.",
    )
    parser.add_argument(
        "--max-show",
        type=int,
        default=8,
        help="Max tokens/phrases to show per boundary/type (default: 8).",
    )
    parser.add_argument(
        "--pair",
        nargs=2,
        type=int,
        action="append",
        metavar=("A", "B"),
        help="Show anchor details for a specific boundary A->B (can repeat).",
    )
    args = parser.parse_args()

    if args.min_n < 1 or args.max_n < args.min_n:
        print(f"Invalid n-gram range: min_n={args.min_n}, max_n={args.max_n}", file=sys.stderr)
        return 2

    hypotheses_text = args.hypotheses.read_text(encoding="utf-8")
    blocks = parse_proposed_order(hypotheses_text, version=args.version)
    order = [p for block in blocks for p in block.pages]

    token_sets, ngram_sets, token_df, ngram_df = build_df_indexes(
        pages_dir=args.pages_dir,
        min_n=args.min_n,
        max_n=args.max_n,
    )

    boundaries: list[Boundary] = []
    if args.mode == "all":
        for i in range(len(order) - 1):
            boundaries.append(Boundary(a=order[i], b=order[i + 1]))
    else:
        for i in range(len(blocks) - 1):
            left = blocks[i]
            right = blocks[i + 1]
            boundaries.append(
                Boundary(
                    a=left.pages[-1],
                    b=right.pages[0],
                    left_block=_short_block_label(left.label),
                    right_block=_short_block_label(right.label),
                )
            )

    stats_by_boundary: dict[Boundary, AnchorStats] = {}
    zero: list[Boundary] = []
    weak: list[Boundary] = []
    for boundary in boundaries:
        stats = boundary_stats(
            boundary,
            token_sets=token_sets,
            ngram_sets=ngram_sets,
            token_df=token_df,
            ngram_df=ngram_df,
            min_n=args.min_n,
            max_n=args.max_n,
        )
        stats_by_boundary[boundary] = stats
        if stats.anchor_count() == 0:
            zero.append(boundary)
        if stats.anchor_count() <= args.weak_threshold:
            weak.append(boundary)

    print(f"{args.version} ({args.mode} boundaries): {len(boundaries)} total")
    print(f"- zero-anchor (df==2 tokens + df==2 ngrams): {len(zero)}")
    if args.list == "weak":
        print(f"- weak (<= {args.weak_threshold} total anchors): {len(weak)}")

    def should_print(b: Boundary) -> bool:
        if args.list == "none":
            return False
        if args.list == "all":
            return True
        if args.list == "zero":
            return b in zero
        if args.list == "weak":
            return b in weak
        raise AssertionError(f"Unhandled list mode: {args.list}")

    if args.list != "none":
        for boundary in boundaries:
            if not should_print(boundary):
                continue
            stats = stats_by_boundary[boundary]
            print(f"- {boundary.label()}: {stats.token_count()} token, {stats.ngram_count()} ngram anchors")
            if not args.show_anchors:
                continue
            if stats.df2_tokens:
                shown = stats.df2_tokens[: args.max_show]
                suffix = "" if len(shown) == len(stats.df2_tokens) else f" (+{len(stats.df2_tokens) - len(shown)} more)"
                print(f"  - df2 tokens: {', '.join(shown)}{suffix}")
            for n in sorted(stats.df2_ngrams):
                phrases = stats.df2_ngrams[n]
                shown = phrases[: args.max_show]
                suffix = "" if len(shown) == len(phrases) else f" (+{len(phrases) - len(shown)} more)"
                print(f"  - df2 {n}-grams: {', '.join(shown)}{suffix}")

    if args.pair:
        for a, b in args.pair:
            boundary = Boundary(a=a, b=b)
            stats = boundary_stats(
                boundary,
                token_sets=token_sets,
                ngram_sets=ngram_sets,
                token_df=token_df,
                ngram_df=ngram_df,
                min_n=args.min_n,
                max_n=args.max_n,
            )
            print(f"\nPair p{a}→p{b}: {stats.token_count()} token, {stats.ngram_count()} ngram anchors")
            if stats.df2_tokens:
                shown = stats.df2_tokens[: args.max_show]
                suffix = "" if len(shown) == len(stats.df2_tokens) else f" (+{len(stats.df2_tokens) - len(shown)} more)"
                print(f"- df2 tokens: {', '.join(shown)}{suffix}")
            for n in sorted(stats.df2_ngrams):
                phrases = stats.df2_ngrams[n]
                shown = phrases[: args.max_show]
                suffix = "" if len(shown) == len(phrases) else f" (+{len(phrases) - len(shown)} more)"
                print(f"- df2 {n}-grams: {', '.join(shown)}{suffix}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

