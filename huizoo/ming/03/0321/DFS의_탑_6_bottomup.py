# 돌다리 건너기
import sys
input = sys.stdin.readline


magic = input().rstrip()
bridge = tuple(input().rstrip() for _ in range(2))
N = len(magic)
L = len(bridge[0])
start = magic[0]
cnt = 0

dp = [[[0]*(L+1) for _ in range(2)] for _ in range(N)]

for i in range(2):
    for j in range(L-N+1):
        if bridge[i][j] == start:
            dp[0][i][j] = 1

for idx in range(1, N):
    for y in range(2):
        py = 1 - y

        # 반대 줄 누적합 구하기
        prefix = [0] * (L + 1)
        for i in range(L):
            prefix[i + 1] = prefix[i] + dp[idx - 1][py][i]

        for x in range(L):
            if bridge[y][x] != magic[idx]:
                continue
            dp[idx][y][x] = prefix[x]

for y in range(2):
    for x in range(L):
        cnt += dp[N-1][y][x]

print(cnt)