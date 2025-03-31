from collections import deque

st_y,st_x=map(int,input().split())
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]

direct_y=[0,0,1,-1]
direct_x=[1,-1,0,0]

result=[[21e8]*N for _ in range(N)]
result[st_y][st_x]=arr[st_y][st_x]

q=deque()
q.append((st_y,st_x,result[st_y][st_x]))

while q:
    y,x,cost=q.popleft()

    for i in range(4):
        dy=direct_y[i]+y
        dx=direct_x[i]+x
        if dy>N-1 or dx>N-1 or dx<0 or dy<0:continue
        if arr[dy][dx] == -1 : continue
        if result[dy][dx] <= arr[dy][dx] + cost:continue
        result[dy][dx] = arr[dy][dx] + cost
        q.append((dy,dx,result[dy][dx]))

Max=-21e8
for i in result:
    for j in i:
        if j != 21e8:
            Max=max(Max,j)

print(Max)








