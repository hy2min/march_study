import sys
sys.stdin = open("input.txt", "r")


def dfs(x, Sum):
    global Min
    if Min < Sum:
        return

    if x == N:
        Min = Sum
        return

    for i in range(N):
        if visited[i] == 1: continue
        visited[i] = 1
        dfs(x + 1, Sum + arr[x][i])
        visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = []
    Min = 1e9
    visited = [0]*N
    dfs(0, 0)
    print(f'#{tc} {Min}')