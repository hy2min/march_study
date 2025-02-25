n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [0]*n
def dfs(level):
    for i in range(n):
        if visited[i] == 0 and arr[level][i] == 1:
            visited[i] = 1
            print(i, end=" ")
            dfs(i)
            visited[i] = 0

visited[0] = 1
print(0, end=' ')
dfs(0)