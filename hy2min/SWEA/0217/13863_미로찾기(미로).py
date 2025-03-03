
def dfs(y,x):
    global flag
    
    d_y = [0,0,-1,1]
    d_x = [1,-1,0,0]
    
    if arr[y][x] ==3:
        flag = 1
        return 

    for i in range(4):
        dy = y + d_y[i]
        dx = x + d_x[i]
        if dy <0 or dx < 0 or dy >= n or dx >= n:
            continue
        if arr[dy][dx]==1 or used[dy][dx] == 1:
            continue
        used[dy][dx] = 1
        dfs(dy,dx)
        if flag:
            return

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int,input().strip())) for _ in range(n)]
    
    used = [[0]*n for _ in range(n)]
    
    flag = 0
    sy=sx=-1
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                sy, sx = i,j

    used[sy][sx] = 1
    dfs(sy,sx)
    
    print(f'#{tc} {flag}')