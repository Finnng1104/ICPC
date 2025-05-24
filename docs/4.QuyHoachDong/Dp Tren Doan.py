# 📘 DP trên đoạn (Interval DP)
# Ví dụ: Cắt dây lấy tiền
# Có đoạn dây dài L, muốn cắt tại các điểm cho trước, mỗi lần cắt tốn chi phí bằng chiều dài đoạn đang cắt.
# Tính tổng chi phí nhỏ nhất để cắt hoàn toàn

# ✅ Quy hoạch động:
# dp[i][j] = chi phí tối thiểu để cắt đoạn từ điểm i đến j

INF = int(1e9)

def min_cost_cut(L, cuts):
    cuts = [0] + sorted(cuts) + [L]
    n = len(cuts)
    dp = [[0]*n for _ in range(n)]

    for length in range(2, n):  # khoảng cách giữa i và j
        for i in range(n - length):
            j = i + length
            dp[i][j] = INF
            for k in range(i + 1, j):
                cost = cuts[j] - cuts[i] + dp[i][k] + dp[k][j]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n-1]

# 📌 Ví dụ:
L = 10
cuts = [2, 4, 7]
print("Chi phí cắt tối thiểu:", min_cost_cut(L, cuts))

# 🧠 Ý tưởng:
# - Cắt tại điểm k tốn chi phí = chiều dài đoạn (j - i)
# - dp[i][j] = min tất cả các cách chọn điểm k ở giữa i..j
# - Phù hợp với bài: ghép chuỗi, phân đoạn, gộp tập con liên tiếp
