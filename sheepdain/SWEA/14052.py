from collections import deque
 
T = int(input())
for test_case in range(1, T + 1):
    n=int(input())
    arr=[list(map(int,input())) for _ in range(n)]
    y,x=0,0
    for i in range(n):
        if y!=0: break
        for j in range(n):
            if arr[i][j]==2:
                y,x=i,j
                break
    directy=[-1,0,0,1]
    directx=[0,-1,1,0]
    q=deque()
    q.append((y,x,0))
    used=[[0]*n for _ in range(n)]
    used[y][x]=1
    ret=0
    while q:
        y,x,cnt=q.popleft()
        if arr[y][x]==3:
            ret=cnt-1
            break
 
        for i in range(4):
            dy=y+directy[i]
            dx=x+directx[i]
            if dy<0 or dx<0 or dy>=n or dx>=n: continue
            if used[dy][dx]==1 or arr[dy][dx]==1:continue
            used[dy][dx]=1
            q.append((dy,dx,cnt+1))
 
    print(f'#{test_case}', ret)