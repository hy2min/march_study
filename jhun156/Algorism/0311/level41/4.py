n = int(input())
cnt = 0

def dfs(level,Sum):

    global cnt
    if Sum > 7:
        return
    if level == n:
        if Sum == 7:
            cnt += 1
            return
        return

    for i in range(10):
        dfs(level+1, Sum+i)

dfs(0,0)
print(cnt)