# 📘 LCA ĐƠN GIẢN - Lowest Common Ancestor

# Tìm tổ tiên chung thấp nhất của 2 đỉnh u, v trong cây

# Cách đơn giản: đưa 2 đỉnh về cùng độ sâu, sau đó cùng đi lên cha đến khi gặp nhau

from collections import defaultdict

tree = defaultdict(list)
edges = [
(0, 1),
(0, 2),
(1, 3),
(1, 4),
(2, 5),
(2, 6)
]
for u, v in edges:
tree[u].append(v)
tree[v].append(u)

n = 7
parent = [-1] _ n
depth = [0] _ n

def dfs(u, p):
parent[u] = p
for v in tree[u]:
if v != p:
depth[v] = depth[u] + 1
dfs(v, u)

dfs(0, -1)

def lca(u, v):
while depth[u] > depth[v]:
u = parent[u]
while depth[v] > depth[u]:
v = parent[v]
while u != v:
u = parent[u]
v = parent[v]
return u

# 📌 Ví dụ:

print("LCA của 3 và 4:", lca(3, 4)) # → 1
print("LCA của 3 và 5:", lca(3, 5)) # → 0

# 🧠 Ghi nhớ:

# - Phù hợp với số lượng truy vấn ít

# - Độ phức tạp mỗi lần là O(h) với h là chiều cao cây

# - Nếu cần xử lý nhiều truy vấn → dùng Binary Lifting (nâng cao)
