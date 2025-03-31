from collections import deque
def bfs(start):
    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()
        print(now, end=" ")

        for i in range(6):
            if arr[now][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = 1
arr = [
    [0,1,0,0,1,0],
    [0,0,1,0,0,1],
    [0,0,0,1,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]

visited = [0] * 6

k = int(input())
bfs(k)