# import sys
# sys.stdin = open("input.txt","r")
from collections import deque

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
used = [[0] * M for _ in range(N)]
cnt = 0

def bfs(y,x):

    q = deque()
    q.append((y,x))
    used[y][x] = 1
    diY = [0,0,1,-1]
    diX = [1,-1,0,0]
    global cnt
    cnt += 1

    while q:
        ny,nx = q.popleft()
        for i in range(4):
            dy = ny + diY[i]
            dx = nx + diX[i]
            if dy < 0 or dy > N - 1 or dx < 0 or dx > M - 1: continue
            if arr[dy][dx] == 0: continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            q.append((dy,dx))

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and used[i][j] == 0:
            bfs(i,j)

print(cnt)