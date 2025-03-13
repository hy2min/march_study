delta = [(1, 0), (0, 1)]
def dfs(y,x):
        for d_y, d_x in delta:
            dy = y + d_y
            dx = x + d_x
            if



mx = -21e8
arr = [list(map(int, input().split())) for _ in range(4)]

for i in range(4):
     for j in range(8):
         if arr[i][j] != 0:
             dfs(i,j)