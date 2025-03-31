from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
K = int(input())

bus_info = [None] * (K + 1)
visited = [0] * (K + 1)
q = deque()

for _ in range(K):
    b, x1, y1, x2, y2 = map(int, input().split())

    x1, x2 = sorted((x1, x2))
    y1, y2 = sorted((y1, y2))

    bus_info[b] = (y1, x1, y2, x2)

sx, sy, dx, dy = map(int, input().split())

for b in range(1, K + 1):
    y1, x1, y2, x2 = bus_info[b]
    if y1 <= sy <= y2 and x1 <= sx <= x2:
        visited[b] = 1
        q.append(b)

while q:
    now = q.popleft()
    y1, x1, y2, x2 = bus_info[now]

    if y1 <= dy <= y2 and x1 <= dx <= x2:
        print(visited[now])
        break

    for b in range(1, K + 1):
        if not visited[b]:
            ny1, nx1, ny2, nx2 = bus_info[b]
            if y1 <= ny2 and ny1 <= y2 and x1 <= nx2 and nx1 <= x2:
                visited[b] = visited[now] + 1
                q.append(b)
