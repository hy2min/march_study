def dfs(level):
    global cnt
    if level == 3:
        cnt+=1
        if target == ''.join(path):
            print(f'{cnt}번째')
        return
    for alp in ['A','B','C','D']:
        path.append(alp)
        dfs(level+1)
        path.pop()
target = input()
cnt = 0
path = []
dfs(0)