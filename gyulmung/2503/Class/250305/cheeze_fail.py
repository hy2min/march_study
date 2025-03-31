#치즈먹고 여자친구
from collections import deque

arr=[[0,0,0,0,0,0],
     [1,1,0,0,1,0],
     [1,0,0,0,1,0],
     [2,0,0,0,0,3]]

directy=[0,0,-1,1]
directx=[1,-1,0,0]
answer=0
arr[3][5] = 3
arr[3][0] = 2
ca, cb = 0, 0
ret1 = 0
ret2 = 0

route1 = deque()
route2 = deque()
route1.append((0,0,0))


while 1:
    y, x, cnt = route1.popleft()
    arr[y][x] = 1
    for i in range(4):
        dy = directy[i] + y
        dx = directx[i] + x
        if 0 <= dy < 4 and 0 <= dx < 5:
            if arr[dy][dx] == 1: continue
            if arr[dy][dx] == 2:
                ca = dy
                cb = dx
                ret1 += cnt
                break
            route1.append((dy, dx, cnt+1))
            arr[dy][dx] = 1
    if ret1: break

arr=[[0,0,0,0,0,0],
     [1,0,0,0,1,0],
     [1,0,0,0,1,0],
     [2,0,0,0,0,3]]

route2.append((ca,cb,0))
while 1:
    y, x, cnt = route2.popleft()
    arr[y][x] = 1
    for i in range(4):
        dy = directy[i] + y
        dx = directx[i] + x
        if 0 <= dy < 4 and 0 <= dx < 5:
            if arr[dy][dx] == 1: continue
            if arr[dy][dx] == 3:
                ca = dy
                cb = dx
                ret2 += cnt
                break
            route2.append((dy, dx, cnt+1))
            arr[dy][dx] = 1
    if ret2: break

print(ret1 + ret2)