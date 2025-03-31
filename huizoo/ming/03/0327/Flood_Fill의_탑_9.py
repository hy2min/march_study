# 친구 만나러 가는길
import sys
from collections import deque
input = sys.stdin.readline

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

N, M = map(int, input().split())
arr = [list(input().split()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'S':
            S = (i, j)
        elif arr[i][j] == 'C':
            C = (i, j)
        elif arr[i][j] == 'D':
            D = (i, j)

cnt = 0
def bfs(start, end):
    q = deque([start])
    visited = [[0]*M for _ in range(N)]
    ey, ex = end
    while q:
        yy, xx = q.popleft()
        for dy, dx in d:
            ny, nx = yy+dy, xx+dx
            if ny<0 or nx<0 or ny>=N or nx>=M: continue
            if ny == ey and nx == ex: return visited[yy][xx] + 1
            if visited[ny][nx] != 0: continue
            if arr[ny][nx] == '.':
                visited[ny][nx] = visited[yy][xx] + 1
                q.append((ny, nx))

cnt += bfs(S, C)
cnt += bfs(C, D)

print(cnt)