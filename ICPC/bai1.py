a = list(map(int, input().split()))
b = list(map(int, input().split()))

m = a[0]
n = a[1]

p = b[0]
q = b[1]
max = 8

if 1 < p < m:
    if 1 == q or q == n:
        max -=3
else:
    max -= 3
    if 1 == q or n == q:
        max -= 2
print(max)