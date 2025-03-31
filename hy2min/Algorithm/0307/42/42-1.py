def dfs(level, start):
    if level == 3:
        print("".join(path))
        return

    for i in range(start,len(arr)):
        path[level] = arr[i]
        dfs(level+1, i)
        path[level] = 0
path = [""] * 3
arr = input()
dfs(0,0)