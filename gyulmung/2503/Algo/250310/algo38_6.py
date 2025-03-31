# 시간초과
# 너무 많은 배열을 읽음
# visited를 이용해서 이미 지나온 길은 없앨것
# visited((y,x))를 만들어 확인할 것

import sys
sys.stdin = open('input.txt','r')

from collections import deque

def Find_1(y, x):
    global ret
    q = deque()
    q.append((y, x, 0))
    while 1:
        y, x, cnt = q.popleft()
        if arr[y][x] == '1':
            ret += cnt
            return cnt, x, y
        for i in range(5):
            dy = directY[i] + y
            dx = directX[i] + x
            if dy < 0 or dx < 0 or dy >= Y or dx >= X: continue
            if arr[dy][dx] == '#': continue
            q.append((dy, dx, cnt+1))

def Find_2(y, x):
    global ret
    q = deque()
    q.append((y, x, 0))
    while 1:
        y, x, cnt = q.popleft()
        if arr[y][x] == '2':
            ret += cnt
            return cnt, x, y
        for i in range(5):
            dy = directY[i] + y
            dx = directX[i] + x
            if dy < 0 or dx < 0 or dy >= Y or dx >= X: continue
            if arr[dy][dx] == '#': continue
            q.append((dy, dx, cnt+1))

def Find_3(y, x):
    global ret
    q = deque()
    q.append((y, x, 0))
    while 1:
        y, x, cnt = q.popleft()
        if arr[y][x] == '3':
            ret += cnt
            return cnt, x, y
        for i in range(5):
            dy = directY[i] + y
            dx = directX[i] + x
            if dy < 0 or dx < 0 or dy >= Y or dx >= X: continue
            if arr[dy][dx] == '#': continue
            q.append((dy, dx, cnt+1))

def Find_4(y, x):
    global ret
    q = deque()
    q.append((y, x, 0))
    while 1:
        y, x, cnt = q.popleft()
        if arr[y][x] == '4':
            ret += cnt
            return cnt, x, y
        for i in range(5):
            dy = directY[i] + y
            dx = directX[i] + x
            if dy < 0 or dx < 0 or dy >= Y or dx >= X: continue
            if arr[dy][dx] == '#': continue
            q.append((dy, dx, cnt+1))


Y, X = map(int,input().split())
arr = [list(input()) for _ in range(Y)]
directY = [0, 0, 0, 1, -1]
directX = [0, 1, -1, 0, 0]
ret = 0
cnt1, next_X1, next_Y1 = Find_1(0, 0)
cnt2, next_X2, next_Y2 = Find_2(next_Y1, next_X1)
cnt3, next_X3, next_Y3 = Find_3(next_Y2, next_X2)
cnt4, next_X4, next_Y4 = Find_4(next_Y3, next_X3)
print(f'{ret}회')