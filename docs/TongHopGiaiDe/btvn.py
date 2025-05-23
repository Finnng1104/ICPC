n = int(input())

arr = input().split()
for i in range(len(arr)):
    arr[i] = int(arr[i])

chan = []
le = []

for i in range(n):
    if arr[i] % 2 == 0:
        chan.append(arr[i])
    else:
        le.append(arr[i])

# Sắp xếp mảng chẵn
for i in range(len(chan)):
    for j in range(len(chan) - 1):
        if chan[j] > chan[j + 1]:
            temp = chan[j]
            chan[j] = chan[j + 1]
            chan[j + 1] = temp

# Sắp xếp mảng lẻ
for i in range(len(le)):
    for j in range(len(le) - 1):
        if le[j] > le[j + 1]:
            temp = le[j]
            le[j] = le[j + 1]
            le[j + 1] = temp

# In kết quả
for i in range(len(chan)):
    print(chan[i], end=' ')
for i in range(len(le)):
    print(le[i], end=' ')


n, k = map(int, input().split())
arr = list(map(int, input().split()))

found = False

for i in range(len(arr)):
  for j in range(len(arr) -1):
    if arr[i] + arr[j] == k:
      found = True
      break

if found == True:
  print("Yes")
else:
  print("No")
