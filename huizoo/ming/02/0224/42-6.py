N, M = map(int, input().split())
arr = list(map(int, input().split()))
path = []
Min = 500
ans = []
used = [0]*N
def dfs(x, mul):
    global Min, ans
    if x == M:
        if Min > mul:
            Min = mul
            ans = path[:]
        return
    for i in range(N):
        if not used[i]:
            path.append(arr[i])
            used[i] = 1
            dfs(x+1, mul*arr[i])
            path.pop()
            used[i] = 0

dfs(0, 1)
print(*sorted(ans))