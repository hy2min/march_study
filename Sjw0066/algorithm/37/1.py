from collections import deque
N=int(input())

y1,x1,y2,x2=map(int,input().split())

arr=[[0]*N for _ in range(N)]

direct_y=[0,0,1,-1]
direct_x=[1,-1,0,0]
arr[y1][x1]=1
arr[y2][x2]=1

q=deque()
q.append((y1,x1))
q.append((y2,x2))
while q:
    y,x=q.popleft()

    for i in range(4):
        dy=direct_y[i] + y
        dx=direct_x[i] + x
        if dy>N-1 or dy<0 or dx<0 or dx>N-1:continue
        if arr[dy][dx] != 0: continue
        arr[dy][dx] = arr[y][x] + 1
        q.append((dy,dx))

for i in arr:
    print(*i,sep="")

