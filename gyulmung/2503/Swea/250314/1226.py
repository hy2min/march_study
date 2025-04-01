import sys
sys.stdin = open('input.txt','r')


from collections import deque
T = 1

for test in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(16)]

    q = deque()
    q.append((1,1,0))
    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    visited = set()
    visited.add((1, 1))
    ret = 0
    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if dy < 0 or dx < 0 or dy >=16 or dx >= 16: continue
            if arr[dy][dx] == '1' or (dy, dx) in visited: continue
            if arr[dy][dx] == '3':
                ret = cnt
            visited.add((dy, dx))
            q.append((dy, dx, cnt+1))
        if ret:
            break
    if ret:
        print(f'#{test} {1}')
    else:
        print(f'#{test} {0}')