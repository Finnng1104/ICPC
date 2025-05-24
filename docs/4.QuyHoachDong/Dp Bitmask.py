# 📘 DP + Bitmask - Ví dụ Traveling Salesman Problem (TSP)
# Bài toán: Cho n thành phố và chi phí đi giữa mỗi cặp.
# Xuất phát từ thành phố 0, đi qua tất cả các thành phố đúng 1 lần rồi quay lại 0
# Tìm chi phí nhỏ nhất

# ✅ dp[mask][u] = chi phí nhỏ nhất để đi từ 0 đến u và đã đi qua các điểm có trong mask

INF = int(1e9)

def tsp(cost):
    n = len(cost)
    dp = [[INF]*n for _ in range(1<<n)]
    dp[1][0] = 0  # bắt đầu từ thành phố 0, chỉ đi qua 0

    for mask in range(1<<n):
        for u in range(n):
            if not (mask & (1<<u)): continue  # u chưa được thăm trong mask này
            for v in range(n):
                if mask & (1<<v): continue  # v đã đi rồi
                new_mask = mask | (1<<v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + cost[u][v])

    # quay lại 0
    return min(dp[(1<<n)-1][i] + cost[i][0] for i in range(n))

# 📌 Ví dụ:
cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print("Chi phí đi TSP:", tsp(cost))

# 🧠 Ghi nhớ:
# - mask là bit thể hiện trạng thái các điểm đã đi
# - Với mỗi trạng thái mask, duyệt u → v chưa đi
# - Tổng trạng thái: 2^n * n → dùng cho n <= 16
