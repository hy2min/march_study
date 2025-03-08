branch, level = map(int, input().split())
cnt = 0
def dfs(n):
    global cnt
    cnt += 1
    if n == level:
        return
    for _ in range(branch):
        dfs(n+1)
dfs(0)
print(cnt)