import sys
sys.stdin = open('input.txt','r')

from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
a, b = map(int, input().split())

q = deque()
q.append((a, b, 1))
diry = [0, 0, 1, -1]
dirx = [1, -1, 0, 0]
ret = 0
while q:
    y, x, cnt = q.popleft()
    ret = cnt
    for i in range(4):
        dy = diry[i] + y
        dx = dirx[i] + x
        if dy < 0 or dx < 0 or dy >= N or dx >= N: continue
        if arr[dy][dx] == 1: continue # 정수 1 때문에 오류 발생시 값을 받을 때 str 로 변경
        arr[dy][dx] = 1
        q.append((dy, dx, cnt + 1))

print(ret-1)