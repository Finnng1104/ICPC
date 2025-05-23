# 📚 Tổng quan chủ đề SẮP XẾP (Sorting) - ICPC

## ✅ Mục tiêu:

- Ôn lại các thuật toán sắp xếp cơ bản và nâng cao
- Hiểu rõ khi nào nên dùng từng loại
- Biết ứng dụng sắp xếp trong bài toán thực tế
- Làm quen với `sort()` trong Python và các kỹ thuật `key`, `lambda`

---

## 🔢 Danh sách thuật toán cần nắm:

| Thuật toán     | Độ phức tạp | Ổn định | Khi nào dùng                    |
| -------------- | ----------- | ------- | ------------------------------- |
| Bubble Sort    | O(n²)       | ✅      | Dễ học, minh hoạ cơ bản         |
| Selection Sort | O(n²)       | ❌      | Học cơ chế chọn min             |
| Insertion Sort | O(n²)       | ✅      | Mảng gần sắp xếp                |
| Merge Sort     | O(n log n)  | ✅      | Cần ổn định, chia để trị        |
| Quick Sort     | O(n log n)  | ❌      | Nhanh, chia để trị, thường dùng |
| Heap Sort      | O(n log n)  | ❌      | Không đệ quy, dùng heap         |

> _Ghi nhớ_:
>
> - `sort()` trong Python dùng **Timsort** (ổn định, O(n log n))

---

## 🧠 Một số mẹo thường gặp:

- Dùng `arr.sort(key=lambda x: x[1])` để sắp theo nhiều tiêu chí
- `sorted()` trả về list mới, `sort()` thay đổi list tại chỗ
- Có thể sắp xếp đảo ngược bằng `reverse=True`

---

## 📌 Các bài toán thực tế:

| Dạng bài                      | Gợi ý thuật toán |
| ----------------------------- | ---------------- |
| Sắp xếp theo nhiều trường     | Python `key=`    |
| Tìm phần tử thứ K sau sắp xếp | QuickSort + đếm  |
| Đếm số cặp nghịch thế         | MergeSort        |
| Sắp xếp chuỗi, từ             | Python sort      |

---

## 📁 Cấu trúc thư mục kèm theo:

```
SapXep/
├── 2_thuat_toan/
│   ├── bubble_sort.py
│   ├── quick_sort.py
│   ├── merge_sort.py
├── 3_bai_tap_mau/
│   ├── count_inversions.py
│   ├── sort_strings.py
```

---

## ✅ Checklist ôn tập:

- [ ] Biết viết lại các sort cơ bản
- [ ] Biết dùng `sort()` với `key`
- [ ] Biết ứng dụng Merge Sort để đếm nghịch thế
- [ ] Biết cách chọn thuật toán phù hợp

> File này là nền tảng để bạn ôn các thuật toán sắp xếp thi ICPC. Nên đọc trước khi làm bài.
