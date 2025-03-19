n = int(input())
path = []
cnt = 0
def dfs(level):
    global cnt
    if level == 3:
        cnt += 1
        return
    for i in range(n):
        if i not in path:
            path.append(i)
            dfs(level+1)
            path.pop()
dfs(0)
print(cnt)