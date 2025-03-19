from collections import deque
arr = [list(map(int, input().split())) for _ in range(4)]
def bbq(y, x):
    cnt = 0
    d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    q = deque([(y, x)])
    arr[y][x] = 1
    while q:
        yy, xx = q.popleft()
        for dy, dx in d:
            ny, nx = yy+dy, xx+dx
            if ny<0 or nx<0 or ny>=4 or nx>=6: continue
            if arr[ny][nx] == 1:continue
            if arr[ny][nx] == 2:
                cnt += 1
            arr[ny][nx] = 1
            q.append((ny, nx))
    return cnt

print(bbq(0, 0))