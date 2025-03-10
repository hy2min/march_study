from collections import deque

arr = [list(map(int,input().split())) for _ in range(4)]
used = [[0] * 4 for _ in range(4)]
used[0][0] = 1
q = deque()
q.append((0,0))
diX = [0,0,1,-1]
diY = [1,-1,0,0]
cnt = 1

while q:
    ny,nx = q.popleft()
    for i in range(4):
        dy = ny + diY[i]
        dx = nx + diX[i]
        if dy < 0 or dy > 3 or dx < 0 or dx > 3:
            continue
        if arr[dy][dx] == 0:
            continue
        if used[dy][dx] == 1:
            continue
        used[dy][dx] = 1
        cnt += 1
        q.append((dy,dx))

print(cnt)