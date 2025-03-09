def dfs(level, Sum):
    global mn,best_path

    if level == m:
        if mn > Sum:
            mn = Sum
            best_path = path[:]
            return
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            path.append(arr[i])
            dfs(level+1, Sum * arr[i])
            path.pop()
            visited[i] = 0


n, m = map(int, input().split())
arr = list(map(int,input().split()))
path = []
best_path = []
visited = [0] * n
mn = 21e8

dfs(0,1) # level, sum
print(*sorted(best_path))