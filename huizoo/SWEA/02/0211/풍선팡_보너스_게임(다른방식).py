T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_score = float('inf')
    max_score = -float('inf')
    for i in range(N):
        for j in range(N):
            current_score = -arr[i][j]
            for k in range(N):
                current_score += arr[i][k] + arr[k][j]
            min_score = min(min_score, current_score)
            max_score = max(max_score, current_score)

    print(f'#{tc} {max_score-min_score}')