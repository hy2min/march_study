import sys
input = sys.stdin.readline


def dfs(idx, ny, nx):
    global cnt
    # 남아서 더 탐색해야 하는 수보다 탐색할 곳의 수가 부족할 때
    if N - idx > L - nx:
        return

    if idx == N:
        cnt += 1
        return

    y = (ny + 1) % 2
    for x in range(nx, L):
        if bridge[y][x] == magic[idx]:
            dfs(idx + 1, y, x+1)

magic = input().rstrip()
bridge = tuple(input().rstrip() for _ in range(2))
N = len(magic)
L = len(bridge[0])
start = magic[0]
cnt = 0
# 확인할 magic 인덱스, y, x
for i in range(2):
    for j in range(L-N+1):
        if bridge[i][j] == start:
            dfs(1, i, j+1)

print(cnt)