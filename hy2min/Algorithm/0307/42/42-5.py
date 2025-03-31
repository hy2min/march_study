def dfs(level, sm):
    global cnt
    if level == n:
        if sm == 10:
            cnt += 1
        return
    for i in range(1, 10):
        dfs(level+1, sm + i)

n = int(input())
cnt = 0
dfs(0, 0)
print(cnt)