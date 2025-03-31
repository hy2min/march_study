arr = list(input().split())
used = [0] * 3
path = [0] * 3

def dfs(level):

    if level == 3:
        for i in range(3):
            print(path[i],end='')
        print()
        return

    for i in range(3):
        if used[i] == 0:
            used[i] = 1
            path[level] = arr[i]
            dfs(level+1)
            used[i] = 0

dfs(0)