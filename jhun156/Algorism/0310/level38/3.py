# import sys
# sys.stdin = open("input.txt","r")
from collections import deque

# 새우는 1, 오징어는 2, 새우는 3칸씩, 오징어는 4칸씩
arr = [list(map(int,input())) for _ in range(7)]
flag = 0
dY = [0,0,1,-1]
dX = [1,-1,0,0]

def shrimp(y,x):

    global flag
    q = deque()
    q.append((y,x))

    while q:
        ny,nx = q.popleft()
        for i in range(4):
            for j in range(1,3):
                dy = ny + dY[i] * j
                dx = nx + dX[i] * j
                if dy < 0 or dy > 6 or dx < 0 or dx > 6:
                    continue
                if arr[dy][dx] == 1:
                    flag = 1
                    return


def squid(y, x):

    global flag
    q = deque()
    q.append((y, x))

    while q:
        ny, nx = q.popleft()
        for i in range(4):
            for j in range(1, 4):
                dy = ny + dY[i] * j
                dx = nx + dX[i] * j
                if dy < 0 or dy > 6 or dx < 0 or dx > 6:
                    continue
                if arr[dy][dx] == 2:
                    flag = 1
                    return

for i in range(7):
    for j in range(7):
        if arr[i][j] == 1:
            shrimp(i,j)
        elif arr[i][j] == 2:
            squid(i,j)
        if flag:
            break
    if flag:
        break

if flag:
    print("fail")
else:
    print("pass")