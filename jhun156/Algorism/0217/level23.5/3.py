arr = [[0] * 4 for _ in range(4)]
lst = [list(map(int,input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        arr[i][j] = lst[i][j]

for i in range(3):
    for j in range(3):
        arr[3][i] += arr[j][i]
        arr[i][3] += arr[i][j]
    arr[3][3] += arr[i][i]

for i in range(4):
    print(*arr[i])