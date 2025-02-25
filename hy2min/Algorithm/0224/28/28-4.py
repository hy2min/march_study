n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

visited = [0] * n
path = []
def dfs(level):
        for i in range(n):
            if visited[i] == 0 and arr[level][i] == 1:
                visited[i] = 1
                path.append(i)
                dfs(i)
                visited[i] = 0
path.append(0)
dfs(0)
print(*path)