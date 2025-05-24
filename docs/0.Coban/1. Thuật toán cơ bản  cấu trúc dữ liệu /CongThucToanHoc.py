# ICPC - Tổng hợp công thức toán học rút gọn tính nhanh
# Bao gồm số học, tổ hợp, hình học, bitwise

from math import sqrt, isqrt

# 1. Tổng từ 1 đến n
# Công thức: n * (n + 1) // 2
n = 100
print("1+2+...+n:", n * (n + 1) // 2)

# 2. Tổng bình phương 1^2 + 2^2 + ... + n^2
print("Tổng bình phương:", n * (n + 1) * (2 * n + 1) // 6)

# 3. Tổng lập phương: (1+2+...+n)^2
print("Tổng lập phương:", (n * (n + 1) // 2) ** 2)

# 4. Trung bình cộng dãy liên tiếp
print("Trung bình 1..n:", (1 + n) / 2)

# 5. Tổng cấp số cộng: a + (a+d) + ...
def sum_arith(a, d, n):
    return n * (2 * a + (n - 1) * d) // 2
print("CSC:", sum_arith(2, 2, 5))  # 2+4+6+8+10

# 6. Tổng cấp số nhân
# a * (r^n - 1) // (r - 1)
def sum_geo(a, r, n):
    return a * (r**n - 1) // (r - 1)
print("CSN:", sum_geo(1, 2, 4))  # 1 + 2 + 4 + 8

# 7. Tổng số lẻ đầu tiên: 1+3+5+...+(2n-1) = n^2
k = 5
print("Tổng số lẻ:", k**2)

# 8. Tổng dãy bất kỳ: (số phần tử) * (a1 + an) / 2
print("Tổng dãy đều:", 5 * (2 + 10) // 2)

# 9. Sàng nguyên tố
def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i, val in enumerate(is_prime) if val]
print("Sàng nguyên tố <= 30:", sieve(30))

# 10. GCD & LCM
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)
print("GCD(12, 18):", gcd(12, 18))
print("LCM(12, 18):", lcm(12, 18))

# 11. Tổ hợp C(n, k)
def C(n, k):
    if k == 0 or k == n: return 1
    return C(n-1, k-1) + C(n-1, k)
print("C(5,2):", C(5, 2))

# 12. Tổng tổ hợp: 2^n
print("Tổng tổ hợp C(n,k):", 2**5)

# 13. Tổ hợp có lặp: C(n + k - 1, k)
def C_repeat(n, k):
    from math import comb
    return comb(n + k - 1, k)
print("Chọn 3 từ 2 loại có lặp:", C_repeat(2, 3))

# 14. Tổng chữ số
print("digit_sum(1234):", sum(map(int, str(1234))))

# 15. Số chính phương
print("is 49 perfect square?", isqrt(49)**2 == 49)

# 16. Palindrome
print("121 is palindrome?", str(121) == str(121)[::-1])

# 17. Khoảng cách Euclidean
print("Distance (0,0)-(3,4):", sqrt((3-0)**2 + (4-0)**2))

# 18. Diện tích tam giác từ tọa độ
x1,y1,x2,y2,x3,y3 = 0,0,4,0,0,3
S = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2
print("Diện tích tam giác:", S)

# 19. Shoelace: diện tích đa giác
def shoelace(x, y):
    n = len(x)
    area = 0
    for i in range(n):
        area += x[i]*y[(i+1)%n] - x[(i+1)%n]*y[i]
    return abs(area)/2
print("Shoelace diện tích:", shoelace([0,4,4,0], [0,0,3,3]))

# 20. Tích có hướng
print("Cross product:", (4 - 0)*(3 - 0) - (0 - 0)*(4 - 0))

# 21. Tích vô hướng
# a = (x1,y1), b = (x2,y2) => a·b = x1*x2 + y1*y2
print("Dot product:", 1*2 + 3*4)

# 22. XOR từ 1 đến n
def xor_to_n(n):
    return [n, 1, n+1, 0][n % 4]
print("XOR 1..10:", xor_to_n(10))

# 23. Đếm bit 1
print("Bit count 13:", bin(13).count('1'))

# 24. Tắt bit phải nhất đang bật
x = 10
print("Tắt bit cuối:", x & (x - 1))

# 25. Lấy bit phải nhất bật
print("Bit cuối bật:", x & -x)

# 26. Fast power
def fast_pow(a, b, mod):
    res = 1
    while b:
        if b % 2:
            res = res * a % mod
        a = a * a % mod
        b //= 2
    return res
print("2^10 % 1000:", fast_pow(2, 10, 1000))

print("\n✅ Đã tổng hợp 31 công thức toán học hữu ích cho ICPC.")
