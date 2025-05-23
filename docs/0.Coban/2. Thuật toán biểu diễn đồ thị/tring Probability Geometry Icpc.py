# ICPC - Chuỗi (KMP, Trie, Hash), Xác suất tổ hợp, Hình học 2D
# Bao gồm giải thích, luồng chạy, code mẫu

from collections import defaultdict
from math import comb, gcd, sqrt

# ==== 1. KMP Algorithm ====
# Tìm chuỗi con (pattern) trong chuỗi lớn (text)
# Luồng chạy: Tiền xử lý mảng LPS → duyệt text với pattern

def kmp(pattern, text):
    # Tạo LPS (Longest Prefix Suffix)
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length:
            length = lps[length - 1]
        else:
            i += 1

    # Tìm pattern trong text
    i = j = 0
    res = []
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            res.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            j = lps[j - 1] if j else 0
    return res

# ==== 2. Trie nâng cao với từ điển đếm số lần ====
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end += 1

    def count_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return self._count(node)

    def _count(self, node):
        total = node.end
        for child in node.children.values():
            total += self._count(child)
        return total

# ==== 3. Hashing chuỗi (rolling hash) ====
# So sánh nhanh 2 chuỗi con
MOD = 10**9 + 7
BASE = 31

def hash_prefix(s):
    n = len(s)
    h = [0]*(n+1)
    p = [1]*(n+1)
    for i in range(n):
        h[i+1] = (h[i] * BASE + ord(s[i])) % MOD
        p[i+1] = (p[i] * BASE) % MOD
    return h, p

def get_hash(h, p, l, r):
    return (h[r] - h[l]*p[r-l]) % MOD

# ==== 4. Xác suất tổ hợp ====
# Chọn k phần tử từ n: C(n, k)
# Xác suất rút đúng: C(a, k) / C(a+b, k)

def probability_choose(a, b, k):
    return comb(a, k) / comb(a + b, k)

# ==== 5. Hình học 2D: Convex Hull (Graham scan) ====
# Luồng chạy: sort → chọn trái/phải → kiểm tra quay trái

def cross(o, a, b):
    return (a[0] - o[0])*(b[1] - o[1]) - (a[1] - o[1])*(b[0] - o[0])

def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    lower, upper = [], []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]  # bỏ điểm trùng

# ==== 6. Line Sweep: Giao đoạn thẳng theo trục x ====
# Kiểm tra có giao nhau giữa các đoạn [l, r] không

def line_sweep(intervals):
    events = []
    for l, r in intervals:
        events.append((l, 'start'))
        events.append((r, 'end'))
    events.sort()

    active = 0
    for pos, typ in events:
        if typ == 'start':
            active += 1
            if active > 1:
                return True  # có giao
        else:
            active -= 1
    return False

# ==== Demo ====
print("KMP vị trí của 'ana' trong 'bananana':", kmp("ana", "bananana"))
trie = Trie()
for word in ["apple", "app", "ape"]:
    trie.insert(word)
print("Prefix 'ap':", trie.count_prefix("ap"))
s = "abcabc"
h, p = hash_prefix(s)
print("Hash abc vs abc:", get_hash(h, p, 0, 3) == get_hash(h, p, 3, 6))
print("Xác suất rút 2 đỏ từ 3 đỏ, 2 xanh:", probability_choose(3, 2, 2))
points = [(0,0), (1,1), (2,2), (0,2), (2,0)]
print("Convex Hull:", convex_hull(points))
print("Có giao đoạn?:", line_sweep([(1,5), (4,7), (8,10)]))

print("\n✅ Đã tổng hợp thuật toán chuỗi, xác suất, hình học 2D kèm giải thích và ví dụ.")
