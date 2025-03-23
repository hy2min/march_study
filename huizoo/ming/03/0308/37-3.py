arr = [input().split() for _ in range(4)]
queue = []
for i in range(4):
    for j in range(5):
        if arr[i][j] == '1':
            queue.append((i, j))
            arr[i][j] = 0
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
time = 0
while queue:
    y, x = queue.pop(0)
    time = max(time, arr[y][x])
    for i in range(8):
        ny, nx = y+dy[i], x+dx[i]
        if ny<0 or nx<0 or ny>=4 or nx>=5: continue
        if arr[ny][nx] != '0': continue
        arr[ny][nx] = arr[y][x] + 1
        queue.append((ny, nx))
print(time)