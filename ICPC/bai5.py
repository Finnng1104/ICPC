# 📝 Bài 5: Tìm tổ tiên chung gần nhất (LCA)
# ===============================================
"""
Đề bài: Cho một cây có N đỉnh, gốc là đỉnh 1.
Cho Q truy vấn, mỗi truy vấn yêu cầu tìm tổ tiên chung gần nhất
của hai đỉnh u và v.

Input:
- Dòng 1: N và Q (1 ≤ N,Q ≤ 10^5)
- N-1 dòng tiếp: Mỗi dòng gồm hai số u và v thể hiện cạnh nối
- Q dòng tiếp: Mỗi dòng gồm hai số u và v cần tìm LCA

Output:
- Q dòng, mỗi dòng là LCA của cặp đỉnh tương ứng

Ví dụ:
Input:
7 3
1 2
1 3
2 4
2 5
3 6
3 7
4 5
6 7
4 7

Output:
2
3
1
"""

from collections import defaultdict, deque

def solve():
    # Đọc input
    n, q = map(int, input().split())
    
    # Xây dựng cây
    tree = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
    
    # Tính toán các thông tin cần thiết cho LCA
    LOG = 20  # log2(10^5) ≈ 17
    parent = [[0]*(n+1) for _ in range(LOG)]
    depth = [0]*(n+1)
    
    # BFS để tính depth và parent[0]
    q_bfs = deque([1])
    visited = {1}
    parent[0][1] = 0  # Không có cha của gốc
    
    while q_bfs:
        u = q_bfs.popleft()
        for v in tree[u]:
            if v not in visited:
                visited.add(v)
                depth[v] = depth[u] + 1
                parent[0][v] = u
                q_bfs.append(v)
    
    # Tính bảng nhảy (sparse table)
    for k in range(1, LOG):
        for v in range(1, n+1):
            parent[k][v] = parent[k-1][parent[k-1][v]]
    
    def lca(u, v):
        # Đưa u và v về cùng độ sâu
        if depth[u] < depth[v]:
            u, v = v, u
        
        # Nhảy u lên để cùng độ sâu với v
        for k in range(LOG-1, -1, -1):
            if depth[u] - (1 << k) >= depth[v]:
                u = parent[k][u]
        
        if u == v:
            return u
        
        # Nhảy cả u và v lên cho đến khi gặp nhau
        for k in range(LOG-1, -1, -1):
            if parent[k][u] != parent[k][v]:
                u = parent[k][u]
                v = parent[k][v]
        
        return parent[0][u]
    
    # Xử lý các truy vấn
    for _ in range(q):
        u, v = map(int, input().split())
        print(lca(u, v))
    
    # Phần mở rộng: In đường đi từ u đến v
    print("\nĐường đi từ u đến v:")
    for _ in range(q):
        u, v = map(int, input().split())
        ancestor = lca(u, v)
        
        # Tìm đường đi từ u đến ancestor
        path1 = []
        while u != ancestor:
            path1.append(u)
            u = parent[0][u]
        
        # Tìm đường đi từ v đến ancestor
        path2 = []
        while v != ancestor:
            path2.append(v)
            v = parent[0][v]
        
        # In kết quả
        print(" -> ".join(map(str, path1 + [ancestor] + path2[::-1])))

if __name__ == "__main__":
    solve() 