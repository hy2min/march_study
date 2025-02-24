n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [False]*n

def dfs(x) : 
    print(x, end = ' ')
    visited[x] = True
    for i in range(n):
        if arr[x][i] == 1 and visited[i] == False:
            dfs(i)
    return

dfs(0)