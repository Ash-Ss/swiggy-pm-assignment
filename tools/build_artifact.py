"""Write a copy of index.html that can be published as a claude.ai Artifact.

The Artifact host wraps every page in its own doctype, html, head and body tags, so this copy
drops those wrapper lines and the charset and viewport metas. Everything else is unchanged.

Usage: python3 tools/build_artifact.py [OUT.html]   (default: /tmp/ai-trip-planner.html)
"""
import pathlib
import sys

src = pathlib.Path(__file__).resolve().parent.parent / "index.html"
dst = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/ai-trip-planner.html")
drop = {'<!doctype html>', '<html lang="en">', '<head>', '</head>', '<body>', '</body>', '</html>', '<meta charset="utf-8">'}
lines = [l for l in src.read_text().splitlines()
         if l.strip() not in drop and not l.strip().startswith('<meta name="viewport"')]
dst.write_text("\n".join(lines) + "\n")
print(f"{dst}: {dst.stat().st_size} bytes, first line: {lines[0]}")
