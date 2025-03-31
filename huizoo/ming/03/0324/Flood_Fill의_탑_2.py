# Bloom
import sys
from collections import deque
input = sys.stdin.readline

h, w = map(int, input().split())
y1, x1 = map(int, input().split())
y2, x2 = map(int, input().split())
arr = [[0]*w for _ in range(h)]
q = deque()
q.append((y1, x1))
q.append((y2, x2))
arr[y1][x1] = 1
arr[y2][x2] = 1
while q:
    yy, xx = q.popleft()
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ny, nx = yy+dy, xx+dx
        if ny<0 or nx<0 or ny>=h or nx>=w: continue
        if arr[ny][nx] == 0:
            arr[ny][nx] = arr[yy][xx] + 1
            q.append((ny, nx))

print(arr[yy][xx])