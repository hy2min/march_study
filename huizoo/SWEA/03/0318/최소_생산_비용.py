def abc(level, Sum):
    global Min
    if Sum >= Min:
        return
    if level == N:
        Min = min(Min, Sum)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            abc(level + 1, Sum + arr[level][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Min = 1e9
    visited = [0]*N
    abc(0, 0)
    print(f'#{tc} {Min}')