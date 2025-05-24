# 📝 Bài 3: Bài toán cái túi (Knapsack)
# ===============================================
"""
Đề bài: Cho N đồ vật, mỗi đồ vật có trọng lượng w[i] và giá trị v[i].
Có một cái túi có sức chứa tối đa là W.
Tìm cách chọn các đồ vật để tổng trọng lượng không vượt quá W
và tổng giá trị là lớn nhất.

Input:
- Dòng 1: N và W (1 ≤ N ≤ 100, 1 ≤ W ≤ 1000)
- N dòng tiếp: Mỗi dòng gồm w[i] và v[i] (1 ≤ w[i],v[i] ≤ 1000)

Output:
- Tổng giá trị lớn nhất có thể đạt được

Ví dụ:
Input:
4 7
3 4
4 5
5 6
6 7

Output:
10
"""

def solve():
    # Đọc input
    n, w = map(int, input().split())
    weights = []
    values = []
    
    for _ in range(n):
        wi, vi = map(int, input().split())
        weights.append(wi)
        values.append(vi)
    
    # Khởi tạo mảng DP
    # dp[i][j]: giá trị lớn nhất có thể đạt được với i đồ vật đầu tiên và túi có sức chứa j
    dp = [[0]*(w+1) for _ in range(n+1)]
    
    # Tính DP
    for i in range(1, n+1):
        for j in range(w+1):
            # Không chọn đồ vật thứ i
            dp[i][j] = dp[i-1][j]
            
            # Thử chọn đồ vật thứ i nếu có thể
            if j >= weights[i-1]:
                dp[i][j] = max(dp[i][j], 
                             dp[i-1][j-weights[i-1]] + values[i-1])
    
    # In kết quả
    print(dp[n][w])
    
    # In các đồ vật được chọn (phần mở rộng)
    print("\nCác đồ vật được chọn:")
    i, j = n, w
    chosen = []
    
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            chosen.append(i)
            j -= weights[i-1]
        i -= 1
    
    for item in reversed(chosen):
        print(f"Đồ vật {item}: w={weights[item-1]}, v={values[item-1]}")

if __name__ == "__main__":
    solve() 