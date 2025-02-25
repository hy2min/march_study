level = int(input())
branch = int(input())
def dfs(n):
    if n == level:
        return
    for _ in range(branch):
        dfs(n+1)
dfs(0)