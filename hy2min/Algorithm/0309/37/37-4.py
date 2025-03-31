from collections import deque

d_y = [-1,1,0,0]
d_x = [0,0,-1,1]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    cnt = 1
    arr[y][x] = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            dy = y + d_y[i]
            dx = x + d_x[i]
            if dy < 0 or dx < 0 or dy >= 4 or dx >= 4:
                continue
            if arr[dy][dx] == 1:
                q.append((dy, dx))
                cnt += 1
                arr[dy][dx] = 0
    return cnt

arr = [list(map(int, input().split())) for _ in range(4)]
mx = -21e8

for i in range(4):
    for j in range(4):
        if arr[i][j] == 1:
            ans = bfs(i, j)
            mx = max(ans, mx)
print(mx)