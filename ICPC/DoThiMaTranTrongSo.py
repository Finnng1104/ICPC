# 🧩 BÀI TOÁN VÍ DỤ - BIỂU DIỄN ĐỒ THỊ CÓ TRỌNG SỐ BẰNG MA TRẬN KỀ
# Đề bài: Cho một đồ thị có hướng có N đỉnh và M cạnh.
# Mỗi cạnh đi từ đỉnh u đến đỉnh v có trọng số w.
# Yêu cầu: xây dựng ma trận kề trọng số của đồ thị.

# ===== INPUT =====
# Dòng đầu: N M (số đỉnh, số cạnh)
# M dòng tiếp theo: u v w (cạnh từ u đến v có trọng số w)

# ===== OUTPUT =====
# Ma trận kề N x N:
# - Nếu có cạnh từ i đến j: in trọng số
# - Nếu không có: in 0 (hoặc vô cực nếu yêu cầu rõ)

# ===== VÍ DỤ =====
# Input:
# 4 5
# 1 2 3
# 1 3 2
# 2 4 4
# 3 2 1
# 4 1 7
# Output:
# 0 3 2 0
# 0 0 0 4
# 0 1 0 0
# 7 0 0 0

# ===== CODE KÈM GIẢI THÍCH =====

n, m = map(int, input().split())  # Đọc số đỉnh và cạnh

# Tạo ma trận kề trọng số n x n khởi tạo bằng 0
adj = [[0]*n for _ in range(n)]  # adj[i][j] = trọng số cạnh i→j nếu có

for _ in range(m):
    u, v, w = map(int, input().split())  # đọc 1 cạnh có trọng số
    u -= 1  # chuyển về chỉ số 0-based
    v -= 1
    adj[u][v] = w  # gán trọng số vào ma trận

# In ma trận kề trọng số
for row in adj:
    print(' '.join(map(str, row)))
