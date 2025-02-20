arr = [[0] * 4 for _ in range(4)]

arr1 = [list(map(int, input().split())) for _ in range(3)]


for i in range(3):
    arr[3][3] += arr1[i][i]
    for j in range(3):
        arr[i][j] = arr1[i][j]
        arr[3][i] += arr1[j][i]
        arr[i][3] += arr1[i][j]

for i in arr:
    print(*i)

