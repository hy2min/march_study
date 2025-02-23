def ant(y,x):
    directy = [1,-1,0,0]
    directx = [0,0,-1,1]
    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]
        if dy < 0 or dx < 0 or dy >=4 or dx >=4:
            continue
        if arr[dy][dx] == 1:
            return 0
    return 1


arr = [list(map(int,input().split())) for _ in range(4)]
flag = 1

for i in range(4):
    for j in range(4):
        if arr[i][j] == 1:
            if ant(i,j) == 0:
                print('위험한 상태')
                flag = 0
                break
    if not flag:
        break
if flag:
    print('안전한 상태')