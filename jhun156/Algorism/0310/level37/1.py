from collections import deque

N = int(input())
arr = [[0] * N for _ in range(N)]
used = [[0]* N for _ in range(N)]
q = deque()
y1,x1,y2,x2 = map(int,input().split())
q.append((y1,x1))
q.append((y2,x2))
arr[y1][x1] = 1
arr[y2][x2] = 1
used[y1][x1] = 1
used[y2][x2] = 1
directY = [0,0,-1,1]
directX = [1,-1,0,0]

while q:
    nowy,nowx = q.popleft()

    for i in range(4):
        dy = nowy + directY[i]
        dx = nowx + directX[i]
        if dy < 0 or dy > N - 1 or dx < 0 or dx > N - 1:
            continue
        if arr[dy][dx] != 0:
            continue
        if arr[dy][dx] == 0 and used[dy][dx] == 0:
            used[dy][dx] = 1
            if arr[nowy][nowx] == 9:
                arr[dy][dx] = 9
            else:
                arr[dy][dx] = arr[nowy][nowx] + 1
            q.append((dy,dx))

for i in range(N):
    for j in range(N):
        print(arr[i][j],end='')
    print()