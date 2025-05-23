# Python ICPC - Cấu trúc dữ liệu cơ bản và cú pháp
# Tác giả: ChatGPT hỗ trợ Thanh Tiến

import sys
import heapq
from collections import deque, defaultdict, Counter

# ==== LIST ====
# List là danh sách, giống mảng linh hoạt
# Syntax: a = [1, 2, 3]
a = [1, 2, 3]
a.append(4)         # Thêm vào cuối
a.pop()             # Xoá phần tử cuối
a.remove(2)         # Xoá giá trị có giá trị 2
a.sort()            # Sắp xếp tăng dần
a.reverse()         # Đảo ngược danh sách
print("List:", a)

# ==== TUPLE ====
# Tuple giống list nhưng bất biến (không thay đổi được)
t = (1, 2)
a, b = t
print("Tuple:", a, b)

# ==== SET ====
# Set là tập hợp không trùng lặp
s = set([1, 2, 3])
s.add(4)
s.discard(2)         # discard không lỗi nếu không tìm thấy
print("Set:", s)

# ==== DICT ====
# Dict là từ điển key-value
d = {'a': 1, 'b': 2}
d['c'] = 3
for k, v in d.items():
    print(f"Key: {k}, Value: {v}")

# ==== defaultdict ====
# defaultdict tự khởi tạo value mỗi khi truy cập key chưa có
dd = defaultdict(list)
dd['a'].append(1)
print("defaultdict:", dd)

# ==== Counter ====
# Counter dùng để đếm số lần xuất hiện
cnt = Counter([1,2,2,3])
print("Counter:", cnt)

# ==== DEQUE ====
# deque là hàng đợi 2 đầu
# append / appendleft / pop / popleft
dq = deque()
dq.append(1)
dq.appendleft(2)
dq.pop()
dq.popleft()
print("Deque:", dq)

# ==== HEAP ====
# heapq là heap min (priority queue)
h = []
heapq.heappush(h, 5)
heapq.heappush(h, 3)
heapq.heappop(h)     # luôn pop ra phần tử nhỏ nhất
print("Heap:", h)

# ==== BIT MANIPULATION ====
# Dùng bit để lưu trạng thái nhanh chẳng hạn: x & (1 << k)
x = 10                # 10 = 1010
print("Bit k=1:", x & (1 << 1))  # Kiểm tra bit tứ 1

# ==== FUNCTION ====
# Định nghĩa hàm

def add(a, b):
    return a + b
print("Add:", add(2, 3))

# ==== LAMBDA - MAP - FILTER ====
# lambda: hàm ẩn danh inline
# map: áp dụng hàm lên list
# filter: lọc theo điều kiện
square = lambda x: x * x
print("Map:", list(map(square, [1,2,3])))
print("Filter:", list(filter(lambda x: x%2==0, [1,2,3,4])))

# ==== CLASS ====
# Tạo lớp và object
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
n = Node(5)
print("Node:", n.val)

# ==== IF/ELSE ====
a = 5
if a == 5:
    print("A is 5")

# ==== FOR - WHILE ====
for i in range(3):
    print("For:", i)

x = 3
while x > 0:
    print("While:", x)
    x -= 1

# ==== LIST COMPREHENSION ====
# Cách rút gọn danh sách
squares = [x*x for x in range(5) if x%2==0]
print("List comp:", squares)

# ==== SORT VỚI KEY ====
# Sắp xếp theo key tuý chỉnh
arr = [(1,2), (3,1), (2,4)]
arr.sort(key=lambda x: x[1])
print("Sorted by 2nd:", arr)

# ==== ENUMERATE / ZIP ====
# enumerate: lấy index khi duyệt
# zip: ghép 2 list
for i, val in enumerate(['a', 'b']):
    print(f"{i} - {val}")

for x, y in zip([1,2], [3,4]):
    print(f"Sum: {x+y}")

# ==== INPUT/OUTPUT THI ICPC ====
# Dùng sys.stdin.readline để tối ưu I/O
# input = sys.stdin.readline
# n = int(input())
# arr = list(map(int, input().split()))

# ==== NHIỀU TEST CASE ====
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     a = list(map(int, input().split()))

# ==== DEBUG ====
def debug(*args):
    print("DEBUG:", *args, file=sys.stderr)
debug("This is debug info")

# ==== MẸO DÙNG TRONG THI ====
# set: xử lý không trùng
# heapq: hàng đợi ưu tiên
# deque: duyệt hai đầu
# Counter: đếm nhanh
# defaultdict: cấu trúc map nâng cao
# zip / enumerate: xử lý nhiều list cùng lúc
# list comp: rút gọn dòng
# lambda + sort: sắp xếp tuý biến

print("\nTổng hợp hoàn chỉnh cho phần cấu trúc dữ liệu và cú pháp cơ bản Python đã xong.")
