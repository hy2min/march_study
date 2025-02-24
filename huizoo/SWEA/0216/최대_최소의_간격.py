t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = list(map(int, input().split()))
    Max = -21e8
    Min = 21e8
    Max_idx = 0
    Min_idx = 0
    for i in range(N):
        if arr[i] < Min:
            Min = arr[i]
            Min_idx = i
        if arr[i] >= Max:
            Max = arr[i]
            Max_idx = i
    print(f'#{tc} {abs(Max_idx-Min_idx)}')