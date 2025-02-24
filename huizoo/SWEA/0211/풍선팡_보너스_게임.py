def boom(y, x):
    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]
    score = arr[y][x]
    for i in range(4):
        for p in range(1, N):
            ny, nx = y+dy[i]*p, x+dx[i]*p
            if 0 <= ny < N and 0 <= nx < N:
                score += arr[ny][nx]
    return score

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_score = float('inf')
    max_score = -float('inf')
    for i in range(N):
        for j in range(N):
            current_score = boom(i, j)
            min_score = min(min_score, current_score)
            max_score = max(max_score, current_score)

    print(f'#{tc} {max_score-min_score}')