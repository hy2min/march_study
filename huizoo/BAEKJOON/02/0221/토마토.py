from collections import deque
import sys

M, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))

while q:
    yy, xx = q.popleft()
    for i in range(4):
        ny, nx = yy+dy[i], xx+dx[i]
        if ny<0 or nx<0 or ny>=N or nx>=M:continue
        if arr[ny][nx]:continue
        arr[ny][nx] = arr[yy][xx] + 1
        q.append((ny,nx))

def tomato():
    Max = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                return -1
            Max = max(arr[i][j], Max)
    return Max - 1
print(tomato())
