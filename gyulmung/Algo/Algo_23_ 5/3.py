arr = [[0]*4 for _ in range(4)]
lst = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        arr[i][j] = lst[i][j]
        arr[i][-1] += lst[i][j]
        arr[-1][i] += lst[j][i]
arr[-1][-1] = arr[0][0] + arr[1][1] + arr[2][2]

for i in arr:
    print(*i)