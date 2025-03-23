import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().strip() for _ in range(N)]
visited = [[0]*M for _ in range(N)]
sty, stx = 0, 0
visited[sty][stx] = 1
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
q = deque()
q.append((sty, stx))
flag = 0
while q:
    y1, x1 = q.popleft()
    for i in range(4):
        ny, nx = y1+dy[i], x1+dx[i]
        if ny<0 or nx<0 or ny>N-1 or nx>M-1:continue
        if arr[ny][nx] != '1':continue
        if visited[ny][nx]:continue
        q.append((ny, nx))
        visited[ny][nx] = visited[y1][x1] + 1
        if ny == N-1 and nx == M-1:
            print(visited[ny][nx])
            flag = 1
            break
    if flag:
        break
