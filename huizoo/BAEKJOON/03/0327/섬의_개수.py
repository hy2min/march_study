import sys
from collections import deque
input = sys.stdin.readline

def land(y, x):
    q = deque([(y, x)])
    arr[y][x] = 2
    while q:
        yy, xx = q.popleft()
        for dy, dx in d:
            ny, nx = yy+dy, xx+dx
            if 0<=ny<N and 0<=nx<M:
                if arr[ny][nx] == 1:
                    arr[ny][nx] = 2
                    q.append((ny, nx))


d = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


while 1:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        exit()
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                land(i, j)

    print(cnt)
