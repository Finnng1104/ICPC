# 📘 Tổng hợp kiến thức SỐ HỌC ICPC - Python

# Bao gồm: GCD/LCM, sàng nguyên tố, lũy thừa nhanh, nghịch đảo modulo, tổ hợp, bitwise

# === 1. GCD và LCM ===

from math import gcd

def lcm(a, b):
return a \* b // gcd(a, b)

print("GCD(12,18):", gcd(12, 18)) # 6
print("LCM(12,18):", lcm(12, 18)) # 36

# === 2. Sàng nguyên tố ===

def sieve(n):
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(n\*\*0.5) + 1):
if is_prime[i]:
for j in range(i*i, n+1, i):
is_prime[j] = False
return [i for i, val in enumerate(is_prime) if val]

print("Số nguyên tố <= 30:", sieve(30))

# === 3. Fast Power ===

def fast_pow(a, b, mod):
res = 1
while b:
if b % 2:
res = res _ a % mod
a = a _ a % mod
b //= 2
return res

print("2^10 % 1000:", fast_pow(2, 10, 1000))

# === 4. Modulo Inverse ===

def modinv(a, mod):
return pow(a, mod - 2, mod) # Fermat's little theorem (mod là số nguyên tố)

print("Nghịch đảo của 3 mod 13:", modinv(3, 13)) # 9

# === 5. Combinatorics ===

from math import comb

def combinations_with_repetition(n, k):
return comb(n + k - 1, k)

print("C(5,2):", comb(5,2))
print("Tổ hợp có lặp C(2+3-1,3):", combinations_with_repetition(2, 3))

# === 6. Bitwise Operations ===

x = 13 # 1101
print("13 & 6:", 13 & 6) # 4
print("13 | 6:", 13 | 6) # 15
print("13 ^ 6:", 13 ^ 6) # 11
print("Bit count:", bin(13).count('1')) # 3
print("Tắt bit 1 cuối:", 13 & (13 - 1)) # 12
print("Giữ bit 1 cuối:", 13 & -13) # 1

# ✅ Tổng hợp các kỹ thuật số học đã hoàn tất!
