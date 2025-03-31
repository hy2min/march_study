import sys
input = sys.stdin.readline

N = int(input())
arr = tuple(tuple(map(int, input().split())) for _ in range(N))
dp = [[None]*(1 << N) for _ in range(N)]
INF = 1e9
def dfs(now, chk):
    if chk == ((1 << N) - 1):
        return arr[now][0] if arr[now][0] != 0 else INF

    if dp[now][chk] is not None:
        return dp[now][chk]


    Min = INF
    for i in range(1, N):
        if (arr[now][i] != 0) and (chk & (1 << i)) == 0:
            Min = min(Min, dfs(i, chk | 1 << i) + arr[now][i])

    dp[now][chk] = Min

    return Min

print(dfs(0, 1))