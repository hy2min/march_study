import sys
input = sys.stdin.readline

N = int(input())
arr = tuple(tuple(map(int, input().split())) for _ in range(N))
INF = 1e9
dp = [[INF]*(1 << N) for _ in range(N)]

for i in range(1, N):
    if arr[0][i]:
        dp[i][1 | (1 << i)] = arr[0][i]

for k in range(1 << N):
    for i in range(1, N):
        if dp[i][k] != INF:
            for j in range(1, N):
                if (arr[i][j] != 0 and
                    k & (1 << j) == 0 and
                    dp[j][k | (1 << j)] > dp[i][k] + arr[i][j]
                ):
                    dp[j][k | (1 << j)] = dp[i][k] + arr[i][j]


Min = INF
for i in range(1, N):
    if arr[i][0] != 0 and Min > dp[i][(1 << N) - 1] + arr[i][0]:
        Min = dp[i][(1 << N) - 1] + arr[i][0]

print(Min)