from collections import deque
N=int(input())
arr=[list(input()) for _ in range(N)]
first=list(map(int,input().split()))

direct_y=[0,0,1,-1]
direct_x=[1,-1,0,0]

def bfs_to_fire_ex(st,ed):
    q=deque()
    cnt = 1
    q.append((st[0],st[1],cnt))
    visited=[[0]*N for _ in range(N)]
    visited[st[0]][st[1]] = 1
    while q:
        y,x,level=q.popleft()
        for i in range(4):
            dy=direct_y[i] + y
            dx=direct_x[i] + x
            if dy>N-1 or dy<0 or dx>N-1 or dx<0:continue
            if visited[dy][dx] == 1 : continue
            if arr[dy][dx] == '#' or arr[dy][dx] == '$':continue
            if dy==ed[0] and dx==ed[1]:
                return level
            visited[dy][dx] = 1
            q.append((dy,dx,level+1))

def bfs_to_fire(st):
    q = deque()
    cnt = 1
    q.append((st[0], st[1],cnt))
    visited = [[0] * N for _ in range(N)]
    visited[st[0]][st[1]] = 1
    while q:
        y, x ,level= q.popleft()
        for i in range(4):
            dy = direct_y[i] + y
            dx = direct_x[i] + x
            if dy > N - 1 or dy < 0 or dx > N - 1 or dx < 0: continue
            if visited[dy][dx] == 1: continue
            if arr[dy][dx] == '#' or arr[dy][dx] == 'A': continue
            if arr[dy][dx] == "$":
                return level
            visited[dy][dx] = 1
            q.append((dy, dx,level+1))
Min=21e8
answer=0
for i in range(N):
    for j in range(N):
        if arr[i][j] == "A":
            answer=bfs_to_fire_ex(first,(i,j)) + bfs_to_fire((i,j))
            if Min>answer:
                Min=answer
print(Min)