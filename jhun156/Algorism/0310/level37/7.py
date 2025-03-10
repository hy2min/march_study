# import sys
# sys.stdin = open("input.txt","r")
from collections import deque

q = deque()
N, M = map(int,input().split())
arr = [list(input().split()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'S':
            Sy,Sx = i,j
        elif arr[i][j] == 'D':
            Ey,Ex = i,j
        elif arr[i][j] == 'C':
            Cy,Cx = i,j

diY = [0,0,1,-1]
diX = [1,-1,0,0]

def bfs1(sy,sx,ey,ex):

    used = [[0] * M for _ in range(N)]
    used[sy][sx] = 1
    global Min
    q.append((sy,sx,0))

    while q:
        ny, nx, cnt = q.popleft()
        if ny == ey and nx == ex:
            Min = min(Min,cnt)

        for i in range(4):
            dy = ny + diY[i]
            dx = nx + diX[i]
            if dy < 0 or dy > N - 1 or dx < 0 or dx > M - 1: continue
            if used[dy][dx] == 1: continue
            if arr[dy][dx] == 'x': continue
            if arr[dy][dx] == 'D': continue
            used[dy][dx] = 1
            q.append((dy,dx,cnt+1))

    return Min


def bfs2(sy, sx, ey, ex):
    used = [[0] * M for _ in range(N)]
    used[sy][sx] = 1
    global Min
    q.append((sy, sx, 0))

    while q:
        ny, nx, cnt = q.popleft()
        if ny == ey and nx == ex:
            Min = min(Min, cnt)

        for i in range(4):
            dy = ny + diY[i]
            dx = nx + diX[i]
            if dy < 0 or dy > N - 1 or dx < 0 or dx > M - 1: continue
            if used[dy][dx] == 1: continue
            if arr[dy][dx] == 'x': continue
            used[dy][dx] = 1
            q.append((dy, dx, cnt+1))

    return Min

Min = 1e9
ans = 0
ans += bfs1(Sy,Sx,Cy,Cx)
Min = 1e9
ans += bfs2(Cy,Cx,Ey,Ex)
print(ans)