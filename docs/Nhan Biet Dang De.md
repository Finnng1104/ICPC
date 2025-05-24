# 🧠 Hướng Dẫn Nhận Biết Dạng Đề Trong Lập Trình Thi Đấu

Trong các kỳ thi như ICPC, một kỹ năng quan trọng là **nhận biết được bài toán thuộc dạng nào** để áp dụng đúng thuật toán. Dưới đây là tổng hợp 10 dạng đề phổ biến và cách nhận ra chúng qua tín hiệu trong đề bài.

---

## 1. ✅ Quy hoạch động (Dynamic Programming - DP)

### 📌 Nhận biết:

- Tối ưu tổng / đếm số cách / có ràng buộc thứ tự (tính từ 1 đến n)
- Dữ liệu không quá lớn (n <= 10^5)
- Có sự phụ thuộc giữa các trạng thái

### 🔍 Ví dụ từ đề bài:

- "Tìm số cách để đi đến đỉnh n"
- "Tìm dãy con có tổng lớn nhất"
- "Chia dãy thành k phần sao cho..."

---

## 2. ✅ Tham lam (Greedy)

### 📌 Nhận biết:

- Bài yêu cầu **chọn từng bước tốt nhất tại thời điểm hiện tại**
- Có thể sắp xếp đầu vào theo thứ tự
- Đề thường không yêu cầu "tìm tất cả cách" mà chỉ "tối ưu nhanh"

### 🔍 Ví dụ từ đề bài:

- "Chọn số lượng ít nhất để bao phủ"
- "Tối thiểu hoá chi phí khi chọn"

---

## 3. ✅ Tìm kiếm nhị phân / Nhị phân trên đáp án

### 📌 Nhận biết:

- Đề hỏi **giá trị lớn nhất/nhỏ nhất thỏa mãn điều kiện**
- Dữ liệu lớn (n <= 10^18)
- Có hàm kiểm tra điều kiện đúng/sai

### 🔍 Ví dụ từ đề bài:

- "Tìm kích thước nhỏ nhất sao cho..."
- "Tìm số lớn nhất mà vẫn..."

---

## 4. ✅ Cây (Tree)

### 📌 Nhận biết:

- n đỉnh và n - 1 cạnh, không có chu trình, liên thông
- Đề bài yêu cầu: cha-con, tổ tiên, subtree

### 🔍 Ví dụ từ đề bài:

- "Cho cây có gốc 1, mỗi đỉnh có giá trị..."
- "Tìm tổ tiên chung thấp nhất (LCA)"

---

## 5. ✅ Đồ thị (Graph)

### 📌 Nhận biết:

- Dạng dữ liệu: cạnh, đỉnh, đường đi, chu trình
- Có trọng số hoặc không trọng số

### 🔍 Ví dụ từ đề bài:

- "Tìm đường đi ngắn nhất từ u đến v"
- "Có chu trình hay không"

---

## 6. ✅ Bitmask

### 📌 Nhận biết:

- Bài toán yêu cầu duyệt tất cả tổ hợp nhỏ (n <= 20)
- Trạng thái có thể biểu diễn bằng nhị phân

### 🔍 Ví dụ từ đề bài:

- "Chọn tập con các thành phố"
- "Duyệt qua tất cả hoán vị nhỏ"

---

## 7. ✅ Xử lý chuỗi

### 📌 Nhận biết:

- Đề bài liên quan đến thao tác với chuỗi: so sánh, con, độ dài
- Thường dùng KMP, Z, Hash, Trie

### 🔍 Ví dụ:

- "Tìm chuỗi con xuất hiện nhiều nhất"
- "Tìm số lượng xâu con giống nhau"

---

## 8. ✅ Toán học / Số học

### 📌 Nhận biết:

- Bài toán không cần cấu trúc dữ liệu, thiên về công thức
- GCD, chia hết, tổ hợp, modulo

### 🔍 Ví dụ:

- "Đếm số chia hết cho x trong đoạn"
- "Tính C(n, k) mod 10^9+7"

---

## 9. ✅ Sắp xếp / Hai con trỏ / Prefix sum

### 📌 Nhận biết:

- Tìm cặp / đoạn / tổng / đếm thoả mãn điều kiện
- Có thể dùng sắp xếp, prefix, hai con trỏ

### 🔍 Ví dụ:

- "Tìm đoạn có tổng ≤ k"
- "Đếm số đoạn thoả mãn điều kiện"

---

## 10. ✅ Backtracking / Brute Force

### 📌 Nhận biết:

- Bài nhỏ (n <= 10)
- Cần thử tất cả khả năng / tìm tất cả lời giải

### 🔍 Ví dụ:

- "Sinh tất cả hoán vị"
- "Đếm số cách tô màu hợp lệ"

---

## 🎯 Kết luận:

> Việc đọc đề bài và nhận ra "đây là DP", "đây là cây", "cần backtrack" là **kỹ năng cần luyện thường xuyên**.

Hãy cố gắng luyện tập mỗi ngày và phân tích mỗi bài đã làm: **nó thuộc dạng gì, vì sao, áp dụng kỹ thuật nào.**
