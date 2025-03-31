d_y = [-1,-1,-1,0,0,1,1,1]
d_x = [-1,0,1,-1,1,-1,0,1]


def landing(y,x):
    cnt = 0
    for i in range(8):
        dy = y + d_y[i]
        dx = x + d_x[i]
        if dy < 0 or dx < 0 or dy >= n or dx >= m:
            continue
        if arr[y][x] > arr[dy][dx]:
            cnt += 1
    return cnt


t = int(input())
for tc in range(1, t+1):
    n,m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(m):
            if landing(i,j) >= 4:
                
                ans += 1
    print(f'#{tc} {ans}')