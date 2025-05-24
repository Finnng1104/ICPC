# Bài toán: Kẻ trộm mang đồ với 1 tay + balo, tối đa hóa giá trị

def solve(n, W, H, items):
    dp = [0] * (W + 1)

    # Khởi tạo dp khi không dùng tay (balo)
    for i in range(n):
        w, c = items[i]
        for j in range(W, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + c)

    res = max(dp)  # Trường hợp không cầm tay

    # Thử từng món làm món cầm tay
    for i in range(n):
        w_hand, c_hand = items[i]
        if w_hand > H:
            continue  # Không thể cầm món này bằng tay

        # Loại bỏ món này khỏi balo
        # Dùng DP lại nhưng bỏ qua item[i]
        temp_dp = dp[:]  # sao chép dp đã tính toàn bộ
        w, c = items[i]
        for j in range(W, w - 1, -1):
            if temp_dp[j] == dp[j - w] + c:
                temp_dp[j] = dp[j - w]  # rollback món đang thử mang tay

        best_with_hand = max(temp_dp) + c_hand
        res = max(res, best_with_hand)

    return res


# ===============================
# Nhập dữ liệu
# ===============================
if __name__ == "__main__":
    import sys

    # Đọc số lượng món, trọng lượng balo, trọng lượng tay
    n, W, H = map(int, input().split())

    items = []
    for _ in range(n):
        w, c = map(int, input().split())
        items.append((w, c))

    print(solve(n, W, H, items))

# Input test
# n = 3
# W = 10
# H = 2
# items = [(2, 5), (1, 9), (4, 6)]
# print(solve(n, W, H, items))  # Output: 20

# n = 3
# W = 2
# H = 4
# items = [(2, 5), (1, 9), (4, 6)]
# print(solve(n, W, H, items))  # Output: 15


# Bài toán: Kẻ trộm mang đồ bằng balo và một tay
# Mục tiêu: tối đa hóa tổng trọng lượng (value), với chi phí (cost) không quá m (balo),
# và có thể thêm 1 món cầm tay nếu cost của nó <= h

import sys

n, m, h = map(int, input().split())
c = []  # cost (giá trị tiền phải trả để lấy món)
w = []  # weight (trọng lượng món)

for _ in range(n):
    ci, wi = map(int, input().split())
    c.append(ci)
    w.append(wi)

s = sum(w)  # tổng trọng lượng tối đa có thể xảy ra
INF = sys.maxsize

dp = [INF] * (s + 1)  # dp[i] = cost tối thiểu để đạt trọng lượng i
dp[0] = 0  # không lấy gì thì cost = 0

used = [0] * (s + 1)  # bitmask món đã dùng trong dp[i]

for i in range(n):
    for j in range(s, w[i] - 1, -1):
        if dp[j - w[i]] != INF:
            new_cost = dp[j - w[i]] + c[i]
            if new_cost < dp[j]:
                dp[j] = new_cost
                used[j] = used[j - w[i]] | (1 << i)  # đánh dấu đã dùng món i

ans = 0

for i in range(s + 1):
    if dp[i] <= m:  # nếu có thể mang bằng balo
        ans = max(ans, i)
        for j in range(n):  # thử từng món chưa dùng làm món cầm tay
            if not (used[i] & (1 << j)) and c[j] <= h:
                ans = max(ans, i + w[j])

print(ans)
