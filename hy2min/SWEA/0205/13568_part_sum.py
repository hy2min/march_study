T = int(input())
for idx in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    min_sum = float('inf')
    max_sum = -float('inf')
    for i in range(N-M+1):
        if min_sum > sum(numbers[i:i+M]):
            min_sum = sum(numbers[i:i+M])
        if max_sum < sum(numbers[i:i+M]):
            max_sum = sum(numbers[i:i+M])
    print(f'#{idx+1} {max_sum-min_sum}')

