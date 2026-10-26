#!/usr/bin/env python3
"""Checks data/apps.csv for duplicates and broken rows.

Run this before opening a pull request:

    python3 scripts/validate.py
"""

import csv
import os
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "data", "apps.csv")

CATEGORIES = {
    "Office, Productivity & AI Utilities",
    "Other Indian Apps",
    "Social Media, Messaging & Networking",
    "EdTech & Learning",
    "Zoho Apps",
    "Media, Streaming & Audio",
    "Government, e-Governance & Citizen Services",
    "Fintech, Payments & Banking",
    "Health, Fitness & Pharmacy",
    "E-Commerce, Quick-Commerce & Retail",
    "Travel, Mobility & Commute",
    "Gaming & Esports",
    "Food Delivery, Restaurants & Logistics",
    "Play Store alternatives (not Indian)",
    "Indian Native App Store Platforms",
}

REQUIRED = ["name", "category", "open_source", "status", "has_icon"]


def main():
    if not os.path.exists(CSV_PATH):
        print("missing: " + CSV_PATH)
        return 1

    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    problems = []

    for i, r in enumerate(rows, start=2):
        for field in REQUIRED:
            if not (r.get(field) or "").strip():
                problems.append("line %d: missing %s" % (i, field))
        cat = (r.get("category") or "").strip()
        if cat and cat not in CATEGORIES:
            problems.append("line %d: unknown category '%s'" % (i, cat))
        pkg = (r.get("package") or "").strip()
        url = (r.get("play_url") or "").strip()
        if pkg and url and "store/apps/details" in url and ("id=" + pkg) not in url:
            problems.append("line %d: play_url does not match package" % i)

    packages = [(r.get("package") or "").strip() for r in rows]
    packages = [p for p in packages if p]
    dupes = [p for p, n in Counter(packages).items() if n > 1]

    for p in dupes:
        problems.append("duplicate package: " + p)

    print("rows: %d" % len(rows))
    print("with package: %d" % len(packages))
    print("duplicates: %d" % len(dupes))

    if problems:
        print("")
        for p in problems[:60]:
            print("  " + p)
        if len(problems) > 60:
            print("  ... and %d more" % (len(problems) - 60))
        print("")
        print("FAILED with %d problem(s)" % len(problems))
        return 1

    print("")
    print("OK - no problems found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
