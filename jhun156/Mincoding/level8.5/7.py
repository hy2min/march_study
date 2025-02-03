arr = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

a,b,c = map(int,input().split())

arr[a][b] = c

for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j], end = ' ')
    print()

