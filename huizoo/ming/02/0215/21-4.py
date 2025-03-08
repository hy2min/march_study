n = int(input())
def dfs(level):
    print(level, end='')
    if level == n:
        return
    for _ in range(2):
        dfs(level+1)
dfs(0)