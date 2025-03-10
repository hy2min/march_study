from collections import deque

d_y = [0,0,-1,1]
d_x = [-1,1,0,0]


arr = [list(map(int, input().split())) for _ in range(4)]
visited = [[0] * 6 for _ in range(4)]
si, sj = 0, 0

q = deque()
q.append((si,sj))
visited[si][sj] = 1

cnt = 0

while q:
    y, x = q.popleft()
    for i in range(4):
        dy = y + d_y[i]
        dx = x + d_x[i]
        if dy < 0 or dx < 0 or dy >= 4 or dx >= 6:
            continue
        if arr[dy][dx] == 0 and visited[dy][dx] == 0:
            visited[dy][dx] = 1
            q.append((dy, dx))

        if arr[dy][dx] == 2 and visited[dy][dx] == 0:
            visited[dy][dx] = 1
            cnt += 1
            q.append((dy, dx))
print(cnt)