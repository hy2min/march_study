T=int(input())

def dfs(level,Sum):
    global Min

    if level==N:
        if Sum<Min:
            Min=Sum
        return

    if Sum>Min:
        return

    for i in range(N):
        if used[i]==1:continue
        used[i] = 1
        dfs(level+1,Sum+arr[level][i])
        used[i] = 0

for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    used=[0] * N
    Min=21e8
    dfs(0,0)
    print(f'#{tc} {Min}')