from collections import deque

arr = [
    ['0','0','0','0'],
    ['1','1','0','1'],
    ['0','0','0','0'],
    ['1','0','1','0'],
]

y1, x1 = map(int, input().split())
y2, x2 = map(int, input().split())
arr[y1][x1] = 0
def bfs(y1, x1):
    q = deque([(y1, x1)])
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if ny<0 or nx<0 or ny>=4 or nx>=4: continue
            if arr[ny][nx] != '0': continue
            arr[ny][nx] = arr[y][x] + 1
            if ny == y2 and nx == x2:
                print(f'{arr[ny][nx]}회')
                return
            q.append((ny, nx))
bfs(y1, x1)