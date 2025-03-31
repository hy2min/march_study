def findstart():
    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2':
                return i, j
    return -1, -1

def findend(y, x):
    visited = [[0]*16 for _ in range(16)]
    q = []
    q.append((y, x))
    visited[y][x] = 1
    while q:
        yy, xx = q.pop(0)
        for i in range(4):
            ny, nx = yy+dy[i], xx+dx[i]
            if ny<0 or nx<0 or ny>15 or nx>15:continue
            if visited[ny][nx] != 0:continue
            if arr[ny][nx] !='0' and arr[ny][nx] !='3':continue
            if arr[ny][nx] == '3':
                return 1
            q.append((ny,nx))
            visited[ny][nx] = 1
    return 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for _ in range(10):
    tc = input()
    arr = [input() for _ in range(16)]
    y, x = findstart()
    print(f'#{tc} {findend(y, x)}')