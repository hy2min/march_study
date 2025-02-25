def catch(y,x):
    flag = 0
    d_y = [-1,1,0,0]
    d_x = [0,0,-1,1]
    for i in range(4):
        dy = y + d_y[i]
        dx = x + d_x[i]
        if dy < 0 or dx < 0 or dy >= 7 or dx >= 7:
            continue
        if arr[dy][dx] == 0:
            flag = 1
            break

    return flag

arr = [
    [0,0,0,0,0,0,0],
    [0,0,1,0,1,0,0],
    [0,1,2,0,2,1,0],
    [0,0,1,2,1,0,0],
    [0,0,2,1,0,1,0],
    [0,1,1,0,0,0,0],
    [0,0,0,0,0,0,0],
]
n,m = map(int, input().split())
arr[n][m] = 1
cnt = 0
for i in range(7):
    for j in range(7):
        if arr[i][j] == 2:
            if catch(i,j) == 0:
                cnt += 1
print(cnt)