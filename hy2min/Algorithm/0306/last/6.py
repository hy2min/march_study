def dfs(level, path):
    if level == 3:
        print(*path)
        return
    for i in range(3):
        dfs(level+1, path + [arr[i]])

arr = list(input().split())

dfs(0,[])