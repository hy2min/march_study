def dfs(level):
    global cnt
    if level == n:
        if 'S' in path:
            cnt+=1
            return
        return
    for i in 'BTSKR':
        if i not in path:
            path.append(i)
            dfs(level+1)
            path.pop()
n = int(input())
cnt = 0
path = []
dfs(0)
print(cnt)