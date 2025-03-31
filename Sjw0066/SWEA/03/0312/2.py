T=int(input())

def dfs(y,x,Sum):
    global Min

    if y==N-1 and x== N-1 :
        if Min>Sum:
            Min=Sum
        return

    if Min<Sum:
        return

    for i in range(2):
        dy=direct_y[i] + y
        dx=direct_x[i] + x
        if dy>N-1 or dx>N-1 : continue
        dfs(dy,dx,Sum+arr[dy][dx])



for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    direct_y=[1,0]
    direct_x=[0,1]
    Min=21e8
    dfs(0,0,arr[0][0])
    print(f'#{tc} {Min}')
