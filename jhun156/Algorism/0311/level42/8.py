N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
visited[0][0] = 1
dY = [0,0,1,-1]
dX = [1,-1,0,0]
flag = 0

def dfs(y,x):

    global flag
    if y == N - 1 and x == N - 1:
        flag = 1
        return

    for i in range(4):
        dy = y + dY[i]
        dx = x + dX[i]
        if dy < 0 or dy > N - 1 or dx < 0 or dx > N - 1: continue
        if visited[dy][dx] == 1: continue
        if arr[dy][dx] == 1: continue
        visited[dy][dx] = 1
        dfs(dy,dx)
        visited[dy][dx] = 0

dfs(0,0)
if flag:
    print("가능")
else:
    print("불가능")