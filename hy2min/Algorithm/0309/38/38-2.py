from collections import deque

d_y = [0,0,-1,1]
d_x = [-1,1,0,0]

def bfs(y, x):
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    cnt = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            dy = y + d_y[i]
            dx = x + d_x[i]
            if dy < 0 or dx < 0 or dy >=4 or dx >= 9:
                continue
            if visited[dy][dx] == 0 and arr[dy][dx] == arr[y][x]:
                visited[dy][dx] = 1
                q.append((dy,dx))
                cnt += 1
    return cnt       

arr = [list(map(int, input().split())) for _ in range(4)]
visited = [[0] * 9 for _ in range(4)]

mx = 0
max_value = 0

for i in range(4):
    for j in range(9):
        if not visited[i][j]:
            cnt = bfs(i,j)
            if cnt > mx:
                mx = cnt
                max_value = arr[i][j]

print(mx * max_value)
