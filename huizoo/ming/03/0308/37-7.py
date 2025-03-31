from collections import deque
N, M = map(int, input().split())
arr = [input().split() for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'S':
            S = (i, j)
        elif arr[i][j] == 'C':
            C = (i, j)
        elif arr[i][j] == 'D':
            D = (i, j)

def bfs(start, end):
    sy, sx = start
    d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited = [[0]*M for _ in range(N)]
    q = deque([(sy, sx)])
    visited[sy][sx] = 1
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if ny<0 or nx<0 or ny>=N or nx>=M: continue
            if visited[ny][nx]: continue
            if (ny, nx) == end:
                return visited[y][x]
            if arr[ny][nx] != '.': continue
            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))

print(bfs(S, C) + bfs(C, D))