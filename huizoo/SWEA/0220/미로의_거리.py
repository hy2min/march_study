def bfs(y, x):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((y,x))
    visited[y][x] = 1
    found = 0
    while q:
        y1, x1 = q.pop(0)
        for i in range(4):
            ny, nx = y1+dy[i], x1+dx[i]
            if ny<0 or nx<0 or ny>N-1 or nx>N-1: continue
            if visited[ny][nx]:continue
            if arr[ny][nx] != '0' and arr[ny][nx] != '3': continue
            if arr[ny][nx] == '3':
                found = 1
                print(f'#{tc} {visited[y1][x1]-1}')
            q.append((ny,nx))
            visited[ny][nx] = visited[y1][x1] + 1
    if not found:
        print(f'#{tc} {0}')

t = int(input())
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
for tc in range(1, t+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                start = (i, j)

    bfs(*start)