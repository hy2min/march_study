lst = [list(map(int, input().split())) for _ in range(5)]

def find_one(y, x):
    count = 0
    direct_Y = [0, 0, 1, -1, 1, 1, -1, -1]
    direct_X = [1, -1, 0, 0, 1, -1, 1, -1]
    for i in range(8):
        dy = direct_Y[i] + y
        dx = direct_X[i] + x
        if dy < 0 or dx < 0 or dy >= 5 or dx >= 4:
            continue
        elif lst[dy][dx] == 1:
            count += 1
    return count

count = 0
for i in range(5):
    for j in range(4):
        if lst[i][j] == 1:
            count += find_one(i, j)

if count == 0:
    print('안정된 상태')
else:
    print('불안정한 상태')
