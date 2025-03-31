T = int(input())
for tc in range(1, T+1):
    cost_day, cost_month, cost_month3, cost_year = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    dp = [0]*12
    dp[0] = min(cost_day * arr[0], cost_month)
    dp[1] = dp[0] + min(arr[1] * cost_day, cost_month)
    for month in range(2, 12):
        dp[month] = min(dp[month-3] + cost_month3,
                        dp[month-1] + (arr[month] * cost_day),
                        dp[month-1] + cost_month)
    print(f'#{tc} {min(dp[11], cost_year)}')