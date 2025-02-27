def dfs(y,x):
    global ret
    if arr[y][x]=='3':
        ret=1
        return
 
    for i in range(4):
        if ret==1:
            return
        dy=y+directy[i]
        dx=x+directx[i]
        if dy<0 or dx<0 or dy>=n or dx>=n: continue
        if arr[dy][dx]=='1':continue
        if used[dy][dx]==1: continue
        used[dy][dx]=1
        dfs(dy,dx)
 
T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    st=[]
    arr=[]
    for i in range(n):
        arr.append(input())
        for j in range(n):
            if arr[i][j]=='2':
                st=[i,j]
    directy=[-1,1,0,0]
    directx=[0,0,-1,1]
    used=[[0]*n for _ in range(n)]
    used[st[0]][st[1]]=1
    ret = 0
    dfs(st[0],st[1])
    print(f'#{test_case}',ret)