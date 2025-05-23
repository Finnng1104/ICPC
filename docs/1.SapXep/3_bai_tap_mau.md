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

```python
# bubble_sort.py
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([5, 2, 4, 1]))
```

## 🔹 Selection Sort

**Ý tưởng**: Với mỗi vị trí, tìm phần tử nhỏ nhất còn lại và đưa vào đúng chỗ.

```python
# selection_sort.py
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([5, 2, 4, 1]))
```

## 🔹 Insertion Sort

**Ý tưởng**: Giống như xếp bài – đưa phần tử vào đúng chỗ trong đoạn đã sắp xếp.

```python
# insertion_sort.py
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertion_sort([5, 2, 4, 1]))
```

## 🔹 Merge Sort

**Ý tưởng**: Chia mảng → đệ quy sắp xếp → trộn hai mảng đã sắp

```python
# merge_sort.py
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:] + right[j:]
    return merged

print(merge_sort([5, 2, 4, 1]))
```

## 🔹 Quick Sort

**Ý tưởng**: Chọn pivot → chia thành phần nhỏ và lớn hơn → đệ quy sắp

```python
# quick_sort.py
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([5, 2, 4, 1]))
```

## 🔹 Heap Sort

**Ý tưởng**: Dùng heap để lấy phần tử nhỏ nhất liên tục

```python
# heap_sort.py
import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

print(heap_sort([5, 2, 4, 1]))
```

---

## 🔄 Sắp xếp theo nhiều tiêu chí (2 key, 3 key)

```python
# Sắp theo key1 tăng, nếu bằng thì theo key2 giảm
arr = [("A", 3), ("B", 2), ("C", 3), ("D", 1)]
sorted_arr = sorted(arr, key=lambda x: (x[1], -ord(x[0][0])))
print("Sắp theo 2 key:", sorted_arr)

# Sắp theo key1, key2, key3
arr3 = [("A", 3, 7), ("B", 3, 4), ("C", 2, 5), ("D", 3, 4)]
sorted_3 = sorted(arr3, key=lambda x: (x[1], x[2], x[0]))
print("Sắp theo 3 key:", sorted_3)
```

> Luôn ưu tiên sắp xếp bằng `sorted()` hoặc `list.sort()` với `key=` để tùy biến.
