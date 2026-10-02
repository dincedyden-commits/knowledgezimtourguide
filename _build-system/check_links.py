import os, re, sys
from urllib.parse import urlparse

ROOT = "/home/claude/ztg"
broken = []
checked = 0

for dirpath, dirs, files in os.walk(ROOT):
    if "__pycache__" in dirpath:
        continue
    for fname in files:
        if not fname.endswith(".html"):
            continue
        fpath = os.path.join(dirpath, fname)
        with open(fpath, encoding="utf-8") as f:
            content = f.read()
        hrefs = re.findall(r'href="([^"]+)"', content)
        for href in hrefs:
            checked += 1
            if href.startswith("http") or href.startswith("mailto:") or href.startswith("tel:") or href.startswith("#"):
                continue
            # resolve relative to the file's directory
            target = os.path.normpath(os.path.join(dirpath, href))
            if not os.path.isfile(target):
                broken.append((fpath.replace(ROOT, ""), href, target.replace(ROOT, "")))

print(f"Checked {checked} hrefs across the site.")
if broken:
    print(f"\n❌ {len(broken)} BROKEN LINKS FOUND:\n")
    for src, href, target in broken:
        print(f"  {src}  ->  {href}   (resolved: {target})")
    sys.exit(1)
else:
    print("✅ All internal links resolve correctly.")


