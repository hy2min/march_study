T=int(input())

def dfs(cnt,level):
    global Max

    if level==N-1:
        if cnt>Max:
            Max=cnt

    for i in range(level+1,N):
        if arr[i][0]>=arr[level][1]:
            dfs(cnt+1,i)

for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    arr.sort()
    Max=-21e8
    for i in range(N):
        dfs(1,i)
    print(f'#{tc} {Max}')