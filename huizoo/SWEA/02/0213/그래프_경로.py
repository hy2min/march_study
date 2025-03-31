def dfs(start):
    global OX
    if start == G-1:
        OX = 1
        return
    visited[start] = 1
    for i in range(V):
        if arr[start][i] and not visited[i]:
            dfs(i)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0]*V for _ in range(V)]
    for _ in range(E):
        y, x = map(int, input().split())
        arr[y-1][x-1] = 1
    S, G = map(int, input().split())
    OX = 0
    visited = [0] * V
    dfs(S-1)
    print(f'#{tc} {OX}')