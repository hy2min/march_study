# 미생물 관찰
import sys
from collections import deque
input = sys.stdin.readline

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def size(y, x, micro):
    global micro_A, micro_B
    if micro == 'A':
        micro_A += 1
    else:
        micro_B += 1

    cnt = 1
    q = deque([(y, x)])
    sample[y][x] = '_'
    while q:
        yy, xx = q.popleft()
        for dy, dx in d:
            ny, nx = yy+dy, xx+dx
            if 0<=ny<N and 0<=nx<M:
                if sample[ny][nx] == micro:
                    cnt += 1
                    sample[ny][nx] = '_'
                    q.append((ny, nx))

    return cnt

N, M = map(int, input().split())
sample = [list(input()) for _ in range(N)]

Max = -1e9

micro_A, micro_B = 0, 0
for i in range(N):
    for j in range(M):
        if sample[i][j] != '_':
            Max = max(Max, size(i, j, sample[i][j]))


print(micro_A, micro_B)
print(Max)
