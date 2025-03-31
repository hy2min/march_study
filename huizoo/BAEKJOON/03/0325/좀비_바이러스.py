import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
y1 = x1 = -1
y2 = x2 = -1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            y1, x1 = i, j
        elif arr[i][j] == 2:
            y2, x2 = i, j

q = deque([(y1, x1, 1, 1), (y2, x2, 2, 1)])
visited = [[0]*M for _ in range(N)]
visited[y1][x1] = 1
visited[y2][x2] = 1
a, b, c = 1, 1, 0

while q:
    yy, xx, virus, time = q.popleft()
    if arr[yy][xx] == 3:
        continue
    for dy, dx in d:
        ny, nx = yy+dy, xx+dx
        if 0<=ny<N and 0<=nx<M:
            if arr[ny][nx] == 0 and visited[ny][nx] == 0:
                visited[ny][nx] = time+1
                arr[ny][nx] = virus
                if virus == 1:
                    a += 1
                elif virus == 2:
                    b += 1
                q.append((ny, nx, virus, time+1))
            elif (arr[ny][nx] == 1 and virus == 2) or (arr[ny][nx] == 2 and virus == 1):
                if visited[ny][nx] == time+1:
                    arr[ny][nx] = 3
                    if virus == 1:
                        b -= 1
                    elif virus == 2:
                        a -= 1
                    c += 1

print(a, b, c)
