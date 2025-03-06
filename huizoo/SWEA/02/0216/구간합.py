t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    Max = -21e8
    Min = 21e8
    for i in range(N-M+1):
        Sum = 0
        for j in range(i, i+M):
            Sum += arr[j]
        if Max < Sum:
            Max = Sum
        if Min > Sum:
            Min = Sum
    print(f'#{tc} {Max-Min}')