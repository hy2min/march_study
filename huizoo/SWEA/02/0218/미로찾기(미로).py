import copy

def abc(y, x):
    global OX
    if arr[y][x] == '3':
        OX = 1
        return
    for i in range(4):
        if OX: return
        ny, nx = y+dy[i], x+dx[i]
        if ny<0 or nx<0 or ny>N-1 or nx>N-1:continue
        if used[ny][nx] == '1': continue
        used[ny][nx] = '1'
        abc(ny, nx)

t = int(input())

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
for tc in range(1, t+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    used = copy.deepcopy(arr)
    OX = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                abc(i, j)
    print(f'#{tc} {OX}')