#!/bin/bash
# Set GitHub token for API rate limits
export GITHUB_TOKEN=$(gh auth token)

# Fetch latest software stats (stars, downloads)
python3 scripts/fetch_stats.py

# CV: pull the latest compiled PDF from the sibling cv_typst clone (Axect/cv_typst)
set -e
git -C ../cv_typst pull --ff-only --quiet
test -f ../cv_typst/cv.pdf

# Build Hugo site
rm -rf ../axect.github.io/*
rm -rf public/
hugo -t hello-friend-ng
cp -r public/* ../axect.github.io/
cp ../cv_typst/cv.pdf ../axect.github.io/cv.pdf
