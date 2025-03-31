# 플러드필
import sys
from collections import deque
input = sys.stdin.readline

y, x = map(int, input().split())

arr = [[0]*5 for _ in range(5)]

q = deque([(y, x)])
arr[y][x] = 1

while q:
    yy, xx = q.popleft()
    for dy, dx in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        ny, nx = dy+yy, dx+xx
        if ny<0 or nx<0 or ny>=5 or nx>=5: continue
        if arr[ny][nx] == 0:
            arr[ny][nx] = arr[yy][xx] + 1
            q.append((ny, nx))

for row in arr:
    print(*row)
