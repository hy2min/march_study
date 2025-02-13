arr = [list(map(int, input().split())) for _ in range(5)]

def stable_state(y, x):
    d_y = [1, 1, 1, 0, 0, -1, -1, -1]
    d_x = [1, 0, -1, 1, -1, 1, 0, -1]
    for i in range(8):
        dy = y + d_y[i]
        dx = x + d_x[i]
        if 0 <= dy < 5 and 0 <= dx < 4:
            if arr[dy][dx] == 1:
                return 0
    return 1

for i in range(5):
    for j in range(4):
        if arr[i][j] == 1:
            result = stable_state(i, j)
            break

if result:
    print('안정된 상태')
else:
    print('불안정한 상태')
