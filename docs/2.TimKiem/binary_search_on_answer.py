# 🧠 Binary Search on Answer - Nhị phân trên miền kết quả

# ✅ Bài toán ví dụ:
# Có N cây, chiều cao từng cây là h[i]. Bạn có thể cắt mỗi cây xuống độ cao H bất kỳ,
# phần dư ra sẽ gom lại. Tìm H lớn nhất sao cho tổng phần dư >= M.

# ➕ Đây là bài toán kinh điển dùng binary search trên miền kết quả (0 → max(h))

def check(h, heights, M):
    total = sum(max(0, tree - h) for tree in heights)
    return total >= M

def binary_search_answer(heights, M):
    l, r = 0, max(heights)
    res = 0
    while l <= r:
        mid = (l + r) // 2
        if check(mid, heights, M):
            res = mid
            l = mid + 1  # cố gắng tăng H hơn nữa
        else:
            r = mid - 1
    return res

# 📌 Ví dụ:
heights = [20, 15, 10, 17]
M = 7
print(f"Chiều cao cắt lớn nhất có thể: {binary_search_answer(heights, M)}")

# 💡 Giải thích:
# - Mỗi H → ta kiểm tra tổng gỗ cắt được (qua hàm check)
# - Nếu đủ gỗ → thử tăng H để tối ưu
# - Nếu thiếu → giảm H
# - Tìm max H thỏa mãn điều kiện → nhị phân

# 🧠 Khi gặp bài tìm min/max thoả mãn điều kiện → luôn nghĩ đến BS on answer
