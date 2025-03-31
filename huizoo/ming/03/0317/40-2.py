def abc(n, memo = {}):
    if n <= 0:
        return 0
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        memo[n] = abc(n-2, memo) + abc(n-1, memo)
    return memo[n]

# def abc(n):
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     dp = [0] * (n+1)
#     dp[1], dp[2] = 1, 2
#     for i in range(3, n+1):
#         dp[i] = dp[i-1]+dp[i-2]
#     return dp[n]

N = int(input())
print(abc(N))
