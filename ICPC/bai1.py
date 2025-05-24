# 📝 Bài 1: Sắp xếp và tìm kiếm
# ===============================================
"""
Đề bài: Cho một dãy số nguyên A có N phần tử. Thực hiện các thao tác:
1. Sắp xếp dãy tăng dần
2. Tìm vị trí đầu tiên của số X trong dãy đã sắp xếp
3. Đếm số lần xuất hiện của X

Input:
- Dòng 1: N và X (1 ≤ N ≤ 10^5, 1 ≤ X ≤ 10^9)
- Dòng 2: N số nguyên A[i] (1 ≤ A[i] ≤ 10^9)

Output:
- Dòng 1: Dãy A sau khi sắp xếp
- Dòng 2: Vị trí đầu tiên của X (0-based, -1 nếu không tìm thấy)
- Dòng 3: Số lần xuất hiện của X

Ví dụ:
Input:
5 3
1 3 3 2 3

Output:
1 2 3 3 3
2
3
"""

def solve():
    # Đọc input
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Sắp xếp dãy
    a.sort()
    print(*a)  # In dãy đã sắp xếp
    
    # Tìm vị trí đầu tiên của x
    try:
        first_pos = a.index(x)
        print(first_pos)
    except ValueError:
        print(-1)
    
    # Đếm số lần xuất hiện
    count = a.count(x)
    print(count)

if __name__ == "__main__":
    solve()