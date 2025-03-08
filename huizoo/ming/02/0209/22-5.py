n = int(input())

path = []

def dfs(level, max_level) : 
    if level == max_level : 
        print(''.join(map(str, path)))
        return
    for i in range(1, n+1) : 
        path.append(i)
        for i in range(1, n+1) : 
            path.append(i)
            dfs(level+1, max_level)
            path.pop()
        path.pop()

dfs(0, 2)