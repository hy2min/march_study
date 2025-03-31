from collections import deque

arr = [[0,1,0,0,1,0],
       [0,0,1,0,0,1],
       [0,0,0,1,0,0],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0],]

q=deque()
N = int(input())
visited = [0]*6
visited[N] = 1
q.append((N, visited))
while q:
    now, visited = q.popleft()
    print(now, end=' ')
    for i in range(6):
        if arr[now][i] ==1:
            visited[i] = 1
            q.append((i, visited))
