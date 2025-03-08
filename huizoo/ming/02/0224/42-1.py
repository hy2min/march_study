st = input()
path = []
def dfs(x, n):
    if x == 3:
        print(*path, sep='')
        return
    for i in range(n, len(st)):
        path.append(st[i])
        dfs(x+1, i)
        path.pop()
dfs(0, 0)