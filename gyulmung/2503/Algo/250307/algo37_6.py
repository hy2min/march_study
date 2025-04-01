import sys
sys.stdin=open('input.txt', 'r')

from collections import deque

arr = [list(map(int, input().split())) for _ in range(4)]

diry = [0, 0, 1, -1]
dirx = [1, -1, 0, 0]

q = deque()
q.append((0,0))
cnt = 0
while q:
    y, x = q.popleft()

    for i in range(4):
        dy = diry[i] + y
        dx = dirx[i] + x
        if dy < 0 or dx < 0 or dy >= 4 or dx >= 6: continue
        if arr[dy][dx] == 1: continue
        if arr[dy][dx] == 2:
            cnt += 1
        q.append((dy, dx))
        arr[dy][dx] = 1
print(cnt)