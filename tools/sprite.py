"""Print Lucide icons as <symbol> elements for the sprite at the top of index.html.

Get the icon files once (the npm registry works where some CDNs are blocked):
    curl -sL https://registry.npmjs.org/lucide-static/-/lucide-static-1.49.0.tgz | tar xz -C /tmp
Then:
    python3 tools/sprite.py /tmp/package/icons train-front scale
and paste the output before </defs></svg>. Use an icon as <svg class="ic"><use href="#i-NAME"/></svg>,
or ic('NAME') inside the revised-architecture content.
"""
import pathlib
import re
import sys

base = pathlib.Path(sys.argv[1])
for name in sys.argv[2:]:
    svg = (base / f"{name}.svg").read_text()
    inner = re.search(r"<svg[^>]*>(.*)</svg>", svg, re.S).group(1)
    inner = re.sub(r"\s*\n\s*", "", inner).replace(" />", "/>")
    print(f'<symbol id="i-{name}" viewBox="0 0 24 24">{inner}</symbol>')
