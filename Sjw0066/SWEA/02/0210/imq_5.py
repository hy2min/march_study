
T=int(input())

for tc in range(1,T+1):
    N,M=map(int,input().split())
    a=[list(map(int,input().split())) for _ in range(N)]

    def check_land(y,x):
        direct_y=[1,1,1,-1,-1,-1,0,0]
        direct_x=[1,0,-1,1,0,-1,1,-1]

        cnt=0

        for i in range(len(direct_x)):
            ny=y+direct_y[i]
            nx=x+direct_x[i]
            if ny>N-1 or ny<0 or nx>M-1 or nx<0:
                continue
            if a[y][x] > a[ny][nx]:
                cnt+=1

        if cnt>=4:
            return 1
        else:
            return 0

    answer=0

    for i in range(N):
        for j in range(M):
            answer += check_land(i,j)


    print(f'#{tc} {answer}')