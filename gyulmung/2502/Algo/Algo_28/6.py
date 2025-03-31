string = input()
arr = [list(map(int, input().split())) for _ in range(len(string))]
path = []

def dfs(now):
    global path
    path.append(string[now])
    for i in range(len(string)):
        if arr[now][i] == 1:
            dfs(i)

dfs(0)
print(*path, sep='')