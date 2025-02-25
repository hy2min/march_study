def dfs(level):
    if level == 4:
        print(*path,sep='')
        return
    for i in 'EWABC':
        if i not in path and i != a:
            path.append(i)
            dfs(level+1)
            path.pop()

path = []
a = input()
dfs(0)