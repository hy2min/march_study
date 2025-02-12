T = int(input())
for idx in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N <= M:
        max_total = 0
        for i in range(M - N + 1):
            arr_B = B[i:i+N]
            total = 0
            for j in range(N):
                total += A[j] * arr_B[j]
            if max_total < total:
                max_total = total

    if N > M:
        max_total = 0
        for i in range(N - M + 1):
            arr_A = A[i:i + M]
            total = 0
            for j in range(M):
                total += arr_A[j] * B[j]
            if max_total < total:
                max_total = total

    print(f'#{idx+1} {max_total}')
