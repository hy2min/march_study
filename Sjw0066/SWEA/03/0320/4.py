from collections import deque
T=int(input())

for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    result=[[21e8]*N for _ in range(N)]
    result[0][0] = 0
    direct_y=[0,0,1,-1]
    direct_x=[1,-1,0,0]

    q=deque()
    q.append((0,0,0))

    while q:
        y,x,now=q.popleft()
        if result[y][x] < now: continue
        for i in range(4):
            dy=direct_y[i]+y
            dx=direct_x[i]+x
            if dy<0 or dx<0 or dy>N-1 or dx>N-1:continue
            if arr[dy][dx] > arr[y][x] :
                Next=now+1+abs(arr[dy][dx]-arr[y][x])
            else:
                Next=now+1

            if result[dy][dx] > Next:
                result[dy][dx] = Next
                q.append((dy,dx,Next))

    print(f'#{tc} {result[N - 1][N - 1]}')










