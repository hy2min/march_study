a,b = map(int,input().split())
arr = []

for i in range(6):
    row = []
    target = 10 + i
    for j in range(3):
        row.append(target)
        target += 6
    arr.append(row)

for i in range(a,b+1):
    for j in range(3):
        arr[i][j] = 7

for i in arr:
    for j in i:
        print(j,end= ' ')
    print()