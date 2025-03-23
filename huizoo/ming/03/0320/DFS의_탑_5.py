# 해밀턴 회로
import sys
input = sys.stdin.readline

def dfs(x, level, cost):
    global Min
    if Min <= cost:
        return

    if level == N-1 and arr[x][0]:
        Min = min(Min, cost+arr[x][0])
        return

    for i in range(N):
        if arr[x][i] and not visited[i]:
            visited[i] = 1
            dfs(i, level+1, cost+arr[x][i])
            visited[i] = 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
Min = 1e9
visited = [0]*N
visited[0] = 1
if N == 1:
    print(0)
else:
    dfs(0, 0, 0)
    print(Min)