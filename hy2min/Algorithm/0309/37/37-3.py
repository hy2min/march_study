from collections import deque

arr = [list(map(int, input().split())) for _ in range(4)]

d_y = [-1,-1,-1,0,0,1,1,1]
d_x = [-1,0,1,-1,1,-1,0,1]

q = deque()
for i in range(4):
    for j in range(5):
        if arr[i][j] == 1:
           q.append((i, j))

while q:
    y, x = q.popleft()
    for i in range(8):
        dy = y + d_y[i]
        dx = x + d_x[i]
        if dy < 0 or dx < 0 or dy >= 4 or dx >= 5:
            continue
        if arr[dy][dx] == 0:
            arr[dy][dx] = arr[y][x] + 1
            q.append((dy, dx))
mx = -21e8
for i in arr:
    for j in i:
        mx = max(mx, j)
        mx -= 1
print(mx)