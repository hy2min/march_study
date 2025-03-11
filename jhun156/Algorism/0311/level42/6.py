N,M = map(int,input().split())
arr = list(map(int,input().split()))
path = [0] * M
used = [0] * N
Min = 10000
ans = []

def dfs(level,Mul):

    global Min,ans,path
    if level == M:
        if Min > Mul:
            Min = Mul
            ans = path[:]
        return

    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            path[level] = arr[i]
            dfs(level+1,Mul*arr[i])
            used[i] = 0

dfs(0,1)
ans.sort()
print(*ans)