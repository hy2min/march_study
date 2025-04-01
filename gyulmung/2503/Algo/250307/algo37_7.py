import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

N, M = map(int, input().split())
arr = [list(input().split()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'C':
            ch = (i,j)

q = deque()
q.append((ch[0],ch[1],0))
diry = [0, 0, 1, -1]
dirx = [1, -1, 0, 0]
cMin = 1e8
mMin = 1e8

while q:
    y, x, cnt = q.popleft()
    for i in range(4):
        dy = diry[i] + y
        dx = dirx[i] + x
        if dy < 0 or dx < 0 or dy >= N or dx >= M: continue
        if arr[dy][dx] == 'x': continue
        if arr[dy][dx] == 'S':
            if mMin > cnt:
                mMin = cnt+1
        if arr[dy][dx] == 'D':
            if cMin > cnt:
                cMin = cnt+1
        q.append((dy, dx, cnt+1))
        arr[dy][dx] = 'x'

print(cMin + mMin)