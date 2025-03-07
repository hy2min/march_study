def dfs(level,path):
    if level == 3:
        print(path)
        return
    for i in range(3):
        if used[i] == 0:
            used[i] = 1
            dfs(level+1, path + arr[i])
            used[i] = 0

arr = list(input().split())
used = [0] * 3
dfs(0,'')