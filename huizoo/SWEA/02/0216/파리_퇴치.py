t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            Sum = 0
            for k in range(M):
                for l in range(M):
                    Sum += arr[i+k][j+l]
            if Max < Sum:
                Max = Sum
    print(f'#{tc} {Max}')