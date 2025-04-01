# bottom-up 방식
def fibo(n):
    global dp
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

dp = [0]*5
dp[0] = 0
dp[1] = 1
fibo(4)
print(*dp)