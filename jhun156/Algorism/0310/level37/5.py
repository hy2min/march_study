from collections import deque

q = deque()
arr = [
    [0,0,0,0],
    [1,1,0,1],
    [0,0,0,0],
    [1,0,1,0],
]
used = [[0] * 4 for _ in range(4)]
Min = 1e9
sy,sx = map(int,input().split())
ey,ex = map(int,input().split())
used[sy][sx] = 1
q.append((sy,sx,0))
diY = [0,0,1,-1]
diX = [1,-1,0,0]

while q:

    ny,nx,cnt = q.popleft()
    if ny == ey and nx == ex:
        if Min > cnt:
            Min = cnt

    for i in range(4):
        dy = ny + diY[i]
        dx = nx + diX[i]
        if dy < 0 or dy > 3 or dx < 0 or dx > 3:
            continue
        if arr[dy][dx] == 1:
            continue
        if used[dy][dx] == 1:
            continue
        used[dy][dx] = 1
        q.append((dy,dx,cnt+1))

print(f"{Min}회")