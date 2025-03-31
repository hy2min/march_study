tree = [
    [0,0,1,1,0,1],
    [0,0,0,1,1,1],
    [0,0,0,0,1,1],
    [0,0,0,0,0,0],
    [1,0,0,0,0,1],
    [0,0,0,0,0,0],
]

visited = [False]*6

def dfs(x):
    print(x, end = " ")
    visited[x] = True
    for i in range(6):
        if tree[x][i] == 1 and not visited[i]:
            dfs(i)

n = int(input())
dfs(n)