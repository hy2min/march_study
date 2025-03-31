n = int(input())
shoot = ['']*4
def dfs(level):
    if level == n:
        print(''.join(shoot))
        return
    for ox in ['o','x']:
        shoot[level] = ox
        dfs(level+1)

dfs(0)