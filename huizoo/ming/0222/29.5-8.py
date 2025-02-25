arr = [list(input()) for _ in range(4)]
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
a, c, d = None, None, None
for i in range(4):
    for j in range(3):
        if arr[i][j] == 'A':
            a = [i, j]
        if arr[i][j] == 'C':
            c = [i, j]
        if arr[i][j] == 'D':
            d = [i, j]
for i in range(5):
    diy, dix = direct[i % 4]
    ay, ax = diy + a[0], dix + a[1]
    if 0<=ay<4 and 0<=ax<3:
        if arr[ay][ax] == '_':
            arr[ay][ax], arr[a[0]][a[1]] = arr[a[0]][a[1]], arr[ay][ax]
            a = [ay, ax]
    cy, cx = diy + c[0], dix + c[1]
    if 0<=cy<4 and 0<=cx<3:
        if arr[cy][cx] == '_':
            arr[cy][cx], arr[c[0]][c[1]] = arr[c[0]][c[1]], arr[cy][cx]
            c = [cy, cx]
    dy, dx = diy + d[0], dix + d[1]
    if 0<=dy<4 and 0<=dx<3:
        if arr[dy][dx] == '_':
            arr[dy][dx], arr[d[0]][d[1]] = arr[d[0]][d[1]], arr[dy][dx]
            d = [dy, dx]

for row in arr:
    print(*row, sep='')