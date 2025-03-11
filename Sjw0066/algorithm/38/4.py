from collections import deque
arr=[list(input()) for _ in range(8)]
Min=21e8
st_y=0
st_x=0
visited=[[0]*9 for _ in range(8)]
direct_y=[-1,1,0,0]
direct_x=[0,0,1,-1]
max_y=0
Min=21e8
for i in range(8):
    for j in range(9):
        if arr[i][j] == '#':
            st_y = i
            st_x = j
            break
    break

q=deque()
visited[st_y][st_x] = 1
q.append((st_y,st_x))
q2=deque()

while q:
    y,x=q.popleft()
    q2.append((y, x, 0))

    for i in range(4):
        dy = direct_y[i] + y
        dx = direct_x[i] + x
        if dy > 7 or dy < 0 or dx > 8 or dx < 0: continue
        if arr[dy][dx] != '#': continue
        if visited[dy][dx] == 1: continue
        visited[dy][dx] = 1
        q.append((dy,dx))

while q2:
    y,x,cnt=q2.popleft()
    if max_y<y:
        max_y=y
    for i in range(4):
        dy = direct_y[i] + y
        dx = direct_x[i] + x
        if dy > 7 or dy < 0 or dx > 8 or dx < 0: continue
        if arr[dy][dx] != '_': continue
        if visited[dy][dx] == 1: continue
        visited[dy][dx] = 1
        arr[dy][dx] = cnt+1
        q2.append((dy,dx,cnt+1))


for i in range(max_y,8):
    for j in range(9):
        if arr[i][j] !="#":
            if Min>arr[i][j]:
                Min=arr[i][j]
            break

print(Min)


