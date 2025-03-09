from collections import deque

n = int(input())
y1, x1, y2, x2 = map(int, input().split())
arr = [[0] * n for _ in range(n)]

arr[y1][x1] = arr[y2][x2] = 1
q = deque()
q.append((y1,x1))
q.append((y2,x2))

d_y = [0,0,-1,1]
d_x = [-1,1,0,0]
while q:
    y,x = q.popleft()
    for i in range(4):
        dy = y + d_y[i]
        dx = x + d_x[i]
        if dy < 0 or dx < 0 or dy >= n or dx >= n:
            continue
        if arr[dy][dx] != 0:
            continue
        arr[dy][dx] = arr[y][x] + 1
        q.append((dy,dx))
for i in arr:
    for j in i:
        print(j,end="")
    print()