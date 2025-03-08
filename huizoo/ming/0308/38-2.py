from collections import deque

def bfs(y, x, num):
    q = deque([(y, x)])
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited[y][x] = 1
    cnt = 0
    while q:
        yy, xx = q.popleft()
        cnt += 1
        for dy, dx in d:
            ny, nx = yy + dy, xx + dx
            if ny < 0 or nx < 0 or ny >= 4 or nx >= 9: continue
            if arr[ny][nx] != num: continue
            if visited[ny][nx]: continue
            visited[ny][nx] = 1
            q.append((ny, nx))

    return cnt, num

arr = [list(map(int, input().split())) for _ in range(4)]
Max = 0
Max_cnt = 0
visited = [[0] * 9 for _ in range(4)]
for i in range(4):
    for j in range(9):
        if not visited[i][j]:
            cnt, num = bfs(i, j, arr[i][j])
            if Max_cnt < cnt:
                Max_cnt = cnt
                Max = num

print(Max*Max_cnt)