from collections import deque
import sys
sys.stdin = open("input.txt", "r")

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    q = deque()
    dist = [[-1]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                q.append((i, j))
                dist[i][j] = 0

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = dy+y, dx+x
            if ny<0 or nx<0 or ny>=N or nx>=M:continue
            if dist[ny][nx] != -1: continue
            dist[ny][nx] = dist[y][x] + 1
            q.append((ny, nx))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'L':
                cnt += dist[i][j]

    print(f'#{tc} {cnt}')