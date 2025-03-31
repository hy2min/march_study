import sys # 18분
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    Max = -1e8
    if N > M:
        N, M = M, N
        Ai, Bj = Bj, Ai
    for j in range(0, M - N + 1):
        Sum = 0
        for k in range(N):
            Sum += Ai[k] * Bj[j+k]
        if Max < Sum:
            Max = Sum

    print(f'#{i} {Max}')