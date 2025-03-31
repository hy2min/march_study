def dfs(now):
    global Sum

    print(now, Sum)
    for i in range(6):
        if arr[now][i] != 0 and visited[i] == 0:
            visited[i] = 1
            Sum += arr[now][i]
            dfs(i)


arr = [
    [0,0,1,0,2,0],
    [5,0,3,0,0,0],
    [0,0,0,0,0,7],
    [2,0,0,0,8,0],
    [0,0,9,0,0,0],
    [4,0,0,7,0,0],
]

visited = [0] * 6
Sum = 0
k = int(input())
visited[k] = 1
dfs(k)