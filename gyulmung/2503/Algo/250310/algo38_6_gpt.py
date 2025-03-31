# 시간초과

import sys
sys.stdin = open('input.txt','r')

from collections import deque
import copy

def Find(y, x, target):
    global ret
    q = deque()
    q.append((y, x, 0))
    arr = lst
    while q:
        y, x, cnt = q.popleft()
        if arr[y][x] == target:
            ret += cnt
            return cnt, x, y
        arr[y][x] = '#'
        for i in range(5):
            dy = directY[i] + y
            dx = directX[i] + x
            if 0 <= dy < Y and 0 <= dx < X and arr[dy][dx] != '#':
                q.append((dy, dx, cnt + 1))

Y, X = map(int, input().split())
arr = [list(input()) for _ in range(Y)]
directY = [0, 0, 0, 1, -1]
directX = [0, 1, -1, 0, 0]
lst = copy.deepcopy(arr)
ret = 0

next_Y, next_X = 0, 0
for target in ['1', '2', '3', '4']:
    cnt, next_X, next_Y = Find(next_Y, next_X, target)

print(f'{ret}회')
