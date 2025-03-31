# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    used = [0] * N
    Min = 21e8

    def dfs(y,level,sum):

        global Min
        if sum > Min:
            return
        if level == N:
            if sum < Min:
                Min = sum
                return

        for j in range(N):
            if used[j] == 0:
                used[j] = 1
                dfs(y+1,level+1,sum+arr[y][j])
                used[j] = 0

    dfs(0,0,0)
    print(f"#{tc} {Min}")