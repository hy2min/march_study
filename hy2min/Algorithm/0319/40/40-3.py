arr = list(map(int, input().split())) + [0]

dp = [0] * 13  # 누적합 저장
#
for i in range(2, 13):
    t1 = dp[i-2]
    t2 = dp[i-3]

    t3 = dp[i//2] if i >= 1 else 0

    if i % 2 == 0:
        dp[i] = arr[i] + max(t1, t2, t3)
    else:
        dp[i] = arr[i] + max(t1, t2)

print(max(dp))
