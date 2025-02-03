arr = []

for i in range(2):
    row = list(map(int,input().split()))
    arr.append(row)

lst = []

for i in arr:
    for j in i:
        lst.append(j)
lst.sort()

count = 0
for i in range(2):
    for j in range(3):
        arr[i][j] = lst[count]
        count += 1

for i in arr:
    for j in i:
        print(j,end=' ')
    print()