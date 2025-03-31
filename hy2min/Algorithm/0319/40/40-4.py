arr = [list(map(int, input().split())) for _ in range(7)]

dp = [[0]*3 for _ in range(7)]

dp[0][0] = 1

for i in range(1,7):
    for j in range(3):
        if arr[i][j] == 0:
            continue
        if j == 0:
            dp[i][j] = arr[i][j] + max(dp[i-1][j], dp[i-1][j+1])
        elif j == 1:
            dp[i][j] = arr[i][j] + max(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
        else:
            dp[i][j] = arr[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[-1]))