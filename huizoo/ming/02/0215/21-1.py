def dfs(level):
    if level == 2:
        return
    for _ in range(3):
        dfs(level+1)
dfs(0)