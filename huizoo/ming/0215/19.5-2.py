arr = [list(map(int, input().split())) for _ in range(5)]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
def isStable(y, x):
    for i in range(8):
        ny, nx = y+dy[i], x+dx[i]
        if ny<0 or nx<0 or ny>4 or nx>3:continue
        if arr[ny][nx] != 0:
            return 0
    return 1
ok = 1
for i in range(5):
    for j in range(4):
        if arr[i][j]:
             ok = isStable(i, j)
             if not ok:
                 break
    if not ok:
        break
if not ok:
    print('불안정한 상태')
else:
    print('안정된 상태')