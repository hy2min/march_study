def cross(N, M, A, B):
    max_total = float('-inf')
    for i in range(M - N + 1):
        total = 0
        for j in range(N):
            total += A[j] * B[j + i]
        if max_total < total:
            max_total = total
    return max_total

T = int(input())
for idx in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N <= M:
        max_total = cross(N, M, A, B)
    else:
        max_total = cross(M, N, B, A)

    print(f'#{idx+1} {max_total}')

