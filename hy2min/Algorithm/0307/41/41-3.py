t, n = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()

inf = 21e8
dp = [inf] * (t+1)

for coin in coins:
    for i in range(coin, t+1):
        if i % coin == 0:
            dp[i] = i // coin
        else:
            if i // coin != 0:
                dp[i] = min(dp[i], i//coin + dp[i % coin])
if dp[-1] == inf:
    print('impossible')
else:
    print(dp[-1])