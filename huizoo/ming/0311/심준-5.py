n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = []
for i in range(n):
    for j in range(m):
        arr2.append((arr[i][j], i, j))

arr2.sort(key=lambda x: (-x[0], x[1], x[2]))
for i in range(3):
     print(f'{arr2[i][0]}({arr2[i][1]},{arr2[i][2]})')


