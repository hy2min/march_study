table = [
    [0,0,1,1,0,1],
    [0,0,0,1,1,1],
    [0,0,0,0,1,1],
    [0,0,0,0,0,0],
    [1,0,0,0,0,1],
    [0,0,0,0,0,0],
]
K = int(input())
visited = [0]*6
visited[K] = 1

def dfs(x):
    print(x, end=' ')
    for i in range(6):
        if table[x][i] and not visited[i]:
            visited[i] = 1
            dfs(i)

dfs(K)