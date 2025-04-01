import sys
sys.stdin=open('input.txt','r')

from collections import deque
T = int(input())

for test in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    st, ed =0, 0
    for i in range(N):
        if arr[0][i] == 3:
            st, ed = 0,i
            break


    q = deque()
    q.append((st, ed))

    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    Flag = False
    visited = [[0]*N for _ in range(N)]
    visited[st][ed] = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if dy < 0 or dx < 0 or dy >= N or dx>=N: continue
            if arr[dy][dx] == 1 or visited[dy][dx] == 1: continue
            if arr[dy][dx] == 2:
                Flag = True
                break
            visited[dy][dx] = 1
            q.append((dy, dx))
        if Flag:
            break
        else:
            continue

    if Flag:
        print(f'#{test} {1}')
    else:
        print(f'#{test} {0}')