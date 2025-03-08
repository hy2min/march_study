def dfs(level):
    if level == 3:
        print(*path,sep='')
        return
    for i in st:
        if i not in path:
            path.append(i)
            dfs(level+1)
            path.pop()
st = input()
path=[]
dfs(0)
