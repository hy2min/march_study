st = input()
length = len(st)
def dfs(level):
    print(level, end=' ')
    if level == 1:
        return
    dfs(level-1)
    print(level, end=' ')
dfs(length)