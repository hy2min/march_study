from collections import deque

d_y = [0,0,-1,1]
d_x = [-1,1,0,0]

def bfs(si, sj, ei, ej):
    q = deque()
    q.append((si, sj, 0))
    visited = [[0] * m for _ in range(n)]
    visited[si][sj] = 1

    while q:
        y, x, cnt = q.popleft()
        if (y, x) == (ei, ej):
            return cnt
        for i in range(4):
            dy = y + d_y[i]
            dx = x + d_x[i]
            if dy < 0 or dx < 0 or dy >= n or dx >= m:
                continue
            if arr[dy][dx] == 'x' or visited[dy][dx] == 1:
                continue
            visited[dy][dx] = 1
            q.append((dy, dx, cnt+1))




n, m = map(int, input().split())
arr = [list(input().split()) for _ in range(n)]

si = sj = ci = cj = di = dj = -1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S':
            si, sj = i, j
        if arr[i][j] == 'C':
            ci, cj = i, j
        if arr[i][j] == 'D':
            di, dj = i, j

ans = bfs(si, sj, ci, cj) + bfs(ci, cj, di, dj)
print(ans)

