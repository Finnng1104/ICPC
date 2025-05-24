# ICPC - Thuật toán đồ thị cơ bản và nâng cao
# Bao gồm biểu diễn, BFS, DFS, Dijkstra, Bellman-Ford, Floyd-Warshall, TopoSort, MST, SCC

import heapq
from collections import deque, defaultdict

# ==== 1. BIỂU DIỄN ĐỒ THỊ ====
"""
Có 3 cách biểu diễn chính:

1. Danh sách kề (Adjacency List):
   - Ưu điểm: 
     + Tiết kiệm bộ nhớ O(V + E)
     + Duyệt các đỉnh kề nhanh
     + Phù hợp với đồ thị thưa
   - Nhược điểm:
     + Kiểm tra tồn tại cạnh chậm O(degree(v))
     + Không phù hợp với đồ thị dày
   - Mục đích: Biểu diễn đồ thị thưa, ít cạnh

2. Ma trận kề (Adjacency Matrix):
   - Ưu điểm:
     + Kiểm tra tồn tại cạnh nhanh O(1)
     + Dễ cài đặt
   - Nhược điểm:
     + Tốn bộ nhớ O(V²)
     + Không hiệu quả với đồ thị thưa
   - Mục đích: Biểu diễn đồ thị dày, nhiều cạnh

3. Đồ thị có trọng số (Weighted Graph):
   - Ưu điểm:
     + Lưu được thông tin trọng số
     + Vẫn giữ được ưu điểm của danh sách kề
   - Nhược điểm:
     + Tốn thêm bộ nhớ cho trọng số
   - Mục đích: Biểu diễn đồ thị có trọng số trên cạnh
"""

# Danh sách kề (ưu tiên dùng trong ICPC)
graph_list = defaultdict(list)  # Tự động tạo list rỗng cho các node mới
graph_list[0].append(1)  # Thêm cạnh từ node 0 đến node 1
graph_list[1].append(2)  # Thêm cạnh từ node 1 đến node 2

# Ma trận kề (ít dùng nếu n lớn)
n = 4  # Số đỉnh
adj_matrix = [[0]*n for _ in range(n)]  # Khởi tạo ma trận nxn với giá trị 0
adj_matrix[0][1] = 1  # Thêm cạnh từ node 0 đến node 1
adj_matrix[1][2] = 1  # Thêm cạnh từ node 1 đến node 2

# Có trọng số (dùng tuple)
weighted_graph = defaultdict(list)
weighted_graph[0].append((1, 5))  # (node, weight) - cạnh từ 0 đến 1 với trọng số 5

# ==== 2. BFS (Breadth-First Search) ====
"""
Mục đích sử dụng:
- Tìm đường đi ngắn nhất (số cạnh) từ start đến các đỉnh khác
- Kiểm tra tính liên thông
- Tìm thành phần liên thông
- Kiểm tra đồ thị 2 phía

Ưu điểm:
- Luôn tìm được đường đi ngắn nhất (nếu có)
- Đơn giản, dễ cài đặt
- Phù hợp với đồ thị không có trọng số

Nhược điểm:
- Không phù hợp với đồ thị có trọng số
- Tốn bộ nhớ khi đồ thị rộng
- Không tối ưu cho việc tìm đường đi có trọng số

Độ phức tạp: O(V + E) với V là số đỉnh, E là số cạnh
"""

def bfs(graph, start):
    visited = set()  # Tập các đỉnh đã thăm
    queue = deque([start])  # Hàng đợi chứa các đỉnh cần thăm
    
    while queue:  # Lặp khi còn đỉnh trong hàng đợi
        node = queue.popleft()  # Lấy đỉnh đầu tiên ra
        if node in visited:  # Bỏ qua nếu đã thăm
            continue
        visited.add(node)  # Đánh dấu đã thăm
        print("BFS visit:", node)  # In ra đỉnh đang thăm
        for neighbor in graph[node]:  # Duyệt các đỉnh kề
            queue.append(neighbor)  # Thêm vào hàng đợi

# ==== 3. DFS (Depth-First Search) ====
"""
Mục đích sử dụng:
- Tìm chu trình
- Kiểm tra tính liên thông
- Tìm thành phần liên thông
- Sắp xếp topo (với DAG)
- Tìm đường đi Euler

Ưu điểm:
- Tiết kiệm bộ nhớ (chỉ lưu đường đi hiện tại)
- Phù hợp với việc khám phá sâu
- Hiệu quả cho việc tìm chu trình

Nhược điểm:
- Không đảm bảo tìm được đường đi ngắn nhất
- Có thể bị tràn stack với đồ thị quá sâu
- Không phù hợp với việc tìm đường đi ngắn nhất

Độ phức tạp: O(V + E) với V là số đỉnh, E là số cạnh
"""

def dfs(graph, node, visited=None):
    if visited is None:  # Khởi tạo visited nếu chưa có
        visited = set()
    if node in visited:  # Dừng nếu đã thăm
        return
    visited.add(node)  # Đánh dấu đã thăm
    print("DFS visit:", node)  # In ra đỉnh đang thăm
    for neighbor in graph[node]:  # Duyệt các đỉnh kề
        dfs(graph, neighbor, visited)  # Đệ quy thăm đỉnh kề

# ==== 4. Dijkstra ====
"""
Mục đích sử dụng:
- Tìm đường đi ngắn nhất từ một đỉnh đến tất cả các đỉnh khác
- Chỉ áp dụng cho đồ thị có trọng số không âm

Ưu điểm:
- Hiệu quả với đồ thị có trọng số không âm
- Sử dụng heap để tối ưu thời gian
- Luôn tìm được đường đi ngắn nhất

Nhược điểm:
- Không xử lý được trọng số âm
- Độ phức tạp cao hơn BFS
- Cần cài đặt heap

Độ phức tạp: O((V + E)logV) với V là số đỉnh, E là số cạnh
"""

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}  # Khởi tạo khoảng cách vô cùng
    dist[start] = 0  # Khoảng cách từ start đến chính nó là 0
    heap = [(0, start)]  # Heap ưu tiên theo khoảng cách
    
    while heap:
        d, u = heapq.heappop(heap)  # Lấy đỉnh có khoảng cách nhỏ nhất
        if d > dist[u]: continue  # Bỏ qua nếu đã có đường đi tốt hơn
        
        for v, w in graph[u]:  # Duyệt các đỉnh kề
            if dist[v] > dist[u] + w:  # Nếu tìm thấy đường đi tốt hơn
                dist[v] = dist[u] + w  # Cập nhật khoảng cách
                heapq.heappush(heap, (dist[v], v))  # Thêm vào heap
    return dist

# ==== 5. Bellman-Ford ====
"""
Mục đích sử dụng:
- Tìm đường đi ngắn nhất từ một đỉnh đến tất cả các đỉnh khác
- Có thể xử lý trọng số âm
- Phát hiện chu trình âm

Ưu điểm:
- Xử lý được trọng số âm
- Phát hiện được chu trình âm
- Đơn giản, dễ cài đặt

Nhược điểm:
- Độ phức tạp cao O(VE)
- Chậm hơn Dijkstra
- Không hiệu quả với đồ thị lớn

Độ phức tạp: O(VE) với V là số đỉnh, E là số cạnh
"""

def bellman_ford(edges, n, start):
    dist = [float('inf')] * n  # Khởi tạo khoảng cách vô cùng
    dist[start] = 0  # Khoảng cách từ start đến chính nó là 0
    
    # Lặp n-1 lần để cập nhật khoảng cách
    for _ in range(n - 1):
        for u, v, w in edges:  # Duyệt tất cả các cạnh
            if dist[u] + w < dist[v]:  # Nếu tìm thấy đường đi tốt hơn
                dist[v] = dist[u] + w  # Cập nhật khoảng cách
    
    # Kiểm tra chu trình âm
    for u, v, w in edges:
        if dist[u] + w < dist[v]:  # Nếu vẫn có thể cập nhật
            return "Chu trình âm"  # Tồn tại chu trình âm
    return dist

# ==== 6. Floyd-Warshall ====
"""
Mục đích sử dụng:
- Tìm đường đi ngắn nhất giữa mọi cặp đỉnh
- Có thể xử lý trọng số âm
- Phát hiện chu trình âm

Ưu điểm:
- Tìm được đường đi ngắn nhất giữa mọi cặp đỉnh
- Xử lý được trọng số âm
- Phát hiện được chu trình âm

Nhược điểm:
- Độ phức tạp cao O(V³)
- Không hiệu quả với đồ thị lớn
- Tốn bộ nhớ O(V²)

Độ phức tạp: O(V³) với V là số đỉnh
"""

def floyd_warshall(matrix):
    n = len(matrix)  # Số đỉnh
    
    # Khởi tạo ma trận khoảng cách
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0 and i != j:
                matrix[i][j] = float('inf')
    
    # Cập nhật khoảng cách qua từng đỉnh trung gian
    for k in range(n):  # Đỉnh trung gian
        for i in range(n):  # Đỉnh nguồn
            for j in range(n):  # Đỉnh đích
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    return matrix

# ==== 7. Topological Sort ====
"""
Mục đích sử dụng:
- Sắp xếp các đỉnh theo thứ tự topo
- Chỉ áp dụng cho DAG (Directed Acyclic Graph)
- Dùng trong lập lịch, biên dịch

Ưu điểm:
- Đơn giản, dễ cài đặt
- Hiệu quả với DAG
- Phát hiện được chu trình

Nhược điểm:
- Chỉ áp dụng được cho DAG
- Không xử lý được đồ thị có chu trình
- Cần DFS để cài đặt

Độ phức tạp: O(V + E) với V là số đỉnh, E là số cạnh
"""

def topo_sort(graph, n):
    visited = [False]*n  # Mảng đánh dấu đỉnh đã thăm
    stack = []  # Stack lưu thứ tự topo
    
    def dfs_topo(u):
        visited[u] = True  # Đánh dấu đã thăm
        for v in graph[u]:  # Duyệt các đỉnh kề
            if not visited[v]:  # Nếu chưa thăm
                dfs_topo(v)  # Đệ quy thăm
        stack.append(u)  # Thêm vào stack khi backtrack
    
    # Duyệt tất cả các đỉnh
    for i in range(n):
        if not visited[i]:
            dfs_topo(i)
    return stack[::-1]  # Đảo ngược stack để có thứ tự topo

# ==== 8. Minimum Spanning Tree (Kruskal) ====
"""
Mục đích sử dụng:
- Tìm cây khung nhỏ nhất
- Kết nối tất cả các đỉnh với tổng trọng số nhỏ nhất
- Dùng trong thiết kế mạng, clustering

Ưu điểm:
- Đơn giản, dễ cài đặt
- Hiệu quả với đồ thị thưa
- Sử dụng DSU để tối ưu

Nhược điểm:
- Cần sắp xếp cạnh
- Không hiệu quả với đồ thị dày
- Cần cài đặt DSU

Độ phức tạp: O(ElogE) với E là số cạnh
"""

class DSU:
    """Disjoint Set Union - Cấu trúc dữ liệu để quản lý các tập hợp rời rạc"""
    def __init__(self, n):
        self.parent = list(range(n))  # Mảng cha của mỗi đỉnh
    
    def find(self, x):
        """Tìm đại diện của tập chứa x"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Nén đường đi
        return self.parent[x]
    
    def union(self, x, y):
        """Hợp nhất hai tập chứa x và y"""
        rx, ry = self.find(x), self.find(y)
        if rx == ry: return False  # Đã cùng tập
        self.parent[ry] = rx  # Gán ry làm con của rx
        return True

def kruskal(n, edges):
    dsu = DSU(n)  # Khởi tạo DSU
    mst_weight = 0  # Tổng trọng số cây khung
    edges.sort(key=lambda x: x[2])  # Sắp xếp cạnh theo trọng số
    
    for u, v, w in edges:  # Duyệt các cạnh theo thứ tự trọng số
        if dsu.union(u, v):  # Nếu hợp nhất được
            mst_weight += w  # Cộng trọng số vào kết quả
    return mst_weight

# ==== 9. Tarjan's Algorithm (Strongly Connected Components - SCC) ====
"""
Mục đích sử dụng:
- Tìm các thành phần liên thông mạnh
- Phân tích đồ thị có hướng
- Dùng trong biên dịch, phân tích chương trình

Ưu điểm:
- Tìm được tất cả SCC trong một lần duyệt
- Hiệu quả với đồ thị lớn
- Có thể phát hiện chu trình

Nhược điểm:
- Khó cài đặt
- Cần hiểu rõ về DFS
- Cần quản lý nhiều biến trạng thái

Độ phức tạp: O(V + E) với V là số đỉnh, E là số cạnh
"""

# Biến toàn cục cho Tarjan
index = 0  # Chỉ số cho mỗi đỉnh
stack = []  # Stack lưu các đỉnh đang xét
on_stack = set()  # Tập các đỉnh trong stack
indices = {}  # Chỉ số của mỗi đỉnh
lowlink = {}  # Giá trị lowlink của mỗi đỉnh
SCCs = []  # Danh sách các SCC

def tarjan(graph):
    def strongconnect(v):
        """Hàm DFS để tìm SCC chứa đỉnh v"""
        global index
        indices[v] = lowlink[v] = index  # Khởi tạo chỉ số và lowlink
        index += 1
        stack.append(v)  # Thêm vào stack
        on_stack.add(v)  # Đánh dấu trong stack

        for w in graph[v]:  # Duyệt các đỉnh kề
            if w not in indices:  # Chưa thăm
                strongconnect(w)  # Đệ quy thăm
                lowlink[v] = min(lowlink[v], lowlink[w])  # Cập nhật lowlink
            elif w in on_stack:  # Đã thăm và trong stack
                lowlink[v] = min(lowlink[v], indices[w])  # Cập nhật lowlink

        if lowlink[v] == indices[v]:  # Tìm thấy SCC
            scc = []
            while True:
                w = stack.pop()  # Lấy đỉnh ra khỏi stack
                on_stack.remove(w)  # Xóa khỏi tập on_stack
                scc.append(w)  # Thêm vào SCC
                if w == v:  # Đã lấy hết SCC
                    break
            SCCs.append(scc)  # Thêm SCC vào kết quả

    # Duyệt tất cả các đỉnh
    for v in graph:
        if v not in indices:
            strongconnect(v)
    return SCCs

# ==== 10. A* Search Algorithm ====
"""
Mục đích sử dụng:
- Tìm đường đi ngắn nhất có heuristic
- Tối ưu hóa tìm kiếm với hàm đánh giá
- Dùng trong game, AI, robotics

Ưu điểm:
- Hiệu quả hơn Dijkstra với heuristic tốt
- Luôn tìm được đường đi ngắn nhất
- Có thể tùy chỉnh heuristic

Nhược điểm:
- Cần hàm heuristic tốt
- Tốn bộ nhớ hơn Dijkstra
- Khó cài đặt hơn

Độ phức tạp: O(ElogV) với V là số đỉnh, E là số cạnh
"""

def a_star(graph, start, goal, heuristic):
    open_set = [(heuristic[start], 0, start)]  # (f, g, node) - f = g + h
    came_from = {}  # Lưu đường đi
    g_score = defaultdict(lambda: float('inf'))  # Khoảng cách từ start
    g_score[start] = 0  # Khoảng cách từ start đến chính nó

    while open_set:
        _, g, current = heapq.heappop(open_set)  # Lấy đỉnh có f nhỏ nhất

        if current == goal:  # Đã đến đích
            path = []
            while current in came_from:  # Truy vết đường đi
                path.append(current)
                current = came_from[current]
            return path[::-1] + [goal]  # Trả về đường đi

        for neighbor, weight in graph[current]:  # Duyệt các đỉnh kề
            tentative_g = g + weight  # Khoảng cách mới
            if tentative_g < g_score[neighbor]:  # Nếu tốt hơn
                came_from[neighbor] = current  # Cập nhật đường đi
                g_score[neighbor] = tentative_g  # Cập nhật khoảng cách
                f = tentative_g + heuristic[neighbor]  # Tính f
                heapq.heappush(open_set, (f, tentative_g, neighbor))  # Thêm vào heap

    return []  # Không tìm thấy đường đi

# ==== 11. Johnson's Algorithm ====
"""
Mục đích sử dụng:
- Tìm đường đi ngắn nhất giữa mọi cặp đỉnh
- Xử lý được trọng số âm
- Tối ưu hơn Floyd-Warshall

Ưu điểm:
- Hiệu quả hơn Floyd-Warshall
- Xử lý được trọng số âm
- Không cần ma trận kề

Nhược điểm:
- Phức tạp hơn Floyd-Warshall
- Cần chạy Bellman-Ford và Dijkstra
- Không hiệu quả với đồ thị dày

Độ phức tạp: O(VElogV) với V là số đỉnh, E là số cạnh
"""

def johnson(graph, n):
    # Bước 1: Thêm đỉnh mới nối đến tất cả đỉnh khác
    new_graph = defaultdict(list, graph)
    for u in range(n):
        new_graph[n].append((u, 0))  # Thêm cạnh với trọng số 0

    # Bước 2: Chạy Bellman-Ford từ đỉnh mới
    dist = [float('inf')] * (n + 1)
    dist[n] = 0
    for _ in range(n):
        for u in new_graph:
            for v, w in new_graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    # Bước 3: Điều chỉnh trọng số
    reweight = defaultdict(list)
    for u in graph:
        for v, w in graph[u]:
            rw = w + dist[u] - dist[v]  # Trọng số mới
            reweight[u].append((v, rw))

    # Bước 4: Chạy Dijkstra từ mỗi đỉnh
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
        return [d[i] + dist[i] - dist[src] for i in range(n)]  # Điều chỉnh lại khoảng cách

    return [dijkstra(u) for u in range(n)]  # Trả về ma trận khoảng cách

# ==== 12. Edmonds-Karp Algorithm (Luồng cực đại) ====
"""
Mục đích sử dụng:
- Tìm luồng cực đại trong mạng
- Giải quyết bài toán ghép cặp
- Tối ưu hóa mạng

Ưu điểm:
- Đơn giản, dễ cài đặt
- Luôn tìm được luồng cực đại
- Sử dụng BFS để tìm đường tăng

Nhược điểm:
- Chậm hơn Dinic
- Không hiệu quả với mạng lớn
- Cần ma trận kề

Độ phức tạp: O(VE²) với V là số đỉnh, E là số cạnh
"""

def edmonds_karp(capacity, s, t):
    n = len(capacity)  # Số đỉnh
    flow = [[0]*n for _ in range(n)]  # Ma trận luồng
    max_flow = 0  # Giá trị luồng cực đại

    while True:
        parent = [-1]*n  # Mảng cha để truy vết
        q = deque([s])  # Queue cho BFS
        while q:
            u = q.popleft()
            for v in range(n):
                # Nếu còn khả năng tăng luồng và chưa thăm
                if capacity[u][v] - flow[u][v] > 0 and parent[v] == -1:
                    parent[v] = u
                    q.append(v)
        if parent[t] == -1:  # Không còn đường tăng
            break

        # Tìm giá trị tăng luồng nhỏ nhất
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
            flow[u][v] += f  # Tăng luồng thuận
            flow[v][u] -= f  # Giảm luồng ngược
            v = u
        max_flow += f  # Cập nhật giá trị luồng cực đại

    return max_flow

# ==== 13. Dinic's Algorithm (Luồng cực đại tối ưu) ====
"""
Mục đích sử dụng:
- Tìm luồng cực đại trong mạng
- Tối ưu hơn Edmonds-Karp
- Giải quyết bài toán ghép cặp lớn

Ưu điểm:
- Nhanh hơn Edmonds-Karp
- Hiệu quả với mạng lớn
- Sử dụng level graph

Nhược điểm:
- Phức tạp hơn Edmonds-Karp
- Khó cài đặt
- Cần quản lý nhiều cấu trúc dữ liệu

Độ phức tạp: O(V²E) với V là số đỉnh, E là số cạnh
"""

class Dinic:
    def __init__(self, n):
        self.n = n  # Số đỉnh
        self.graph = [[] for _ in range(n)]  # Danh sách kề
        self.cap = {}  # Từ điển lưu sức chứa

    def add_edge(self, u, v, c):
        """Thêm cạnh từ u đến v với sức chứa c"""
        self.graph[u].append(v)  # Thêm cạnh thuận
        self.graph[v].append(u)  # Thêm cạnh ngược
        self.cap[(u, v)] = c  # Sức chứa cạnh thuận
        self.cap[(v, u)] = 0  # Sức chứa cạnh ngược

    def bfs(self, s, t, level):
        """BFS để xây dựng level graph"""
        q = deque([s])
        level[s] = 0
        while q:
            u = q.popleft()
            for v in self.graph[u]:
                # Nếu còn khả năng tăng luồng và chưa có level
                if self.cap[(u, v)] > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] != -1  # Trả về True nếu tìm được đường tăng

    def dfs(self, u, t, f, level, next_):
        """DFS để tìm đường tăng trong level graph"""
        if u == t:  # Đã đến đích
            return f
        for i in range(next_[u], len(self.graph[u])):
            v = self.graph[u][i]
            # Nếu còn khả năng tăng luồng và đúng level
            if self.cap[(u, v)] > 0 and level[v] == level[u] + 1:
                pushed = self.dfs(v, t, min(f, self.cap[(u, v)]), level, next_)
                if pushed:  # Nếu tìm được đường tăng
                    self.cap[(u, v)] -= pushed  # Giảm sức chứa cạnh thuận
                    self.cap[(v, u)] += pushed  # Tăng sức chứa cạnh ngược
                    return pushed
            next_[u] += 1  # Tăng con trỏ next
        return 0  # Không tìm được đường tăng

    def max_flow(self, s, t):
        """Tìm luồng cực đại từ s đến t"""
        flow = 0  # Giá trị luồng cực đại
        level = [-1]*self.n  # Mảng level
        while self.bfs(s, t, level):  # Lặp khi còn đường tăng
            next_ = [0]*self.n  # Mảng con trỏ next
            while True:
                pushed = self.dfs(s, t, float('inf'), level, next_)  # Tìm đường tăng
                if not pushed:  # Không còn đường tăng
                    break
                flow += pushed  # Cập nhật giá trị luồng
            level = [-1]*self.n  # Reset level
        return flow

print("\n✅ Đã bổ sung chi tiết các thuật toán đồ thị với giải thích, mục đích, ưu/nhược điểm và độ phức tạp.")