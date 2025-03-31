def dfs(n,cnt):
    global mn
    if n < 0 or cnt >= mn :
        return
    if n == 0:
        mn = min(cnt,mn)
        return
    for i in arr:
        dfs(n-i, cnt+1)
        
arr = [10, 40, 60]
mn = 21e8
n = int(input())
dfs(n,0)
print(mn)