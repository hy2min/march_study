def dfs(level):
    if level == 4:
        print(*path, sep='')
        return
    for i in range(1, n+1):
        path.append(i)
        dfs(level+1)
        path.pop()

n = int(input())
path = []
dfs(0)
