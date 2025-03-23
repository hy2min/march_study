def dfs(x):
    path.append(x)
    for i in range(n):
        if arr[x][i]:
            dfs(i)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
path = []
dfs(0)
print(*path)