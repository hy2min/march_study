T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    Min = 21e8
    def dfs(level, Sum):
        global Min
        if Sum >= B:
            Min = min(Sum, Min)
            return
        if level == N:
            return
        dfs(level+1, Sum+arr[level])
        dfs(level+1, Sum)

    dfs(0, 0)
    print(f'#{tc} {Min-B}')