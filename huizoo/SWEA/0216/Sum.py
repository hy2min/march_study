for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    Max = -float('inf')
    for i in range(100):
        Sum = sum(arr[i])
        if Max < Sum:
            Max = Sum
    arr2 = list(zip(*arr))
    for i in range(100):
        Sum = sum(arr2[i])
        if Max < Sum:
            Max = Sum
    Sum = 0
    for i in range(100):
        Sum += arr[i][i]
    if Max < Sum:
        Max = Sum
    Sum = 0
    for i in range(100):
        Sum += arr[i][-i-1]
    if Max < Sum:
        Max = Sum
    print(f'#{tc} {Max}')