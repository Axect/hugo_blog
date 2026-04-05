#!/usr/bin/env python3
"""Fetch GitHub stars and crates.io downloads for software projects."""

import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SOFTWARE_FILE = PROJECT_ROOT / "data" / "software.yaml"
STATS_FILE = PROJECT_ROOT / "data" / "software_stats.json"

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")


def fetch_json(url: str, headers: dict | None = None) -> dict | None:
    """Fetch JSON from a URL, return None on failure."""
    h = {"User-Agent": "hugo-blog-stats/1.0"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read())
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
        print(f"  WARN: {url} — {e}", file=sys.stderr)
        return None


def github_stars(repo_url: str) -> int | None:
    """Extract owner/repo from GitHub URL and fetch star count."""
    parts = repo_url.rstrip("/").split("/")
    owner, repo = parts[-2], parts[-1]
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    data = fetch_json(f"https://api.github.com/repos/{owner}/{repo}", headers)
    if data and "stargazers_count" in data:
        return data["stargazers_count"]
    return None


def crates_downloads(crate_name: str) -> int | None:
    """Fetch total downloads from crates.io."""
    data = fetch_json(f"https://crates.io/api/v1/crates/{crate_name}")
    if data and "crate" in data:
        return data["crate"].get("downloads")
    return None


def format_number(n: int) -> str:
    """Format large numbers for display: 1062209 -> '1.0M', 6625 -> '6.6K'."""
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    elif n >= 1_000:
        return f"{n / 1_000:.1f}K"
    return str(n)


def main():
    if not SOFTWARE_FILE.exists():
        print(f"ERROR: {SOFTWARE_FILE} not found", file=sys.stderr)
        sys.exit(1)

    with open(SOFTWARE_FILE) as f:
        projects = yaml.safe_load(f)

    # Load previous stats for fallback
    prev_stats = {}
    if STATS_FILE.exists():
        with open(STATS_FILE) as f:
            prev_stats = json.load(f)

    stats = {}
    for proj in projects:
        name = proj["name"]
        entry = {}
        print(f"Fetching stats for {name}...")

        # GitHub stars
        if "github" in proj:
            stars = github_stars(proj["github"])
            if stars is not None:
                entry["stars"] = stars
            elif name in prev_stats and "stars" in prev_stats[name]:
                entry["stars"] = prev_stats[name]["stars"]
                print(f"  Using cached stars for {name}")

        # Crates.io downloads (Rust packages)
        if proj.get("crates_name"):
            downloads = crates_downloads(proj["crates_name"])
            if downloads is not None:
                entry["downloads"] = format_number(downloads)
            elif name in prev_stats and "downloads" in prev_stats[name]:
                entry["downloads"] = prev_stats[name]["downloads"]
                print(f"  Using cached downloads for {name}")

        if entry:
            stats[name] = entry

    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=2)

    print(f"Stats written to {STATS_FILE}")


if __name__ == "__main__":
    main()
