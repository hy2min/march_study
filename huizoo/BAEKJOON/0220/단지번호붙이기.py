def abc(y, x, Sum):
    global Max
    Max = max(Max, Sum)
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if ny<0 or nx<0 or ny>=n or nx>=n:continue
        if arr[ny][nx] == '0':continue
        if visited[ny][nx]:continue
        visited[ny][nx] = 1
        abc(ny, nx, Sum+1)

n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]

cnt = 0
max_arr = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == '1':
            Max = 1
            cnt += 1
            abc(i, j, 0)
            max_arr.append(Max)
print(cnt)
print(*max_arr, sep='\n')