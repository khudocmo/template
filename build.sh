#!/usr/bin/env bash
set -e

EPUB="${FILES_DIR}/${BASE_NAME}.epub"
AZW3="${FILES_DIR}/${BASE_NAME}.azw3"
HTML="${FILES_DIR}/${BASE_NAME}.html"

pandoc "$DOC_PATH" -f markdown -t epub -s -o "$EPUB" \
  --metadata title="$TITLE" \
  --metadata author="$AUTHOR" \
  --metadata language="vi" \
  --css="$CSS_PATH"

ebook-convert "$EPUB" "$AZW3"

pandoc "$DOC_PATH" -s -o "$HTML"