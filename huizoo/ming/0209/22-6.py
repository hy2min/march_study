st = list(input())
arr = ['A', 'B', 'C', 'D']
path = []
cnt = 0
def dfs(level, max_level) : 
    global cnt
    if level == max_level : 
        cnt += 1
        if path == st : 
            print(f'{cnt}번째')
            return
        return
    for alp in arr : 
        path.append(alp)
        dfs(level+1, max_level)
        path.pop()

dfs(0, 3)

