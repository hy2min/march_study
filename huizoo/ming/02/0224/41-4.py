n = int(input())
arr = [i for i in range(10)]
cnt = 0
pick = []
def dfs(x, Sum):
    global cnt
    if x == n:
        if Sum == 7:
            cnt += 1
        return
    if Sum > 7:
        return
    for i in arr:
        dfs(x+1, Sum+i)
dfs(0, 0)
print(cnt)