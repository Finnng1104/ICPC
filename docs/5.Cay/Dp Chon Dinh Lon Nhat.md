# 📘 DP TRÊN CÂY - Chọn đỉnh lớn nhất sao cho không kề nhau (Maximum Independent Set)

# Cho cây có trọng số tại mỗi đỉnh. Chọn một tập các đỉnh sao cho:

# - Không có 2 đỉnh nào kề nhau

# - Tổng trọng số là lớn nhất

from collections import defaultdict

n = 7
values = [1, 2, 3, 4, 5, 6, 7] # giá trị tại mỗi đỉnh
edges = [
(0, 1), (0, 2),
(1, 3), (1, 4),
(2, 5), (2, 6)
]
tree = defaultdict(list)
for u, v in edges:
tree[u].append(v)
tree[v].append(u)

dp = [[0, 0] for \_ in range(n)] # dp[u][0] = không chọn u, dp[u][1] = chọn u

def dfs(u, p):
dp[u][1] = values[u]
for v in tree[u]:
if v == p: continue
dfs(v, u)
dp[u][0] += max(dp[v][0], dp[v][1]) # không chọn u → chọn hoặc không chọn con
dp[u][1] += dp[v][0] # nếu chọn u → con không được chọn

dfs(0, -1)

print("Tổng giá trị lớn nhất:", max(dp[0][0], dp[0][1]))

# 🧠 Ghi nhớ:

# - Trạng thái dp[u][0]: max nếu không chọn u

# - Trạng thái dp[u][1]: max nếu chọn u

# - Không được chọn cả cha và con → cây là trường hợp lý tưởng để DP theo DFS
