from collections import deque
arr=[[0, 0, 1, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 0, 0],
     [0, 0, 1, 0, 0, 0],
     [1, 0, 0, 0, 1, 0]]


diy = [0, 0, 1, -1]
dix = [1, -1, 0, 0]

def bfs(a, b):
    global arr
    q = deque()
    q.append((a, b))
    cnt = 1
    arr[a][b] = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            dy = diy[i] + y
            dx = dix[i] + x
            if dx < 0 or dy < 0 or dx > 5 or dy > 4: continue
            if arr[dy][dx] == 1:
                q.append((dy, dx))
                cnt += 1
                arr[dy][dx] = 0
    return cnt
island = []
for i in range(5):
    for j in range(6):
        if arr[i][j] == 1:
            a = bfs(i,j)
            island.append(a)
print(f'가장 큰섬:{max(island)}')
print(f'가장 작은섬:{min(island)}')
print(f'섬의 개수:{len(island)}')