# 돌다리 건너기
import sys
input = sys.stdin.readline


def dfs(idx, y, x):
    # 남아서 더 탐색해야 하는 수보다 탐색할 곳의 수가 부족할 때
    if N - idx > L - x:
        return 0
    if idx == N:
        return 1
    if dp[idx][y][x] != -1:
        return dp[idx][y][x]

    ret = 0
    ny = (y + 1) % 2
    for nx in range(x, L):
        if bridge[ny][nx] == magic[idx]:
            ret += dfs(idx + 1, ny, nx+1)

    dp[idx][y][x] = ret
    return ret

magic = input().rstrip()
bridge = tuple(input().rstrip() for _ in range(2))
N = len(magic)
L = len(bridge[0])
start = magic[0]
cnt = 0

dp = [[[-1]*(L+1) for _ in range(2)] for _ in range(N+1)]

# 확인할 magic 인덱스, y, x
for i in range(2):
    for j in range(L-N+1):
        if bridge[i][j] == start:
            cnt += dfs(1, i, j+1)

print(cnt)