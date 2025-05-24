# 📘 Quy hoạch động - Dãy con tăng dài nhất (LIS)

# ✅ Bài toán:
# Cho một dãy số nguyên a[] có n phần tử.
# Tìm độ dài dãy con tăng dài nhất (không cần liên tiếp).

# Ví dụ: a = [10, 9, 2, 5, 3, 7, 101, 18] → LIS là [2, 3, 7, 101] → độ dài = 4

# 🧠 Ý tưởng:
# dp[i] = độ dài LIS kết thúc tại chỉ số i
# Với mỗi i, xét các j < i sao cho a[j] < a[i] → dp[i] = max(dp[j]) + 1

def LIS(a):
    n = len(a)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# 📌 Ví dụ:
a = [10, 9, 2, 5, 3, 7, 101, 18]
print("Độ dài LIS:", LIS(a))

# 💡 Giải thích:
# - Khởi tạo dp[i] = 1 vì mỗi phần tử là dãy dài nhất có thể tại chính nó
# - Với mỗi i, duyệt lại tất cả j < i và cập nhật dp[i] nếu tìm được phần tử tăng
# - Độ phức tạp: O(n^2), có thể tối ưu O(n log n) bằng binary search

# 🧠 Khi dùng:
# - Bài toán chọn phần tử rời rạc sao cho tăng dần dài nhất
# - Các bài tương tự: dãy con giảm, dãy con chia hết, dãy tăng đoạn con,...