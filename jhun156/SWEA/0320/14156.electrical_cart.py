# import sys
# sys.stdin = open("input.txt","r")

def dfs(level,Sum,x):

    global ans
    if level == N - 1:
        Sum += arr[x][0]
        ans = min(ans,Sum)
        return

    for i in range(1,N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(level+1, Sum+arr[x][i], i)
            visited[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 21e8
    visited = [0] * N
    dfs(0,0,0)
    print(f"#{tc} {ans}")