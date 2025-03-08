arr = [
    [0,1,0,0,1,0],
    [0,0,1,0,0,1],
    [0,0,0,1,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]
K = int(input())
q = []
q.append(K)
visited = [0]*6
visited[K] = 1
while q:
    now = q.pop(0)
    print(now, end = ' ')
    for nxt in range(6):
        if arr[now][nxt] and not visited[nxt]:
            q.append(nxt)
            visited[nxt] = 1

