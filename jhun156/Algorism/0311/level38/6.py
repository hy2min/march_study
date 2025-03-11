# import sys
# sys.stdin = open("input.txt","r")
from collections import deque

N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j].isdigit():
            arr[i][j] = int(arr[i][j])

dY = [-1,1,0,0]
dX = [0,0,-1,1]

def find(y,x,cnt,num):

    q = deque()
    q.append((y,x,cnt))
    visited = [[0] * M for _ in range(N)]
    visited[y][x] = 1

    while q:
        ny,nx,time = q.popleft()
        if arr[ny][nx] == num:
            return ny,nx,time

        for i in range(4):
            dy = ny + dY[i]
            dx = nx + dX[i]
            if dy < 0 or dy > N - 1 or dx < 0 or dx > M - 1: continue
            if visited[dy][dx] == 1: continue
            if arr[dy][dx] == '#': continue
            visited[dy][dx] = 1
            q.append((dy,dx,time+1))

Y,X = 0,0
ans = 0
for i in range(1,5):
    Y,X,num = find(Y,X,0,i)
    ans += num

print(f"{ans}회")