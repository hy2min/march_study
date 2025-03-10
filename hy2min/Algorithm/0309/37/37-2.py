from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = -1

y, x = map(int, input().split())
d_y = [0, 0, -1, 1]
d_x = [-1, 1, 0, 0]

q = deque()
q.append((y, x))

while q:
    y, x = q.popleft()
    for i in range(4):
        dy = y + d_y[i]
        dx = x + d_x[i]
        if dy < 0 or dx < 0 or dy >= n or dx >= m:
            continue
        if graph[dy][dx] == 0:
            graph[dy][dx] = graph[y][x] + 1
            q.append((dy, dx))
mx = -21e8
for i in graph:
    for j in i:
        mx = max(j,mx)
print(mx)