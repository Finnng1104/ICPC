# ICPC - Thuật toán Cây, Lý thuyết trò chơi, Grid map & nâng cao
# Bao gồm DFS cây, LCA, Minimax, Grundy, BFS trên lưới
# Ứng dụng: Game AI, Tìm đường, Phân tích cấu trúc cây

from collections import deque

# ==== 0. Giới thiệu và ứng dụng thực tế ====
"""
Các thuật toán trong file này có nhiều ứng dụng thực tế:

1. Thuật toán cây:
   - Phân tích cấu trúc dữ liệu phân cấp
   - Tìm kiếm tổ tiên chung
   - Quản lý hệ thống file
   - Phân tích mạng xã hội

2. Lý thuyết trò chơi:
   - AI cho game (cờ vua, cờ tướng)
   - Phân tích chiến lược
   - Tối ưu hóa quyết định
   - Game theory trong kinh tế

3. Grid map:
   - Tìm đường trong game
   - Robot navigation
   - Phát hiện va chạm
   - Mô phỏng môi trường

Ví dụ thực tế:
1. Game AI: Minimax cho cờ vua
2. Social Network: LCA để tìm quan hệ
3. Game Development: BFS cho pathfinding
4. Competitive Programming: Grundy cho game theory
"""

# ==== 1. DFS trên cây ====
"""
Mục đích: Duyệt và phân tích cấu trúc cây

Cách hoạt động (cho người mới):
1. DFS (Depth-First Search):
   - Đi sâu nhất có thể theo một nhánh
   - Quay lui khi gặp lá
   - Lưu thông tin về cha và độ sâu

2. Ứng dụng:
   - Tìm đường đi từ gốc đến lá
   - Tính toán các giá trị trên cây
   - Phân tích cấu trúc cây

Ví dụ thực tế:
- Phân tích cây gia phả
- Quản lý thư mục
- Phân tích mạng xã hội
"""

def dfs_tree(u, parent, depth, graph, par, dep):
    """
    Duyệt cây bằng DFS và lưu thông tin
    
    Tham số:
    - u: node hiện tại
    - parent: node cha
    - depth: độ sâu hiện tại
    - graph: danh sách kề của cây
    - par: mảng lưu node cha
    - dep: mảng lưu độ sâu
    """
    # Lưu thông tin node hiện tại
    par[u] = parent
    dep[u] = depth
    
    # Duyệt các node con
    for v in graph[u]:
        if v != parent:  # Tránh quay lại node cha
            dfs_tree(v, u, depth + 1, graph, par, dep)

# ==== 2. Lowest Common Ancestor (LCA) ====
"""
Mục đích: Tìm tổ tiên chung gần nhất của hai node

Cách hoạt động (cho người mới):
1. LCA là node chung gần nhất của hai node
2. Các bước tìm LCA:
   - Đưa hai node về cùng độ sâu
   - Đi lên cha cho đến khi gặp nhau
3. Ứng dụng:
   - Tìm quan hệ họ hàng
   - Tính khoảng cách trên cây
   - Tối ưu hóa truy vấn

Ví dụ thực tế:
- Tìm quan hệ trong gia phả
- Phân tích mạng xã hội
- Tìm đường đi ngắn nhất trên cây
"""

def lca(u, v, par, dep):
    """
    Tìm tổ tiên chung thấp nhất của hai node
    
    Tham số:
    - u, v: hai node cần tìm LCA
    - par: mảng lưu node cha
    - dep: mảng lưu độ sâu
    
    Trả về: node LCA
    """
    # Đưa hai node về cùng độ sâu
    while dep[u] > dep[v]:
        u = par[u]
    while dep[v] > dep[u]:
        v = par[v]
    
    # Đi lên cha cho đến khi gặp nhau
    while u != v:
        u = par[u]
        v = par[v]
    
    return u

# ==== 3. Minimax (Game 2 người) ====
"""
Mục đích: Tìm nước đi tối ưu trong game hai người

Cách hoạt động (cho người mới):
1. Minimax là thuật toán:
   - Người chơi 1 (Max) muốn điểm cao nhất
   - Người chơi 2 (Min) muốn điểm thấp nhất
   - Luân phiên chọn nước đi tốt nhất

2. Ứng dụng:
   - AI cho game cờ
   - Phân tích chiến lược
   - Tối ưu hóa quyết định

Ví dụ thực tế:
- AI cờ vua, cờ tướng
- Game đối kháng
- Phân tích rủi ro
"""

def minimax(depth, is_max, values, left, right):
    """
    Tìm giá trị tối ưu theo minimax
    
    Tham số:
    - depth: độ sâu hiện tại
    - is_max: True nếu là lượt Max
    - values: mảng giá trị
    - left, right: phạm vi xét
    
    Trả về: giá trị tối ưu
    """
    # Trường hợp cơ sở
    if left == right:
        return values[left]
    
    # Lượt Max: chọn giá trị lớn nhất
    if is_max:
        return max(
            minimax(depth+1, False, values, left, (left+right)//2),
            minimax(depth+1, False, values, (left+right)//2+1, right)
        )
    # Lượt Min: chọn giá trị nhỏ nhất
    else:
        return min(
            minimax(depth+1, True, values, left, (left+right)//2),
            minimax(depth+1, True, values, (left+right)//2+1, right)
        )

# ==== 4. Grundy Number (Game Theory) ====
"""
Mục đích: Phân tích trạng thái thắng/thua trong game

Cách hoạt động (cho người mới):
1. Grundy Number:
   - 0: trạng thái thua
   - >0: trạng thái thắng
   - Tính bằng MEX (Minimum EXcluded)

2. Ứng dụng:
   - Phân tích game đơn giản
   - Kết hợp nhiều game
   - Tìm chiến lược thắng

Ví dụ thực tế:
- Game Nim
- Game đố
- Phân tích rủi ro
"""

def grundy(n):
    """
    Tính Grundy Number cho trạng thái n
    
    Tham số:
    - n: trạng thái hiện tại
    
    Trả về: Grundy Number
    """
    # Trạng thái 0 là thua
    if n == 0:
        return 0
    
    # Tập các Grundy Number có thể đạt được
    s = set()
    for x in range(1, n+1):
        s.add(grundy(n - x))
    
    # Tìm MEX (Minimum EXcluded)
    g = 0
    while g in s:
        g += 1
    
    return g

# ==== 5. BFS trên lưới - Grid map ====
"""
Mục đích: Tìm đường đi ngắn nhất trên lưới

Cách hoạt động (cho người mới):
1. BFS (Breadth-First Search):
   - Mở rộng theo mọi hướng
   - Đảm bảo đường đi ngắn nhất
   - Tránh các ô cấm

2. Ứng dụng:
   - Tìm đường trong game
   - Robot navigation
   - Phát hiện va chạm

Ví dụ thực tế:
- Game mê cung
- Robot di chuyển
- Tìm đường tối ưu
"""

def bfs_grid(grid, sx, sy, ex, ey):
    """
    Tìm đường đi ngắn nhất trên lưới
    
    Tham số:
    - grid: ma trận lưới ('.' là đường đi, '#' là cấm)
    - sx, sy: điểm bắt đầu
    - ex, ey: điểm kết thúc
    
    Trả về: độ dài đường đi ngắn nhất, -1 nếu không tìm thấy
    """
    n, m = len(grid), len(grid[0])
    visited = [[False]*m for _ in range(n)]
    q = deque([(sx, sy, 0)])  # (x, y, distance)
    visited[sx][sy] = True
    
    # 4 hướng di chuyển: lên, xuống, trái, phải
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]

    while q:
        x, y, d = q.popleft()
        
        # Đã đến đích
        if (x, y) == (ex, ey):
            return d
            
        # Thử các hướng di chuyển
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            # Kiểm tra hợp lệ và chưa thăm
            if (0 <= nx < n and 0 <= ny < m and 
                grid[nx][ny] != '#' and not visited[nx][ny]):
                visited[nx][ny] = True
                q.append((nx, ny, d+1))
    
    return -1  # Không tìm thấy đường đi

# ==== Demo ====
if __name__ == "__main__":
    print("\n=== Demo các thuật toán với ví dụ thực tế ===")
    
    # 1. Demo cây và LCA
    print("\n1. Phân tích cây gia phả:")
    tree = {
        0: [1, 2],  # 0 là gốc, có 2 con là 1 và 2
        1: [0, 3],  # 1 có con là 3
        2: [0],     # 2 là lá
        3: [1]      # 3 là lá
    }
    par = [-1]*4  # Mảng lưu cha
    dep = [0]*4   # Mảng lưu độ sâu
    
    # Duyệt cây từ gốc
    dfs_tree(0, -1, 0, tree, par, dep)
    print("Cấu trúc cây:")
    print("      0")
    print("    /   \\")
    print("   1     2")
    print("  /")
    print(" 3")
    print(f"LCA(3,2) = {lca(3,2,par,dep)} (tổ tiên chung gần nhất)")
    
    # 2. Demo Minimax
    print("\n2. Phân tích game:")
    values = [3, 5, 2, 9]  # Giá trị các nước đi
    print("Giá trị các nước đi:", values)
    print(f"Giá trị tối ưu (Max) = {minimax(0, True, values, 0, 3)}")
    
    # 3. Demo Grundy
    print("\n3. Phân tích trạng thái game:")
    n = 4
    print(f"Grundy({n}) = {grundy(n)}")
    print("> 0: trạng thái thắng")
    print("= 0: trạng thái thua")
    
    # 4. Demo Grid BFS
    print("\n4. Tìm đường trên lưới:")
    grid = [
        ['.','.','.'],  # . là đường đi
        ['#','#','.'],  # # là cấm
        ['.','.','.']
    ]
    print("Lưới:")
    for row in grid:
        print(row)
    print(f"Đường đi ngắn nhất từ (0,0) đến (2,2) = {bfs_grid(grid, 0, 0, 2, 2)}")
    
    print("\n✅ Đã demo các thuật toán cây, game theory và grid map.")
