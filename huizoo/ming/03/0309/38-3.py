from collections import deque
arr = [list(map(int, input())) for _ in range(7)]
d = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def bfs(y ,x, i, level):
    q = deque([(y, x)])
    visited = [[0]*7 for _ in range(7)]
    visited[y][x] = 1
    while q:
        yy, xx = q.popleft()
        for dy, dx in d:
            ny, nx = yy+dy, xx+dx
            if ny<0 or nx<0 or ny>=7 or nx>=7: continue
            if visited[ny][nx]: continue
            if arr[ny][nx] == i:
                return 1
            visited[ny][nx] = visited[yy][xx] + 1
            if visited[ny][nx] != level:
                q.append((ny, nx))
    return 0

def search():
    for i in range(7):
        for j in range(7):
            if arr[i][j]:
                if arr[i][j] == 1:
                    level = 3
                else:
                    level = 4
                if bfs(i, j, arr[i][j], level):
                    return 'fail'

    return 'pass'


print(search())
