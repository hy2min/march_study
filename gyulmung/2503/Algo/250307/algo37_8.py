import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
diry = [0, 0, 1, -1]
dirx = [1, -1, 0, 0]

def bfs(y,x):
    q=deque()
    q.append((y, x))

    while q:
        y,x = q.popleft()
        for i in range(4):
            dy = diry[i] + y
            dx = dirx[i] + x
            if dy < 0 or dx < 0 or dy >= N or dx >= M: continue
            if arr[dy][dx] == 0: continue
            q.append((dy, dx))
            arr[dy][dx] = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cnt += 1
            bfs(i, j)

print(cnt)