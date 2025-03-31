# 값 입력 받기
N, M = map(int, input().split())


def dfs(now, ind):
    arr = ['_', '_', '_', '_', '_']
    if now == 0 or ind > 4:
        print(*arr, sep='')
        return
    arr[ind] = now
    print(*arr, sep='')
    dfs(now-1, ind+1)

dfs(N, M)