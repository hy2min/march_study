
def dfs(level, Sum):
    global Min
    if Sum >= Min:
        return

    if level == N:
        if Sum < Min:
            Min = Sum
        return Min

    for i in range(N):
        if not used[i]:
            used[i] = 1
            dfs(level+1, Sum + arr[level][i])
            used[i] = 0

T = int(input())
for idx in range(T):
    N = int(input())
    used = [0] * N
    Min = 21e8
    arr = [list(map(int,input().split())) for _ in range(N)]


    dfs(0,0)
    print(f'#{idx+1} {Min}')