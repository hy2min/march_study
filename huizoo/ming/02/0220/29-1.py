n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
def dfs(x):
    for i in range(n):
        if i not in path and arr[x][i]:
            path.append(i)
            dfs(i)

path = [0]
dfs(0)
print(*path)



