import sys, copy
from collections import deque
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
virus = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i, j))
def bfs():
    global ans, arr2
    q = deque(virus)
    arr2 = copy.deepcopy(arr)
    while q:
        yy, xx = q.popleft()
        for i in range(4):
            ny, nx = yy+dy[i], xx+dx[i]
            if ny<0 or nx<0 or ny>N-1 or nx>M-1:continue
            if arr2[ny][nx] != 0:continue
            q.append((ny, nx))
            arr2[ny][nx] = 2
    cnt = 0
    for i in range(N):
        cnt += arr2[i].count(0)
    ans = max(ans,cnt)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt+1)
                arr[i][j] = 0

wall(0)
print(ans)