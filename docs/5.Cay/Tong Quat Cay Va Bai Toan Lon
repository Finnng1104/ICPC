# 📘 TỔNG QUÁT CHỦ ĐỀ "CÂY" TRONG THI ICPC
# ==========================================
# Cây là đồ thị liên thông, không chu trình, có N đỉnh và N-1 cạnh.
# → Tức là: luôn có đúng 1 đường đi giữa 2 đỉnh bất kỳ, không có vòng lặp.

# ========= CÁC DẠNG BÀI PHỔ BIẾN =========
# 1. DFS trên cây → Duyệt toàn bộ cây để tính thông tin theo nhánh
# 2. Tính độ sâu, cha, subtree size
# 3. Lowest Common Ancestor (LCA) → Tìm tổ tiên chung gần nhất
# 4. Cây nhị phân, cây nhị phân tìm kiếm (BST)
# 5. Cây khung (Spanning Tree) → nâng cao

# ========= DẠNG 1: DFS trên cây =========
# ❓ Đề: Cho cây có N đỉnh, in ra thứ tự các đỉnh được thăm khi duyệt DFS từ gốc
# 💡 Ý tưởng: dùng đệ quy từ gốc, đi đến tất cả con chưa thăm

# Đồ thị (cây) dưới dạng danh sách kề
#      0
#     / \
#    1   2
#   / \
#  3   4
tree = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

visited = [False]*5

def dfs(u):
    print("Thăm:", u)            # In đỉnh được duyệt
    visited[u] = True           # Đánh dấu đã thăm
    for v in tree[u]:          # Duyệt các đỉnh kề u
        if not visited[v]:     # Nếu chưa thăm thì đi tiếp
            dfs(v)             # Gọi đệ quy

print("\n🔍 DFS từ đỉnh 0:")
dfs(0)  # DFS từ gốc 0

# ========= DẠNG 2: Tính cha, độ sâu =========
# ❓ Đề: Với mỗi đỉnh, in ra cha của nó và độ sâu tính từ gốc (gốc là 0)
# 💡 Ý tưởng: Dùng DFS có truyền thêm cha và depth

parent = [-1]*5
depth = [0]*5

def dfs_depth(u, p):
    parent[u] = p
    for v in tree[u]:
        if v != p:
            depth[v] = depth[u] + 1
            dfs_depth(v, u)

print("\n🔍 DFS tính cha và độ sâu:")
dfs_depth(0, -1)
print("Cha:", parent)
print("Độ sâu:", depth)

# ========= DẠNG 3: LCA đơn giản =========
# ❓ Đề: Cho 2 đỉnh u, v → Tìm đỉnh tổ tiên chung gần nhất của u và v
# 💡 Ý tưởng: Đưa cả 2 lên cùng độ sâu, sau đó đi lên song song đến khi gặp nhau

def lca(u, v):
    while depth[u] > depth[v]: u = parent[u]
    while depth[v] > depth[u]: v = parent[v]
    while u != v:
        u = parent[u]
        v = parent[v]
    return u

print("LCA(3,4):", lca(3, 4))

# ========= DẠNG 4: Subtree size =========
# ❓ Đề: Tính số lượng đỉnh trong cây con gốc tại mỗi đỉnh
# 💡 Ý tưởng: DFS từ dưới lên, mỗi node = tổng size con + 1

size = [0]*5

def dfs_size(u, p):
    size[u] = 1
    for v in tree[u]:
        if v != p:
            dfs_size(v, u)
            size[u] += size[v]

dfs_size(0, -1)
print("Subtree size:", size)

# ========= BÀI TOÁN LỚN ỨNG DỤNG =========
# ❓ Đề: Cho cây có N đỉnh, đếm số cặp đỉnh (u, v) sao cho u là tổ tiên của v.
# 💡 Mỗi node có (subtree_size - 1) hậu duệ → cộng dồn

N = 5
total = sum(size[i]-1 for i in range(N))
print("\n✅ Tổng số cặp (u là tổ tiên của v):", total)

# ========= MẸO & LƯU Ý =========
# - Cây là đồ thị có N đỉnh, N-1 cạnh và liên thông
# - Duyệt cây nên tránh quay lại cha → dùng DFS(u, p)
# - Subtree size cực hữu ích để đếm số node con
# - LCA được dùng nhiều trong bài toán liên quan đến tổ tiên, đường đi
# - Tư duy từ gốc → đệ quy xuống → thu thập thông tin
# - Đề ICPC thường ẩn "cây" trong bài → kiểm tra N-1 cạnh

# ==========================================
# Đây là file tổng hợp toàn bộ lý thuyết + ứng dụng + bài toán lớn về CÂY