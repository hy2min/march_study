arr = []
a = ord('A')

for i in range(3):
    row = []
    for j in range(3):
        row.append(chr(a))
        a += 1
    arr.append(row)

a,b = map(int,input().split())
c,d = map(int,input().split())

tmp = arr[a][b]
arr[a][b] = arr[c][d]
arr[c][d] = tmp

for i in range(3):
    for j in range(3):
        print(arr[i][j],end='')
    print()

