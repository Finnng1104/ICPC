# ICPC - Thuật toán đồ thị cơ bản và nâng cao
# Bao gồm biểu diễn, BFS, DFS, Dijkstra, Bellman-Ford, Floyd-Warshall, TopoSort, MST, SCC

import heapq
from collections import deque, defaultdict

# ==== 1. Biểu diễn đồ thị ====
# Danh sách kề (ưu tiên dùng trong ICPC)
graph_list = defaultdict(list)
graph_list[0].append(1)
graph_list[1].append(2)

# Ma trận kề (ít dùng nếu n lớn)
n = 4
adj_matrix = [[0]*n for _ in range(n)]
adj_matrix[0][1] = 1
adj_matrix[1][2] = 1

# Có trọng số (dùng tuple)
weighted_graph = defaultdict(list)
weighted_graph[0].append((1, 5))  # (node, weight)

# ==== 2. BFS ====
# Duyệt theo chiều rộng
# Luồng chạy: Queue → đánh dấu đã thăm → duyệt theo tầng

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        print("BFS visit:", node)
        for neighbor in graph[node]:
            queue.append(neighbor)

# ==== 3. DFS ====
# Duyệt theo chiều sâu
# Luồng chạy: gọi đệ quy / dùng Stack → thăm sâu trước

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node in visited:
        return
    visited.add(node)
    print("DFS visit:", node)
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)

# ==== 4. Dijkstra ====
# Tìm đường đi ngắn nhất không âm, dùng heap
# Luồng chạy: ưu tiên đỉnh có khoảng cách nhỏ nhất chưa duyệt

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist

# ==== 5. Bellman-Ford ====
# Cho phép trọng số âm, phát hiện chu trình âm
# Luồng chạy: lặp n-1 lần cập nhật tất cả cạnh

def bellman_ford(edges, n, start):
    dist = [float('inf')] * n
    dist[start] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    # Check chu trình âm
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return "Chu trình âm"
    return dist

# ==== 6. Floyd-Warshall ====
# All-pairs shortest paths
# Luồng chạy: thử qua từng đỉnh trung gian k

def floyd_warshall(matrix):
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    return matrix

# ==== 7. Topological Sort ====
# Chỉ dùng với DAG
# Luồng chạy: DFS + thêm vào stack khi backtrack

def topo_sort(graph, n):
    visited = [False]*n
    stack = []
    def dfs_topo(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs_topo(v)
        stack.append(u)
    for i in range(n):
        if not visited[i]:
            dfs_topo(i)
    return stack[::-1]

# ==== 8. Minimum Spanning Tree (Kruskal) ====
# Chọn cạnh rẻ nhất không tạo chu trình
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry: return False
        self.parent[ry] = rx
        return True

def kruskal(n, edges):
    dsu = DSU(n)
    mst_weight = 0
    edges.sort(key=lambda x: x[2])  # sort by weight
    for u, v, w in edges:
        if dsu.union(u, v):
            mst_weight += w
    return mst_weight

# ==== 9. Tarjan's Algorithm (Strongly Connected Components - SCC) ====
# Luồng chạy: DFS + lowlink

index = 0
stack = []
on_stack = set()
indices = {}
lowlink = {}
SCCs = []

def tarjan(graph):
    def strongconnect(v):
        global index
        indices[v] = lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)

        for w in graph[v]:
            if w not in indices:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w in on_stack:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                scc.append(w)
                if w == v:
                    break
            SCCs.append(scc)

    for v in graph:
        if v not in indices:
            strongconnect(v)
    return SCCs

print("\n✅ Đã tổng hợp thuật toán đồ thị cơ bản và nâng cao với giải thích, ví dụ, luồng chạy.")

# ICPC - Thuật toán đồ thị nâng cao: A*, Johnson, Luồng cực đại (Edmonds-Karp, Dinic)
# Bao gồm giải thích, luồng chạy, ví dụ code

import heapq
from collections import deque, defaultdict

# ==== A* Search Algorithm ====
# Tìm đường đi ngắn nhất có heuristic (ví dụ: khoảng cách Euclid)
# Luồng chạy: giống Dijkstra nhưng ưu tiên f(n) = g(n) + h(n)

def a_star(graph, start, goal, heuristic):
    open_set = [(heuristic[start], 0, start)]  # (f, g, node)
    came_from = {}
    g_score = defaultdict(lambda: float('inf'))
    g_score[start] = 0

    while open_set:
        _, g, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1] + [goal]

        for neighbor, weight in graph[current]:
            tentative_g = g + weight
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic[neighbor]
                heapq.heappush(open_set, (f, tentative_g, neighbor))

    return []

# ==== Johnson’s Algorithm ====
# Dùng Bellman-Ford để chuẩn hóa trọng số, sau đó chạy Dijkstra nhiều lần
# Dùng cho đồ thị có trọng số âm (không có chu trình âm), all-pairs shortest paths

def johnson(graph, n):
    # Bước 1: thêm đỉnh mới nối đến tất cả đỉnh khác với trọng số 0
    new_graph = defaultdict(list, graph)
    for u in range(n):
        new_graph[n].append((u, 0))

    # Bước 2: chạy Bellman-Ford từ đỉnh mới
    dist = [float('inf')] * (n + 1)
    dist[n] = 0
    for _ in range(n):
        for u in new_graph:
            for v, w in new_graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    # Bước 3: điều chỉnh trọng số
    reweight = defaultdict(list)
    for u in graph:
        for v, w in graph[u]:
            rw = w + dist[u] - dist[v]
            reweight[u].append((v, rw))

    # Bước 4: chạy Dijkstra từ mỗi đỉnh
    def dijkstra(src):
        d = [float('inf')] * n
        d[src] = 0
        pq = [(0, src)]
        while pq:
            du, u = heapq.heappop(pq)
            if du > d[u]: continue
            for v, w in reweight[u]:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    heapq.heappush(pq, (d[v], v))
        return [d[i] + dist[i] - dist[src] for i in range(n)]

    result = [dijkstra(u) for u in range(n)]
    return result

# ==== Edmonds-Karp Algorithm (Luồng cực đại) ====
# Dùng BFS để tìm đường tăng (path augmenting)

def edmonds_karp(capacity, s, t):
    n = len(capacity)
    flow = [[0]*n for _ in range(n)]
    max_flow = 0

    while True:
        parent = [-1]*n
        q = deque([s])
        while q:
            u = q.popleft()
            for v in range(n):
                if capacity[u][v] - flow[u][v] > 0 and parent[v] == -1:
                    parent[v] = u
                    q.append(v)
        if parent[t] == -1:
            break  # không còn đường tăng

        # Tìm min capacity trên đường
        f = float('inf')
        v = t
        while v != s:
            u = parent[v]
            f = min(f, capacity[u][v] - flow[u][v])
            v = u

        # Cập nhật luồng
        v = t
        while v != s:
            u = parent[v]
            flow[u][v] += f
            flow[v][u] -= f
            v = u
        max_flow += f

    return max_flow

# ==== Dinic’s Algorithm (Luồng cực đại tối ưu hơn) ====
# BFS + DFS với nhiều mức độ (level graph)

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.cap = {}

    def add_edge(self, u, v, c):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.cap[(u, v)] = c
        self.cap[(v, u)] = 0

    def bfs(self, s, t, level):
        q = deque([s])
        level[s] = 0
        while q:
            u = q.popleft()
            for v in self.graph[u]:
                if self.cap[(u, v)] > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] != -1

    def dfs(self, u, t, f, level, next_):
        if u == t:
            return f
        for i in range(next_[u], len(self.graph[u])):
            v = self.graph[u][i]
            if self.cap[(u, v)] > 0 and level[v] == level[u] + 1:
                pushed = self.dfs(v, t, min(f, self.cap[(u, v)]), level, next_)
                if pushed:
                    self.cap[(u, v)] -= pushed
                    self.cap[(v, u)] += pushed
                    return pushed
            next_[u] += 1
        return 0

    def max_flow(self, s, t):
        flow = 0
        level = [-1]*self.n
        while self.bfs(s, t, level):
            next_ = [0]*self.n
            while True:
                pushed = self.dfs(s, t, float('inf'), level, next_)
                if not pushed:
                    break
                flow += pushed
            level = [-1]*self.n
        return flow

print("\n✅ Đã bổ sung A*, Johnson, Edmonds-Karp, Dinic với luồng chạy và code mẫu.")