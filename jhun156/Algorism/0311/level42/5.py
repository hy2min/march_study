n = int(input())
cnt = 0

def dfs(level,Sum):
    global cnt
    if Sum > 10 or level > n:
        return
    if level == n:
        if Sum == 10:
            cnt += 1
            return
        return

    for i in range(1,10):
        dfs(level+1,Sum+i)

dfs(0,0)
print(cnt)