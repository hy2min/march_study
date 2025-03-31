T=int(input())

for tc in range(1,T+1):
    N=int(input())
    N=N//10
    dp=[0]*(N+1)
    dp[0] = 1
    dp[1] = 1

    # dp[0]=1
    # dp[1]=1
    # dp[2]=1+2
    # dp[3]=3+2
    # dp[4]=5+6
    # dp[5]=10+11
    # dp[6]=22+21
    # dp[7]=42+43

    for i in range(N+1):
        if i>1:
            dp[i] = dp[i-1]+dp[i-2]*2

    print(f'#{tc} {dp[N]}')