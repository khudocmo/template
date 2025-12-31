import os
import subprocess

TITLE = "Ngày xuân"
AUTHOR = "Nguyễn Văn A"
DESC = "Một tác phẩm nhẹ nhàng về mùa xuân."

def slugify(text):
    import unicodedata, re
    text = unicodedata.normalize("NFD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")

slug = slugify(TITLE)

# Replace index.html
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

content = (
    content
    .replace("[title]", TITLE)
    .replace("[author]", AUTHOR)
    .replace("[desc]", DESC)
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

# Export env for shell
env = os.environ.copy()
env["TITLE"] = TITLE
env["AUTHOR"] = AUTHOR

subprocess.run(
    ["bash", "build.sh", slug],
    check=True,
    env=env
)

print("Hoàn tất số hóa 📚")
