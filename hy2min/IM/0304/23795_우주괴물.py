def neon(y,x):
    d_y = [0,0,-1,1]
    d_x = [-1,1,0,0]
    for i in range(4):
        for j in range(1,n+1):
            dy = y + d_y[i] * j
            dx = x + d_x[i] * j
            if dy < 0 or dx < 0 or dy >= n or dx >= n:
                break
            if arr[dy][dx]  == 1:
                break
            arr[dy][dx] = 3
    return

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    mi = mj = -1
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                mi, mj = i,j
    neon(mi,mj)

    cnt = 0
    for i in arr:
        for j in i:
            if j == 0:
                cnt += 1

    print(f'#{tc} {cnt}')