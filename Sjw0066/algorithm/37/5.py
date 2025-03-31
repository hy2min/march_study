from collections import deque
arr=[
    [0,0,0,0],
    [1,1,0,1],
    [0,0,0,0],
    [1,0,1,0],
]
direct_y=[0,0,1,-1]
direct_x=[1,-1,0,0]
st_y,st_x=map(int,input().split())
ed_y,ed_x=map(int,input().split())

q=deque()
q.append((st_y,st_x))
while q:
    y,x=q.popleft()
    for i in range(4):
        dy = direct_y[i] + y
        dx = direct_x[i] + x
        if dy > 3 or dy < 0 or dx > 3 or dx < 0: continue
        if arr[dy][dx] != 0: continue
        arr[dy][dx] = arr[y][x] + 1
        q.append((dy,dx))
print(f'{arr[ed_y][ed_x]}회')
