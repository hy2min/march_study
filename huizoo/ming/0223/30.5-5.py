name = input()
pick = int(input())
path = []
def dfs(x):
    if x == 2:
        print(*path, sep='')
        return
    for i in name:
        path.append(i)
        dfs(x+1)
        path.pop()
dfs(0)