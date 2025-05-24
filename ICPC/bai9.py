# 📝 Bài 9: Truy vấn đoạn con
# ===============================================
"""
Đề bài: Cho một dãy số A có N phần tử. Có Q truy vấn, mỗi truy vấn thuộc một trong hai loại:
1. Cập nhật: Thay đổi giá trị A[i] thành x
2. Truy vấn: Tìm tổng, giá trị lớn nhất và nhỏ nhất trong đoạn [l, r]

Input:
- Dòng 1: N và Q (1 ≤ N,Q ≤ 10^5)
- Dòng 2: N số nguyên A[i] (-10^9 ≤ A[i] ≤ 10^9)
- Q dòng tiếp: Mỗi dòng là một truy vấn:
  + "1 i x": Cập nhật A[i] = x
  + "2 l r": Truy vấn đoạn [l, r]

Output:
- Với mỗi truy vấn loại 2, in ra tổng, max và min của đoạn [l, r]

Ví dụ:
Input:
5 3
1 2 3 4 5
2 1 3
1 2 6
2 1 3

Output:
6 3 1
10 6 1
"""

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        
        # Khởi tạo các mảng
        self.sum = [0] * (2 * self.size)
        self.max = [-float('inf')] * (2 * self.size)
        self.min = [float('inf')] * (2 * self.size)
        
        # Điền giá trị ban đầu
        for i in range(self.n):
            self.sum[self.size + i] = arr[i]
            self.max[self.size + i] = arr[i]
            self.min[self.size + i] = arr[i]
        
        # Xây dựng cây
        for i in range(self.size - 1, 0, -1):
            self.sum[i] = self.sum[2*i] + self.sum[2*i+1]
            self.max[i] = max(self.max[2*i], self.max[2*i+1])
            self.min[i] = min(self.min[2*i], self.min[2*i+1])
    
    def update(self, pos, value):
        pos += self.size
        self.sum[pos] = value
        self.max[pos] = value
        self.min[pos] = value
        
        while pos > 1:
            pos //= 2
            self.sum[pos] = self.sum[2*pos] + self.sum[2*pos+1]
            self.max[pos] = max(self.max[2*pos], self.max[2*pos+1])
            self.min[pos] = min(self.min[2*pos], self.min[2*pos+1])
    
    def query(self, l, r):
        l += self.size
        r += self.size
        res_sum = 0
        res_max = -float('inf')
        res_min = float('inf')
        
        while l <= r:
            if l % 2 == 1:
                res_sum += self.sum[l]
                res_max = max(res_max, self.max[l])
                res_min = min(res_min, self.min[l])
                l += 1
            if r % 2 == 0:
                res_sum += self.sum[r]
                res_max = max(res_max, self.max[r])
                res_min = min(res_min, self.min[r])
                r -= 1
            l //= 2
            r //= 2
        
        return res_sum, res_max, res_min

def solve():
    # Đọc input
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Khởi tạo Segment Tree
    st = SegmentTree(arr)
    
    # Xử lý các truy vấn
    for _ in range(q):
        query = list(map(int, input().split()))
        
        if query[0] == 1:
            # Cập nhật
            i, x = query[1]-1, query[2]  # Chuyển về 0-indexed
            st.update(i, x)
        else:
            # Truy vấn
            l, r = query[1]-1, query[2]-1  # Chuyển về 0-indexed
            sum_val, max_val, min_val = st.query(l, r)
            print(sum_val, max_val, min_val)
    
    # Phần mở rộng: In trạng thái hiện tại của cây
    print("\nTrạng thái hiện tại của dãy số:")
    print("Vị trí:", end=" ")
    for i in range(n):
        print(f"{i+1:4d}", end=" ")
    print("\nGiá trị:", end=" ")
    for i in range(n):
        print(f"{arr[i]:4d}", end=" ")
    print()
    
    # In thống kê
    print("\nThống kê:")
    total_sum, total_max, total_min = st.query(0, n-1)
    print(f"Tổng tất cả: {total_sum}")
    print(f"Giá trị lớn nhất: {total_max}")
    print(f"Giá trị nhỏ nhất: {total_min}")
    print(f"Giá trị trung bình: {total_sum/n:.2f}")

if __name__ == "__main__":
    solve() 