arr = [
    [0,0,1,0,2,0],
    [5,0,3,0,0,0],
    [0,0,0,0,0,7],
    [2,0,0,0,8,0],
    [0,0,9,0,0,0],
    [4,0,0,7,0,0],
]
K = int(input())
visited = [0]*6

def dfs(x):
    global Sum
    print(x, Sum)
    for i in range(6):
        if arr[x][i] and not visited[i]:
            visited[i] = 1
            Sum += arr[x][i]
            dfs(i)

visited[K] = 1
Sum = 0
dfs(K)