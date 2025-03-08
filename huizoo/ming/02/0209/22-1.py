path = []

def dfs(level, max_level) : 
    if level == max_level : 
        print(''.join(path))
        return

    for char in ['A', 'B', 'C'] : 
        path.append(char)
        dfs(level+1, max_level)
        path.pop()

dfs(0, 2)