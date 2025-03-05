n = int(input())

def dfs(level, path):
    if level == n:
        print(path)
        return
    for i in "ox":
        dfs(level+1, path+i)

dfs(0,"")