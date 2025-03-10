from collections import deque
d_y = [-1,1,0,0]
d_x = [0,0,-1,1]

def bfs(si,sj,ei,ej):
    q = deque()
    q.append((si, sj,0))
    visited = [[0] * 4 for _ in range(4)]
    visited[si][sj] = 1

    while q:
        y, x, level = q.popleft()

        if (y, x) == (ei, ej):
            return level

        for i in range(4):
            dy = y + d_y[i]
            dx = x + d_x[i]
            if dy < 0 or dx < 0 or dy >= 4 or dx >= 4:
                continue
            if arr[dy][dx] == 0 and visited[dy][dx] == 0:
                visited[dy][dx] = 1
                q.append((dy, dx, level+1))

arr = [
    [0,0,0,0],
    [1,1,0,1],
    [0,0,0,0],
    [1,0,1,0]
]
mn = 21e8
si, sj = map(int, input().split())
ei, ej = map(int, input().split())

mn = bfs(si,sj,ei,ej)
print(str(mn) + '회')