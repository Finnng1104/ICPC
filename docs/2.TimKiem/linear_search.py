# 🔍 Linear Search - Tìm kiếm tuyến tính

# ✅ Bài toán ví dụ:
# Cho mảng arr và số x, tìm xem x có xuất hiện trong arr không?
# Nếu có, trả về chỉ số đầu tiên. Nếu không, trả về -1.

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Trả về vị trí đầu tiên tìm thấy
    return -1

# 📌 Ví dụ sử dụng:
arr = [5, 3, 7, 1, 4]
x = 1
idx = linear_search(arr, x)
print(f"Tìm {x} → Kết quả: {idx}")

x = 6
idx = linear_search(arr, x)
print(f"Tìm {x} → Kết quả: {idx}")

# 💡 Lý giải:
# - Duyệt lần lượt từng phần tử từ trái sang phải
# - So sánh với x → nếu bằng thì trả về luôn chỉ số
# - Nếu duyệt hết mà không thấy thì trả -1
# - Độ phức tạp: O(n)

# 🧠 Khi dùng:
# - Mảng chưa sắp xếp
# - Ít phần tử (N <= 10^5), không truy vấn nhiều lần
