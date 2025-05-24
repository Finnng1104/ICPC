# 🎒 Bài toán Balo 0/1 (0/1 Knapsack)
# ----------------------------------------
# ✅ Mô tả:
# Cho n vật, mỗi vật có trọng lượng w[i] và giá trị v[i]
# Chọn một tập không vượt quá trọng lượng W sao cho tổng giá trị là lớn nhất

# ✅ Quy hoạch động:
# dp[i][j] = max giá trị với i vật đầu tiên, tổng khối lượng ≤ j

# ✅ Độ phức tạp: O(nW)

# ----------------------------------------

def knapsack_01(n, W, w, v):
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(W + 1):
            if j >= w[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - w[i-1]] + v[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]

# 📌 Ví dụ:
n = 4
W = 8
w = [3, 4, 5, 2]  # trọng lượng
v = [2, 3, 4, 3]  # giá trị
print("Tối đa hóa giá trị:", knapsack_01(n, W, w, v))

# 🧠 Ghi chú:
# - Với mỗi vật, có 2 lựa chọn: chọn hoặc không
# - Nếu chọn: phải đảm bảo đủ trọng lượng
# - Nếu không chọn: giữ nguyên giá trị tối ưu cũ
# - Đây là một trong các dạng DP quan trọng nhất
# - Có thể tối ưu xuống 1D: dp[j] = max(dp[j], dp[j - w[i]] + v[i]) từ j=W về 0
