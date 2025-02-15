def dfs(level):
    global cnt
    if level>=2 :
        if path[-2:] == ['B','T'] or path[-2:] == ['T','B']:
            return
    if level == 4:
        cnt += 1
        return
    for i in st:
        path.append(i)
        dfs(level+1)
        path.pop()

st = input()
cnt = 0
path = []
dfs(0)
print(cnt)