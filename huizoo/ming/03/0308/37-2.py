N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
Y, X = map(int, input().split())
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
time = 0
queue = [(Y, X)]
arr[Y][X] = 10
while queue:
    y, x = queue.pop(0)
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if ny<0 or nx<0 or ny>=N or nx>=M: continue
        if arr[ny][nx] != 0: continue
        arr[ny][nx] = arr[y][x] + 1
        queue.append((ny, nx))
        time = max(time, arr[ny][nx])

print(time-10)
