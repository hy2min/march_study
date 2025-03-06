t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Min = min(N, M)
    Max = max(N, M)
    multi_max = -21e8
    for i in range(Max-Min+1):
        multi = 0
        if Min == N:
            for j in range(Min):
                multi += A[j]*B[i+j]
        elif Min == M:
            for j in range(Min):
                multi += A[i+j]*B[j]
        if multi_max < multi:
            multi_max = multi
    print(f'#{tc} {multi_max}')