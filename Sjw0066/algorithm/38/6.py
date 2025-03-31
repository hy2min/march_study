from collections import deque
N,M=map(int,input().split())
arr=[list(input()) for _ in range(N)]
Min=21e8
direct_y=[-1,1,0,0]
direct_x=[0,0,1,-1]
visited=[[0]*M for _ in range(N)]
visited[0][0]=1
q=deque()
q.append((0,0,0))
target='1'
answer=0
while q:
    y,x,cnt=q.popleft()
    if arr[y][x]==target:
        temp=int(target)+1
        target=str(temp)
        answer+=cnt
        visited=[[0]*M for _ in range(N)]
        q.clear()
        q.append((y,x,0))
        continue

    for i in range(4):
        dy=direct_y[i]+y
        dx=direct_x[i]+x
        if dy>N-1 or dy<0 or dx>M-1 or dx<0:continue
        if arr[dy][dx] == '#':continue
        if visited[dy][dx] == 1:continue
        visited[dy][dx] = 1
        q.append((dy,dx,cnt+1))

print(f'{answer}회')