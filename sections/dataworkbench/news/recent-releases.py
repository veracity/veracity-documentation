# This script generates a list of 5 most recent Data Workbench and Data Platform releases with the links to them, and creates an overview Markdown page with those links.

import os
import re
from datetime import datetime

# Use the directory where this script resides
RELEASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(RELEASE_DIR, "recent-releases.md")  # updated filename

MONTHS = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4,
    "may": 5, "jun": 6, "jul": 7, "aug": 8,
    "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12
}

MONTH_FULL_NAMES = {
    "jan": "January", "feb": "February", "mar": "March", "apr": "April",
    "may": "May", "jun": "June", "jul": "July", "aug": "August",
    "sep": "September", "sept": "September", "oct": "October",
    "nov": "November", "dec": "December"
}

SUFFIX_RANK = {
    '': 0, 'sec': 1, 'trd': 2, 'frh': 3, 'fth': 4,
    '5th': 5, '6th': 6, '7th': 7, '8th': 8, '9th': 9
}

SUFFIX_WORDS = {
    'sec': 'second',
    'trd': 'third',
    'frh': 'fourth',
    'fth': 'fifth',
    '5th': 'fifth',
    '6th': 'sixth',
    '7th': 'seventh',
    '8th': 'eighth',
    '9th': 'ninth',
    '': ''
}

def parse_release_file(filename):
    # Updated for "dp-" instead of "dp."
    match = re.match(r"(dp-)?release([a-z]{3,4})(\d{2})([a-z0-9]*)\.md", filename)
    if not match:
        return None

    dp_prefix, month_str, year_suffix, suffix = match.groups()
    month = MONTHS.get(month_str)
    full_month = MONTH_FULL_NAMES.get(month_str)
    if month is None or full_month is None:
        print(f"Skipping file due to unrecognized month abbreviation: {filename}")
        return None

    year = 2000 + int(year_suffix)
    rank = SUFFIX_RANK.get(suffix, 99)
    suffix_word = SUFFIX_WORDS.get(suffix, suffix)

    title = f"{full_month} 20{year_suffix}"
    if suffix_word:
        title += f" {suffix_word} release"
    else:
        title += " release"

    return {
        "filename": filename,
        "title": title,
        "datetime": datetime(year, month, 1),
        "rank": rank,
        "is_dp": bool(dp_prefix)
    }

def get_latest_releases(n=5):
    dp_releases = []
    dw_releases = []

    for fname in os.listdir(RELEASE_DIR):
        if fname.endswith(".md") and "release" in fname:
            parsed = parse_release_file(fname)
            if parsed:
                if parsed["is_dp"]:
                    dp_releases.append(parsed)
                else:
                    dw_releases.append(parsed)

    dp_releases.sort(key=lambda r: (r["datetime"], -r["rank"]), reverse=True)
    dw_releases.sort(key=lambda r: (r["datetime"], -r["rank"]), reverse=True)

    dp_links = [f"[{r['title']}]({r['filename']})" for r in dp_releases[:n]]
    dw_links = [f"[{r['title']}]({r['filename']})" for r in dw_releases[:n]]

    return dp_links, dw_links

def write_markdown(dw_links, dp_links):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        # YAML front matter
        f.write("---\n")
        f.write("author: Veracity\n")
        f.write("description: This is an overview of recent releases of Data Workbench and Data Platform.\n")
        f.write("---\n\n")

        # Title
        f.write("# Overview of recent release notes for Data Workbench and Data Platform\n\n")

        # Data Workbench section
        f.write("## Recent Data Workbench changes\n\n")
        for i, link in enumerate(dw_links, start=1):
            f.write(f"{i}. {link}\n")
        f.write("\n")

        # Data Platform section
        f.write("## Recent Data Platform changes\n\n")
        for i, link in enumerate(dp_links, start=1):
            f.write(f"{i}. {link}\n")
        f.write("\n")

        # API section
        f.write("## Recent API changes\n\n")
        f.write("The latest API specification is available through our [API Explorer](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json).\n")

if __name__ == "__main__":
    dp_links, dw_links = get_latest_releases()
    write_markdown(dw_links, dp_links)
    print("✅ Markdown file 'recent-releases.md' has been generated.")
