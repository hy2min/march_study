
T=int(input())

for tc in range(1,T+1):
    N,M=map(int,input().split())
    a=[list(map(int,input().split())) for _ in range(N)]

    def sum_plus(y,x):
        direct_y=[0,0,-1,1]
        direct_x=[-1,1,0,0]

        sum1=0

        for j in range(1,M):
            for i in range(4):
                ny=j*direct_y[i]+y
                nx=j*direct_x[i]+x

                if ny>N-1 or ny<0 or nx>N-1 or nx<0:
                    continue

                sum1+=a[ny][nx]
        return sum1 + a[y][x]

    def sum_x(y,x):
        direct_y = [1,1,-1,-1]
        direct_x = [1,-1,1,-1]

        sum1 = 0

        for j in range(1,M):
            for i in range(4):
                ny = j * direct_y[i] + y
                nx = j * direct_x[i] + x

                if ny > N-1 or ny < 0 or nx > N-1 or nx < 0:
                    continue

                sum1 += a[ny][nx]

        return sum1 + a[y][x]

    answer=-21e8

    for i in range(N):
        for j in range(N):

            ret1,ret2=sum_x(i,j),sum_plus(i,j)

            if ret1>ret2:
                if ret1>answer:
                    answer = ret1
                    y=i
                    x=j
            else:
                if ret2>answer:
                    answer = ret2
                    y = i
                    x = j

    print(f'#{tc} {answer}')