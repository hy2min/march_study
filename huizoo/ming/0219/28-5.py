def dfs(level, x):
    if level == 3:
        print(*path)
        return
    for i in range(N):
        if arr[x][i]:
            path[level] = i
            dfs(level+1, i)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
path = [0]*3
dfs(1, 0)
