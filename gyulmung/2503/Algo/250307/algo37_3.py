import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

arr = [list(map(int, input().split())) for _ in range(4)]

diry = [0, 0, 1, -1, 1, 1, -1, -1]
dirx = [1, -1, 0, 0, 1, -1, 1, -1]
q = deque()
ret = 0
for i in range(4):
    for j in range(5):
        if arr[i][j] == 1:
            q.append((i, j, 1))

while q:
    y, x, cnt = q.popleft()
    for i in range(8):
        dy = diry[i] + y
        dx = dirx[i] + x
        if dy < 0 or dx < 0 or dy >= 4 or dx >= 5: continue
        if arr[dy][dx] == 1: continue
        arr[dy][dx] = 1
        ret = cnt
        q.append((dy, dx, cnt + 1))

print(ret)