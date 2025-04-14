def abc(start, end, st):
    sy, sx = start
    ey, ex = end
    d = 0
    for order in st:
        if order == 'R':
            d = (d + 1) % 4
        elif order == 'L':
            d = (d - 1) % 4
        else:
            ny, nx = sy + DIR[d][0], sx + DIR[d][1]
            if ny<0 or nx<0 or ny>=N or nx>=N: continue
            if arr[ny][nx] == 'T': continue
            sy, sx = ny, nx

    if sy == ey and sx == ex:
        return 1
    else:
        return 0

T = int(input())
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    X = Y = None
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'T':
                T = (i, j)
            elif arr[i][j] == 'X':
                X = (i, j)
            elif arr[i][j] == 'Y':
                Y = (i, j)

    Q = int(input())
    print(f'#{tc}', end=' ')
    for _ in range(Q):
        C, command = input().split()
        print(f'{abc(X, Y, command)}', end=' ')
    print()
