T = int(input())
dy = [-1,-1,-1,0,0,1,1,1]
dx = [-1,0,1,-1,1,-1,0,1]
for tc in range(1, T+1) : 
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    candi = 0
    for y in range(N) : 
        for x in range(M) :
            cnt = 0 
            for i in range(8) : 
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < N and 0 <= nx < M : 
                    if arr[y][x] > arr[ny][nx] : 
                        cnt += 1 
            if cnt >= 4 : 
                candi += 1
    print(f'#{tc} {candi}')