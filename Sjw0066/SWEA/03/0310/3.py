from collections import deque
T=int(input())

def bfs(y,x):
    q=deque()
    visited[y][x] = 1
    q.append((y,x))

    while q:
        nowy,nowx=q.popleft()
        dirs=types[arr[nowy][nowx]]
        for i in range(4):
            if dirs[i] == 0: continue
            dy=direct_y[i]+nowy
            dx=direct_x[i]+nowx
            if dy>N-1 or dy<0 or dx>M-1 or dx<0:continue
            if visited[dy][dx] >= 1: continue
            if arr[dy][dx] == 0 :continue
            next_dirs=types[arr[dy][dx]]
            if i%2==0 and next_dirs[i+1]==0:continue
            if i%2==1 and next_dirs[i-1]==0:continue
            visited[dy][dx] = visited[nowy][nowx]+1
            q.append((dy,dx))


for tc in range(1,T+1):
    N,M,R,C,L = map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    visited=[[0]*M for _ in range(N)]
    types={
        1:[1,1,1,1],
        2:[1,1,0,0],
        3:[0,0,1,1],
        4:[1,0,0,1],
        5:[0,1,0,1],
        6:[0,1,1,0],
        7:[1,0,1,0],
    }
    direct_y=[-1,1,0,0]
    direct_x=[0,0,-1,1]
    cnt=0
    bfs(R,C)
    for i in range(N):
        for j in range(M) :
            if 0<visited[i][j] <=L:
                cnt+=1

    print(f'#{tc} {cnt}')