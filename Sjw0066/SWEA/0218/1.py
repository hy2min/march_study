T= int(input())

def dfs(now,Sum):
    global Min

    if now==N:
        if Min>Sum:
            Min=Sum
        return

    if Sum>Min:
        return

    for i in range(N):
        if used[i]: continue
        used[i]=1
        dfs(now+1,Sum+arr[now][i])
        used[i]=0

for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    used=[0]*N
    Min=21e8
    dfs(0,0)
    print(f'#{tc} {Min}')
