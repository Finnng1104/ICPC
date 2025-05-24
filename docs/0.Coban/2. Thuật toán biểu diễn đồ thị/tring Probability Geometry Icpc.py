# ICPC - Chuỗi (KMP, Trie, Hash), Xác suất tổ hợp, Hình học 2D
# Bao gồm giải thích, luồng chạy, code mẫu và ứng dụng thực tế

from collections import defaultdict
from math import comb, gcd, sqrt
import numpy as np  # Thêm thư viện numpy để xử lý ảnh

# ==== 0. Giới thiệu và ứng dụng thực tế ====
"""
Các thuật toán trong file này có nhiều ứng dụng thực tế:

1. Xử lý chuỗi (KMP, Trie, Hash):
   - Tìm kiếm văn bản trong Word, Google
   - Gợi ý từ khi gõ (autocomplete)
   - Kiểm tra đạo văn
   - Nén dữ liệu

2. Xác suất tổ hợp:
   - Tính xác suất trúng xổ số
   - Phân tích dữ liệu thống kê
   - Machine Learning
   - Game theory

3. Hình học 2D:
   - Xử lý ảnh (nhận dạng đối tượng)
   - Game development
   - CAD/CAM
   - Robotics
   - Computer Vision

Ví dụ thực tế:
1. KMP: Tìm kiếm từ khóa trong văn bản
2. Trie: Gợi ý từ khi gõ trên điện thoại
3. Hash: Kiểm tra file trùng lặp
4. Convex Hull: Nhận dạng đối tượng trong ảnh
5. Line Sweep: Phát hiện va chạm trong game
"""

# ==== 1. KMP Algorithm (Knuth-Morris-Pratt) ====
"""
Mục đích sử dụng:
- Tìm tất cả vị trí xuất hiện của chuỗi con (pattern) trong chuỗi lớn (text)
- Tối ưu hơn so với tìm kiếm thông thường
- Dùng trong tìm kiếm văn bản, xử lý chuỗi

Ví dụ thực tế:
1. Tìm kiếm từ khóa trong văn bản (Ctrl+F)
2. Kiểm tra đạo văn
3. Tìm kiếm DNA trong chuỗi gen
4. Xử lý văn bản tự động

Cách hoạt động (cho người mới):
1. Giống như tìm kiếm thông thường, nhưng thông minh hơn
2. Khi không khớp, không quay lại đầu pattern mà nhảy tới vị trí thích hợp
3. Sử dụng thông tin từ các lần so khớp trước để tối ưu

Ví dụ đơn giản:
Text:    "AABAACAADAABAAABAA"
Pattern: "AABA"
Kết quả: [0, 9, 13] (các vị trí bắt đầu của "AABA")
"""

def kmp(pattern, text):
    # Tạo LPS (Longest Prefix Suffix) - mảng lưu độ dài tiền tố hậu tố dài nhất
    lps = [0] * len(pattern)  # Khởi tạo mảng LPS với giá trị 0
    length = 0  # Độ dài tiền tố hậu tố hiện tại
    i = 1  # Vị trí đang xét trong pattern
    
    # Xây dựng mảng LPS
    while i < len(pattern):
        if pattern[i] == pattern[length]:  # Nếu ký tự khớp
            length += 1  # Tăng độ dài tiền tố hậu tố
            lps[i] = length  # Lưu độ dài vào LPS
            i += 1  # Xét ký tự tiếp theo
        elif length:  # Nếu không khớp và length > 0
            length = lps[length - 1]  # Quay lui về vị trí trước
        else:  # Nếu không khớp và length = 0
            i += 1  # Xét ký tự tiếp theo

    # Tìm pattern trong text
    i = j = 0  # i: vị trí trong text, j: vị trí trong pattern
    res = []  # Danh sách vị trí tìm thấy
    
    while i < len(text):
        if pattern[j] == text[i]:  # Nếu ký tự khớp
            i += 1  # Tăng vị trí text
            j += 1  # Tăng vị trí pattern
        if j == len(pattern):  # Nếu tìm thấy pattern
            res.append(i - j)  # Thêm vị trí vào kết quả
            j = lps[j - 1]  # Quay lui về vị trí trước
        elif i < len(text) and pattern[j] != text[i]:  # Nếu không khớp
            j = lps[j - 1] if j else 0  # Quay lui hoặc reset
    return res

# ==== 2. Trie nâng cao với từ điển đếm số lần ====
"""
Mục đích sử dụng:
- Lưu trữ và tìm kiếm chuỗi hiệu quả
- Đếm số lượng tiền tố
- Dùng trong từ điển, gợi ý từ, tìm kiếm

Ví dụ thực tế:
1. Gợi ý từ khi gõ trên điện thoại
2. Tự động hoàn thành trong IDE
3. Kiểm tra chính tả
4. Tìm kiếm thông minh

Cách hoạt động (cho người mới):
1. Giống như cây gia phả, mỗi node là một chữ cái
2. Các từ có tiền tố chung sẽ dùng chung đường đi
3. Dễ dàng tìm kiếm và đếm số lượng tiền tố

Ví dụ đơn giản:
Từ điển: ["apple", "app", "ape", "banana"]
- "ap" là tiền tố của 3 từ: "apple", "app", "ape"
- "ban" là tiền tố của 1 từ: "banana"
"""

class TrieNode:
    """Node trong cây Trie"""
    def __init__(self):
        self.children = {}  # Từ điển lưu các node con
        self.end = 0  # Số lượng chuỗi kết thúc tại node này

class Trie:
    """Cây Trie với chức năng đếm tiền tố"""
    def __init__(self):
        self.root = TrieNode()  # Node gốc

    def insert(self, word):
        """Thêm một chuỗi vào Trie"""
        node = self.root
        for c in word:  # Duyệt từng ký tự
            if c not in node.children:  # Nếu chưa có node con
                node.children[c] = TrieNode()  # Tạo node con mới
            node = node.children[c]  # Di chuyển xuống node con
        node.end += 1  # Tăng số lượng chuỗi kết thúc

    def count_prefix(self, prefix):
        """Đếm số lượng chuỗi có tiền tố là prefix"""
        node = self.root
        for c in prefix:  # Duyệt từng ký tự của tiền tố
            if c not in node.children:  # Nếu không tìm thấy
                return 0  # Trả về 0
            node = node.children[c]  # Di chuyển xuống node con
        return self._count(node)  # Đếm tổng số chuỗi từ node này

    def _count(self, node):
        """Đệ quy đếm tổng số chuỗi từ một node"""
        total = node.end  # Số chuỗi kết thúc tại node
        for child in node.children.values():  # Duyệt các node con
            total += self._count(child)  # Cộng dồn số chuỗi từ node con
        return total

# ==== 3. Hashing chuỗi (rolling hash) ====
"""
Mục đích sử dụng:
- So sánh nhanh hai chuỗi con
- Tìm chuỗi con lặp lại
- Kiểm tra tính đối xứng

Ví dụ thực tế:
1. Kiểm tra file trùng lặp
2. Tìm kiếm văn bản nhanh
3. Nén dữ liệu
4. Bảo mật (mật khẩu, chữ ký)

Cách hoạt động (cho người mới):
1. Chuyển chuỗi thành số (hash)
2. Các chuỗi giống nhau sẽ có hash giống nhau
3. So sánh hash thay vì so sánh chuỗi

Ví dụ đơn giản:
"abc" -> hash = 1*31^2 + 2*31^1 + 3*31^0
"abc" và "abc" có hash giống nhau
"abc" và "abd" có hash khác nhau
"""

MOD = 10**9 + 7  # Số nguyên tố lớn để tránh đụng độ
BASE = 31  # Cơ số cho hash (thường chọn số nguyên tố)

def hash_prefix(s):
    """Tính hash cho tất cả tiền tố của chuỗi s"""
    n = len(s)
    h = [0]*(n+1)  # Mảng lưu hash của các tiền tố
    p = [1]*(n+1)  # Mảng lưu lũy thừa của BASE
    
    for i in range(n):
        # Cập nhật hash: h[i+1] = h[i]*BASE + s[i]
        h[i+1] = (h[i] * BASE + ord(s[i])) % MOD
        # Cập nhật lũy thừa: p[i+1] = p[i]*BASE
        p[i+1] = (p[i] * BASE) % MOD
    return h, p

def get_hash(h, p, l, r):
    """Lấy hash của chuỗi con s[l..r]"""
    # Công thức: hash(s[l..r]) = (h[r] - h[l]*p[r-l]) % MOD
    return (h[r] - h[l]*p[r-l]) % MOD

# ==== 4. Xác suất tổ hợp ====
"""
Mục đích sử dụng:
- Tính xác suất trong các bài toán tổ hợp
- Tính số cách chọn k phần tử từ n phần tử
- Giải quyết bài toán xác suất rút thăm

Ví dụ thực tế:
1. Tính xác suất trúng xổ số
2. Phân tích dữ liệu thống kê
3. Machine Learning
4. Game theory

Cách hoạt động (cho người mới):
1. C(n,k): số cách chọn k phần tử từ n phần tử
2. Xác suất = (số trường hợp thuận lợi) / (tổng số trường hợp)
3. Sử dụng công thức tổ hợp để tính nhanh

Ví dụ đơn giản:
- Xác suất rút 2 quả bóng đỏ từ 3 đỏ, 2 xanh
- Xác suất trúng 6 số trong xổ số
- Xác suất nhận được 3 lá bài cùng chất
"""

def probability_choose(a, b, k):
    """
    Tính xác suất rút k phần tử từ a+b phần tử, trong đó có a phần tử đặc biệt
    Công thức: C(a,k) / C(a+b,k)
    """
    return comb(a, k) / comb(a + b, k)

# ==== 5. Hình học 2D: Convex Hull (Graham scan) ====
"""
Mục đích sử dụng:
- Tìm bao lồi của tập điểm
- Tìm đa giác lồi nhỏ nhất chứa tất cả điểm
- Dùng trong xử lý hình ảnh, game

Ví dụ thực tế:
1. Nhận dạng đối tượng trong ảnh
2. Tìm đường đi ngắn nhất tránh chướng ngại vật
3. Vẽ viền đối tượng
4. Tối ưu hóa không gian

Cách hoạt động (cho người mới):
1. Giống như bọc một món quà bằng giấy
2. Tìm các điểm ngoài cùng để tạo thành đa giác lồi
3. Loại bỏ các điểm nằm trong đa giác

Ví dụ với xử lý ảnh:
def find_object_boundary(image):
    # Chuyển ảnh sang nhị phân
    binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]
    
    # Tìm các điểm biên
    points = np.column_stack(np.where(binary > 0))
    
    # Tìm bao lồi
    hull = convex_hull(points)
    
    # Vẽ viền
    cv2.drawContours(image, [hull], 0, (0,255,0), 2)
    return image
"""

def cross(o, a, b):
    """Tính tích có hướng của vector OA và OB"""
    return (a[0] - o[0])*(b[1] - o[1]) - (a[1] - o[1])*(b[0] - o[0])

def convex_hull(points):
    """Tìm bao lồi của tập điểm bằng thuật toán Graham scan"""
    points = sorted(set(points))  # Sắp xếp và loại bỏ điểm trùng
    if len(points) <= 1:  # Trường hợp đặc biệt
        return points

    lower, upper = [], []  # Bao lồi dưới và trên
    for p in points:  # Xây dựng bao lồi dưới
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()  # Loại bỏ điểm không thuộc bao lồi
        lower.append(p)
    for p in reversed(points):  # Xây dựng bao lồi trên
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()  # Loại bỏ điểm không thuộc bao lồi
        upper.append(p)
    return lower[:-1] + upper[:-1]  # Kết hợp và bỏ điểm trùng

# ==== 6. Line Sweep: Giao đoạn thẳng ====
"""
Mục đích sử dụng:
- Kiểm tra giao điểm của các đoạn thẳng
- Tìm số lượng giao điểm
- Dùng trong xử lý hình học, game

Ví dụ thực tế:
1. Phát hiện va chạm trong game
2. Vẽ đồ thị không bị chồng chéo
3. Tìm giao điểm của các đường thẳng
4. Tối ưu hóa bố cục

Cách hoạt động (cho người mới):
1. Giống như quét từ trái sang phải
2. Theo dõi các đoạn đang "hoạt động"
3. Kiểm tra giao điểm khi có nhiều đoạn cùng lúc

Ví dụ với game:
def check_collision(objects):
    # Chuyển đối tượng thành đoạn thẳng
    intervals = [(obj.x, obj.x + obj.width) for obj in objects]
    
    # Kiểm tra va chạm
    if line_sweep(intervals):
        print("Có va chạm!")
    else:
        print("Không có va chạm")
"""

def line_sweep(intervals):
    """Kiểm tra có giao điểm giữa các đoạn thẳng không"""
    events = []  # Danh sách sự kiện
    for l, r in intervals:  # Tạo các sự kiện bắt đầu và kết thúc
        events.append((l, 'start'))  # Sự kiện bắt đầu đoạn
        events.append((r, 'end'))  # Sự kiện kết thúc đoạn
    events.sort()  # Sắp xếp theo vị trí

    active = 0  # Số đoạn đang xét
    for pos, typ in events:  # Duyệt các sự kiện
        if typ == 'start':  # Nếu là sự kiện bắt đầu
            active += 1  # Tăng số đoạn đang xét
            if active > 1:  # Nếu có nhiều hơn 1 đoạn
                return True  # Có giao điểm
        else:  # Nếu là sự kiện kết thúc
            active -= 1  # Giảm số đoạn đang xét
    return False  # Không có giao điểm

# ==== 7. Ứng dụng xử lý ảnh ====
"""
Các thuật toán trên có thể kết hợp để xử lý ảnh:

1. Nhận dạng đối tượng:
   - Dùng Convex Hull để tìm viền
   - Dùng Hash để so sánh đặc trưng
   - Dùng KMP để tìm mẫu

2. Phát hiện chuyển động:
   - Dùng Line Sweep để kiểm tra giao điểm
   - Dùng Hash để so sánh khung hình
   - Dùng xác suất để lọc nhiễu

3. OCR (Nhận dạng chữ):
   - Dùng Trie để lưu từ điển
   - Dùng KMP để tìm từ
   - Dùng Hash để so sánh ký tự

Ví dụ code xử lý ảnh đơn giản:
"""

def process_image(image):
    """Xử lý ảnh đơn giản với các thuật toán đã học"""
    # 1. Chuyển ảnh sang nhị phân
    binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]
    
    # 2. Tìm các đối tượng
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 3. Với mỗi đối tượng
    for contour in contours:
        # Tìm bao lồi
        hull = convex_hull(contour)
        
        # Tính hash của đối tượng
        obj_hash = hash_object(hull)
        
        # So sánh với mẫu (dùng KMP)
        if match_pattern(obj_hash, template_hash):
            # Vẽ viền xanh
            cv2.drawContours(image, [hull], 0, (0,255,0), 2)
        else:
            # Vẽ viền đỏ
            cv2.drawContours(image, [hull], 0, (0,0,255), 2)
    
    return image

def hash_object(points):
    """Tính hash của đối tượng dựa trên các điểm"""
    # Chuyển points thành chuỗi
    s = ''.join(str(p) for p in points)
    # Tính hash
    h, p = hash_prefix(s)
    return get_hash(h, p, 0, len(s))

def match_pattern(obj_hash, template_hash):
    """So sánh hash của đối tượng với mẫu"""
    # Dùng KMP để tìm mẫu
    return len(kmp(template_hash, obj_hash)) > 0

# ==== Demo ====
print("\n=== Demo các thuật toán với ví dụ thực tế ===")

# 1. KMP - Tìm kiếm văn bản
text = "Người dùng tìm kiếm từ khóa trong văn bản dài"
pattern = "tìm kiếm"
print(f"KMP: Tìm '{pattern}' trong văn bản -> Vị trí:", kmp(pattern, text))

# 2. Trie - Gợi ý từ
trie = Trie()
words = ["python", "programming", "project", "problem", "practice"]
for word in words:
    trie.insert(word)
print(f"Trie: Gợi ý từ 'pro' -> Số lượng:", trie.count_prefix("pro"))

# 3. Hash - So sánh chuỗi
s1 = "hello"
s2 = "hello"
h1, p1 = hash_prefix(s1)
h2, p2 = hash_prefix(s2)
print(f"Hash: So sánh '{s1}' và '{s2}' ->", 
      get_hash(h1, p1, 0, len(s1)) == get_hash(h2, p2, 0, len(s2)))

# 4. Xác suất - Bài toán thực tế
print(f"Xác suất: Rút 2 quả bóng đỏ từ 3 đỏ, 2 xanh ->", 
      probability_choose(3, 2, 2))

# 5. Convex Hull - Xử lý ảnh
points = [(0,0), (1,1), (2,2), (0,2), (2,0)]
print(f"Convex Hull: Tìm viền đối tượng ->", convex_hull(points))

# 6. Line Sweep - Game
intervals = [(1,5), (4,7), (8,10)]
print(f"Line Sweep: Kiểm tra va chạm ->", line_sweep(intervals))

print("\n✅ Đã tổng hợp thuật toán với ví dụ thực tế và ứng dụng xử lý ảnh.")
