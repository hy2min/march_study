def dfs(level,Sum):
    global cnt
    if Sum > 7:
        return
    if level == n:
        if Sum == 7:
            cnt += 1
        return
    for i in range(10):
        if i > 7:
            return
        dfs (level+1, Sum + i)


n = int(input())
cnt = 0
dfs(0,0)
print(cnt)