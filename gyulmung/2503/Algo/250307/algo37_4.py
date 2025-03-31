import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

arr = [list(map(int, input().split())) for _ in range(4)]

q = deque()
q.append((0, 0))
diry = [0, 0, 1, -1]
dirx = [1, -1, 0, 0]
ret = 0
while q:
    y, x= q.popleft()
    for i in range(4):
        dy = diry[i] + y
        dx = dirx[i] + x
        if dy < 0 or dx < 0 or dy >= 4 or dx >= 4: continue
        if arr[dy][dx] != 1: continue
        q.append((dy, dx))
        ret += 1
        arr[dy][dx] = 0



print(ret)