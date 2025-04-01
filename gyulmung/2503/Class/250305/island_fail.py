from collections import deque

island = [[0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 0, 1, 0, 0]]

def bfs(a, b):
    width = deque()
    width.append((a, b))
    arr = [[0]*5 for _ in range(5)]
    ret = 0
    island[a][b] = 0
    diy = [0, 0, 1, -1]
    dix = [1, -1, 0, 0]
    while width:
        x, y = width.popleft()
        for i in range(4):
            dy = diy[i] + y
            dx = dix[i] + x
            if dy < 0 or dx < 0 or dy >= 5 or dx >= 5: continue
            if island[dy][dx] == 1:
                width.append((dy, dx))
                island[dy][dx] = 0
                ret += 1

    return ret

for i in range(5):
    for j in range(5):
        if island[i][j] == 1:
            print(bfs(i, j))