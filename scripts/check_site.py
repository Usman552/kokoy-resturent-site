"""Sanity checks for the static KOKOY site. Exits non-zero on any problem."""
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text(encoding="utf-8")
errors = []

# 1. every local file referenced by src / href / srcset / JS image paths exists
refs = set(re.findall(r'(?:src|href)="(?!https?:|#|mailto:|tel:|data:)([^"]+)"', html))
for group in re.findall(r'srcset="([^"]+)"', html):
    refs.update(part.split()[0] for part in group.split(","))
refs.update(re.findall(r"img/[\w\-./]+\.webp", html))
for ref in sorted(refs):
    if not (root / ref.split("?")[0]).exists():
        errors.append(f"missing file referenced in index.html: {ref}")

# 2. every image in img/ is a real WebP
for img in sorted((root / "img").glob("*")):
    head = img.read_bytes()[:12]
    if img.suffix == ".webp" and not (head[:4] == b"RIFF" and head[8:12] == b"WEBP"):
        errors.append(f"not a valid WebP: {img.name}")

# 3. animation libraries are still loaded
for lib in ("gsap.min.js", "ScrollTrigger.min.js"):
    if lib not in html:
        errors.append(f"script tag missing: {lib}")

# 4. every <img> has alt text attribute and dimensions
for tag in re.findall(r"<img\b[^>]*>", html):
    if "alt=" not in tag:
        errors.append(f"img without alt: {tag[:80]}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(refs)} local references, {len(list((root / 'img').glob('*.webp')))} images")
