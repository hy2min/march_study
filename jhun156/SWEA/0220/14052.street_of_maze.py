# import sys
# sys.stdin = open("input.txt","r")
from collections import deque

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    sty = stx = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                sty,stx = i,j
                break
    Min = 21e8
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append((sty,stx))
    visited[sty][stx] = 1

    def bfs(y,x,level):

        global Min
        if arr[y][x] == 3:
            if Min > level:
                Min = level
                return
        directY = [0, 0, 1, -1]
        directX = [1, -1, 0, 0]
        while q:
            y, x = q.popleft()
            for i in range(4):
                dy = y + directY[i]
                dx = x + directX[i]
                if dy < 0 or dy > N - 1 or dx < 0 or dx > N - 1:
                    continue
                if visited[dy][dx] == 1 or arr[dy][dx] == 1:
                    continue
                visited[dy][dx] = 1
                q.append((dy, dx))
                bfs(dy,dx,level+1)
                visited[dy][dx] = 0

    bfs(sty,stx,-1)
    if Min == 21e8:
        print(f"#{tc} {0}")
    else:
        print(f"#{tc} {Min}")
