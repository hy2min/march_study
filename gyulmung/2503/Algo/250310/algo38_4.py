import sys
sys.stdin=open('input.txt', 'r')

from collections import deque
arr = [list(input()) for _ in range(8)]

def bfs1(y, x):
    global arr
    q1 = deque()
    q2 = deque()
    q1.append((y, x, 0))
    while 1:
        y, x, cnt = q1.popleft()
        for i in range(4):
            dy = diry[i] + y
            dx = dirx[i] + x
            if dy < 0 or dx < 0 or dy >= 8 or dx >= 9: continue
            if arr[dy][dx] == '#':
                arr[dy][dx] = '_'
                q1.append((dy, dx, cnt))
                q2.append((dy, dx, cnt))
        if not q1:
            return q2

diry = [0, 0, 1, -1]
dirx = [1, -1, 0, 0]
island = []
for i in range(8):
    for j in range(9):
        if arr[i][j] == '#':
            island = bfs1(i, j)
            break
    if island:
        break
ret = 0
while island:
    y, x, cnt = island.popleft()
    for i in range(4):
        dy = diry[i] + y
        dx = dirx[i] + x
        if dy < 0 or dx < 0 or dy >= 8 or dx >= 9: continue
        if arr[dy][dx] == '#':
            ret = cnt
            break
        island.append((dy, dx, cnt+1))
    if ret:
        break

print(ret)