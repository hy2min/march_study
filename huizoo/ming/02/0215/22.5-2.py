def dfs(level):
    if level == n:
        print(*path,sep='')
        return
    for ox in ['x','o']:
        path.append(ox)
        dfs(level+1)
        path.pop()
n = int(input())
path = []
dfs(0)

