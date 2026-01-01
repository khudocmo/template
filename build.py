#!/usr/bin/env python3

import sys
import os
import subprocess
from pathlib import Path

if len(sys.argv) != 5:
    print('Cấu trúc lệnh: python3 build.py "Tên tác phẩm" "Tên tác giả" "Mô tả" /path/to/doc.md')
    sys.exit(1)

TITLE = sys.argv[1]
AUTHOR = sys.argv[2]
DESC = sys.argv[3]
DOC_PATH = Path(sys.argv[4]).expanduser().resolve()

if not DOC_PATH.exists():
    print(f"Lỗi: Markdown file not found: {DOC_PATH}")
    sys.exit(1)

# Tệp config

SCRIPT_DIR = Path(__file__).resolve().parent

TEMPLATE_PATH = SCRIPT_DIR / "template.html"
CSS_PATH = SCRIPT_DIR / "minimal.css"

# Project FILE STRUCTURE

PROJECT_DIR = DOC_PATH.parent
BASE_NAME = PROJECT_DIR.name

DOCS_DIR = PROJECT_DIR / "docs"
FILES_DIR = DOCS_DIR / "files"

DOCS_DIR.mkdir(exist_ok=True)
FILES_DIR.mkdir(parents=True, exist_ok=True)

INDEX_PATH = DOCS_DIR / "index.html"

# Generate index.html

content = TEMPLATE_PATH.read_text(encoding="utf-8")

content = (
    content
    .replace("[title]", TITLE)
    .replace("[author]", AUTHOR)
    .replace("[desc]", DESC)
    .replace("[ten-tep]", BASE_NAME)
)

INDEX_PATH.write_text(content, encoding="utf-8")


env = os.environ.copy()
env.update({
    "TITLE": TITLE,
    "AUTHOR": AUTHOR,
    "DOC_PATH": str(DOC_PATH),
    "BASE_NAME": BASE_NAME,
    "FILES_DIR": str(FILES_DIR),
    "CSS_PATH": str(CSS_PATH),
})

subprocess.run(
    ["bash", str(SCRIPT_DIR / "build.sh")],
    check=True,
    env=env
)

print(f"Hoàn tất: {DOCS_DIR}")
