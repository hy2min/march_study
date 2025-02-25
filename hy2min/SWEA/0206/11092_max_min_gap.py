T = int(input())
for idx in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    max_n = -float('inf')
    min_n = float('inf')

    max_idx, min_idx = -1, -1
    for i in range(N):
        if arr[i] >= max_n:
            max_n = arr[i]
            max_idx = i
    for i in range(N-1, -1, -1):
        if arr[i] <= min_n:
            min_n = arr[i]
            min_idx = i


    print(f'#{idx+1} {abs(max_idx-min_idx)}')
