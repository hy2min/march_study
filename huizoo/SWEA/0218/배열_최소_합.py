def abc(level, Sum):
    global Min
    if Sum > Min:
        return
    if level == N:
        Min = min(Min, Sum)
        return
    for i in range(N):
        if not used[i]:
            used[i] = 1
            abc(level+1, Sum+arr[level][i])
            used[i] = 0

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Min = 21e8
    used = [0]*N
    for i in range(N):
        used[i] = 1
        abc(1, arr[0][i])
        used[i] = 0

    print(f'#{tc} {Min}')