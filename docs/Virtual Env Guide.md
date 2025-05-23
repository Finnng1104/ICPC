# 🛠️ Hướng dẫn sử dụng Virtual Environment (icpc-env) trong dự án ICPC

## ✅ Mục đích của Virtual Environment

Virtual environment (môi trường ảo) giúp bạn:

- Cài thư viện Python độc lập cho từng dự án
- Tránh xung đột giữa các thư viện toàn hệ thống
- Quản lý dễ dàng các package cần thiết khi thi offline (ICPC, hackathon,...)

---

## 📁 Cấu trúc chuẩn:

```
ICPC/
├── icpc-env/            # ⚠️ Không lưu code ở đây!
├── code/                # ✅ Code Python chính
├── docs/                # ✅ Tài liệu Markdown, PDF
```

---

## 🔄 Cách kích hoạt môi trường ảo

### 👉 Bước 1: Tạo virtual env (chỉ cần tạo 1 lần)

```bash
python3 -m venv icpc-env
```

### 👉 Bước 2: Kích hoạt (mỗi lần mở terminal mới)

```bash
source icpc-env/bin/activate
```

> Nếu đúng, bạn sẽ thấy dòng terminal đổi thành:

```bash
(icpc-env) user@your-laptop ICPC %
```

---

## ⚙️ Cài thư viện sau khi kích hoạt

```bash
pip install opencv-python pillow numpy torch torchvision
```

### 👉 Ghi lại các thư viện đã cài:

```bash
pip freeze > requirements.txt
```

### 👉 Cài lại sau này chỉ cần:

```bash
pip install -r requirements.txt
```

---

## ❗ Lưu ý quan trọng

- KHÔNG lưu `.py`, `.md`, `.pdf` trong thư mục `icpc-env/`
- PHẢI kích hoạt `source icpc-env/bin/activate` trước khi chạy bất kỳ file `.py` nào

---

## ✅ Kiểm tra đã kích hoạt chưa?

Chạy thử:

```bash
which python
```

Nếu đúng sẽ trả ra đường dẫn trong `icpc-env/bin/python`

---

## 💡 Mẹo tự động kích hoạt khi vào thư mục (nâng cao)

Nếu dùng `direnv`, có thể tạo file `.envrc`:

```bash
eval "$(direnv hook zsh)"
layout python3
source icpc-env/bin/activate
```

---

## 🧪 Test nhanh

Tạo file `test_import.py`:

```python
import cv2, numpy, torch, torchvision, PIL
print("✅ Virtual env hoạt động và đã cài đủ thư viện!")
```

---

> Đây là tài liệu bắt buộc nên có nếu bạn dùng virtual environment trong các dự án ICPC.
