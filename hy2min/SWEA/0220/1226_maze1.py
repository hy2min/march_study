from collections import deque

T = 10
for _ in range(T):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                start_y, start_x = i,j
            if arr[i][j] == 3:
                end_y, end_x = i,j


    d_y = [1,-1,0,0]
    d_x = [0,0,1,-1]

    visited = [[0] * 16 for _ in range(16)]
    visited[start_y][start_x] = 1

    q = deque()
    q.append((start_y,start_x))

    flag = 0
    while q:
        y,x = q.popleft()
        for i in range(4):
            dy = y + d_y[i]
            dx = x + d_x[i]
            if dy < 0 or dx < 0 or dy >= 16 or dx >= 16:
                continue
            if arr[dy][dx] == 1:
                continue
            if visited[dy][dx] == 1:
                continue
            visited[dy][dx] = 1
            if dy == end_y and dx == end_x:
                flag = 1
                break
            q.append((dy,dx))

    if flag:
        print(f'#{N} 1')
    else:
        print(f'#{N} 0')