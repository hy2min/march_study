def abc(y, x):
    global Sum
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if ny<0 or nx<0 or ny>=n or nx>=n:continue
        if arr[ny][nx] == '0':continue
        if visited[ny][nx]:continue
        visited[ny][nx] = 1
        Sum += 1
        abc(ny, nx)

n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]

cnt = 0
sum_arr = []
for i in range(n):
    for j in range(n):
        if i == 4 and j == 1:
            debug = 1
        if not visited[i][j] and arr[i][j] == '1':
            cnt += 1
            Sum = 1
            visited[i][j] = 1
            abc(i, j)
            sum_arr.append(Sum)
sum_arr.sort()
print(cnt)
print(*sum_arr, sep='\n')