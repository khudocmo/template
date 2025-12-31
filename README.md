# Trang xử lý sách

Trong thư mục docs sẽ có những tệp sau:

- `index.html`: Trang HTML chính - giới thiệu sách cũng như thông tin về sách và đường dẫn tải xuống.
- Trong thư mục `files` sẽ bao gồm:
    - `.epub`: Được tạo bằng `pandoc`.
    - `.azw3`: Được tạo bằng Calibre (`ebook-convert`).
    - `.html`: Được tạo bằng `pandoc`.

Toàn bộ các lệnh chạy đều được lưu trữ ở tệp [COMMAND.md](COMMAND.md)

## Viết một script xử lý

Chạy lệnh

```
python3 build.py
```