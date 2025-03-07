def dfs(level):
    global mx, mn
    if level == 5:
        sm = (path[0]*path[1])-(path[2]*path[3])+path[4]
        mx = max(mx, sm)
        mn = min(mn, sm)
        return
    for i in range(5):
        if used[i] == 0:
            used[i] = 1
            path[level] = arr[i]
            dfs(level+1)
            used[i] = 0

arr = list(map(int, input().split()))
path = [0] * 5
used = [0] * 5
mx = -21e8
mn = 21e8
dfs(0)
print(mx)
print(mn)