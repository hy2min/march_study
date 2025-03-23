names = input()
path = []
def dfs(level, max_level) :
    if level == max_level :
        print(''.join(path))

    for name in names :
        if name not in path :
            path.append(name)
            dfs(level+1, max_level)
            path.pop()

dfs(0, 3)
