# 📘 Đếm số lần mỗi cạnh xuất hiện trong các đường đi

# Bài toán: Cho cây có n đỉnh, m truy vấn. Mỗi truy vấn là một cặp (u, v).

# Với mỗi truy vấn, tăng count các cạnh nằm trên đường đi từ u đến v

# Mục tiêu: đếm số lần mỗi cạnh được đi qua

from collections import defaultdict

n = 7
edges = [
(0, 1), (0, 2),
(1, 3), (1, 4),
(2, 5), (2, 6)
]

tree = defaultdict(list)
for idx, (u, v) in enumerate(edges):
tree[u].append((v, idx)) # lưu kèm chỉ số cạnh
tree[v].append((u, idx))

parent = [-1] _ n
depth = [0] _ n

def dfs*init(u, p):
parent[u] = p
for v, * in tree[u]:
if v != p:
depth[v] = depth[u] + 1
dfs_init(v, u)

dfs_init(0, -1)

# Tìm đường đi từ u đến v, đánh dấu cạnh được đi qua

cnt = [0] \* len(edges)

def add_path(u, v):
while u != v:
if depth[u] < depth[v]:
u, v = v, u
for w, idx in tree[u]:
if w == parent[u]:
cnt[idx] += 1
break
u = parent[u]

# 📌 Truy vấn:

queries = [(3, 4), (3, 5), (6, 4)]
for u, v in queries:
add_path(u, v)

print("Số lần mỗi cạnh được đi qua:", cnt)

# 🧠 Ghi nhớ:

# - Với mỗi truy vấn (u, v), đi ngược lên cho đến khi gặp nhau

# - Tăng đếm ở mỗi cạnh gặp phải

# - Phù hợp cho m <= 1e5, cần tối ưu hơn nếu m lớn hơn (DSU on Tree / HLD)
