arr = [
    [4,5,4,5,4],
    [8,9,8,9,8],
    [1,2,1,2,1],
    [4,5,4,5,4],
    [6,7,6,7,6],
]

for i in range(5):
    a,b = map(int,input().split())
    arr[a][b] += 1
    if arr[a][b] == 10:
        arr[a][b] = 0

for i in arr:
    for j in i:
        print(j,end='')
    print()