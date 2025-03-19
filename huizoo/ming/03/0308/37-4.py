arr = [list(map(int, input().split())) for _ in range(4)]
visited = [[0]*4 for _ in range(4)]
def bfs(y, x):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [(y, x)]
    visited[y][x] = 1
    cnt = 0
    while queue:
        yy, xx = queue.pop(0)
        cnt += 1
        for dy, dx in d:
            ny, nx = yy+dy, xx+dx
            if ny<0 or nx<0 or ny>=4 or nx>=4: continue
            if visited[ny][nx]: continue
            if not arr[ny][nx]: continue
            queue.append((ny, nx))
            visited[ny][nx] = 1
    return cnt
print(bfs(0, 0))