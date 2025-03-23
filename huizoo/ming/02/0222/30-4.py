K = int(input())
arr = [
    [0,0,0,0,1,0],
    [1,0,1,0,0,1],
    [1,0,0,1,0,0],
    [1,1,0,0,0,0],
    [0,1,0,1,0,1],
    [0,0,1,1,0,0],
]
visited = [0]*6
q = []
q.append(K)
visited[K] = 1
while q:
    now = q.pop(0)
    print(now)
    for i in range(6):
        if arr[now][i] and not visited[i]:
            visited[i] = 1
            q.append(i)