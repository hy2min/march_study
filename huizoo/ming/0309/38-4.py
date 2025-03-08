from collections import deque

def bfs1(y, x):
    q = deque([(y, x)])
    d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    visited = [[0]*9 for _ in range(8)]
    visited[y][x] = 1
    while q:
        yy, xx = q.popleft()
        for dy, dx in d:
            ny, nx = yy+dy, xx+dx
            if ny<0 or nx<0 or ny>=8 or nx>=9: continue
            if arr[ny][nx] != '#': continue
            if visited[ny][nx]: continue
            visited[ny][nx] = 1
            q.append((ny, nx))
    return visited

def bfs2(y, x):
    q = deque([(y, x)])
    d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    visited = [[0]*9 for _ in range(8)]
    visited[y][x] = 1
    while q:
        yy, xx = q.popleft()
        for dy, dx in d:
            ny, nx = yy+dy, xx+dx
            if ny<0 or nx<0 or ny>=8 or nx>=9: continue
            if man1[ny][nx]:
                return visited[yy][xx] - 1
            if arr[ny][nx] != '_': continue
            if visited[ny][nx]: continue
            visited[ny][nx] = visited[yy][xx] + 1
            q.append((ny, nx))

    return 21e8

arr = [input() for _ in range(8)]
man1 = []
Min = 21e8
for i in range(8):
    for j in range(9):
        if arr[i][j] == '#':
            if not man1:
                man1 = bfs1(i, j)
            elif not man1[i][j]:
                Min = min(Min, bfs2(i, j))

print(Min)