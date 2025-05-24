# 📘 Cây nhị phân tìm kiếm (Binary Search Tree - BST)

# ✅ Mỗi node: bên trái < node < bên phải

# ✅ Các thao tác phổ biến: thêm, tìm kiếm, in thứ tự

class Node:
def **init**(self, val):
self.val = val
self.left = None
self.right = None

# 🔹 Thêm phần tử vào BST

def insert(root, val):
if not root:
return Node(val)
if val < root.val:
root.left = insert(root.left, val)
else:
root.right = insert(root.right, val)
return root

# 🔹 Duyệt inorder: in theo thứ tự tăng

def inorder(root):
if root:
inorder(root.left)
print(root.val, end=' ')
inorder(root.right)

# 🔹 Tìm kiếm phần tử trong BST

def search(root, val):
if not root: return False
if root.val == val: return True
if val < root.val:
return search(root.left, val)
else:
return search(root.right, val)

# 📌 Ví dụ:

root = None
for x in [5, 3, 8, 2, 4, 7, 9]:
root = insert(root, x)

print("Duyệt inorder:", end=' ')
inorder(root)
print("\nTìm 4:", search(root, 4)) # True
print("Tìm 6:", search(root, 6)) # False

# 🧠 Ghi nhớ:

# - BST hiệu quả khi cân bằng (O(logN)), xấu nhất là O(n) nếu bị lệch

# - Có thể dùng AVL/Red-Black Tree để cân bằng nếu cần (nâng cao)
