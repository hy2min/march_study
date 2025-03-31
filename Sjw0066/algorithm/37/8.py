from collections import deque
N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
direct_y=[0,0,1,-1]
direct_x=[1,-1,0,0]
cnt=0

def bfs(a,b):
    arr[a][b] = 0
    q=deque()
    q.append((a,b))
    while q:
        y,x = q.popleft()
        for i in range(4):
            dy=direct_y[i] + y
            dx=direct_x[i] + x
            if dy>N-1 or dy<0 or dx>M-1 or dx<0:continue
            if arr[dy][dx] == 0: continue
            arr[dy][dx] = 0
            q.append((dy,dx))

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            bfs(i,j)
            cnt+=1

print(cnt)

