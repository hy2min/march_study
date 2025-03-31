T= int(input())

def bomb(y,x):
    Sum=lst[y][x]

    for i in range(4):
        for j in range(1,N):
            ny=y+direct_y[i] * j
            nx=x+direct_x[i] * j

            if ny>N-1 or ny<0 or nx<0 or nx>N-1:
                continue
            Sum+=lst[ny][nx]

    return Sum

for tc in range(1,T+1):
    N=int(input())
    lst=[list(map(int,input().split())) for _ in range(N)]

    direct_x=[0,0,1,-1]
    direct_y=[-1,1,0,0]

    Max=-21e8
    Min=21e8
    for i in range(N):
        for j in range(N):
            result=bomb(i,j)

            if result>Max:
                Max=result
            if result<Min:
                Min=result

    print(f'#{tc} {Max-Min}')
