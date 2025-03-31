import sys
sys.stdin=open('input.txt','r')

from collections import deque

def bfs(y,x):
    global arr
    q = deque()
    q.append((y, x))
    target = arr[y][x]
    arr[y][x] = '-'
    cnt = 1
    while 1:
        y, x= q.popleft()
        for i in range(4):
            dy = diry[i] + y
            dx = dirx[i] + x
            if dy < 0 or dx < 0 or dx >= 9 or dy >= 4: continue
            if arr[dy][dx] != target: continue
            arr[dy][dx] = '_'
            cnt += 1
            q.append((dy, dx))

        if not q:
            return cnt



arr = [list(input().split()) for _ in range(4)]
Max = -1e8
Max_bee = 0
diry = [0, 0, 1, -1]
dirx = [1, -1, 0, 0]


for i in range(4):
    for j in range(9):
        if arr[i][j] != '_':
            target = arr[i][j]
            cnt = bfs(i, j)
            if Max < cnt:
                Max = cnt
                Max_bee = int(target)
print(Max * Max_bee)
