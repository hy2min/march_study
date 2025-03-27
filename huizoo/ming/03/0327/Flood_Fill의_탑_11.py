# Fire Fighter
import sys
from collections import deque
input = sys.stdin.readline

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def abc(start, end):
    sy, sx = start
    ey, ex = end
    q = deque([start])
    visited = [[-1]*N for _ in range(N)]
    visited[sy][sx] = 0
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = dy+y, dx+x
            if ny<0 or nx<0 or ny>=N or nx>=N: continue
            if ny==ey and nx==ex: return visited[y][x] + 1
            if visited[ny][nx] != -1: continue
            if arr[ny][nx] not in ['#', '$']:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))


N = int(input())
arr = [list(input()) for _ in range(N)]
Y, X = map(int, input().split())

items = []
fire = None
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'A':
            items.append((i, j))
        elif arr[i][j] == '$':
            fire = (i, j)

Min = 1e9
for item in items:
    Min = min(Min, abc((Y, X), item) + abc(item, fire))


print(Min)