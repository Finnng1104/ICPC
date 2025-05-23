# ICPC Python - Cấu trúc dữ liệu và Thuật toán nâng cao
# Bao gồm: DS nâng cao + Thuật toán cơ bản + Thuật toán tổng hợp

import sys
import heapq
from collections import deque

# ==================== STACK / QUEUE / DEQUE ====================
# Stack: cấu trúc LIFO (Last In First Out)
stack = []
stack.append(1)
stack.append(2)
stack.pop()

# Queue: cấu trúc FIFO (First In First Out)
queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()

# Deque: hàng đợi hai đầu
# appendleft, popleft cho đầu; append, pop cho cuối

# ==================== PRIORITY QUEUE (HEAP) ====================
# Heap: dùng heapq (heap min)
heap = []
heapq.heappush(heap, 2)
heapq.heappush(heap, 1)
heapq.heappop(heap)

# ==================== UNION-FIND / DSU ====================
# Tìm đại diện của tập hợp và gộp tập
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr != yr:
            self.parent[yr] = xr

# ==================== TRIE ====================
# Dùng để lưu từ, tìm kiếm prefix nhanh
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.end

# ==================== FENWICK TREE (BIT) ====================
# Dùng cho bài toán cộng đoạn, cập nhật 1 điểm
class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (size + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += (i & -i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= (i & -i)
        return res

# ==================== TÌM KIẾM ====================
# Tuyến tính - O(n)
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Nhị phân - O(log n)
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

# ==================== SẮP XẾP ====================
# QuickSort - chia để trị, trung bình O(n log n), tệ nhất O(n^2)
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

# MergeSort - chia để trị, ổn định, luôn O(n log n)
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:] + right[j:]
    return res

# HeapSort - dùng heap để sắp, O(n log n), không ổn định
def heapsort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

# ==================== QUY HOẠCH ĐỘNG (DP) ====================
memo = {}
def fib(n):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

# ==================== GREEDY ====================
def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)
    res = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            res += 1
    return res

# ==================== BACKTRACKING ====================
res = []
def backtrack(path, options):
    if not options:
        res.append(path)
        return
    for i in range(len(options)):
        backtrack(path + [options[i]], options[:i] + options[i+1:])

# ==================== BIT MANIPULATION ====================
x = 10  # 1010
bit1 = x & (1 << 1)  # kiểm tra bit thứ 1
x_on = x | (1 << 2)  # bật bit thứ 2
x_off = x & ~(1 << 1) # tắt bit thứ 1

# ==================== THUẬT TOÁN TỔNG HỢP ====================
# Sàng Eratosthenes - tìm tất cả số nguyên tố <= n
def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i, val in enumerate(is_prime) if val]

# Ước chung lớn nhất (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Bội chung nhỏ nhất (LCM)
def lcm(a, b):
    return a * b // gcd(a, b)

# Tổng chuỗi chưa sắp xếp
unsorted_arr = [3, 1, 5, 2]
print("Tổng chưa sắp xếp:", sum(unsorted_arr))

# Tổng chuỗi đã sắp xếp
sorted_arr = sorted(unsorted_arr)
print("Tổng đã sắp xếp:", sum(sorted_arr))

print("\n✅ Đã chuẩn bị đầy đủ DS nâng cao, thuật toán tìm kiếm, sắp xếp, DP, greedy, backtracking, bit, GCD/LCM, sieve, tổng dãy...")
