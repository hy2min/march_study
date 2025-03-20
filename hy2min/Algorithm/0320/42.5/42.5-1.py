d_y = [-1,1,0,0]
d_x = [0,0,-1,1]


def dfs(y, x):
    


arr = [list(input()) for _ in range(4)]

for i in range(4):
    for j in range(4):
        if arr[i][j].isalpha():
            dfs(i,j)