n = int(input())
path = []
def dfs(x):
    if x == n:
        print(*path, sep='')
        return
    for ox in ['o','x']:
        path.append(ox)
        dfs(x+1)
        path.pop()
dfs(0)

