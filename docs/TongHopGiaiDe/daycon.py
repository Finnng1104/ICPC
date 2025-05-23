t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    found = False
    for j in range(n):
        for k in range(j + 2, n):
            if a[j] == a[k]:
                print("YES")
                found = True
                break
        if found:
            break 
    if not found:
        print("NO")