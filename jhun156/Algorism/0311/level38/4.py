# import sys
# sys.stdin = open("input.txt","r")
from collections import deque
from copy import deepcopy

arr = [list(input()) for _ in range(8)]
visited = [[0] * 9 for _ in range(8)]
flag = 0
dY = [0,0,1,-1]
dX = [1,-1,0,0]

def find(y,x):
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    result = deque()
    result.append((y,x))

    while q:
        ny, nx = q.popleft()
        for i in range(4):
            dy = ny + dY[i]
            dx = nx + dX[i]
            if dy < 0 or dy > 7 or dx < 0 or dx > 8: continue
            if visited[dy][dx] == 1: continue
            if arr[dy][dx] == '_': continue
            visited[dy][dx] = 1
            q.append((dy,dx))
            result.append((dy,dx))

    return result

for i in range(8):
    for j in range(9):
        if arr[i][j] == '#':
            p = find(i,j)
            flag = 1
        if flag:
            break
    if flag:
        break

Q = deque()
while p:
    y,x = p.popleft()
    Q.append((y,x,0))
# Q에 visited를 포함해서 다시 넣기

Min = 21e8
lst = deepcopy(visited)

while Q:
    visited = lst
    ny, nx, cnt = Q.popleft()
    if arr[ny][nx] == '#' and cnt != 0:
        Min = min(cnt-1, Min)

    for i in range(4):
        dy = ny + dY[i]
        dx = nx + dX[i]
        if dy < 0 or dy > 7 or dx < 0 or dx > 8: continue
        if visited[dy][dx] == 1: continue
        visited[dy][dx] = 1
        Q.append((dy,dx,cnt+1))

print(Min)