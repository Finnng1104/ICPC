# 📘 DFS CƠ BẢN TRÊN CÂY

# Mô tả: Duyệt cây bằng DFS, in ra thứ tự thăm các đỉnh

from collections import defaultdict

# Khởi tạo cây dạng danh sách kề

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

# DFS từ gốc 0

visited = [False] \* 7

def dfs(u):
visited[u] = True
print("Thăm:", u)
for v in tree[u]:
if not visited[v]:
dfs(v)

dfs(0)

# 🧠 Giải thích:

# - Cây có 7 đỉnh (0 đến 6), không chu trình

# - DFS là đệ quy từ gốc 0, thăm con trái trước phải sau (tuỳ thứ tự trong tree)

# - Mỗi đỉnh được đánh dấu visited khi đã đi qua để tránh lặp vô hạn

# - Kết quả là một thứ tự thăm toàn bộ cây
