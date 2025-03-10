from collections import deque

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
Y,X = map(int,input().split())
q = deque()
q.append((Y,X,0))
used = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            used[i][j] = 1

Max = 0
directY = [0,0,-1,1]
directX = [1,-1,0,0]

while q:

    nowy, nowx, cnt = q.popleft()
    arr[nowy][nowx] = cnt
    Max = max(Max,cnt)
    for i in range(4):
        dy = nowy + directY[i]
        dx = nowx + directX[i]
        if dy < 0 or dy > N - 1 or dx < 0 or dx > M - 1:
            continue
        if arr[dy][dx] != 0:
            continue
        if arr[dy][dx] == 0 and used[dy][dx] == 0:
            used[dy][dx] = 1
            q.append((dy,dx,cnt+1))

print(Max)