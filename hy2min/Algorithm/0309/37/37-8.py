from collections import deque

d_y = [0, 0, -1, 1]
d_x = [-1, 1, 0, 0]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    arr[y][x] = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            dy = y + d_y[i]
            dx = x + d_x[i]
            if dy < 0 or dx < 0 or dy >= n or dx >= m:
                continue
            if arr[dy][dx] == 1:
                q.append((dy, dx))
                arr[dy][dx] = 0

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

for i in range(n):
     for j in range(m):
         if arr[i][j] == 1:
             cnt += 1
             bfs(i,j)
print(cnt)