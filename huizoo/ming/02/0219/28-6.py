def dfs(x):
    global path
    for i in range(len(st)):
        if arr[x][i]:
            path += st[i]
            dfs(i)
st = input()
arr = [list(map(int, input().split())) for _ in range(len(st))]

path = st[0]
dfs(0)
print(path)