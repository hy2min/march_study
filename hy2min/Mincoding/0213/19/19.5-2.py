def find(y,x):
        
    d_y = [-1,-1,-1,0,0,1,1,1]
    d_x = [-1,0,1,-1,1,-1,0,1]

    for i in range(8):
        dy = y + d_y[i]
        dx = x + d_x[i]
        if dy < 0 or dx < 0 or dy >= 5 or dx >= 4:
            continue
        if arr[dy][dx] == 1:
            return 0
    return 1

arr = [list(map(int, input().split())) for _ in range(5)]

flag = 1
for y in range(5):
    for x in range(4):
        if arr[y][x] == 1:
            if find(y,x) == 0:
                flag = 0
                break
    if not flag:
        break

if flag:
    print('안정된 상태')
else:
    print('불안정한 상태')
