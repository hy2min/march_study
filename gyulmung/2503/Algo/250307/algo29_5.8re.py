import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
arr = [list(input()) for _ in range(4)]

q = deque()

for i in range(4):
    for j in range(3):
        if arr[i][j] != '_' and arr[i][j] != '#':
            q.append((i, j, 0))

while q:
    y, x, level = q.popleft()
    if level == 0:
        if x + 1 >= 3 or arr[y][x+1] != '_':
            q.append((y, x, level+1))
            continue
        arr[y][x], arr[y][x+1] = arr[y][x+1], arr[y][x]
        q.append((y, x+1, level+1))
    if level == 1:
        if y + 1 >= 4 or arr[y+1][x] != '_':
            q.append((y, x, level+1))
            continue
        arr[y+1][x], arr[y][x] = arr[y][x], arr[y+1][x]
        q.append((y+1, x, level+1))
    if level == 2:
        if x - 1 < 0 or arr[y][x-1] != '_':
            q.append((y, x, level+1))
            continue
        arr[y][x-1], arr[y][x] = arr[y][x], arr[y][x-1]
        q.append((y, x - 1, level+1))
    if level == 3:
        if y - 1 < 0 or arr[y-1][x] != '_':
            q.append((y, x, level+1))
            continue
        arr[y-1][x], arr[y][x] = arr[y][x], arr[y-1][x]
        q.append((y - 1, x, level+1))
    if level == 4:
        if x + 1 >= 3 or arr[y][x+1] != '_':
            q.append((y, x, level+1))
            continue
        arr[y][x], arr[y][x+1] = arr[y][x+1], arr[y][x]
        q.append((y, x + 1, level+1))
    if level > 4:
        continue
for i in arr:
    print(*i, sep ='')
