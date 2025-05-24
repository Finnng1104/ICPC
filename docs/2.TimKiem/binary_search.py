# 🔎 Binary Search - Tìm kiếm nhị phân

# ✅ Bài toán ví dụ:
# Cho mảng đã sắp xếp tăng dần arr và số x, kiểm tra xem x có trong mảng không?
# Nếu có, trả về vị trí đầu tiên. Nếu không, trả về -1.

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

# 📌 Ví dụ sử dụng:
arr = [1, 3, 4, 5, 7, 9, 10]
x = 5
idx = binary_search(arr, x)
print(f"Tìm {x} → Kết quả: {idx}")

x = 6
idx = binary_search(arr, x)
print(f"Tìm {x} → Kết quả: {idx}")

# 💡 Giải thích:
# - Mỗi bước chia đôi mảng
# - Nếu phần tử giữa đúng → trả về
# - Nếu x nhỏ hơn → tìm bên trái; nếu lớn hơn → tìm bên phải
# - Độ phức tạp: O(log n)

# 🧠 Khi dùng:
# - Mảng đã sắp xếp
# - Truy vấn tìm kiếm nhiều
# - Phù hợp với dãy đúng/sai hoặc bài toán nhị phân
