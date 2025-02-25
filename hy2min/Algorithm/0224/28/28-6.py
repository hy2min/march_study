s = input()
arr = [list(map(int, input().split())) for _ in range(8)]

visited = [0]*8
path = []
def dfs(level):
    for i in range(8):
        if visited[i] == 0 and arr[level][i] == 1:
            visited[i] = 1
            path.append(s[i])
            dfs(i)
            visited[i] = 0

visited[0] = 1
path.append(s[0])
dfs(0)

print("".join(path))