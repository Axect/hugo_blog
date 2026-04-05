#!/bin/bash
# Fetch latest software stats (stars, downloads)
python3 scripts/fetch_stats.py

# Build Hugo site
rm -rf ../axect.github.io/*
rm -rf public/
hugo -t hello-friend-ng
cp -r public/* ../axect.github.io/
