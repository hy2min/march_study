import sys
sys.stdin=open('input.txt','r')

from collections import deque
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
visited=set()
visited.add((0,0))
q.append((0, 0))
Flag = False
diry = [0, 0, 1, -1]
dirx = [1, -1, 0, 0]



while q:
    y, x = q.popleft()
    if y == N-1 and x == N-1:
        Flag = True
        break

    for i in range(4):
        dy = diry[i] + y
        dx = dirx[i] + x
        if dy < 0 or dx < 0 or dy >= N or dx >= N: continue
        if arr[dy][dx] == 1: continue
        if (dy, dx) in visited: continue
        visited.add((dy, dx))
        q.append((dy, dx))

if Flag:
    print('가능')
else:
    print('불가능')