import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def virus(q):
    q1 = deque()
    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            dy = diry[i] + y
            dx = dirx[i] + x
            if dy < 0 or dx < 0 or dy >= N or dx >= N: continue
            if arr[dy][dx] != 0: continue
            arr[dy][dx] = cnt
            q1.append((dy, dx, cnt+1))
    return q1

N = int(input())
y1, x1, y2, x2 = map(int, input().split())
arr = [[0]*N for _ in range(N)]

q1 = deque()
q2 = deque()

q1.append((y1, x1, 2))
q2.append((y2, x2, 2))
diry = [0, 0, 1, -1]
dirx = [1, -1, 0, 0]

arr[y1][x1] = 1
arr[y2][x2] = 1

while 1:
    if not q1 and not q2:
        break
    q1 = virus(q1)
    q2 = virus(q2)

for i in arr:
    print(*i, sep='')