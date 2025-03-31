import sys
from collections import deque
input = sys.stdin.readline

d = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
T = int(input())
for _ in range(T):
    N = int(input())
    y1, x1 = map(int, input().split())
    y2, x2 = map(int, input().split())

    q = deque([(y1, x1)])
    visited = [[-1]*N for _ in range(N)]
    visited[y1][x1] = 0

    while q:
        y, x = q.popleft()
        if y == y2 and x == x2:
            print(visited[y][x])
            break
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<N:
                if visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))