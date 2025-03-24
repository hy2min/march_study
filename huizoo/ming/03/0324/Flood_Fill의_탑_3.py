# 좀비 바이러스
import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
d = ((1, 0), (-1, 0), (0, 1), (0, -1))
cnt = 0
zombie = [input() for _ in range(N)]
for row in zombie:
    cnt += row.count('1')
vx, vy = map(int, input().split())
q = deque()
q.append((vy-1, vx-1))
cured = [[0]*M for _ in range(N)]
cured[vy-1][vx-1] = 3
cnt -= 1
while q:
    yy, xx = q.popleft()
    for dy, dx in d:
        ny, nx = yy+dy, xx+dx
        if ny<0 or nx<0 or ny>=N or nx>=M: continue
        if zombie[ny][nx] == '1' and cured[ny][nx] == 0:
            cured[ny][nx] = cured[yy][xx] + 1
            cnt -= 1
            q.append((ny, nx))

print(cured[yy][xx])
print(cnt)