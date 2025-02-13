T = int(input())
for tc in range(1, T+1):
    N = int(input())//10
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N + 1):
        if i + 1 <= N:
            dp[i + 1] += dp[i]
        if i + 2 <= N:
            dp[i + 2] += dp[i]
        if i + 2 <= N:
            dp[i + 2] += dp[i]

    print(f'#{tc} {dp[N]}')

