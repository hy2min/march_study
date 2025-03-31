from collections import deque

arr = [[0,0,0,0,1,0],
       [1,0,1,0,0,1],
       [1,0,0,1,0,0],
       [1,1,0,0,0,0],
       [0,1,0,1,0,1],
       [0,0,1,1,0,0],]

N = int(input())

q = deque()
visited = [0]*6
visited[N] = 1
q.append((N, visited))

while q:
    now, visited = q.popleft()
    print(now)

    for i in range(6):
        if arr[now][i] == 1 and visited[i] == 0:
            visited[i] = 1
            q. append((i, visited))