from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cnt = 0
def bfs(y, x):
    d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    q = deque([(y, x)])
    visited[y][x] = 1
    while q:
        yy, xx = q.popleft()
        for dy, dx in d:
            ny, nx = yy+dy, xx+dx
            if ny<0 or nx<0 or ny>=N or nx>=M: continue
            if not arr[ny][nx]: continue
            if visited[ny][nx]: continue
            visited[ny][nx] = 1
            q.append((ny, nx))

for i in range(N):
    for j in range(M):
        if arr[i][j] and not visited[i][j]:
            cnt += 1
            bfs(i, j)

print(cnt)