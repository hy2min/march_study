N=int(input())
map=[list(map(int,input().split())) for _ in range(N)]
flag=0
visited=[[0]*N for _ in range(N)]

def dfs(y,x):
    global flag

    if y==N-1 and x== N-1:
        flag=1
        return

    direct_y=[1,-1,0,0]
    direct_x=[0,0,-1,1]
    for i in range(4):
        dy=direct_y[i] + y
        dx=direct_x[i] + x
        if dy>N-1 or dy<0 or dx>N-1 or dx<0:continue
        if map[dy][dx] == 1:continue
        if visited[dy][dx] == 1:continue
        visited[dy][dx] = 1
        dfs(dy,dx)

dfs(0,0)
if flag:
    print('가능')
else:
    print('불가능')

