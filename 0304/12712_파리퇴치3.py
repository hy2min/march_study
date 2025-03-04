def cross(y,x):
    sm = arr[y][x]
    d_y = [0,0,-1,1]
    d_x = [-1,1,0,0]
    for i in range(4):
        for power in range(1, m):
            dy = y + d_y[i] * power
            dx = x + d_x[i] * power
            if dy < 0 or dx < 0 or dy >= n or dx >= n:
                continue
            sm += arr[dy][dx]
    return sm

def ex(y,x):
    sm = arr[y][x]
    d_y = [-1,-1,1,1]
    d_x = [-1,1,-1,1]
    for i in range(4):
        for power in range(1, m):
            dy = y + d_y[i] * power
            dx = x + d_x[i] * power
            if dy < 0 or dx < 0 or dy >= n or dx >= n:
                continue
            sm += arr[dy][dx]
    return sm

t = int(input())

for tc in range(1, t+1):
    n,m = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    mx = -21e8
    for i in range(n):
        for j in range(n):
            mx_part = max(cross(i,j), ex(i,j))
            mx = max(mx_part,mx)
    print(f'#{tc} {mx}')
    