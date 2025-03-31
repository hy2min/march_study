# import sys
# sys.stdin = open("input.txt","r")

def dfs(level,mul):

    global ans
    if mul <= ans:
        return

    if level == N:
        ans = max(ans,mul)
        return

    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            dfs(level+1,mul*arr[level][i])
            used[i] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    used = [0] * N
    for i in range(N):
        for j in range(N):
            arr[i][j] /= 100

    dfs(0,1)
    ans *= 100
    print(f"#{tc} {ans:.6f}")