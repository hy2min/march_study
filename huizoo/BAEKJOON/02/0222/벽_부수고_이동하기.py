import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
direct = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def bfs():
    visited = dict()
    q = deque()
    q.append((0, 0, 0))
    visited[(0, 0, 0)] = 1
    while q:
        yy, xx, wall = q.popleft()
        if yy == N - 1 and xx == M - 1:
            return visited[(yy, xx, wall)]
        for dy, dx in direct:
            ny, nx = yy+dy, xx+dx
            if 0<=ny<N and 0<=nx<M:
                if arr[ny][nx] == '0':
                    if wall == 1 and (ny, nx, 0) in visited:
                        continue
                    if (ny, nx, wall) not in visited:
                        visited[(ny, nx, wall)] = visited[(yy, xx, wall)] + 1
                        q.append((ny, nx, wall))
                elif arr[ny][nx] == '1' and wall == 0 and (ny, nx, 1) not in visited:
                    visited[(ny, nx, 1)] = visited[(yy, xx, wall)] + 1
                    q.append((ny, nx, 1))
    return 0

ret = bfs()

if ret:
    print(ret)
else:
    print(-1)