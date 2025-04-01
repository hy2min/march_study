N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
path = [0]*3
level = 0

def dfs(now):
    global level

    if level == 2:
        print(*path)
        return

    for i in range(N):
        if arr[now][i] == 1:
            path[level+1] = i
            level += 1
            dfs(i)
            level -= 1
dfs(0)