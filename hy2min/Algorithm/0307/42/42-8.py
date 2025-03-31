d_y = [0,0,-1,1]
d_x = [-1,1,0,0]
def dfs(y,x):
    if (y,x) == (n-1,n-1):
        return 1

    for k in range(4):
        dy = y + d_y[k]
        dx = x + d_x[k]
        if 0 <= dy < n and 0 <= dx < n:
            if arr[dy][dx] == 0 and visited[dy][dx] == 0:
                visited[dy][dx] = 1
                if dfs(dy,dx):
                    return 1
                visited[dy][dx] = 0
    return 0


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

visited[0][0] = 1
if dfs(0,0):
    print('가능')
else:
    print('불가능')