# 꼴뚜기 게임
import sys
from collections import deque
input = sys.stdin.readline

def jump1(yy, xx):
    return yy, xx-1

def jump2(yy, xx):
    return yy, xx+1

def jump3(yy, xx):
    if yy == 0:
        return yy+1, xx+K
    else:
        return yy-1, xx+K

def bfs():
    q = deque([(0, 0)])
    visited = [[0]*N for _ in range(2)]
    visited[0][0] = 1

    while q:
        y, x = q.popleft()
        for ny, nx in (jump1(y, x), jump2(y, x), jump3(y, x)):
            if nx >= N:
                return 1
            if 0 <= nx < N and visited[ny][nx] == 0 and bridge[ny][nx] == '1':
                visited[ny][nx] = 1
                q.append((ny, nx))

    return 0

N, K = map(int, input().split())
bridge = [input() for _ in range(2)]
print(bfs())