arr = [[0, 0, 1, 0, 2, 0],
       [5, 0, 3, 0, 0, 0],
       [0, 0, 0, 0, 0, 7],
       [2, 0, 0, 0, 8, 0],
       [0, 0, 9, 0, 0, 0],
       [4, 0, 0, 7, 0, 0],]

def dfs(now):
    global Sum
    print(now, Sum)

    for i in range(6):
        if arr[now][i] != 0 and visited[i] == 0:
            visited[i] = 1
            Sum += arr[now][i]
            dfs(i)
Sum = 0
N = int(input())
visited = [0]*6
visited[N] = 1
dfs(N)