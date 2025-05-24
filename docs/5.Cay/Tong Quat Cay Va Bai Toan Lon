# 📘 TỔNG QUÁT CHỦ ĐỀ "CÂY" TRONG THI ICPC
# ==========================================
"""
Cây là một cấu trúc dữ liệu quan trọng trong lập trình thi đấu:

1. Định nghĩa:
   - Đồ thị liên thông (có đường đi giữa mọi cặp đỉnh)
   - Không có chu trình (không có vòng lặp)
   - N đỉnh và N-1 cạnh
   - Có đúng 1 đường đi giữa 2 đỉnh bất kỳ

2. Ứng dụng thực tế:
   - Phân tích cấu trúc phân cấp (gia phả, tổ chức)
   - Quản lý hệ thống file
   - Mạng máy tính (cây khung)
   - Game AI (cây trò chơi)
   - Phân tích mạng xã hội

3. Ưu điểm:
   - Cấu trúc đơn giản, dễ hiểu
   - Nhiều thuật toán hiệu quả
   - Dễ dàng mở rộng
   - Ứng dụng rộng rãi
"""

# ========= CÁC DẠNG BÀI PHỔ BIẾN =========
"""
1. DFS trên cây:
   - Duyệt toàn bộ cây
   - Tính toán thông tin theo nhánh
   - Phân tích cấu trúc

2. Tính toán cơ bản:
   - Độ sâu của mỗi node
   - Node cha của mỗi node
   - Kích thước cây con

3. LCA (Lowest Common Ancestor):
   - Tìm tổ tiên chung gần nhất
   - Tính khoảng cách trên cây
   - Phân tích quan hệ

4. Cây đặc biệt:
   - Cây nhị phân
   - Cây nhị phân tìm kiếm (BST)
   - Cây khung (Spanning Tree)

5. Bài toán nâng cao:
   - Heavy-Light Decomposition
   - Centroid Decomposition
   - Euler Tour Technique
"""

# ========= DẠNG 1: DFS trên cây =========
"""
Mục đích: Duyệt toàn bộ cây để thu thập thông tin

Cách hoạt động (cho người mới):
1. Bắt đầu từ gốc
2. Đi sâu nhất có thể theo một nhánh
3. Quay lui khi gặp lá
4. Đánh dấu các node đã thăm

Ứng dụng:
- Phân tích cấu trúc cây
- Tìm đường đi
- Tính toán thông tin
"""

# Ví dụ cây:
#      0
#     / \
#    1   2
#   / \
#  3   4
tree = {
    0: [1, 2],  # Node 0 kề với 1 và 2
    1: [0, 3, 4],  # Node 1 kề với 0, 3 và 4
    2: [0],     # Node 2 chỉ kề với 0
    3: [1],     # Node 3 chỉ kề với 1
    4: [1]      # Node 4 chỉ kề với 1
}

visited = [False]*5  # Mảng đánh dấu node đã thăm

def dfs(u):
    """
    Duyệt DFS từ node u
    
    Tham số:
    - u: node bắt đầu duyệt
    
    Cách hoạt động:
    1. In node hiện tại
    2. Đánh dấu đã thăm
    3. Duyệt các node con chưa thăm
    """
    print("Thăm:", u)            # In node đang duyệt
    visited[u] = True           # Đánh dấu đã thăm
    for v in tree[u]:          # Duyệt các node kề
        if not visited[v]:     # Nếu chưa thăm
            dfs(v)             # Duyệt tiếp

print("\n🔍 DFS từ đỉnh 0:")
dfs(0)  # Bắt đầu từ gốc

# ========= DẠNG 2: Tính cha, độ sâu =========
"""
Mục đích: Tính toán thông tin cơ bản của mỗi node

Cách hoạt động (cho người mới):
1. Lưu node cha của mỗi node
2. Tính độ sâu từ gốc
3. Duyệt DFS có truyền thêm thông tin

Ứng dụng:
- Xác định quan hệ
- Tính khoảng cách
- Phân tích cấu trúc
"""

parent = [-1]*5  # Mảng lưu node cha
depth = [0]*5    # Mảng lưu độ sâu

def dfs_depth(u, p):
    """
    DFS tính cha và độ sâu
    
    Tham số:
    - u: node hiện tại
    - p: node cha của u
    
    Cách hoạt động:
    1. Lưu node cha
    2. Tính độ sâu cho các node con
    3. Duyệt đệ quy
    """
    parent[u] = p              # Lưu node cha
    for v in tree[u]:         # Duyệt các node con
        if v != p:            # Không quay lại cha
            depth[v] = depth[u] + 1  # Tính độ sâu
            dfs_depth(v, u)   # Duyệt tiếp

print("\n🔍 DFS tính cha và độ sâu:")
dfs_depth(0, -1)  # Bắt đầu từ gốc, cha là -1
print("Cha:", parent)  # In mảng node cha
print("Độ sâu:", depth)  # In mảng độ sâu

# ========= DẠNG 3: LCA đơn giản =========
"""
Mục đích: Tìm tổ tiên chung gần nhất của hai node

Cách hoạt động (cho người mới):
1. Đưa hai node về cùng độ sâu
2. Đi lên cha song song
3. Dừng khi gặp nhau

Ứng dụng:
- Tìm quan hệ họ hàng
- Tính khoảng cách
- Phân tích cấu trúc
"""

def lca(u, v):
    """
    Tìm LCA của hai node
    
    Tham số:
    - u, v: hai node cần tìm LCA
    
    Trả về: node LCA
    
    Cách hoạt động:
    1. Đưa về cùng độ sâu
    2. Đi lên cha song song
    3. Dừng khi gặp nhau
    """
    # Đưa về cùng độ sâu
    while depth[u] > depth[v]: 
        u = parent[u]
    while depth[v] > depth[u]: 
        v = parent[v]
    
    # Đi lên cha song song
    while u != v:
        u = parent[u]
        v = parent[v]
    
    return u

print("\n🔍 Tìm LCA:")
print("LCA(3,4):", lca(3, 4))  # Tìm LCA của node 3 và 4

# ========= DẠNG 4: Subtree size =========
"""
Mục đích: Tính kích thước cây con của mỗi node

Cách hoạt động (cho người mới):
1. DFS từ dưới lên
2. Mỗi node = tổng size con + 1
3. Lưu kết quả vào mảng

Ứng dụng:
- Đếm số node con
- Phân tích cấu trúc
- Tối ưu hóa thuật toán
"""

size = [0]*5  # Mảng lưu kích thước cây con

def dfs_size(u, p):
    """
    DFS tính kích thước cây con
    
    Tham số:
    - u: node hiện tại
    - p: node cha của u
    
    Cách hoạt động:
    1. Khởi tạo size = 1 (bản thân)
    2. Cộng dồn size của các cây con
    3. Lưu kết quả
    """
    size[u] = 1  # Bắt đầu với size = 1
    for v in tree[u]:
        if v != p:
            dfs_size(v, u)  # Tính size cây con
            size[u] += size[v]  # Cộng dồn

dfs_size(0, -1)  # Tính size từ gốc
print("\n�� Kích thước cây con:")
print("Subtree size:", size)

# ========= BÀI TOÁN LỚN ỨNG DỤNG =========
"""
Bài toán: Đếm số cặp (u,v) mà u là tổ tiên của v

Phân tích:
1. Mỗi node u có (subtree_size[u] - 1) hậu duệ
2. Tổng số cặp = tổng (subtree_size[i] - 1) với mọi i

Ứng dụng:
- Phân tích quan hệ
- Đếm số cặp thỏa mãn
- Tối ưu hóa truy vấn
"""

N = 5  # Số node trong cây
total = sum(size[i]-1 for i in range(N))
print("\n🔍 Bài toán lớn:")
print("Tổng số cặp (u là tổ tiên của v):", total)

# ========= MẸO & LƯU Ý =========
"""
1. Đặc điểm cây:
   - N đỉnh, N-1 cạnh
   - Liên thông
   - Không có chu trình
   - Có đúng 1 đường đi giữa 2 đỉnh

2. Kỹ thuật quan trọng:
   - DFS tránh quay lại cha
   - Lưu thông tin node cha
   - Tính toán subtree size
   - Sử dụng LCA hiệu quả

3. Tư duy giải quyết:
   - Bắt đầu từ gốc
   - Đệ quy xuống các nhánh
   - Thu thập thông tin
   - Kết hợp các kỹ thuật

4. Lưu ý khi thi:
   - Kiểm tra N-1 cạnh
   - Xử lý trường hợp đặc biệt
   - Tối ưu hóa bộ nhớ
   - Chọn cấu trúc dữ liệu phù hợp
"""

# ==========================================
# ✅ File tổng hợp toàn bộ lý thuyết + ứng dụng + bài toán lớn về CÂY
# 💡 Hãy thử áp dụng vào các bài toán thực tế!