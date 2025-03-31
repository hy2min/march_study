def dfs(level):
    if level == 2:
        print(*path ,sep='')
        return
    for alp in ['A', 'B', 'C']:
        path.append(alp)
        dfs(level+1)
        path.pop()

path = []
dfs(0)