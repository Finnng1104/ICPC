# 📝 Bài 4: Tìm cặp số có tổng bằng X
# ===============================================
"""
Đề bài: Cho một dãy số nguyên A có N phần tử và một số nguyên X.
Tìm hai số trong dãy có tổng bằng X.
Nếu có nhiều cặp, in ra cặp có số đầu tiên nhỏ nhất.

Input:
- Dòng 1: N và X (1 ≤ N ≤ 10^5, -10^9 ≤ X ≤ 10^9)
- Dòng 2: N số nguyên A[i] (-10^9 ≤ A[i] ≤ 10^9)

Output:
- Nếu tìm thấy: In ra hai số a và b (a ≤ b)
- Nếu không tìm thấy: In ra "KHONG TIM THAY"

Ví dụ:
Input:
5 9
1 2 3 4 5

Output:
4 5
"""

def solve():
    # Đọc input
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Sắp xếp mảng để tìm kiếm nhị phân
    a.sort()
    
    # Tìm cặp số
    left, right = 0, n-1
    result = None
    
    while left < right:
        current_sum = a[left] + a[right]
        
        if current_sum == x:
            # Tìm thấy cặp số
            result = (a[left], a[right])
            # Tiếp tục tìm cặp có số đầu tiên nhỏ hơn
            right -= 1
        elif current_sum < x:
            left += 1
        else:
            right -= 1
    
    # In kết quả
    if result:
        print(result[0], result[1])
    else:
        print("KHONG TIM THAY")
    
    # Phần mở rộng: In tất cả các cặp số có tổng bằng X
    print("\nTất cả các cặp số có tổng bằng X:")
    found = False
    left, right = 0, n-1
    
    while left < right:
        current_sum = a[left] + a[right]
        
        if current_sum == x:
            print(f"{a[left]} {a[right]}")
            found = True
            # Tìm cặp tiếp theo
            left += 1
            right -= 1
        elif current_sum < x:
            left += 1
        else:
            right -= 1
    
    if not found:
        print("KHONG TIM THAY")

if __name__ == "__main__":
    solve() 