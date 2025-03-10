from collections import deque

lst = []
Max = -1
arr = [list(map(int,input().split())) for _ in range(4)]
q = deque()

for i in range(4):
    for j in range(5):
        if arr[i][j] == 1:
            q.append((i,j,0))

directY = [0,0,1,-1,1,1,-1,-1]
directX = [1,-1,0,0,1,-1,1,-1]

while q:

    ny,nx,cnt = q.popleft()
    Max = max(Max,cnt)

    for i in range(8):
        dy = ny + directY[i]
        dx = nx + directX[i]
        if dy < 0 or dy > 3 or dx < 0 or dx > 4:
            continue
        if arr[dy][dx] == 1:
            continue
        arr[dy][dx] = 1
        q.append((dy,dx,cnt+1))

print(cnt)