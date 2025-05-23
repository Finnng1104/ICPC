# ICPC - Thuật toán Cây, Lý thuyết trò chơi, Grid map & nâng cao
# Bao gồm DFS cây, LCA, Minimax, Grundy, BFS trên lưới

from collections import deque

# ==== 1. DFS trên cây ====
# Lưu cha, chiều sâu, tổng trọng số từ gốc

def dfs_tree(u, parent, depth, graph, par, dep):
    par[u] = parent
    dep[u] = depth
    for v in graph[u]:
        if v != parent:
            dfs_tree(v, u, depth + 1, graph, par, dep)

# ==== 2. Lowest Common Ancestor (LCA) cơ bản ====
# Trả về đỉnh tổ tiên chung thấp nhất giữa 2 node u, v

def lca(u, v, par, dep):
    while dep[u] > dep[v]:
        u = par[u]
    while dep[v] > dep[u]:
        v = par[v]
    while u != v:
        u = par[u]
        v = par[v]
    return u

# ==== 3. Minimax (Game 2 người) ====
# Dùng để chơi cờ, chọn nước đi tốt nhất

def minimax(depth, is_max, values, left, right):
    if left == right:
        return values[left]
    if is_max:
        return max(minimax(depth+1, False, values, left, (left+right)//2),
                   minimax(depth+1, False, values, (left+right)//2+1, right))
    else:
        return min(minimax(depth+1, True, values, left, (left+right)//2),
                   minimax(depth+1, True, values, (left+right)//2+1, right))

# ==== 4. Grundy Number (Game lý thuyết trò chơi) ====
# Grundy = 0 là trạng thái thua, >0 là thắng

def grundy(n):
    if n == 0:
        return 0
    s = set()
    for x in range(1, n+1):
        s.add(grundy(n - x))
    g = 0
    while g in s:
        g += 1
    return g

# ==== 5. BFS trên lưới - Grid map ====
# Tìm đường đi ngắn nhất từ (sx, sy) đến (ex, ey)

def bfs_grid(grid, sx, sy, ex, ey):
    n, m = len(grid), len(grid[0])
    visited = [[False]*m for _ in range(n)]
    q = deque([(sx, sy, 0)])
    visited[sx][sy] = True
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]

    while q:
        x, y, d = q.popleft()
        if (x, y) == (ex, ey):
            return d
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#' and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, d+1))
    return -1

# ==== Demo ====
# Cây:      0
#         /   \
#        1     2
#       /
#      3

tree = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
par = [-1]*4
dep = [0]*4
dfs_tree(0, -1, 0, tree, par, dep)
print("LCA(3,2):", lca(3,2,par,dep))

values = [3, 5, 2, 9]
print("Minimax value:", minimax(0, True, values, 0, 3))
print("Grundy(4):", grundy(4))

grid = [
    ['.','.','.'],
    ['#','#','.'],
    ['.','.','.']
]
print("Shortest path on grid:", bfs_grid(grid, 0, 0, 2, 2))

print("\n✅ Đã bổ sung cây, lý thuyết trò chơi, grid map với ví dụ minh hoạ.")
