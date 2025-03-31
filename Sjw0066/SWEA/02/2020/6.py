name=list(input().split())
name.sort()
path=[0]*len(name)

def dfs(level):

    if level==3:
        print(*path)
        return

    for i in range(3):
        path[level] = name[i]
        dfs(level+1)

dfs(0)