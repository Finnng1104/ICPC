# 🧠 Tổng quan chủ đề SỐ HỌC trong ICPC

Số học là một trong những chủ đề **nền tảng nhất** trong thuật toán và thường xuyên xuất hiện trong các bài thi ICPC. Chủ đề này tập trung vào các phép toán cơ bản với số nguyên, đặc biệt là liên quan đến chia hết, đồng dư, tổ hợp và lũy thừa.

---

## 📦 Các dạng bài thường gặp

| Dạng bài toán               | Mô tả                                     | Kỹ thuật                      |
| --------------------------- | ----------------------------------------- | ----------------------------- |
| GCD / LCM                   | Ước chung lớn nhất, bội chung nhỏ nhất    | `math.gcd`, Euclid            |
| Sàng nguyên tố              | Tìm tất cả số nguyên tố <= n              | Sieve of Eratosthenes         |
| Phân tích thừa số nguyên tố | Tìm ước, đếm ước, phân tích               | Duyệt từ 2 đến sqrt(n)        |
| Lũy thừa nhanh              | Tính a^b % mod rất lớn                    | Fast exponentiation           |
| Modulo nghịch đảo           | Tìm số x sao cho (a \* x ≡ 1 mod m)       | Fermat / Extended Euclid      |
| Tổ hợp (C(n,k))             | Đếm số tổ hợp / tổ hợp có lặp             | Pascal, modulo                |
| Tính tổng nhanh             | Dãy cộng, nhân, số lẻ, số chính phương... | Công thức toán học            |
| Bitwise                     | AND, OR, XOR, đếm bit 1, thao tác bit     | `bin(x).count('1')`, `x & -x` |

---

## 🔢 Các công thức số học nên nhớ

- Tổng 1 + 2 + ... + n = `n(n+1)/2`
- Tổng bình phương: `n(n+1)(2n+1)/6`
- Tổng lũy thừa 3: `(n(n+1)/2)^2`
- GCD(a,b): `gcd(b, a % b)` (Euclid)
- LCM(a,b): `a * b // gcd(a,b)`
- a^b % mod: dùng fast_pow

---

## ✅ Checklist khi làm bài số học

- [ ] Dùng `math.gcd()` để tối ưu GCD nhanh
- [ ] Xử lý chia dư `a % m` khi m là số lớn (1e9+7)
- [ ] Với chia cho mod, nếu cần chia → tìm **modulo nghịch đảo**
- [ ] Dùng `pow(a, b, mod)` thay vì `a ** b % mod`
- [ ] Nếu đề hỏi "nguyên tố" hoặc "ước" → nghĩ đến sàng hoặc phân tích thừa số
- [ ] Nếu đếm tổ hợp lớn → dùng tiền xử lý `factorial[]`, `inv_factorial[]`

---

## 📘 Các file tham khảo

| File                    | Nội dung                      |
| ----------------------- | ----------------------------- |
| `gcd_lcm.py`            | GCD, LCM bằng Euclid          |
| `sang_nguyen_to.py`     | Sàng nguyên tố và ứng dụng    |
| `uoc_boi.py`            | Đếm ước, phân tích thừa số    |
| `fast_power.py`         | Lũy thừa nhanh, pow mod       |
| `modulo_inverse.py`     | Nghịch đảo modulo             |
| `combinatorics.py`      | C(n,k), tổ hợp có lặp, Pascal |
| `bitwise_operations.py` | Toán tử bit & ứng dụng        |

---

> Chủ đề số học đòi hỏi nhớ công thức và luyện tay nhiều. Nắm chắc những kỹ thuật này sẽ giúp bạn làm nhanh hơn rất nhiều bài trong ICPC!
