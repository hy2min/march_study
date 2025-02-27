def dfs(level,SUM):
    global MIN
    if SUM>MIN:
        return
    if level==n:
        if MIN>SUM:
            MIN=SUM
        return
 
    for i in range(n):
        if used[i]==1:continue
        used[i]=1
        dfs(level+1,SUM+arr[level][i])
        used[i]=0
 
T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    used=[0]*n
    MIN=21e8
    dfs(0,0)
    print(f'#{test_case}',MIN)