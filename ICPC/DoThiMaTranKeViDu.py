# 🧩 BÀI TOÁN VÍ DỤ - BIỂU DIỄN ĐỒ THỊ BẰNG MA TRẬN KỀ
# Đề bài: Cho một đồ thị vô hướng có N đỉnh và M cạnh.
# Mỗi cạnh nối giữa hai đỉnh u và v.
# Hãy xây dựng ma trận kề của đồ thị.

# ===== INPUT =====
# Dòng đầu: N M (số đỉnh, số cạnh)
# M dòng tiếp theo: mỗi dòng gồm 2 số u v (một cạnh nối u và v)

# ===== OUTPUT =====
# Ma trận kề N x N (0 nếu không nối, 1 nếu có cạnh)

# ===== VÍ DỤ =====
# Input:
# 4 3
# 1 2
# 2 3
# 4 1
# Output:
# 0 1 0 1
# 1 0 1 0
# 0 1 0 0
# 1 0 0 0

# ===== CODE + GIẢI THÍCH TỪNG DÒNG =====

n, m = map(int, input().split())  # Đọc số đỉnh (n) và cạnh (m)

# Tạo ma trận kề kích thước n x n, khởi đầu toàn 0
adj = [[0]*n for _ in range(n)]  # adj[i][j] = 1 nếu có cạnh i-j

for _ in range(m):
    u, v = map(int, input().split())  # đọc cạnh u-v
    u -= 1  # chuyển về chỉ số 0-based (vì input là 1-based)
    v -= 1
    adj[u][v] = 1  # đánh dấu có cạnh giữa u và v
    adj[v][u] = 1  # vì đồ thị vô hướng, nên cả hai chiều

# In ra ma trận kề
for row in adj:
    print(' '.join(map(str, row)))
