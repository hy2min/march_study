# 럭셔리 여행
import sys
input = sys.stdin.readline

def dfs(a, cost = 0):
    global Max, Min
    if a == b:
        Max = max(Max, cost)
        Min = min(Min, cost)
        return

    for i in range(N):
        if arr[a][i] and not visited[i]:
            visited[i] = 1
            dfs(i, cost+arr[a][i])
            visited[i] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
Max = 0
Min = 1e9
a, b = map(int, input().split())

visited = [0]*N
visited[a] = 1
dfs(a)

print(Min)
print(Max)
