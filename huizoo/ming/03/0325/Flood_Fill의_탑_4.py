# 나이트 라이더
import sys
from collections import deque
input = sys.stdin.readline

d = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]

H, W = map(int, input().split())
y1, x1, y2, x2 = map(int, input().split())

q = deque([(y1, x1)])
visited = [[-1]*W for _ in range(H)]
visited[y1][x1] = 0

while q:
    y, x = q.popleft()
    if y == y2 and x == x2:
        print(visited[y][x])
        exit()
    for dy, dx in d:
        ny, nx = y+dy, x+dx
        if 0<=ny<H and 0<=nx<W:
            if visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))