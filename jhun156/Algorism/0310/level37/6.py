# import sys
# sys.stdin = open("input.txt","r")
from collections import deque

used = [[0] * 6 for _ in range(4)]
used[0][0] = 1
q = deque()
arr = [list(map(int,input().split())) for _ in range(4)]
q.append((0,0))
cnt = 0

diY = [0,0,1,-1]
diX = [1,-1,0,0]

while q:

    ny, nx = q.popleft()
    if arr[ny][nx] == 2:
        cnt += 1
    for i in range(4):
        dy = ny + diY[i]
        dx = nx + diX[i]
        if dy < 0 or dy > 3 or dx < 0 or dx > 5:
            continue
        if used[dy][dx] == 1:
            continue
        if arr[dy][dx] == 1:
            continue
        used[dy][dx] = 1
        q.append((dy,dx))

print(cnt)