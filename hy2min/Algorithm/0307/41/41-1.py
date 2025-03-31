def fibo(n, dp):
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = fibo(n-2, dp) + fibo(n-1, dp)
    return dp[n]

n = int(input())
n -= 1

dp = [-1] * (n+1)
ans = fibo(n, dp)
print(ans)