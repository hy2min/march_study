def dfs(level):
    global cnt
    if level == 3:
        cnt += 1
        return
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(level+1)
            visited[i] = 0

n = int(input())
cnt = 0
visited = [0] * n
dfs(0)
print(cnt)