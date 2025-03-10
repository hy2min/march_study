# import sys
# sys.stdin = open("input.txt","r")
from collections import deque

visited = [[0] * 9 for _ in range(4)]
arr = [list(map(int,input().split())) for _ in range(4)]

def bfs(y,x):

    target = arr[y][x]
    cnt = 1
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    dY = [0,0,1,-1]
    dX = [1,-1,0,0]

    while q:
        ny,nx = q.popleft()
        for i in range(4):
            dy = ny + dY[i]
            dx = nx + dX[i]
            if dy < 0 or dy > 3 or dx < 0 or dx > 8: continue
            if visited[dy][dx] == 0 and arr[dy][dx] == target:
                visited[dy][dx] = 1
                cnt += 1
                q.append((dy,dx))

    return cnt

ans = 0
Max = -1000
for i in range(4):
    for j in range(9):
        if arr[i][j] != 0:
            num = bfs(i,j)
            if Max < num:
                Max = num
                ans = Max * arr[i][j]

print(ans)
