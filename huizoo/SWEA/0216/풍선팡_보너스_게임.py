t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    Max = -21e8
    Min = 21e8
    for y in range(N):
        for x in range(N):
            Sum = arr[y][x]
            for p in range(1, N):
                for i in range(4):
                    ny = y+dy[i]*p
                    nx = x+dx[i]*p
                    if ny<0 or nx<0 or ny>=N or nx>=N:continue
                    Sum += arr[ny][nx]
            if Max < Sum:
                Max = Sum
            if Min > Sum:
                Min = Sum
    print(f'#{tc} {Max-Min}')
