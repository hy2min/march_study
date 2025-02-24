def dfs(level):
    global Max
    if level == 3:
        Sum = sum(path)
        if Sum <= M and Max < Sum:
            Max = Sum
        return
    for i in arr:
        if i not in path:
            path.append(i)
            dfs(level+1)
            path.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
path = []
Max = 0
dfs(0)
print(Max)

