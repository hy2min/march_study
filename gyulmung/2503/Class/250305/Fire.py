from collections import deque
N = int(input())
arr = [list(input()) for _ in range(N)]
sty, stx = map(int, input().split())
so = []
fire = []

# 소화기 위치 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j] == "A":
            so.append((i, j))
        elif arr[i][j] == "$":
            fire.append((i, j))

# 가장 가까운 소화기 찾기
Min = 1e8
Miny, Minx = 0, 0

for i, j in so:
    if Min > abs(sty-i)+abs(stx-j):
        Min = abs(sty-i)+abs(stx-j)
        Miny, Minx = i, j

# 소화기 들렸다가 불로 가기
soso = 0
def bfs(sy, sx, ey, ex):
    global soso
    q=deque()
    q.append((sy, sx, 0))
    diy = [0, 0, 1, -1]
    dix = [1, -1, 0, 0]
    while 1:
        y, x, cnt = q.popleft()
        for i in range(4):
            dy = diy[i] + y
            dx = dix[i] + x
            if dy < 0 or dx < 0 or dy >= N or dx >= N: continue
            if arr[dy][dx] == '#': continue
            if arr[dy][dx] == '$' and soso == 0: continue
            if dy == ey and dx == ex:
                if arr[dy][dx] == 'A':
                    soso += 1
                    return cnt + 1
                if arr[dy][dx] == '$' and soso > 0:
                    return cnt + 1
            q.append((dy, dx, cnt+1))
            arr[dy][dx] = '#'

route = 0
route += bfs(sty, stx, Miny, Minx)
route += bfs(Miny, Minx, fire[0][0], fire[0][1])
print(route)