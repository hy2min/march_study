n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
path = []
visited = [0] * n
def dfs(level):

    if len(path) == 3:
        print(*path)
        return

    for i in range(n):
        if visited[i] == 0 and arr[level][i] == 1:
            visited[i] = 1
            path.append(i)
            dfs(i)
            path.pop()
            visited[i] = 0

visited[0]= 1
path.append(0)
dfs(0)
