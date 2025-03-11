from collections import deque

d_y = [0,0,-1,1]
d_x = [-1,1,0,0]

def bfs(y,x,n,step):
    q = deque()
    visited = [[0] * 7 for _ in range(7)]
    q.append((y,x))
    visited[y][x] = 1
    cnt = 0

    while q:
        y,x = q.popleft()
        for i in range(4):
            dy = y + d_y[i]
            dx = x + d_x[i]
            if dy < 0 or dx < 0 or dy >= 7 or dx >= 7:
                continue
            if not visited[dy][dx]:
                visited[dy][dx] = 1
                q.append((dy,dx))
                cnt += 1
            if arr[dy][dx] == n:
                if cnt < step:
                    return 0
    return 1


arr = [list(map(int, input())) for _ in range(7)]

for i in range(7):
    for j in range(7):
        if arr[i][j] == 1:
            ans1 = bfs(i,j,1,3)
        if arr[i][j] == 2:
            ans2 = bfs(i,j,2,4) 

if ans1 and ans2:
    print('pass')
else:
    print('fail')   