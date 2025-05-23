# 📚 TỔNG QUÁT CHỦ ĐỀ TÌM KIẾM - ICPC

## ✅ Mục tiêu:

- Hiểu và áp dụng các thuật toán tìm kiếm cơ bản: tuyến tính, nhị phân
- Nắm được kỹ thuật mở rộng tìm kiếm: lower_bound, upper_bound
- Nhận biết khi nào cần tìm kiếm và áp dụng đúng dạng

---

## 🔍 1. Tìm kiếm tuyến tính (Linear Search)

### 🔹 Ý tưởng:

- Duyệt toàn bộ mảng để tìm giá trị
- Đơn giản nhưng chậm: O(n)

### 🔹 Khi dùng:

- Mảng chưa sắp xếp
- N <= 10^5 vẫn chấp nhận được nếu ít truy vấn

```python
# Tìm x trong mảng:
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # trả về vị trí đầu tiên
    return -1
```

---

## 🔍 2. Tìm kiếm nhị phân (Binary Search)

### 🔹 Ý tưởng:

- Áp dụng cho mảng đã sắp xếp
- Chia đôi và loại bỏ 1 nửa mỗi lượt: O(log n)

### 🔹 Khi dùng:

- Mảng / dãy đã sắp xếp
- Dạng "có thể quy về tìm đoạn đúng/sai liên tiếp"

```python
# Binary search cơ bản:
def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1
```

---

## 🔍 3. Lower Bound / Upper Bound (BS mở rộng)

### 🔹 Lower Bound:

- Tìm vị trí đầu tiên có giá trị >= x

### 🔹 Upper Bound:

- Tìm vị trí đầu tiên có giá trị > x

```python
# Lower Bound:
def lower_bound(arr, x):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l

# Upper Bound:
def upper_bound(arr, x):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] <= x:
            l = mid + 1
        else:
            r = mid
    return l
```

---

## 🧠 Mẹo nhận biết đề dùng Binary Search:

| Dạng đề                                    | Nhận biết                            |
| ------------------------------------------ | ------------------------------------ |
| Tìm min/max thỏa mãn điều kiện             | "Tìm giá trị nhỏ nhất lớn nhất thỏa" |
| Có thể chia đoạn thành Đúng - Sai          | BS có thể áp dụng trên miền liên tục |
| Dạng truy vấn tìm vị trí trong mảng        | Dữ liệu đã sắp xếp + truy vấn nhiều  |
| Dạng tối ưu hóa (ex: tìm min thời gian đủ) | Thường là Binary Search trên kết quả |

---

## 📁 Cấu trúc gợi ý

```
TimKiem/
├── linear_search.py
├── binary_search.py
├── lower_upper_bound.py
├── 1_overview.md
```

---

## ✅ Checklist ôn tập:

- [ ] Hiểu rõ từng loại tìm kiếm
- [ ] Biết khi nào dùng BS, khi nào không nên
- [ ] Biết áp dụng lower/upper bound để giải nhanh hơn
- [ ] Làm quen Binary Search trên miền kết quả (0 → 10^18)

> Chủ đề quan trọng, xuất hiện rất nhiều trong các bài thi ICPC. Nắm chắc để áp dụng kết hợp với DP, Greedy, Two Pointer...

# 📚 TỔNG QUÁT CHỦ ĐỀ TÌM KIẾM - ICPC

## ✅ Mục tiêu:

- Hiểu và áp dụng các thuật toán tìm kiếm cơ bản: tuyến tính, nhị phân
- Nắm được kỹ thuật mở rộng tìm kiếm: lower_bound, upper_bound
- Nhận biết khi nào cần tìm kiếm và áp dụng đúng dạng

---

## 🔍 1. Tìm kiếm tuyến tính (Linear Search)

### 🔹 Ý tưởng:

- Duyệt toàn bộ mảng để tìm giá trị
- Đơn giản nhưng chậm: O(n)

### 🔹 Khi dùng:

- Mảng chưa sắp xếp
- N <= 10^5 vẫn chấp nhận được nếu ít truy vấn

```python
# Tìm x trong mảng:
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # trả về vị trí đầu tiên
    return -1
```

---

## 🔍 2. Tìm kiếm nhị phân (Binary Search)

### 🔹 Ý tưởng:

- Áp dụng cho mảng đã sắp xếp
- Chia đôi và loại bỏ 1 nửa mỗi lượt: O(log n)

### 🔹 Khi dùng:

- Mảng / dãy đã sắp xếp
- Dạng "có thể quy về tìm đoạn đúng/sai liên tiếp"

```python
# Binary search cơ bản:
def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1
```

---

## 🔍 3. Lower Bound / Upper Bound (BS mở rộng)

### 🔹 Lower Bound:

- Tìm vị trí đầu tiên có giá trị >= x

### 🔹 Upper Bound:

- Tìm vị trí đầu tiên có giá trị > x

```python
# Lower Bound:
def lower_bound(arr, x):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l

# Upper Bound:
def upper_bound(arr, x):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] <= x:
            l = mid + 1
        else:
            r = mid
    return l
```

---

## 🧠 Mẹo nhận biết đề dùng Binary Search:

| Dạng đề                                    | Nhận biết                            |
| ------------------------------------------ | ------------------------------------ |
| Tìm min/max thỏa mãn điều kiện             | "Tìm giá trị nhỏ nhất lớn nhất thỏa" |
| Có thể chia đoạn thành Đúng - Sai          | BS có thể áp dụng trên miền liên tục |
| Dạng truy vấn tìm vị trí trong mảng        | Dữ liệu đã sắp xếp + truy vấn nhiều  |
| Dạng tối ưu hóa (ex: tìm min thời gian đủ) | Thường là Binary Search trên kết quả |

---

## 📂 Gợi ý tổ chức file:

```
TimKiem/
├── linear_search.py
├── binary_search.py
├── lower_upper_bound.py
├── bs_on_answer.py
├── 1_overview.md
```

---

## ✅ Checklist ôn tập (Đã triển khai mẫu):

### ✅ Hiểu rõ từng loại tìm kiếm

- Tuyến tính: duyệt đơn giản, áp dụng khi chưa sắp
- Nhị phân: yêu cầu mảng sắp xếp, hoặc tìm kết quả trên miền liên tục
- Lower/Upper Bound: tìm vị trí chèn, số lần xuất hiện

### ✅ Biết khi nào dùng BS, khi nào không nên

- BS áp dụng khi tồn tại cấu trúc "đúng → sai" hoặc dãy có thứ tự
- Không áp dụng nếu không thể xác định ranh giới đúng/sai

### ✅ Biết áp dụng lower/upper bound để giải nhanh hơn

```python
# Ví dụ: đếm số phần tử <= x trong mảng đã sắp:
import bisect
arr = [1, 2, 2, 4, 5, 5, 5, 7, 9]
x = 5
print("Số phần tử <= 5:", bisect.bisect_right(arr, x))
```

### ✅ Làm quen Binary Search trên miền kết quả (0 → 10^18)

```python
# Tìm min x sao cho check(x) == True:
def binary_search_on_answer(lo, hi, check):
    while lo < hi:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

# Ví dụ:
def check(x): return x * x >= 30
print("Min x sao cho x^2 >= 30:", binary_search_on_answer(0, int(1e9), check))
```

> Đã đủ toàn bộ checklist học và ứng dụng tìm kiếm trong ICPC.
