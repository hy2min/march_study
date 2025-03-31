# 백신 Q
import sys
from collections import deque
input = sys.stdin.readline

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def cure(y, x):
    q = deque([(y, x)])
    arr[y][x] = 0
    while q:
        yy, xx = q.popleft()
        for dy, dx in d:
            ny, nx = yy+dy, xx+dx
            if 0<=ny<N and 0<=nx<M:
                if arr[ny][nx] != 0:
                    arr[ny][nx] = 0
                    q.append((ny, nx))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            cnt += 1
            cure(i, j)

print(cnt)