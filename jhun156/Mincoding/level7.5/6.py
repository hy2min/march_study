arr = []

for i in range(2):
    row = []
    for j in range(4):
        row.append(0)
    arr.append(row)

a,b = map(int,input().split())

arr[a][b] = 1

for i in arr:
    for j in i:
        print(j,end = ' ')
    print()