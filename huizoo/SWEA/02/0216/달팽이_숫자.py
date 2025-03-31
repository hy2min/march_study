t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    num = 1
    i = 0
    y, x = 0, 0
    while num <= n**2:
        arr[y][x] = num
        num += 1
        ny, nx = y+dy[i], x+dx[i]

        if ny<0 or nx<0 or ny>=n or nx>=n or arr[ny][nx] !=0:
            i = (i+1)%4
            ny, nx = y+dy[i], x+dx[i]

        y, x = ny, nx

    print(f'#{tc}')
    print('\n'.join(' '.join(map(str, row)) for row in arr))