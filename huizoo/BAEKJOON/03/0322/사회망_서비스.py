import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

dp = [[-1]*2 for _ in range(N+1)]

def dfs(now, p):
    dp[now][0] = 0
    dp[now][1] = 1

    for c in arr[now]:
        if c != p:
            dfs(c, now)

            dp[now][0] += dp[c][1]
            dp[now][1] += min(dp[c])

dfs(1, 0)
print(min(dp[1]))