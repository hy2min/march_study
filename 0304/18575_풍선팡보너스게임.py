def balloon(y,x):
    sm = arr[y][x]
    d_y = [0,0,-1,1]
    d_x = [-1,1,0,0]
    for i in range(4):
        for j in range(1,n):
            dy = y + d_y[i] * j
            dx = x + d_x[i] * j
            if dy < 0 or dx < 0 or dy >= n or dx >= n:
                continue
            sm += arr[dy][dx]
    return sm


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    mx = -21e8
    mn = 21e8

    for i in range(n):
        for j in range(n):
            mx = max(mx,balloon(i,j))
            mn = min(mn,balloon(i,j))
    ans = mx-mn
    print(f'#{tc} {ans}')