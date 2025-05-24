# 🧠 Lý Thuyết Trò Chơi - ICPC Notes

## 🎮 Bài toán 1: Nim Game (Trò chơi Nim)

### Mô tả
Có `n` đống đá, mỗi đống có `a_i` viên. Hai người chơi luân phiên nhau, mỗi lượt một người chọn một đống và lấy đi ít nhất 1 viên đá (nhiều hơn cũng được, miễn là không quá số viên trong đống đó). Người lấy viên đá cuối cùng sẽ thắng. Hỏi người chơi đầu tiên có chiến thắng không nếu cả hai chơi tối ưu?

### Input
- Dòng đầu tiên là số nguyên `n` (1 ≤ n ≤ 10⁵) — số đống đá.  
- Dòng thứ hai là `n` số nguyên `a₁, a₂, ..., aₙ` (0 ≤ aᵢ ≤ 10⁹) — số đá trong từng đống.

### Output
- `"First"` nếu người chơi đầu tiên thắng.  
- `"Second"` nếu người chơi thứ hai thắng.

---

### 🧩 Phân tích

Bài toán này là một ví dụ cổ điển của trò chơi Nim:

- Tính tổng XOR (`⊕`) của các đống đá.
  - Nếu XOR = 0 ⟹ người thứ hai thắng.
  - Nếu XOR ≠ 0 ⟹ người thứ nhất thắng.

Giá trị XOR thể hiện trạng thái thắng/thua:
- XOR = 0: trạng thái thua.
- XOR ≠ 0: trạng thái thắng.

---

### ✅ Code Python

```python
def nim_game(piles):
    xor_sum = 0
    for pile in piles:
        xor_sum ^= pile
    return "First" if xor_sum != 0 else "Second"

# Đọc input
n = int(input())
piles = list(map(int, input().split()))
print(nim_game(piles))
```

---

### 🧪 Ví dụ

**Input**
```
3
1 2 3
```

**Xử lý**
- XOR: 1 ⊕ 2 ⊕ 3 = 0 ⟹ `"Second"`

**Output**
```
Second
```

---

