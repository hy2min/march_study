def dfs(level,sm):
    global mn, best_path
    if level == m:
        if mn > sm:
            mn = sm
            best_path = path[:]
        return
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            path[level] = arr[i]
            dfs(level+1,sm*arr[i])
            visited[i] = 0

n, m = map(int,input().split())
arr = list(map(int, input().split()))

mn = 21e8

path = [0] * m
visited = [0] * n
best_path = []

dfs(0,1)
path.sort()
print(*path)
