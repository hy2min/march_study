from collections import deque

d_y = [0, 0, -1, 1]
d_x = [-1, 1, 0, 0]

def bfs(y, x):
    global person
    person = deque()
    q = deque()
    q.append((y, x))
    person.append((y, x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            dy = y + d_y[i]
            dx = x + d_x[i]
            if dy < 0 or dx < 0 or dy >= 8 or dx >= 9:
                continue
            if arr[dy][dx] == '#':
                q.append((dy, dx))
                person.append((dy, dx))
                arr[dy][dx] = '_'

def find(y, x):
    used = [[0] * 9 for _ in range(8)]
    q = deque()
    q.append((y, x, 0))
    used[y][x] = 1

    while q:
        y, x, cnt = q.popleft()

        if arr[y][x] == '#':
            return cnt

        for i in range(4):
            dy = y + d_y[i]
            dx = x + d_x[i]
            if dy < 0 or dx < 0 or dy >= 8 or dx >= 9:
                continue
            if not used[dy][dx]:
                used[dy][dx] = 1
                q.append((dy, dx, cnt+1))


arr = [list(input()) for _ in range(8)]

flag = 0
for i in range(8):
    for j in range(9):
        if arr[i][j] == '#':
            flag = 1
            bfs(i, j)
            break
    if flag:
        break

mn = 21e8
for (y, x) in person:
    ret = find(y, x) -1
    mn = min(ret, mn)

print(mn)