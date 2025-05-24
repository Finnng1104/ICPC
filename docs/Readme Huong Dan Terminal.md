# 📗 Hướng Dẫn Sử Dụng Terminal Cho Dự Án ICPC

## ❓ Khi nào cần đọc file này?

- Mỗi khi **mở terminal mới** hoặc **mở lại máy tính** để chạy các file Python trong dự án.
- Nếu bạn thấy lỗi như:
  - `command not found: pip`
  - `python: can't open file '3'` hoặc `No such file or directory`

---

## ✅ Các bước chuẩn để chạy file Python

### 🔹 1. Mở Terminal ở đúng thư mục gốc

```bash
cd ~/Documents/ICPC\ Python/ICPC
```

> 📝 Thư mục `ICPC` chứa code `.py`, còn `icpc-env/` cũng nằm tại đây.

---

### 🔹 2. Kích hoạt môi trường ảo

```bash
source icpc-env/bin/activate
```

> Sau lệnh này bạn sẽ thấy dấu `(icpc-env)` ở đầu dòng terminal → là đã thành công.

---

### 🔹 3. Chạy file Python

```bash
python3 ten_file.py
```

✅ Ví dụ:

```bash
python3 test_import.py
```

📛 **Sai lầm thường gặp**:

```bash
python 3 test_import.py    # ❌ sai vì "3" là tên file chứ không phải python3
```

---

### 🔹 4. Thoát khỏi môi trường (khi cần)

```bash
deactivate
```

---

## 🧠 Mẹo:

- Không cần gõ lại `pip install` mỗi lần mở terminal nếu đã cài xong.
- Luôn kiểm tra mình đang đứng đúng thư mục bằng:
  ```bash
  pwd
  ls
  ```
- Nếu `source icpc-env/bin/activate` bị lỗi `no such file or directory`, kiểm tra lại:
  ```bash
  ls icpc-env/bin/
  ```

---

## 📦 Kiểm tra thư viện đã cài

```bash
pip list
```

---

> Đây là quy trình an toàn và chuẩn nhất để đảm bảo bạn luôn chạy đúng môi trường, đúng file trong mọi lần sử dụng Terminal.
