#!/usr/bin/env bash
set -e

SLUG="$1"

pandoc doc.md -f markdown -t epub -s -o "${SLUG}.epub" \
  --metadata title="$TITLE" \
  --metadata author="$AUTHOR" \
  --metadata language="vi" \
  --css="minimal.css"

ebook-convert "${SLUG}.epub" "${SLUG}.azw3"

pandoc doc.md -s -o "${SLUG}.html"

mkdir -p docs/files
mv "${SLUG}.epub" "${SLUG}.azw3" "${SLUG}.html" docs/files/
