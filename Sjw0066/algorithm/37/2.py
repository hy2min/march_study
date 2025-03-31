from collections import deque
N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
st_y,st_x=map(int,input().split())
direct_y=[0,0,1,-1]
direct_x=[1,-1,0,0]

q=deque()
q.append((st_y,st_x))

while q:
    y,x=q.popleft()

    for i in range(4):
        dy=direct_y[i] + y
        dx=direct_x[i] + x
        if dy>N-1 or dy<0 or dx<0 or dx>N-1:continue
        if arr[dy][dx] != 0: continue
        arr[dy][dx] = arr[y][x] + 1
        q.append((dy,dx))


Max=-21e8
for i in arr:
    for j in i:
        if j>Max:
            Max=j

print(Max)