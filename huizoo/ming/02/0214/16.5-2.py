y, x = map(int, input().split())
arr = [[0]*3 for _ in range(6)]
n = 65
for j in range(2, -1, -1):
    for i in range(5, -1, -1):
        arr[i][j] = chr(n)
        n += 1
print(arr[y][x])