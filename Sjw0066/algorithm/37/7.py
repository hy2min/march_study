from collections import deque
N,M=map(int,input().split())
arr=[list(input().split()) for _ in range(N)]
direct_y=[0,0,1,-1]
direct_x=[1,-1,0,0]
Min=21e8

def bfs(now,ed,cnt):
    global Min
    visited=[[0]*M for _ in range(N)]
    visited[now[0]][now[1]] = 1
    q=deque()
    q.append((now[0],now[1],cnt))

    while q:
        y,x,cnt=q.popleft()
        for i in range(4):
            dy=y+direct_y[i]
            dx=x+direct_x[i]
            if dy>N-1 or dy<0 or dx>M-1 or dx<0:continue
            if arr[dy][dx] == 'x' : continue
            if visited[dy][dx] == 1: continue
            if dy == ed[0] and dx == ed[1]:
                return cnt + 1
            visited[dy][dx] = 1
            q.append((dy,dx,cnt+1))

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'S' : country=[i,j]
        if arr[i][j] == 'D' : city=[i,j]
        if arr[i][j] == 'C' : cheese=[i,j]

answer=bfs(country,cheese,0) + bfs(cheese,city,0)
print(answer)

