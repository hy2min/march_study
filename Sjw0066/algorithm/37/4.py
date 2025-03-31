from collections import deque
arr=[list(map(int,input().split())) for _ in range(4)]
direct_y=[0,0,1,-1]
direct_x=[1,-1,0,0]
visited=[[0]*4 for _ in range(4)]
visited[0][0] = 1
q= deque()
q.append((0,0))
cnt=0

while q:
    y,x=q.popleft()
    cnt+=1
    for i in range(4):
        dy=direct_y[i]+y
        dx=direct_x[i]+x
        if dy>3 or dy<0 or dx>3 or dx<0:continue
        if arr[dy][dx] == 0 : continue
        if visited[dy][dx] == 1:continue
        visited[dy][dx] = 1
        q.append((dy,dx))

print(cnt)