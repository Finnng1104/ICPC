# ICPC - Thuật toán sắp xếp cơ bản + khi nào dùng
# Bao gồm: QuickSort, MergeSort, HeapSort, BubbleSort, SelectionSort, InsertionSort + Luồng chạy

import heapq

# ==== 1. QuickSort ====
# Trung bình O(n log n), tệ nhất O(n^2), không ổn định
# Dùng khi dữ liệu lớn, cần tốc độ, không cần giữ thứ tự
# Luồng chạy: Chọn pivot → chia thành 2 nửa → đệ quy từng nửa

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

# ==== 2. MergeSort ====
# Luôn O(n log n), ổn định, cần thêm bộ nhớ phụ
# Dùng khi cần ổn định, hoặc xử lý chuỗi/lưu thứ tự
# Luồng chạy: Chia đôi mảng → đệ quy 2 nửa → trộn đã sắp

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res + left[i:] + right[j:]

# ==== 3. HeapSort ====
# O(n log n), không ổn định, không cần thêm bộ nhớ
# Dùng khi cần đảm bảo O(n log n) trong mọi trường hợp
# Luồng chạy: heapify → liên tục pop ra phần tử nhỏ nhất

def heapsort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

# ==== 4. BubbleSort ====
# O(n^2), đơn giản, dễ cài
# Dùng để minh họa, không dùng cho dữ liệu lớn
# Luồng chạy: duyệt qua mảng → hoán đổi các cặp sai thứ tự

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# ==== 5. SelectionSort ====
# O(n^2), dễ hiểu, không ổn định
# Chọn phần tử nhỏ nhất mỗi lần
# Luồng chạy: tìm phần tử nhỏ nhất từ i → n, hoán đổi với i

def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# ==== 6. InsertionSort ====
# Tốt cho mảng nhỏ, gần như đã sắp xếp; O(n^2)
# Ổn định
# Luồng chạy: chèn từng phần tử vào vị trí đúng phía trước nó

def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# ==== Demo ====
arr = [5, 1, 4, 2, 8, 3]
print("QuickSort:", quicksort(arr[:]))
print("MergeSort:", mergesort(arr[:]))
print("HeapSort:", heapsort(arr[:]))
print("BubbleSort:", bubblesort(arr[:]))
print("SelectionSort:", selectionsort(arr[:]))
print("InsertionSort:", insertionsort(arr[:]))

# ==== Gợi ý khi nào dùng ====
# - QuickSort: dữ liệu lớn, không cần ổn định
# - MergeSort: cần ổn định, xử lý danh sách lớn (ví dụ log ghi)
# - HeapSort: đảm bảo O(n log n), không cần nhớ thêm
# - Bubble/Selection/Insertion: dùng minh họa, dạy học, hoặc mảng nhỏ đã gần đúng

print("\n✅ Đã tổng hợp các thuật toán sắp xếp cơ bản kèm khi nên dùng và luồng chạy chi tiết.")
