n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = []
for i in range(0, n-1):
    for j in range(i+1, n):
        if arr[i][j] > 0:
            arr2.append((arr[i][j], i, j))
for i in range(10):
    arr2.sort(key=lambda x: (x[0], i, j))
    a, b, c = arr2[0]
    a *= 2
    arr2[0] = (a, b, c)
    if i == 9:
        print(f'{a}만원')