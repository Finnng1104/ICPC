# ICPC - Thuật toán cơ bản: Tìm kiếm, Đệ quy, DP, Greedy, Backtracking, Bit
# Bao gồm giải thích, khi dùng, ví dụ minh họa

import sys

# ==== 1. Tìm kiếm tuyến tính (Linear Search) ====
# Tìm từng phần tử, độ phức tạp O(n)
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# ==== 2. Tìm kiếm nhị phân (Binary Search) ====
# Chỉ dùng khi mảng đã được sắp xếp
# O(log n)
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# ==== 3. Đệ quy (Recursion) ====
# Gọi lại chính nó để giải bài toán con
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# ==== 4. Quy hoạch động (Dynamic Programming - DP) ====
# Ghi nhớ kết quả trung gian để tránh tính lại
# Ví dụ: Fibonacci với memoization
memo = {}
def fib(n):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

# ==== 5. Greedy Algorithm ====
# Chọn phương án tốt nhất tại mỗi bước
# Ví dụ: Đổi tiền bằng số xu ít nhất

def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)
    res = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            res += 1
    return res

# ==== 6. Backtracking ====
# Thử tất cả khả năng, quay lui nếu không hợp lệ
# Ví dụ: sinh tất cả hoán vị
res = []
def backtrack(path, options):
    if not options:
        res.append(path)
        return
    for i in range(len(options)):
        backtrack(path + [options[i]], options[:i] + options[i+1:])

# ==== 7. Bit Manipulation ====
x = 10  # 1010
print("Bit thứ 1 có bật không:", x & (1 << 1))      # Kiểm tra
print("Bật bit thứ 2:", x | (1 << 2))               # Bật
print("Tắt bit thứ 1:", x & ~(1 << 1))              # Tắt
print("Lấy bit phải nhất bật:", x & -x)             # Bit cuối cùng
print("XOR từ 1 đến n:", [10, 1, 11, 0][10 % 4])     # XOR nhanh

# ==== Demo ====
arr = [1, 3, 5, 7, 9]
print("Linear Search (5):", linear_search(arr, 5))
print("Binary Search (7):", binary_search(arr, 7))
print("Factorial 5:", factorial(5))
print("Fibonacci 10:", fib(10))
print("Greedy đổi 63 với [25, 10, 1]:", greedy_coin_change([25, 10, 1], 63))
backtrack([], [1, 2, 3])
print("Backtracking permutations của [1,2,3]:", res)

print("\n✅ Đã bổ sung tìm kiếm, đệ quy, DP, greedy, backtracking và bit manipulation với ví dụ rõ ràng.")