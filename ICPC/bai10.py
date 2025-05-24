# 📝 Bài 10: Bài toán người du lịch (TSP)
# ===============================================
"""
Đề bài: Cho N thành phố, mỗi cặp thành phố có một chi phí di chuyển.
Người du lịch xuất phát từ thành phố 1, cần đi qua tất cả các thành phố
mỗi thành phố đúng một lần và quay về thành phố 1. Tìm chi phí nhỏ nhất.

Input:
- Dòng 1: N (1 ≤ N ≤ 20)
- N dòng tiếp: Mỗi dòng gồm N số nguyên, số thứ j trong dòng i
  là chi phí di chuyển từ thành phố i đến thành phố j

Output:
- Chi phí nhỏ nhất của hành trình

Ví dụ:
Input:
4
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0

Output:
80
"""

def solve():
    # Đọc input
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]
    
    # Khởi tạo mảng DP
    # dp[mask][i]: chi phí nhỏ nhất để đi từ thành phố 1 đến thành phố i
    # thông qua các thành phố được đánh dấu trong mask
    dp = [[float('inf')] * n for _ in range(1 << n)]
    
    # Khởi tạo trạng thái ban đầu
    dp[1][0] = 0  # Chỉ có thành phố 1 (bit 0)
    
    # Tính DP
    for mask in range(1 << n):
        for i in range(n):
            if not (mask & (1 << i)):  # Thành phố i chưa được thăm
                continue
            
            # Thử đi từ thành phố j đến i
            for j in range(n):
                if i != j and (mask & (1 << j)):  # Thành phố j đã được thăm
                    prev_mask = mask ^ (1 << i)  # Xóa bit i
                    dp[mask][i] = min(dp[mask][i], 
                                    dp[prev_mask][j] + cost[j][i])
    
    # Tìm kết quả
    final_mask = (1 << n) - 1  # Tất cả các bit đều 1
    result = float('inf')
    
    # Thử kết thúc tại mỗi thành phố (trừ thành phố 1)
    for i in range(1, n):
        result = min(result, dp[final_mask][i] + cost[i][0])
    
    # In kết quả
    print(result)
    
    # Phần mở rộng: In hành trình tối ưu
    print("\nHành trình tối ưu:")
    
    def find_path(mask, pos, path):
        if mask == 1:  # Chỉ còn thành phố 1
            path.append(1)
            return
        
        # Tìm thành phố trước đó
        for prev in range(n):
            if prev != pos and (mask & (1 << prev)):
                prev_mask = mask ^ (1 << pos)
                if dp[mask][pos] == dp[prev_mask][prev] + cost[prev][pos]:
                    path.append(pos + 1)
                    find_path(prev_mask, prev, path)
                    break
    
    # Tìm thành phố cuối cùng
    final_pos = 0
    min_cost = float('inf')
    for i in range(1, n):
        if dp[final_mask][i] + cost[i][0] < min_cost:
            min_cost = dp[final_mask][i] + cost[i][0]
            final_pos = i
    
    # Tìm và in hành trình
    path = []
    find_path(final_mask, final_pos, path)
    path.append(1)  # Quay về thành phố 1
    
    # In kết quả
    print("Thứ tự thăm các thành phố:", " -> ".join(map(str, path)))
    print("Chi phí di chuyển:")
    total_cost = 0
    for i in range(len(path)-1):
        from_city = path[i]
        to_city = path[i+1]
        step_cost = cost[from_city-1][to_city-1]
        total_cost += step_cost
        print(f"  {from_city} -> {to_city}: {step_cost}")
    print(f"Tổng chi phí: {total_cost}")

if __name__ == "__main__":
    solve() 