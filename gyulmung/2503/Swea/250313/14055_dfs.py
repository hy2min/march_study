import sys
sys.stdin = open('input.txt','r')


def dfs(st, cnt):
    global line, Flag
    if st == G:
        line = cnt
        Flag = True
        return
    for i in range(N):
        if arr[st][i] == 1 and not visited[i]:
            visited[i] = True
            dfs(i, cnt + 1)
            visited[i] = False


T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]

    for _ in range(M):
        y, x = map(int, input().split())
        arr[y - 1][x - 1] = 1
        arr[x - 1][y - 1] = 1

    S, G = map(int, input().split())
    S -= 1
    G -= 1

    Flag = False
    line = 0
    visited = [False] * N

    visited[S] = True
    dfs(S, 0)

    print(f'#{test} {line if Flag else 0}')