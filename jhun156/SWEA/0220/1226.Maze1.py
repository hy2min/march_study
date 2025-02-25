# import sys
# sys.stdin = open("input.txt","r")

from collections import deque

T = 10
for i in range(10):
    tc = int(input())
    arr = [list(map(int,input())) for _ in range(16)]
    sty = stx = 0
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                sty,stx = i,j

    visited = [[0] * 16 for _ in range(16)]
    q = deque()
    q.append((sty, stx))
    visited[sty][stx] = 1
    directY = [0, 0, 1, -1]
    directX = [1, -1, 0, 0]
    flag = 0

    while q:
        y,x = q.popleft()
        if arr[y][x] == 3:
            flag = 1
            break

        for i in range(4):
            dy = y + directY[i]
            dx = x + directX[i]
            if dy < 0 or dy > 15 or dx < 0 or dx > 15:
                continue
            if visited[dy][dx] == 1 or arr[dy][dx] == 1:
                continue
            visited[dy][dx] = 1
            q.append((dy,dx))

    print(f"#{tc} {flag}")