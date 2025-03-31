arr = [[0,0,1,1,0,1],
       [0,0,0,1,1,1],
       [0,0,0,0,1,1],
       [0,0,0,0,0,0],
       [1,0,0,0,0,1],
       [0,0,0,0,0,0],]


def dfs(level):
    print(level, end= ' ')


    for i in range(6):
        if arr[level][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)

visited = [0]*6
N = int(input())
visited[N] = 1
dfs(N)