# 📘 Phương Pháp Tính Cơ Bản - ICPC
# Bao gồm: Tổng dãy, GCD/LCM, Số nguyên tố, Modular, Tổ hợp

import math

# ==== 1. Tổng dãy số nhanh ====
# Tổng 1 + 2 + ... + n
n = 10
sum_n = n * (n + 1) // 2
print("1 + 2 + ... + 10 =", sum_n)

# Tổng bình phương 1^2 + 2^2 + ... + n^2
sum_sq = n * (n + 1) * (2 * n + 1) // 6
print("Tổng bình phương 1^2+...+10^2:", sum_sq)

# Tổng lập phương 1^3 + 2^3 + ... + n^3
sum_cube = (n * (n + 1) // 2) ** 2
print("Tổng lập phương 1^3+...+10^3:", sum_cube)

# 🔹 Bài toán ví dụ:
# Cho n, tính tổng 1 + 2 + ... + n mà không dùng vòng lặp.
# → Áp dụng công thức n(n+1)/2

# ==== 2. GCD - LCM ====
a, b = 12, 18
g = math.gcd(a, b)
lcm = a * b // g
print(f"GCD({a},{b}) = {g}, LCM = {lcm}")

# 🔹 Bài toán ví dụ:
# Tìm số nhỏ nhất chia hết cho cả a và b: dùng LCM

# ==== 3. Sàng Eratosthenes - Tìm số nguyên tố ====
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i, p in enumerate(is_prime) if p]

print("Các số nguyên tố <= 30:", sieve(30))

# 🔹 Bài toán ví dụ:
# Tìm tất cả số nguyên tố ≤ n → dùng sàng để giảm từ O(n√n) → O(n log log n)

# ==== 4. Modular Arithmetic ====
MOD = 10**9 + 7

# (a * b) % MOD
x = 123456789
y = 987654321
print("(a*b) % MOD =", (x * y) % MOD)

# Modular exponentiation: a^b % MOD

def mod_pow(a, b, mod):
    result = 1
    a %= mod
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b //= 2
    return result

print("2^20 % MOD =", mod_pow(2, 20, MOD))

# ==== 5. Tổ hợp (nCr) % MOD ====
def prepare_factorials(n, mod):
    fact = [1] * (n + 1)
    inv = [1] * (n + 1)
    for i in range(1, n+1):
        fact[i] = fact[i-1] * i % mod
    inv[n] = pow(fact[n], -1, mod)  # Fermat if mod is prime
    for i in range(n-1, 0, -1):
        inv[i] = inv[i+1] * (i+1) % mod
    return fact, inv

def nCr(n, r, fact, inv, mod):
    if r > n or r < 0:
        return 0
    return fact[n] * inv[r] % mod * inv[n-r] % mod

fact, inv = prepare_factorials(1000, MOD)
print("C(10, 3) =", nCr(10, 3, fact, inv, MOD))

# 🔹 Bài toán ví dụ:
# Cho n, k → đếm số cách chọn k phần tử trong n → dùng nCr
