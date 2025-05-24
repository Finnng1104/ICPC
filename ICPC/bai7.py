# 📝 Bài 7: Cây khung nhỏ nhất với ràng buộc
# ===============================================
"""
Đề bài: Cho đồ thị vô hướng có trọng số với N đỉnh và M cạnh.
Tìm cây khung nhỏ nhất sao cho tổng trọng số các cạnh không vượt quá K
và số cạnh của cây khung là lớn nhất có thể.

Input:
- Dòng 1: N, M và K (1 ≤ N ≤ 10^5, 1 ≤ M ≤ 2*10^5, 1 ≤ K ≤ 10^9)
- M dòng tiếp: Mỗi dòng gồm u, v, w thể hiện cạnh nối u-v có trọng số w

Output:
- Dòng 1: Số cạnh trong cây khung tìm được
- Dòng 2: Tổng trọng số của cây khung
- Dòng 3: Các cạnh trong cây khung (theo thứ tự tăng dần của trọng số)

Ví dụ:
Input:
4 5 10
1 2 3
1 3 4
2 3 2
2 4 5
3 4 1

Output:
3
6
2 3 1
3 4 1
1 2 3
"""

class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0]*(n+1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def solve():
    # Đọc input
    n, m, k = map(int, input().split())
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    
    # Sắp xếp cạnh theo trọng số
    edges.sort()
    
    # Khởi tạo DSU
    dsu = DSU(n)
    
    # Tìm cây khung
    mst_edges = []
    total_weight = 0
    edge_count = 0
    
    for w, u, v in edges:
        if dsu.union(u, v):
            if total_weight + w <= k:
                mst_edges.append((u, v, w))
                total_weight += w
                edge_count += 1
            else:
                break
    
    # In kết quả
    print(edge_count)
    print(total_weight)
    
    # In các cạnh theo thứ tự tăng dần của trọng số
    for u, v, w in sorted(mst_edges, key=lambda x: x[2]):
        print(u, v, w)
    
    # Phần mở rộng: In thông tin chi tiết về cây khung
    print("\nThông tin chi tiết về cây khung:")
    print(f"Số đỉnh: {n}")
    print(f"Số cạnh: {edge_count}")
    print(f"Tổng trọng số: {total_weight}")
    print(f"Trọng số trung bình: {total_weight/edge_count:.2f}")
    
    # Kiểm tra tính liên thông
    components = set(dsu.find(i) for i in range(1, n+1))
    print(f"Số thành phần liên thông: {len(components)}")
    
    if len(components) == 1:
        print("Đồ thị liên thông")
    else:
        print("Đồ thị không liên thông")
        print("Các thành phần liên thông:")
        for comp in components:
            vertices = [i for i in range(1, n+1) if dsu.find(i) == comp]
            print(f"Thành phần {comp}: {vertices}")

if __name__ == "__main__":
    solve() 