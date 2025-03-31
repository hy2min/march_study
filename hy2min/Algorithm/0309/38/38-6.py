from collections import deque

d_y = [-1, 1, 0, 0]
d_x = [0, 0, -1, 1]

def bfs(a, b, target):
    q = deque()
    q.append((a, b, 0))


    while q:
        a, b, cnt = q.popleft()

        if arr[a][b] == target:
            return a, b, cnt

        for i in range(4):
            dy = a + d_y[i]
            dx = b + d_x[i]
            if dy < 0 or dx < 0 or dy >= y or dx >= x:
                continue
            if arr[dy][dx] != '#':
                q.append((dy, dx, cnt + 1))






y, x = map(int, input().split())
arr = [list(input()) for _ in range(y)]
arr = [[int(j) if j.isdigit() else j for j in i] for i in arr]

target = 1
si, sj = 0, 0
total = 0
while target <= 4:
    ei, ej, cnt = bfs(si, sj, target)  # y,x,target
    total += cnt
    target += 1
    si, sj = ei, ej



print(str(total) + '회')