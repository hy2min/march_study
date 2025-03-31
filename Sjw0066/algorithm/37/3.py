from collections import deque

arr=[list(map(int,input().split())) for _ in range(4)]
direct_y=[1,1,1,0,0,-1,-1,-1]
direct_x=[1,0,-1,1,-1,1,0,-1]
q=deque()
for i in range(4):
    for j in range(5):
        if arr[i][j] == 1:
            q.append((i,j))

while q:
    y,x=q.popleft()
    for i in range(8):
        dy=y+direct_y[i]
        dx=x+direct_x[i]
        if dy>3 or dy<0 or dx>4 or dx<0:continue
        if arr[dy][dx] != 0 : continue
        arr[dy][dx] = arr[y][x] + 1
        q.append((dy,dx))

Max=-21e8
for i in arr:
    for j in i :
        if Max<j:
            Max=j

print(Max-1)
