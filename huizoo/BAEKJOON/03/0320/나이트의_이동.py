from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    cnt = 0
    if sy == ey and sx == ex:
        return cnt
    q = deque([(sy, sx, cnt)])
    visited = [[0] * L for _ in range(L)]
    visited[sy][sx] = 1
    while q:
        yy, xx, cnt = q.popleft()
        for dy, dx in d:
            ny, nx = yy + dy, xx + dx
            if ny < 0 or nx < 0 or ny >= L or nx >= L: continue
            if visited[ny][nx]: continue
            if ny == ey and nx == ex:
                return cnt + 1
            visited[ny][nx] = 1
            q.append((ny, nx, cnt+1))

d = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]

T = int(input())
for _ in range(T):
    L = int(input())
    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())
    print(bfs())