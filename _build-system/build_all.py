# -*- coding: utf-8 -*-
"""Run every generator in the correct order to build the full site."""
import subprocess, sys, os

os.chdir("/home/claude/ztg")
scripts = [
    "build_home.py",
    "build_destinations.py",
    "build_tours.py",
    "build_travel_guide.py",
    "build_about.py",
    "build_faq.py",
    "build_contact.py",
    "build_gallery.py",
    "build_legal.py",
]
for s in scripts:
    print(f"\n=== Running {s} ===")
    result = subprocess.run([sys.executable, s], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"ERROR in {s}:\n{result.stderr}")
        sys.exit(1)
print("\n✅ Full site build complete.")


