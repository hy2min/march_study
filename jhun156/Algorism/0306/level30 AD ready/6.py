arr = list(input().split())
path = [0] * 3

def dfs(level):

    if level == 3:
        print(*path)
        return

    for i in range(3):
        path[level] = arr[i]
        dfs(level+1)

dfs(0)