t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    possible = 0
    for y in range(N):
        for x in range(M):
            ship = arr[y][x]
            cnt = 0
            for i in range(8):
                ny, nx = y+dy[i], x+dx[i]
                if ny<0 or nx<0 or ny>=N or nx>=M:continue
                if ship > arr[ny][nx]:
                    cnt += 1
            if cnt>=4:
                possible+=1
    print(f'#{tc} {possible}')