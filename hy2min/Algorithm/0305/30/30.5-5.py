def dfs(level, path):
    if level == n:
        print(path)
        return
    for i in char:
        dfs(level+1, path + i)

char = input()
n = int(input())

dfs(0,"")