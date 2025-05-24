# 🌲 Tổng quan về CÂY trong thi ICPC

Cây (Tree) là một trong những cấu trúc dữ liệu **rất quan trọng và thường gặp** trong các kỳ thi lập trình. Dưới đây là tổng hợp kiến thức, dấu hiệu nhận biết và các dạng bài phổ biến liên quan đến cây.

---

## ✅ Định nghĩa:
- Là một **đồ thị vô hướng**, **liên thông**, **không có chu trình**.
- Có **n đỉnh và n - 1 cạnh**.
- Thường có 1 **đỉnh gốc (root)** nếu là cây có gốc.

---

## 🧠 Dấu hiệu bài toán là CÂY:
| Dấu hiệu trong đề bài | Gợi ý xử lý |
|------------------------|-------------|
| "Gồm n đỉnh và n - 1 cạnh" | Là cây |
| "Đồ thị không có chu trình" | Có thể là cây |
| "Gốc cây là đỉnh 1" hoặc "mỗi đỉnh có cha" | Cây có gốc (DFS từ gốc) |
| "Tính toán theo nhánh" hoặc "con cháu" | DFS trên cây, subtree |

---

## 📦 Các dạng bài phổ biến liên quan đến cây:

| Dạng bài | Mô tả | Kỹ thuật |
|----------|-------|----------|
| DFS trên cây | Duyệt các đỉnh, tính toán thông tin | `dfs(u, parent)` |
| Tính độ sâu, cha, subtree | Xác định thông tin từng đỉnh | DFS, mảng `depth[]`, `parent[]`, `size[]` |
| Tổ tiên chung thấp nhất (LCA) | Tìm node chung gần nhất | Binary Lifting, Sparse Table |
| DP trên cây | Tối ưu hoá trên cây | DFS + DP | 
| Đếm số con, đếm số đường đi | Duyệt cây và tính toán | DFS, prefix sum trên cây |
| Cây nhị phân tìm kiếm (BST) | Cấu trúc đặc biệt của cây | Đệ quy trái phải, inorder |

---

## 🧠 Một số kỹ thuật quan trọng:
- **DFS từ gốc:** để duyệt và lưu thông tin cha, con, độ sâu
- **Time In / Out:** để xác định đoạn subtree
- **DP trên cây:** chọn/bỏ đỉnh, tối ưu hoá qua các con
- **Binary Lifting:** tối ưu tìm tổ tiên (LCA) trong O(logN)

---

## 📘 Các bài toán mẫu gợi ý:
| Tên bài toán | Ý tưởng |
|--------------|---------|
| Tính tổng trong nhánh con | DFS, subtree sum |
| Chọn tập đỉnh không kề nhau | DP trên cây |
| Đếm số con của mỗi đỉnh | DFS, size[u] |
| Tìm đường dài nhất (diameter) | 2 lần DFS |
| Truy vấn tổ tiên cấp k | Binary Lifting |

---

## ✅ Checklist khi làm bài về CÂY:
- [ ] Kiểm tra xem có phải cây không (n-1 cạnh)
- [ ] Có gốc chưa? Nếu chưa → chọn 1 đỉnh làm gốc
- [ ] DFS từ gốc để tính `depth`, `parent`, `size`
- [ ] Nếu cần tối ưu → cân nhắc DP trên cây
- [ ] Nếu có nhiều truy vấn tổ tiên → dùng LCA / Binary Lifting

---

> Cây là nền tảng cho rất nhiều bài toán trong lập trình thi đấu. Hãy luyện tập để thật quen tay nhé 💪
# 🌲 Tổng quan về CÂY trong thi ICPC

Cây (Tree) là một trong những cấu trúc dữ liệu **rất quan trọng và thường gặp** trong các kỳ thi lập trình. Dưới đây là tổng hợp kiến thức, dấu hiệu nhận biết và các dạng bài phổ biến liên quan đến cây.

---

## ✅ Định nghĩa:
- Là một **đồ thị vô hướng**, **liên thông**, **không có chu trình**.
- Có **n đỉnh và n - 1 cạnh**.
- Thường có 1 **đỉnh gốc (root)** nếu là cây có gốc.

---

## 🧠 Dấu hiệu bài toán là CÂY:
| Dấu hiệu trong đề bài | Gợi ý xử lý |
|------------------------|-------------|
| "Gồm n đỉnh và n - 1 cạnh" | Là cây |
| "Đồ thị không có chu trình" | Có thể là cây |
| "Gốc cây là đỉnh 1" hoặc "mỗi đỉnh có cha" | Cây có gốc (DFS từ gốc) |
| "Tính toán theo nhánh" hoặc "con cháu" | DFS trên cây, subtree |

---

## 📦 Các dạng bài phổ biến liên quan đến cây:

| Tệp | Dạng bài | Mô tả | Kỹ thuật |
|-----|----------|--------|----------|
| `dfs_cay_co_ban.py` | DFS trên cây | Duyệt các đỉnh, tính toán thông tin | `dfs(u, parent)` |
| `do_sau_va_so_con.py` | Tính depth, parent, size | Tìm độ sâu và số con mỗi đỉnh | DFS |
| `lca_don_gian.py` | Tổ tiên chung thấp nhất (LCA) | Tìm node chung gần nhất | DFS + nhảy cha |
| `dp_chon_dinh_lon_nhat.py` | DP trên cây | Chọn các đỉnh sao cho không kề nhau và có tổng lớn nhất | DFS + DP |
| `dem_so_canh_duong_di.py` | Đếm cạnh hoặc đỉnh trong đường đi | Đếm số lần 1 cạnh nằm trong đường đi giữa các đỉnh | DFS + Prefix |
| `cay_nhi_phan_tim_kiem.py` | Cây nhị phân tìm kiếm | Cây trái nhỏ hơn gốc, phải lớn hơn | Đệ quy, duyệt inorder |

---

## 🧠 Một số kỹ thuật quan trọng:
- **DFS từ gốc:** để duyệt và lưu thông tin cha, con, độ sâu
- **Time In / Out:** để xác định đoạn subtree
- **DP trên cây:** chọn/bỏ đỉnh, tối ưu hoá qua các con
- **Binary Lifting:** tối ưu tìm tổ tiên (LCA) trong O(logN)

---

## 📘 Các bài toán mẫu gợi ý:
| Tên bài toán | Ý tưởng |
|--------------|---------|
| Tính tổng trong nhánh con | DFS, subtree sum |
| Chọn tập đỉnh không kề nhau | DP trên cây |
| Đếm số con của mỗi đỉnh | DFS, size[u] |
| Tìm đường dài nhất (diameter) | 2 lần DFS |
| Truy vấn tổ tiên cấp k | Binary Lifting |

---

## ✅ Checklist khi làm bài về CÂY:
- [ ] Kiểm tra xem có phải cây không (n-1 cạnh)
- [ ] Có gốc chưa? Nếu chưa → chọn 1 đỉnh làm gốc
- [ ] DFS từ gốc để tính `depth`, `parent`, `size`
- [ ] Nếu cần tối ưu → cân nhắc DP trên cây
- [ ] Nếu có nhiều truy vấn tổ tiên → dùng LCA / Binary Lifting

---

> Cây là nền tảng cho rất nhiều bài toán trong lập trình thi đấu. Hãy luyện tập để thật quen tay nhé 💪
