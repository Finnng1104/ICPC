# 📘 Tính Độ Sâu (depth), Cha (parent) và Kích Thước Subtree (số con)

# Mỗi đỉnh lưu độ sâu từ gốc, cha của nó, và số lượng node trong nhánh con

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
subtree_size = [0] \* n

def dfs_info(u, p):
parent[u] = p
subtree_size[u] = 1 # tính chính nó
for v in tree[u]:
if v != p:
depth[v] = depth[u] + 1
dfs_info(v, u)
subtree_size[u] += subtree_size[v]

dfs_info(0, -1)

print("Độ sâu:", depth)
print("Cha:", parent)
print("Kích thước subtree:", subtree_size)

# 🧠 Giải thích:

# - `depth[u]`: số bước từ gốc đến u

# - `parent[u]`: cha của u trong cây

# - `subtree_size[u]`: tổng số đỉnh trong nhánh có gốc là u (bao gồm cả u)
