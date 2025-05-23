# 📘 Tổng hợp các thuật toán sắp xếp - ICPC

## ✅ Bảng tổng quan

| Thuật toán     | Độ phức tạp | Ổn định | Khi nào dùng                    |
| -------------- | ----------- | ------- | ------------------------------- |
| Bubble Sort    | O(n²)       | ✅      | Dễ học, minh hoạ cơ bản         |
| Selection Sort | O(n²)       | ❌      | Học cơ chế chọn min             |
| Insertion Sort | O(n²)       | ✅      | Mảng gần sắp xếp                |
| Merge Sort     | O(n log n)  | ✅      | Cần ổn định, chia để trị        |
| Quick Sort     | O(n log n)  | ❌      | Nhanh, chia để trị, thường dùng |
| Heap Sort      | O(n log n)  | ❌      | Không đệ quy, dùng heap         |

---

## 🔹 Bubble Sort

**Ý tưởng**: So sánh từng cặp kề nhau và hoán đổi nếu ngược thứ tự. Lặp lại nhiều lượt.

- Code đơn giản, dễ học
- Không hiệu quả với dữ liệu lớn

## 🔹 Selection Sort

**Ý tưởng**: Với mỗi vị trí, tìm phần tử nhỏ nhất còn lại và đưa vào đúng chỗ.

- Không ổn định
- Dễ minh hoạ tư tưởng chọn tham lam

## 🔹 Insertion Sort

**Ý tưởng**: Giống như cách xếp bài – lấy từng phần tử và chèn vào vị trí phù hợp trong đoạn đã sắp xếp.

- Tốt cho mảng nhỏ hoặc gần như đã sắp xếp
- Ổn định

## 🔹 Merge Sort

**Ý tưởng**: Chia mảng làm đôi, sắp xếp từng phần, rồi trộn lại (merge).

- Dùng trong đếm nghịch thế
- Ổn định, O(n log n), nhưng dùng nhiều bộ nhớ

## 🔹 Quick Sort

**Ý tưởng**: Chọn một phần tử làm pivot, chia mảng thành 2 phần (bé hơn, lớn hơn pivot), đệ quy.

- Rất nhanh trên thực tế
- Không ổn định

## 🔹 Heap Sort

**Ý tưởng**: Đưa mảng vào heap, rồi liên tục lấy phần tử min/max ra.

- Không cần đệ quy
- Không ổn định, dùng heapq hoặc tự cài heap

---

## 📂 Gợi ý tổ chức file:

```
2_thuat_toan/
├── bubble_sort.py
├── selection_sort.py
├── insertion_sort.py
├── merge_sort.py
├── quick_sort.py
├── heap_sort.py
```

> Mỗi file có thể gồm: định nghĩa hàm, ví dụ chạy thử, chú thích giải thích từng bước.
