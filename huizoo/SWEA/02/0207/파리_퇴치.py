T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    dy, dx = [], []
    for i in range(M) :
        for j in range(M) :
            dy.append(i)
            dx.append(j)
    for y in range(N) :
        for x in range(N) :
            current_total = 0
            for i in range(M**2) :
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N :
                    current_total += arr[ny][nx]
            if total < current_total :
                total = current_total
    print(f'#{tc} {total}')