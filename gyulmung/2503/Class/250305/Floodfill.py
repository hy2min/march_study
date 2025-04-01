import sys
sys.stdin = open('input.txt','r')

from collections import deque

N = int(input())
arr = [[0]*N for _ in range(N)]
a, b = map(int, input().split())
route = deque()
route.append((a, b, 1))

direct_y = [0, 0, 1, -1]
direct_x = [1, -1, 0, 0]

while 1:
    y, x, cnt = route.popleft()
    arr[y][x] = 1
    if y == 0 and x == 0:
        print(cnt)
        break

    for i in range(4):
        dy = direct_y[i] + y
        dx = direct_x[i] + x
        if dy < 0 or dx < 0 or dy >= N or dx >=N: continue
        if arr[dy][dx] == 1: continue
        route.append((dy, dx, cnt+1))
        arr[dy][dx] = 1
