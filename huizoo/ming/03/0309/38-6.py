from collections import deque

def bfs(y, x, target):
    global sy, sx
    q = deque([(y, x)])
    visited = [[0]*X for _ in range(Y)]
    visited[y][x] = 1
    while q:
        yy, xx = q.popleft()
        for dy, dx in d:
            ny, nx = yy+dy, xx+dx
            if ny<0 or nx<0 or ny>=Y or nx>=X: continue
            if arr[ny][nx] == target:
                sy, sx = ny, nx
                return visited[yy][xx]
            if arr[ny][nx] == '#': continue
            if visited[ny][nx]: continue
            visited[ny][nx] = visited[yy][xx] + 1
            q.append((ny, nx))

Y, X = map(int, input().split())
arr = [input() for _ in range(Y)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
sy, sx = 0, 0
cnt = 0
for i in range(1, 5):
    if arr[sy][sx] == str(i): continue
    cnt += bfs(sy, sx, str(i))
print(f'{cnt}회')