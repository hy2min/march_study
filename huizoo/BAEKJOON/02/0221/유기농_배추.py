import sys
from collections import deque

def abc(y, x):
    q = deque()
    q.append((y, x))
    arr2[y][x] = 1
    while q:
        yy, xx = q.popleft()
        for i in range(4):
            ny, nx = yy + dy[i], xx + dx[i]
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] and not arr2[ny][nx]:
                arr2[ny][nx] = 1
                q.append((ny, nx))

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0]*M for _ in range(N)]
    arr2 = [[0]*M for _ in range(N)]
    for _ in range(K):
        b, a = map(int, sys.stdin.readline().split())
        arr[a][b] = 1

    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not arr2[i][j]:
                cnt += 1
                abc(i, j)
    print(cnt)