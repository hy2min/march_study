def dfs(now,path):
    flag = 1

    for i in range(6):
        if arr[now][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i, path+char[i])
            visited[i] = 0
            flag = 0
    if flag:
        print(path)
char = 'ABCDEF'
arr = [list(map(int, input().split())) for _ in range(6)]
visited = [0] * 6

visited[0] = 1
dfs(0,"A")
