# 📘 DP trên cây - Chọn tập đỉnh độc lập lớn nhất (Maximum Independent Set)
# Mỗi đỉnh có giá trị. Chọn tập đỉnh sao cho không có 2 đỉnh kề nhau và tổng giá trị lớn nhất.

# ✅ Ý tưởng:
# dp[u][0] = max tổng khi không chọn u
# dp[u][1] = max tổng khi chọn u

from collections import defaultdict

n = 5
values = [1, 2, 3, 4, 5]  # giá trị từng node
edges = [(0,1),(0,2),(1,3),(1,4)]
tree = defaultdict(list)
for u, v in edges:
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 0] for _ in range(n)]  # [not take, take]
visited = [False] * n

def dfs(u, parent):
    dp[u][1] = values[u]  # chọn u
    for v in tree[u]:
        if v == parent: continue
        dfs(v, u)
        dp[u][0] += max(dp[v][0], dp[v][1])
        dp[u][1] += dp[v][0]  # nếu chọn u thì con không được chọn

dfs(0, -1)
print("Tổng lớn nhất:", max(dp[0][0], dp[0][1]))

# 🧠 Ghi nhớ:
# - Luôn chạy dfs từ gốc
# - dp[u][0] = chọn tốt nhất từ con mà không chọn u
# - dp[u][1] = chọn u → con không được chọn
# - Thường gặp trong bài chọn nút, phân nhóm, cây nhị phân
