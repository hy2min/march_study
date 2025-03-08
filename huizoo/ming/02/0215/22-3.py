def dfs(level):
    if level == n:
        print(*path, sep='')
        return
    for alp in ['B', 'G', 'T', 'K']:
        path.append(alp)
        dfs(level+1)
        path.pop()
path = []
n = int(input())
dfs(0)