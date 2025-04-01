import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

arr = [[0, 0, 0, 0],
       [1, 1, 0, 1],
       [0, 0, 0, 0],
       [1, 0, 1, 0],]

y1, x1 = map(int, input().split())
y2, x2 = map(int, input().split())

q = deque()
q.append((y1, x1, 0))
diry = [0, 0, 1, -1]
dirx = [1, -1, 0, 0]
ret = 0
while 1:
    y, x, cnt = q.popleft()
    if y == y2 and x == x2:
        ret = cnt
        break
    for i in range(4):
        dy = diry[i] + y
        dx = dirx[i] + x
        if dy < 0 or dx < 0 or dy >= 4 or dx >= 4: continue
        if arr[dy][dx] == 1: continue
        q.append((dy, dx, cnt + 1))
        arr[dy][dx] = 1

print(f'{ret}회')
