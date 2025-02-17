T=10

def dfs(now):
    global flag
    if now==99:
        flag=1
        return

    for i in range(100):
        if arr[now][i] == 1:
            dfs(i)

for tc in range(1,T+1):
    tc,N = map(int,input().split())
    lst=list(map(int,input().split()))
    arr=[[0]*100 for _ in range(100)]
    col=[]
    row=[]
    flag=0
    for i in range(N):
        col.append(lst[i*2])
        row.append(lst[i*2+1])

    for i in range(N):
        arr[col[i]][row[i]] = 1

    dfs(0)

    if flag:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


