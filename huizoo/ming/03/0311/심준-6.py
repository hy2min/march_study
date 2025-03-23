arr = input().split()
path = []
def dfs(level):
    if level == 3:
        print(' '.join(path))
        return
    for who in arr:
        path.append(who)
        dfs(level+1)
        path.pop()

dfs(0)