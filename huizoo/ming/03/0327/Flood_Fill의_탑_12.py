# 천지창조
import sys, copy
from collections import deque
input = sys.stdin.readline

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def bfs(y, x):
    q = deque([(y, x)])
    visited[y][x] = -2
    while q:
        yy, xx = q.popleft()
        for dy, dx in d:
            ny, nx = yy+dy, xx+dx
            if ny<0 or nx<0 or ny>=8 or nx>=9: continue
            if visited[ny][nx] == -1 and arr[ny][nx] == '#':
                visited[ny][nx] = -2
                q.append((ny, nx))

def bfs2(y, x):
    q = deque([(y, x)])
    visited2 = copy.deepcopy(visited)
    visited2[y][x] = 0
    while q:
        yy, xx = q.popleft()
        for dy, dx in d:
            ny, nx = yy + dy, xx + dx
            if ny < 0 or nx < 0 or ny >= 8 or nx >= 9: continue
            if visited2[ny][nx] == -2 and arr[ny][nx] == '#': return visited2[yy][xx] + 1
            if visited2[ny][nx] == -1 and arr[ny][nx] != '#':
                visited2[ny][nx] = visited2[yy][xx] + 1
                q.append((ny, nx))

    return 1e9

arr = [list(input()) for _ in range(8)]
visited = [[-1]*9 for _ in range(8)]
flag = 0
Min = 1e9
for i in range(8):
    for j in range(9):
        if arr[i][j] == '#' and visited[i][j] == -1:
            if flag == 0:
                bfs(i, j)
                flag = 1
            else:
                Min = min(Min, bfs2(i, j))

print(Min)