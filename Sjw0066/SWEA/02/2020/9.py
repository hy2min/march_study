from collections import deque

def bfs(i, j, level,ei,ej):
    global flag

    q = deque()
    q.append((i, j, level))
    direct_y = [0, 0, 1, -1]
    direct_x = [-1, 1, 0, 0]
    visited[i][j] = 1

    while q:
        y, x, cnt = q.popleft()
        if y==ei and x==ej:
            flag=1

        for i in range(4):
            dy = direct_y[i] + y
            dx = direct_x[i] + x
            if dy > N - 1 or dy < 0 or dx > N - 1 or dx < 0: continue
            if visited[dy][dx] == 1: continue
            if arr[dy][dx] == 1: continue
            visited[dy][dx] = 1
            q.append((dy, dx, cnt + 1))


for tc in range(1, 11):
    tc=int(input())
    N = 16
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    flag=0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                st_y = i
                st_x = j
            if arr[i][j] == 3:
                ed_y = i
                ed_x = j

    bfs(st_y, st_x, 0, ed_y, ed_x)

    if flag:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
