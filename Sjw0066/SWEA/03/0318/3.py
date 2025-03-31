T=int(input())

def dfs(level,can):
    global Max
    if level==N:
        if can>Max:
            Max=can
        return

    if can<=Max:
        return

    for i in range(N):
        if used[i]==1:continue
        used[i]=1
        dfs(level+1,can*arr[level][i]/100)
        used[i]=0

for tc in range(1,T+1):
    N=int(input())
    Max=0
    arr=[list(map(int,input().split())) for _ in range(N)]
    used=[0]*N
    dfs(0,1)
    Max=round(Max*100,6)
    ans=f'{Max:.6f}'
    print(f'#{tc} {ans}')
