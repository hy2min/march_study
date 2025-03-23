n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n

def dfs(x):
    print(x, end = ' ')
    
    for i in range(n):
        if tree[x][i] == 1 and not visited[i]:
            dfs(i)

dfs(0)
